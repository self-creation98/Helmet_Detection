# Safety Helmet Detection with YOLOv10

Dự án huấn luyện và chạy inference mô hình YOLOv10 để phát hiện người có đội mũ bảo hộ và không đội mũ bảo hộ trong ảnh hoặc video.

## Điểm chính

- Huấn luyện mô hình YOLOv10 trên dataset `Helmet` / `No Helmet`.
- Chạy dự đoán trên ảnh, video, thư mục ảnh hoặc nguồn stream mà Ultralytics hỗ trợ.
- Có thể chạy bằng notebook trên Google Colab hoặc bằng CLI Python trong môi trường local.
- Cấu trúc project đã tách phần pipeline ra khỏi notebook để dễ bảo trì và mở rộng.

## Cấu trúc

```text
.
├── Project_YOLOv10_Image_Dectection.ipynb
├── src/
│   └── safety_helmet_detection/
│       ├── cli.py
│       ├── config.py
│       └── yolo_pipeline.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Chạy trên Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1q8eSCoqspfTDlR--xRAlUPVNaz59_wzG?usp=sharing)

Khuyến nghị chọn GPU trước khi chạy:

```text
Runtime -> Change runtime type -> T4 GPU
```

Notebook đã được sắp xếp theo luồng:

1. Cài đặt thư viện.
2. Tải pretrained weights và dataset.
3. Huấn luyện mô hình.
4. Đánh giá trên tập test.
5. Chạy dự đoán và lưu kết quả.

## Chạy local

Tạo môi trường ảo và cài dependency:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

Huấn luyện:

```bash
helmet-detect train ^
  --data data/safety_helmet_data/data.yaml ^
  --model weights/yolov10n.pt ^
  --epochs 100 ^
  --imgsz 640 ^
  --batch 16
```

Đánh giá:

```bash
helmet-detect val ^
  --weights runs/detect/helmet-yolov10/weights/best.pt ^
  --data data/safety_helmet_data/data.yaml ^
  --split test
```

Dự đoán:

```bash
helmet-detect predict ^
  --weights runs/detect/helmet-yolov10/weights/best.pt ^
  --source samples/construction-worker.jpg ^
  --output runs/detect/predict ^
  --conf 0.25
```

Kết quả inference được lưu trong thư mục `runs/detect/predict`.

## Dataset

Notebook hiện tải dataset bằng Google Drive ID:

```text
1l7USE19C7ABIjBjArB4Rb9w3OL6k86xP
```

Sau khi giải nén, file cấu hình dataset cần có dạng:

```text
safety_helmet_data/
└── data.yaml
```

## Công nghệ

- [YOLOv10 by THU-MIG](https://github.com/THU-MIG/yolov10)
- [Ultralytics](https://docs.ultralytics.com/)
- OpenCV
- Google Colab

## Demo

![Safety helmet detection demo](https://github.com/user-attachments/assets/ef6ab985-6d63-43c1-9d07-d9c15dd778d4)
