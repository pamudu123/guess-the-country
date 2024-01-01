########### CONFIGURATION FILE ###########

# camera settings
CAMERA_IDX = 0
CAMERA_IP = 'http://192.168.1.3:8080/video'

# UI settings
DISP_IMAGE_WIDTH  = 860
DISP_IMAGE_HEIGHT = 540

# Game settings
ROUND_TIME = 15 # 15sec

WAITING_TIME = 150  #frames (Ex:150 means 150 frames)
PAUSE_TIME = 30 #frames
HINT_TIME = 30  #frames


COUNTRY_MAP_DICT = {0: 'USA', 1: 'AUS', 2: 'GREENLAND', 3: 'BRAZIL', 
                    4: 'CANADA', 5: 'INDIA', 6: 'RUSSIA', 7: 'CHINA'}

# Files
QUESTION_FILE = r'Application/resource_files/country_descriptions.xlsx'
YOLO_SEG_MODEL_PATH = r'Application/resource_files/yolo_seg.pt'







