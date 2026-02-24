##⛑️ Safety Helmet Detection (YOLOv10)
Dự án này sử dụng mô hình YOLOv10 để tự động nhận diện người lao động có trang bị mũ bảo hiểm trong các môi trường công nghiệp hoặc tham gia giao thông. Notebook được thiết kế để chạy hoàn toàn trên môi trường Google Colab, tận dụng miễn phí GPU T4.

##🎯 Mục tiêu dự án
Tự động phát hiện đối tượng: Người đội mũ (Helmet) và Người không đội mũ (No Helmet).

Ứng dụng công nghệ Deep Learning mới nhất (YOLOv10) để đạt tốc độ xử lý nhanh và độ chính xác cao.

Cung cấp giải pháp giám sát an toàn lao động tự động.

##🚀 Hướng dẫn sử dụng

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1q8eSCoqspfTDlR--xRAlUPVNaz59_wzG?usp=sharing)

Mở Notebook: Click vào biểu tượng Open In Colab ở phía trên.

Cài đặt môi trường: * Chạy ô code đầu tiên để cài đặt thư viện ultralytics và tải cấu hình mô hình YOLOv10.

Đảm bảo bạn đã đổi Runtime sang T4 GPU (Runtime -> Change runtime type -> T4 GPU).

Dữ liệu (Dataset):

Notebook sẽ tự động tải bộ dữ liệu (nếu có link gdown) hoặc hướng dẫn bạn upload ảnh/video cần nhận diện lên thư mục /content/.

Chạy nhận diện (Inference):

Kết quả ảnh/video đã được vẽ khung nhận diện (Bounding Box) sẽ được lưu tại thư mục runs/detect/predict/.

##🛠️ Công nghệ sử dụng
YOLOv10: Kiến trúc mạng nơ-ron tích chập tối ưu cho việc phát hiện vật thể thời gian thực.
[YOLOv10 by THU-MIG](https://github.com/THU-MIG/yolov10)

OpenCV: Xử lý hình ảnh và video đầu vào.

Google Colab: Môi trường huấn luyện và chạy thử nghiệm.


##📊 Kết quả Demo
![89572463-0990-4f55-a2e6-62982f7faf95](https://github.com/user-attachments/assets/ef6ab985-6d63-43c1-9d07-d9c15dd778d4)

