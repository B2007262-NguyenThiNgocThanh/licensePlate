from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8m.pt")  # load a pretrained model (recommended for training)

# đoạn mã xử lý lỗi của dataset
import os
from PIL import Image


# Đường dẫn đến thư mục chứa các hình ảnh, txt để huấn luyện mô hình
directory_train_img = '/IT04/hk2/CT208_NL/Project/dataset/images/train'
# directory_train_label = '/IT04/hk2/CT208_NL/Project/dataset/labels/train'
# Duyệt qua từng tệp hình ảnh trong thư mục
for filename in os.listdir(directory_train_img):
    try:
        # Kiểm tra nếu tệp đang xét là tệp hình ảnh (ví dụ: JPEG)
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            # Load hình ảnh
            image_path = os.path.join(directory_train_img, filename)
            image = Image.open(image_path)
            
            # Xử lý hình ảnh ở đây
            # Ví dụ: Thay đổi kích thước, xoay, cắt, v.v.
            
            # Lưu hình ảnh sau khi xử lý
            image.save(image_path)
            # print(f"Processed image: {filename}")

            # # Tạo đường dẫn tuyệt đối đến tệp nhãn tương ứng
            # label_filename = os.path.splitext(filename)[0] + '.txt'
            # label_path = os.path.join(directory_train_img, label_filename)

            # # Kiểm tra xem có tồn tại tệp nhãn tương ứng không
            # if not os.path.exists(label_filename):
            #     print(f"Missing label for image: {filename}")

    except Exception as e:
        print(f"Error processing image {filename}: {e}")


directory_val_img = '/IT04/hk2/CT208_NL/Project/dataset/images/val'
# directory_val_label= '/IT04/hk2/CT208_NL/Project/dataset/labels/val'
# Duyệt qua từng tệp label trong thư mục
for filename in os.listdir(directory_val_img):
    try:
        # Kiểm tra nếu tệp đang xét là tệp hình ảnh (ví dụ: JPEG)
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            # Load hình ảnh
            image_path = os.path.join(directory_val_img, filename)
            image = Image.open(image_path)
            
            # Xử lý hình ảnh ở đây
            # Ví dụ: Thay đổi kích thước, xoay, cắt, v.v.
            
            # Lưu hình ảnh sau khi xử lý
            image.save(image_path)
            # print(f"Processed image: {filename}")

            # Tạo đường dẫn tuyệt đối đến tệp nhãn tương ứng
            # label_filename = os.path.splitext(filename)[0] + '.txt'
            # label_path = os.path.join(directory_val_label, label_filename)

            #  # Kiểm tra xem có tồn tại tệp nhãn tương ứng không
            # if not os.path.exists(label_path):
            #     print(f"Missing label for image: {filename}")
    except Exception as e:
        print(f"Error processing image {filename}: {e}")


# Use the model
results = model.train(data="config.yaml", epochs=15, imgsz = 512)  # train the model -> train 2
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
# path = model.export(format="onnx")  # export the model to ONNX