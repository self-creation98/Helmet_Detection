from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TrainingConfig:
    """Training defaults used by the CLI and notebook examples."""

    data_yaml: Path
    model_path: Path = Path("yolov10n.pt")
    epochs: int = 100
    image_size: int = 640
    batch_size: int = 16
    project: Path = Path("runs/detect")
    run_name: str = "helmet-yolov10"

    @property
    def best_weights_path(self) -> Path:
        return self.project / self.run_name / "weights" / "best.pt"
