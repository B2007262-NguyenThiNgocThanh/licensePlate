# import sys #thư viện lưu trữ thông tin code cơ bản
# import numpy as np
# import pandas as pd
# import torch
# import os
# import cv2
# from ultralytics import YOLO
# from PIL import Image, ImageDraw

# #model
# model = YOLO("D:\IT04\hk2\CT208_NL\Project\\runs\detect\\train2\weights\\best.pt")

# # Đường dẫn tới thư mục chứa hình ảnh cần gán nhãn
# input_dir = 'D:\IT04\hk2\CT208_NL\Project\\test'
# output_labels = 'D:\IT04\hk2\CT208_NL\Project\\test'

# # Tạo thư mục đầu ra nếu nó chưa tồn tại
# if not os.path.exists(output_labels):
#     os.makedirs(output_labels)

# # đọc list img chưa gán nhãn
# image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# # Danh sách các nhãn tương ứng với biển số xe (cần thay đổi tùy theo mô hình của bạn)
# license_plate_labels = ["Plate"]
# idx=0
# for image in image_files:
#     img_path = os.path.join(input_dir, image)

#     try:
#         img = cv2.imread(img_path)
#         wimg, himg = img.shape[:2]

#         # print("width: ", wimg)
#         # print("\nheight: ", himg)
#         if img is None:
#             print(f"error reading image {img_path}")
#             continue
#     except Exception as e:
#         print(f"Exception occurred while reading image {img_path}: {e}")
#         continue

#     # Set model parameters
#     model.conf = 0.25  # Confidence threshold
#     model.iou = 0.45  # IoU threshold

#     # predict
#     results = model(img, classes=15)
#     labels = []

#     # Results
#     for idx, result in enumerate(results):
#         boxes = result.boxes  # Bounding boxes
#         for box in boxes:
#             # Lấy class label và confidence score
#             cls = int(box.cls)
#             conf = box.conf
#             # if conf > 0.25:
#                 # Vẽ bounding box và hiển thị trên ảnh
#             xyxy = box.xyxyn.cpu().numpy().astype(float)[0]  # Lấy tensor xyxy và chuyển về numpy array
#             wimg /= 255.0
#             himg /= 255.0
#             x1, y1, x2, y2 = xyxy  # Unpack thành 4 phần tử

#             x_center = (x1 + x2) / (2.0)
#             y_center = (y1 + y2) / (2.0)
#             width = (x2 - x1) 
#             height = (y2 - y1)
#             # if x_center > 0.1 and x_center < 0.9:
#             labels.append((cls, (x_center, y_center, width, height)))
    
#     # lưu nhãn với tệp txt
#     label_file = os.path.splitext(image)[0] + '.txt'
#     label_path = os.path.join(output_labels, label_file)


#     with open(label_path, 'w') as f:
#         for class_id, bbox in labels:
#             bbox_str = ' '.join(map(str, bbox))
#             f.write(f"{class_id} {bbox_str}\n")

import sys #thư viện lưu trữ thông tin code cơ bản
import numpy as np
import pandas as pd
import torch
import os
import cv2
from ultralytics import YOLO
from PIL import Image, ImageDraw

#model
model = YOLO("D:\IT04\hk2\CT208_NL\Project\\runs\detect\\train2\weights\\best.pt")

# Đường dẫn tới thư mục chứa hình ảnh cần gán nhãn
input_dir = 'D:\IT04\hk2\CT208_NL\Project\\test'
output_labels = 'D:\IT04\hk2\CT208_NL\Project\\test'

# Tạo thư mục đầu ra nếu nó chưa tồn tại
if not os.path.exists(output_labels):
    os.makedirs(output_labels)

# đọc list img chưa gán nhãn
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

# Danh sách các nhãn tương ứng với biển số xe (cần thay đổi tùy theo mô hình của bạn)
license_plate_labels = ["Plate"]
idx=0
for image in image_files:
    img_path = os.path.join(input_dir, image)

    try:
        img = cv2.imread(img_path)
        wimg, himg = img.shape[:2]

        # print("width: ", wimg)
        # print("\nheight: ", himg)
        if img is None:
            print(f"error reading image {img_path}")
            continue
    except Exception as e:
        print(f"Exception occurred while reading image {img_path}: {e}")
        continue

    # Set model parameters
    model.conf = 0.25  # Confidence threshold
    model.iou = 0.45  # IoU threshold

    # predict
    results = model(img, classes=15)
    labels = []

    # Results
    for idx, result in enumerate(results):
        boxes = result.boxes  # Bounding boxes
        for box in boxes:
            # Lấy class label và confidence score
            cls = int(box.cls)
            conf = box.conf
            if conf > 0.25:
                # Vẽ bounding box và hiển thị trên ảnh
                xyxy = box.xyxyn.cpu().numpy().astype(float)[0]  # Lấy tensor xyxy và chuyển về numpy array
                wimg /= 255.0
                himg /= 255.0
                x1, y1, x2, y2 = xyxy  # Unpack thành 4 phần tử

                x_center = (x1 + x2) / (2.0)
                y_center = (y1 + y2) / (2.0)
                width = (x2 - x1) 
                height = (y2 - y1)
                if x_center > 0.1 and x_center < 0.93:
                    labels.append((cls, (x_center, y_center, width, height)))
    
    # lưu nhãn với tệp txt
    label_file = os.path.splitext(image)[0] + '.txt'
    label_path = os.path.join(output_labels, label_file)


    with open(label_path, 'w') as f:
        for class_id, bbox in labels:
            bbox_str = ' '.join(map(str, bbox))
            f.write(f"{class_id} {bbox_str}\n")

