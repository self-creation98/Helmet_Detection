from pathlib import Path
from typing import Any

from safety_helmet_detection.config import TrainingConfig


def load_model(weights_path: str | Path) -> Any:
    """Load a YOLO model lazily so importing this package stays lightweight."""
    from ultralytics import YOLO

    return YOLO(str(weights_path))


def train(config: TrainingConfig) -> Any:
    """Train the helmet detector using the supplied configuration."""
    model = load_model(config.model_path)
    return model.train(
        data=str(config.data_yaml),
        epochs=config.epochs,
        imgsz=config.image_size,
        batch=config.batch_size,
        project=str(config.project),
        name=config.run_name,
    )


def validate(weights_path: str | Path, data_yaml: str | Path, image_size: int = 640, split: str = "test") -> Any:
    """Validate trained weights against a dataset split."""
    model = load_model(weights_path)
    return model.val(data=str(data_yaml), imgsz=image_size, split=split)


def predict(
    weights_path: str | Path,
    source: str | Path,
    output_dir: str | Path = "runs/detect/predict",
    confidence: float = 0.25,
) -> list[Any]:
    """Run inference on an image, video, folder, or stream supported by Ultralytics."""
    model = load_model(weights_path)
    return model.predict(
        source=str(source),
        conf=confidence,
        project=str(Path(output_dir).parent),
        name=Path(output_dir).name,
        save=True,
    )
