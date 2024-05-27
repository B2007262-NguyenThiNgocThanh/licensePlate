import sys #thư viện lưu trữ thông tin code cơ bản
import numpy as np
import pandas as pd
import torch
import os
from PyQt6 import QtGui
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog #lấy ra ứng dụng trong thư viện #Lấy ra giao diện chính #lấy file hình
from PyQt6.QtGui import QPixmap, QImage

from ultralytics import YOLO
from PIL import Image, ImageDraw

from display_1 import Ui_MainWindow #gọi file giao diện

class MainWindow(QMainWindow): 
    def __init__(self): #hàm khởi tạo
        self.main_win = QMainWindow()  
        super().__init__() #thừa hưởng
        self.uic = Ui_MainWindow() #tạo màn hình
        self.uic.setupUi(self.main_win) #đưa code của ui_mainwindow lưu vào main_win 
        
        self.uic.insert_img.clicked.connect(self.insert_link) #khai báo nút thêm 
        self.uic.predict_img.clicked.connect(self.start_predict)

        self.idx = 0

    def insert_link(self):

        #tìm đường dẫn
        link = QFileDialog.getOpenFileName(filter = "*.png *.jpg *.jpeg")
        #mở hình
        self.uic.img.setPixmap(QPixmap(link[0]))
        #hiển thị đường dẫn
        self.uic.text.setText(link[0])
        self.img_save = link[0]
        

    def start_predict(self):
        model = YOLO("D:/IT04/hk2/CT208_NL/Project/runs/detect/train2/weights/best.pt")
        result = model(self.img_save)     
    
        bbox_label=[]

        for r in result:
            # Tạo một bản sao của hình ảnh đầu vào
            img = Image.open(self.img_save)
            img_with_boxes = img.copy()
            draw = ImageDraw.Draw(img_with_boxes)

            for ci, c in enumerate(r):
                label = c.names[c.boxes.cls.tolist().pop()]

                # Lấy tọa độ theo số int
                bbox = tuple(map(int, c.boxes.xyxy[0].tolist()))
                bbox_label.append((bbox, label))

                # Vẽ hộp giới hạn và nhãn lên hình ảnh
                draw.rectangle(bbox, outline="red", width=2)
                draw.text((bbox[0], bbox[1]), label, fill="blue")

            # Tạo tên file mới cho ảnh đã vẽ
            output_dir = "D:\IT04\hk2\CT208_NL\Project\\result_predict"
            os.makedirs(output_dir, exist_ok=True)
            output_filename = f"detected_{self.idx}.jpg"
            output_path = os.path.join(output_dir, output_filename)
            self.idx+=1
            # Lưu ảnh đã vẽ
            img_with_boxes.save(output_path)
             

                
        # sắp xếp theo tọa độ x
        sort_bbox_label = sorted(bbox_label, key=lambda x: x[0][0])
        # print(sort_bbox_label) # type = list 
        # tách thành 2 list nhỏ
        bbox_label1 = []
        bbox_label2 = []
        #so sanh tung cap trong list
        for i in range(1,3):
            bbox_pre, label_pre = sort_bbox_label[i-1]
            bbox, label = sort_bbox_label[i]
            bbox_next, label_next = sort_bbox_label[i+1]

            if (bbox[3] < bbox_pre[3] and bbox[3] <= bbox_next[3]):
                 bbox_label1.append((bbox, label))
            else:
                bbox_label2.append((bbox, label))
        bbox_label2_first, label_label2_first = bbox_label2[0]
        
        # print((bbox_label2_first, label_label2_first))
        #so sanh tung cap trong list
        for i in range(3,len(sort_bbox_label) - 1):
            bbox_pre, label_pre = sort_bbox_label[i-1]
            bbox, label = sort_bbox_label[i]
            bbox_next, label_next = sort_bbox_label[i+1]
            if bbox[3] <= bbox_label2_first[3] and (bbox[3] - bbox_next[3]) < 0 or ( bbox[3] <= bbox_label2_first[3] and abs(bbox[3] - bbox_next[3])<5 and abs(bbox[3] - bbox_label2_first[3])>5):
                bbox_label1.append((bbox, label))
            else:
                bbox_label2.append((bbox, label))

        # print("list 1: ", bbox_label1)
        # print("list 2: ", bbox_label2)

        # print(len(sort_bbox_label))
        bbox_last, label_last = sort_bbox_label[-1]
        bbox_last_pre, label_last_pre = sort_bbox_label[-2]

        if bbox_last[3] < bbox_last_pre[3]:
            bbox_label1.append((bbox_last, label_last))
            # if bbox_last[3] > bbox_last_pre[3]:
        else:
            bbox_label2.append((bbox_last, label_last))

        #NỐI CHUỖI
        str_label1 = ""       
        for i in range(len(bbox_label1)):
            bbox, label = bbox_label1[i]
            str_label1 = str_label1 + " " + label

        str_label2 = ""
        for i in range(len(bbox_label2)):
            bbox, label = bbox_label2[i]
            
            str_label2 = str_label2 + " " + label


        chuoi = str_label1 + " -" + str_label2

        for bbox, label in sort_bbox_label: 
            img_arr = r.plot()         
            img = Image.fromarray(img_arr[..., ::-1])
            img.save('D:\IT04\hk2\CT208_NL\Project\\result_predict\imgDetected.jpg')
        



        # in ra chuỗi các label lên giao diện
        self.uic.plate.setText(chuoi)
        
        # Biển số xe đã detect
        self.out_file = "D:\IT04\hk2\CT208_NL\Project\\result_predict\imgDetected.jpg"
        self.uic.img_detect.setPixmap(QPixmap(self.out_file))

    def show(self): #hiển thị
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow() #màn hình chính
    main_win.show()
    sys.exit(app.exec()) #nút thoát