import cv2
import numpy as np
from random import randint

test_image_path = r'Segmentation/sample_segment_masks/frame_d1_360_jpg.rf.aca7bc32ba5c91ea638994e1f7838c5c.jpg'
test_annotation_path = r'Segmentation/sample_segment_masks/frame_d1_360_jpg.rf.aca7bc32ba5c91ea638994e1f7838c5c.txt'


with open(test_annotation_path, 'r') as f:
    labels = f.read().splitlines()
img = cv2.imread(test_image_path)

h,w = img.shape[:2]

for label in labels:
    print(label)
    class_id, *poly = label.split(' ')
    
    poly = np.asarray(poly,dtype=np.float16).reshape(-1,2) # Read poly, reshape
    poly *= [w,h] # Unscale
    
    cv2.polylines(img, [poly.astype('int')], True, (randint(0,255),randint(0,255),randint(0,255)), 2) # Draw Poly Lines
    cv2.fillPoly(img, [poly.astype('int')], (randint(0,255),randint(0,255),randint(0,255)), cv2.LINE_AA) # Draw area


key = cv2.imshow('SEGMENTATION MASK IMAGE', img)
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()
