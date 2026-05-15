import argparse
from pathlib import Path

from safety_helmet_detection.config import TrainingConfig
from safety_helmet_detection.yolo_pipeline import predict, train, validate


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="helmet-detect",
        description="Train, validate, and run YOLOv10 safety helmet detection.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    train_parser = subparsers.add_parser("train", help="Train a YOLOv10 helmet detector.")
    train_parser.add_argument("--data", required=True, type=Path, help="Path to data.yaml.")
    train_parser.add_argument("--model", default=Path("yolov10n.pt"), type=Path, help="Initial weights.")
    train_parser.add_argument("--epochs", default=100, type=int)
    train_parser.add_argument("--imgsz", default=640, type=int)
    train_parser.add_argument("--batch", default=16, type=int)
    train_parser.add_argument("--project", default=Path("runs/detect"), type=Path)
    train_parser.add_argument("--name", default="helmet-yolov10")

    val_parser = subparsers.add_parser("val", help="Validate trained weights.")
    val_parser.add_argument("--weights", required=True, type=Path)
    val_parser.add_argument("--data", required=True, type=Path)
    val_parser.add_argument("--imgsz", default=640, type=int)
    val_parser.add_argument("--split", default="test", choices=["train", "val", "test"])

    predict_parser = subparsers.add_parser("predict", help="Run inference and save annotated outputs.")
    predict_parser.add_argument("--weights", required=True, type=Path)
    predict_parser.add_argument("--source", required=True, help="Image, video, directory, URL, or stream source.")
    predict_parser.add_argument("--output", default=Path("runs/detect/predict"), type=Path)
    predict_parser.add_argument("--conf", default=0.25, type=float)

    return parser


def main() -> None:
    args = _build_parser().parse_args()

    if args.command == "train":
        config = TrainingConfig(
            data_yaml=args.data,
            model_path=args.model,
            epochs=args.epochs,
            image_size=args.imgsz,
            batch_size=args.batch,
            project=args.project,
            run_name=args.name,
        )
        train(config)
        return

    if args.command == "val":
        validate(args.weights, args.data, image_size=args.imgsz, split=args.split)
        return

    if args.command == "predict":
        predict(args.weights, args.source, output_dir=args.output, confidence=args.conf)
        return


if __name__ == "__main__":
    main()
