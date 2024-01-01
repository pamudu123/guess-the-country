import sys
import numpy as np
import utils
from PySide6.QtGui import QColor

from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt, QThreadPool, QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow


## import custom functions
from GameWindow import Ui_GameWindow
from Q_Loader import CountryDescriptionReader
from video_capture_thread import VideoFeedThread
import args


class GameWindow(QMainWindow, Ui_GameWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.showMaximized()

        # Set up the timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.time_left = args.ROUND_TIME

        # Set up the score
        self.correct_score = 0
        self.wrong_score = 0

        # Initialize Variables
        self.round_count = 0
        self.pause_time_counter = 0
        self.hint_time_counter = 0
        self.pointing_vector = []

        # For randomly pick countries
        self.country_reader = CountryDescriptionReader()

        # Initialize Game 
        self.initialize_ui()
        self.next_round()

        self.threadpool = QThreadPool()
        self.start_video_feed() # Initialize thread

    # Initialize User Settings
    def initialize_ui(self):
        self.n_correct_label.setText(str(self.correct_score))
        self.n_wrong_label.setText(str(self.wrong_score))

        self.n_correct_label.setStyleSheet("font-size: 48px; background-color: rgb(87, 227, 137);\n"
"border-radius: 4;")
        self.n_wrong_label.setStyleSheet("font-size: 48px; background-color: rgb(237, 51, 59);\n"
"border-radius: 4;")

        self.n_correct_label.setAlignment(Qt.AlignCenter)
        self.n_wrong_label.setAlignment(Qt.AlignCenter)
        self.hint_txt.setReadOnly(True)



    ################ Display Image ################
    @staticmethod
    def create_QImage(numpy_array):
        height, width, channel = numpy_array.shape
        bytes_per_line = channel * width
        q_image = QImage(numpy_array.data, width, height, bytes_per_line, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(q_image)
        return pixmap
    

    def display_live_image(self, numpy_image):
        raw_image_pixmap = self.create_QImage(numpy_image)
        self.live_video_label.setPixmap(raw_image_pixmap)
        self.live_video_label.setStyleSheet("border-radius: 45;")


    ################ Start Video Thread ################
    def start_video_feed(self):
        self.cam_feed = VideoFeedThread()
        self.cam_feed.signals.live_image_signal.connect(self.display_live_image)
        self.cam_feed.signals.pointing_coordinate_signal.connect(self.get_pointing_coordinates)
        self.cam_feed.signals.pause_signal.connect(self.capture_pause_game_signal)
        self.cam_feed.signals.hint_signal.connect(self.capture_hint_signal)
        self.cam_feed.signals.map_detected_signal.connect(self.capture_map_detected_signal)

        self.threadpool.start(self.cam_feed.run_realtime)
    
    def capture_map_detected_signal(self):
        self.status_label.setText("MAP NOT DETECTED")

    
    ################ Get Finger Movements ################
    def get_pointing_coordinates(self,country_masks, point_xy):
        # print(f'Point XY : {point_xy}')
        pointing_mask_idx = utils.find_mask_for_coordinate(country_masks, point_xy)
        if pointing_mask_idx is not None: self.pointing_vector.append(pointing_mask_idx)

        # if last x iteams of the list are same make it as a selection
        if len(self.pointing_vector) > args.WAITING_TIME:
            selection = self.pointing_vector[-args.WAITING_TIME :]
            if len(set(selection)) == 1:
                selected_country = args.COUNTRY_MAP_DICT[selection[0]]

                self.check_answer(selected_country)
                self.next_round()


    def capture_hint_signal(self):
        self.hint_time_counter += 1

        if self.hint_time_counter >= args.HINT_TIME:
            print("== HINT SIGNAL ==")
            self.show_hint()
            self.hint_time_counter = 0


    def capture_pause_game_signal(self):
        self.pause_time_counter += 1

        if self.pause_time_counter >= args.PAUSE_TIME:
            print("== PAUSE SIGNAL ==")
            self.pause_timer()
            self.pause_time_counter = 0


    def check_answer(self, user_answer):
        correct_answer = self.country_data['Country Code']
        print(f'User :{user_answer} Correct :{correct_answer}')

        if correct_answer == user_answer:  # correct
            self.correct_score += 1
            self.n_correct_label.setText(str(self.correct_score))

            # Change label color to green for 2 seconds
            background_color = QColor(25, 240, 35)
            self.status_label.setStyleSheet(
                f"background-color: rgb({background_color.red()}, {background_color.green()}, {background_color.blue()});"
                "color: rgb(255, 255, 255);"
                "padding: 5px;"
                "padding-left: 5px;"
                "padding-right: 5px;"
                "border-radius: 10;"
            )
            QTimer.singleShot(2000, self.reset_label_color)

        else:
            self.wrong_score += 1
            self.n_wrong_label.setText(str(self.wrong_score))

            # Change label color to red for 2 seconds
            background_color = QColor(240, 50, 35)
            self.status_label.setStyleSheet(
                f"background-color: rgb({background_color.red()}, {background_color.green()}, {background_color.blue()});"
                "color: rgb(255, 255, 255);"
                "padding: 5px;"
                "padding-left: 5px;"
                "padding-right: 5px;"
                "border-radius: 10;"
            )            
            QTimer.singleShot(2000, self.reset_label_color)
            

    def reset_label_color(self):
        # Reset label color to its original color
        background_color = QColor(28, 113, 216)
        self.status_label.setStyleSheet(
            f"background-color: rgb({background_color.red()}, {background_color.green()}, {background_color.blue()});"
            "color: rgb(255, 255, 255);"
            "padding: 5px;"
            "padding-left: 5px;"
            "padding-right: 5px;"
            "border-radius: 10;"
        )

    ################ Timmer Functionalities ################
    def start_timer(self):
        self.time_left = args.ROUND_TIME + 1
        self.timer.start(1000)  # Timer updates every second

    def update_timer(self):
        self.time_left -= 1
        self.timer_label.setText(str(self.time_left))
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 48px; background-color: rgb(255, 120, 0);\n"
"border-radius: 10;")

        if self.time_left == 0:
            self.next_round()

    def pause_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.emoji_label.hide()
        else:
            self.timer.start()
            self.emoji_label.show()
            self.status_label.setText("")

    def next_round(self):
        self.start_timer()
        self.country_data = self.country_reader.get_random_country_description()
        self.round_count += 1
        self.status_label.setText(f'Round : {self.round_count}')
        
        self.status_label.setAlignment(Qt.AlignCenter)

        self.update_emojis()
        self.hint_txt.setText("")
        
        # empty hand signals
        self.pointing_vector = []
        self.hint_time_counter = 0
        self.pause_time_counter = 0


    def show_hint(self):
        self.hint_txt.show()
        self.hint_txt.setText(self.country_data['Description'])
        self.hint_txt.setFixedSize(400, 100)


    def update_emojis(self):
        self.emoji_label.show()
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setStyleSheet("background-color: rgb(153, 193, 241")
        self.emoji_label.setStyleSheet("font-size: 48px;") 
        self.emoji_label.setFixedSize(400, 100)

        self.emoji_label.setText(self.country_data['Emojis'])

    
    # Close the main window and the entire app
    def close_app(self):
        self.close() 

        
#############################
# app = QApplication(sys.argv)
# w = GameWindow()
# app.exec()

## pyside6-uic gamewindow.ui -o GameWindow.py
