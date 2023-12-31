import numpy as np


CAMERA_IDX = 0

DISP_IMAGE_WIDTH  = 860
DISP_IMAGE_HEIGHT = 540



ROUND_TIME = 30 # 30sec
# QUESTION_FILE = r'Countries_Descriptions_Emojis.xlsx'
QUESTION_FILE = r'GUI/resource_files/country_descriptions.xlsx'


TEST_VIDEO_PATH = r'd1.avi'

YOLO_SEG_MODEL_PATH = r'GUI/resource_files/yolo_seg.pt'


# COUNTRY_MAP_DICT = {1: 'AUS', 3: 'BRAZIL', 4: 'CANADA', 7: 'CHINA', 2: 'GREENLAND', 5: 'INDIA', 6: 'RUSSIA', 0: 'USA'}
COUNTRY_MAP_DICT = {0: 'USA', 1: 'AUS', 2: 'GREENLAND', 3: 'BRAZIL', 4: 'CANADA', 5: 'INDIA', 6: 'RUSSIA', 7: 'CHINA'}


#  'USA', 1: 'AUS', 2: 'GREENLAND', 3: 'BRAZIL', 4: 'CANADA', 5: 'INDIA', 6: 'RUSSIA', 7: 'CHINA'

WAITING_TIME = 150


# 'USA','AUS','GREENLAND','BRAZIL','CANADA','INDIA','RUSSIA','CHINA'
