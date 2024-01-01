import cv2
import mediapipe as mp
from ultralytics import YOLO

from PySide6.QtCore import QRunnable, Slot
from worker_signals import WorkerSignals

# custom scripts
import args
import utils


class VideoFeedThread(QRunnable):
    def __init__(self):
        super(VideoFeedThread, self).__init__()
        self.signals = WorkerSignals()

        self.process_started = True


    @staticmethod
    def create_out_frame(in_frame):
        out_frame = in_frame.copy()
        out_frame = cv2.cvtColor(out_frame,cv2.COLOR_BGR2RGB)
        out_frame = cv2.resize(out_frame,(args.DISP_IMAGE_WIDTH,args.DISP_IMAGE_HEIGHT))
        # out_frame = cv2.resize(out_frame,(0,0),fx=0.5,fy=0.5)
        return out_frame


    @Slot()
    def run_realtime(self):
        self.cap = cv2.VideoCapture(r'/home/pamudu/Desktop/Other_Projects/guess-the-country/GUI/d8.avi')
        # self.cap = cv2.VideoCapture(args.CAMERA_IP)

        mask_available = False

        # Initialize Mediapipe Hand module
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(max_num_hands=1)
        mp_drawing = mp.solutions.drawing_utils

        # Initialize Segmentaton Model
        model = YOLO(args.YOLO_SEG_MODEL_PATH)

        while self.process_started:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Unable to read frame from webcam.")
                self.process_started = False
                break
            
            frame = cv2.resize(frame, dsize=(640,480))
            display_frame = frame.copy()

            # Get Mask
            if not mask_available:
                print("Mask Checking......")
                yolo_results = model(frame, verbose=True)
                country_masks = yolo_results[0].masks.data.cpu().numpy()

                mask_available = True

            if mask_available:
                image_h = frame.shape[0]
                image_w = frame.shape[1]
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Process the frame with Mediapipe Hand module
                results = hands.process(rgb_frame)

                all_fingers_up = False
                index_and_middle_up = False

                # Check if hand landmarks are detected
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:

                        # Check if each finger is raised
                        fingers_raised = {
                            'thumb': utils.is_finger_raised(hand_landmarks.landmark[4], hand_landmarks.landmark[3], image_h),
                            'index': utils.is_finger_raised(hand_landmarks.landmark[8], hand_landmarks.landmark[6], image_h),
                            'middle': utils.is_finger_raised(hand_landmarks.landmark[12], hand_landmarks.landmark[10], image_h),
                            'ring': utils.is_finger_raised(hand_landmarks.landmark[16], hand_landmarks.landmark[14], image_h),
                            'pinky': utils.is_finger_raised(hand_landmarks.landmark[20], hand_landmarks.landmark[18], image_h)
                        }

                        # Check specific combinations
                        # change by checking the results if you want
                        num_fingers_raised = sum(fingers_raised.values())
                        if num_fingers_raised == 5:
                            all_fingers_up = True
                        if num_fingers_raised >=3 and num_fingers_raised <4:
                            index_and_middle_up = True
                        
                        if all_fingers_up:
                            # print(f"All fingers are up")
                            self.signals.pause_signal.emit()
                        elif index_and_middle_up:
                            # print(f"Only index and middle fingers are up")
                            self.signals.hint_signal.emit()
                            

                        # Extract and print the coordinates of each finger tip (landmark index 4 for each finger)
                        for finger_tip in [4, 8, 12, 16, 20]:
                            x_cor, y_cor = int(hand_landmarks.landmark[finger_tip].x*image_w), int(hand_landmarks.landmark[finger_tip].y*image_h)
                            cv2.circle(display_frame, (x_cor, y_cor), 15, (0,255,255), 2) 

                        if fingers_raised['index']:  # index finger up
                            x_index_cor, y_index_cor = int(hand_landmarks.landmark[8].x*image_w), int(hand_landmarks.landmark[8].y*image_h)
                            cv2.circle(display_frame, (x_index_cor, y_index_cor), 12, (0,0,255), -1) 

                            if not all_fingers_up and not index_and_middle_up:
                                self.signals.pointing_coordinate_signal.emit(country_masks, (x_index_cor, y_index_cor))


                        # Draw lines connecting previous index finger coordinates
                        # for i in range(1, len(index_finger_coor)):
                        #     cv2.line(display_frame, (int(index_finger_coor[i-1][0]), int(index_finger_coor[i-1][1])),
                        #             (int(index_finger_coor[i][0]), int(index_finger_coor[i][1])), (0, 255, 0), 2)


                        # Draw hand landmarks on the frame
                        mp_drawing.draw_landmarks(display_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # create image to show in the GUI
            display_frame = self.create_out_frame(display_frame)
            self.signals.live_image_signal.emit(display_frame)

 
    def stop_video_feed(self):
        self.process_started = False

