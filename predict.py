# from ultralytics import YOLO
# from tkinter import*
# from PIL import Image, ImageTk

# # import sys #thư viện lưu trữ thông tin code cơ bản
# # import cv2
# # import numpy as np
# # from time import time
# # import torch
# # from PyQt6 import QtGui
# # from PyQt6.QtCore import QThread, pyqtSignal, Qt
# # #lấy ra ứng dụng trong thư viện #Lấy ra giao diện chính #lấy file hình
# # from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog 
# # from PyQt6.QtGui import QPixmap

# model = YOLO("/IT04/hk2/CT208_NL/Project/runs/detect/train15/weights/best.pt")

# result = model('/IT04/hk2/CT208_NL/Project/hinh2.jpg')

# for r in result:
#     # print(r.boxes)
#     img_arr = r.plot()
#     img = Image.fromarray(img_arr[..., ::-1])
#     # print(img_arr)
#     # img.show()
#     img.save('/IT04/hk2/CT208_NL/Project/result_predict/hinh2_1.jpg')

# # window = Tk()
# # window.title('NHẬN DIỆN BIỂN SỐ XE VỚI YOLOV8')

# # #function 

# # def url():
# #     # model = YOLO("/IT04/hk2/CT208_NL/Project/runs/detect/train4/weights/best.pt")
# #     link = QFileDialog.getOpenFileName(filter = "*.png *.jpg *.jpeg")
# #     return link

# # # img_import = (Image.open(r'D:/IT04/hk2/CT208_NL/Project/hinh1.jpg'))

# # #Thêm các control
# # lb0 = Label(window, text='Image', font=('Time Nem Roman', 20))
# # lb0.grid(column=1, row=1)

# # lb1 = Label(window, text='', font=('Time Nem Roman', 20))
# # lb1.grid(column=0, row=1)

# # #GUI img
# # imgText = Text(window, height=20, width=50)
# # imgText.grid(column=1, row=2)
# # #------
# # lb2=Label(window, text='', font=('Time New Roman', 20))
# # lb2.grid(column=1, row=3)
# # #------ link img
# # urlImg = Text(window, height=2, width=40)
# # urlImg.grid(column=1, row=4)

# # # box
# # boxPlateTitle = Label(window,text='Biển Số ', font=("Time New Roman", 15))
# # boxPlateTitle.grid(column=2, row=2)
# # boxPlate = Text(window, height=2.5, width=30)
# # boxPlate.grid(column=4, row = 2)

# # #----------------
# # insertButtonImage = Button(window, text='SELECT', font=("Arial Bolder", 15), command=url)
# # insertButtonImage.grid(column=2, row = 4)
# # #----------------
# # lb3 = Label(window, text='', font=('Time Nem Roman', 20))
# # lb3.grid(column=3, row=4)
# # #----------------
# # predictButtonImage = Button(window, text='PREDICT', font=("Arial Bolder", 15))
# # predictButtonImage.grid(column=4, row = 4)
# # #----------------
# # lb4 = Label(window, text='', font=('Time Nem Roman', 20))
# # lb4.grid(column=5, row=4)
# # #----------------
# # stopButtonImage = Button(window, text='STOP', font=("Arial Bolder", 15))
# # stopButtonImage.grid(column=6, row = 4)





# # window.geometry('1000x600')
# # window.mainloop()