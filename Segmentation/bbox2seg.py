import os
import cv2

import torch
from ultralytics import SAM
import xml.etree.ElementTree as ET


class BoundingBoxToSegMaskConverter:
    def __init__(self, SAM_model_path, classes):
        # Load Segment Anything Model
        self.SAM_model = SAM(SAM_model_path)
        self.classes = classes
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def parse_xml(self, xml_file):
        # Parse XML annotation file to extract bounding boxes and class IDs
        tree = ET.parse(xml_file)
        root = tree.getroot()

        boxes = []
        class_ids = []

        for obj in root.findall('object'):
            class_name = obj.find('name').text
            class_id = self.classes.index(class_name)

            box = obj.find('bndbox')
            xmin = float(box.find('xmin').text)
            ymin = float(box.find('ymin').text)
            xmax = float(box.find('xmax').text)
            ymax = float(box.find('ymax').text)

            boxes.append([xmin, ymin, xmax, ymax])
            class_ids.append(class_id)

        return torch.tensor(boxes, device=self.device), class_ids

    def bbox2seg_mask(self, xml_path, image_path, output_annotation_folder):
        # Convert bounding boxes to segmentation masks and save the results
        os.makedirs(output_annotation_folder, exist_ok=True)

        # Get Annotations
        save_txt_name = f'{os.path.basename(xml_path)[:-4]}.txt'
        save_img_name = os.path.basename(image_path)

        boxes_tensor, class_ids = self.parse_xml(xml_path)

        # Read image and run SAM model for segmentation
        img_array = cv2.imread(image_path)
        sam_results = self.SAM_model(img_array, bboxes=boxes_tensor, verbose=False, save=False, device=self.device)
        cv2.imwrite(f'{output_annotation_folder}/{save_img_name}', img_array)

        segments = sam_results[0].masks.xyn

        with open(f'{output_annotation_folder}/{save_txt_name}', 'w') as f:
            for i in range(len(segments)):
                s = segments[i]
                if len(s) == 0:
                    continue
                segment = map(str, segments[i].reshape(-1).tolist())
                f.write(f'{class_ids[i]} ' + ' '.join(segment) + '\n')

    def bulk_bbox2seg_mask(self, xml_file_paths, image_file_paths, output_annotation_folder):
        # Process a list of bounding box and image file paths
        for i in range(len(xml_file_paths)):
            print(f'{i+1}/{len(xml_file_paths)} : {xml_file_paths[i]}')
            self.bbox2seg_mask(xml_file_paths[i], image_file_paths[i], output_annotation_folder)




if __name__ == "__main__":
    CLASSES = ['AUS', 'GREENLAND', 'INDIA', 'CANADA', 'USA', 'BRAZIL', 'CHINA', 'RUSSIA']
    model_path = r'Segmentation/sam_b.pt'

    converter = BoundingBoxToSegMaskConverter(model_path, CLASSES)

    # The place where generated masks are saved
    output_folder = f'Segmentation/sample_segment_masks'

    # Here Annotations and Images both are in same folder
    annotation_folder_path = r'Segmentation/sample_annotation'
    train_xml_files = [os.path.join(annotation_folder_path, file) for file in os.listdir(annotation_folder_path) if file.endswith(".xml")]
    train_img_files = [os.path.join(annotation_folder_path, file) for file in os.listdir(annotation_folder_path) if file.endswith(".jpg")]


    converter.bulk_bbox2seg_mask(train_xml_files, train_img_files, output_folder)
