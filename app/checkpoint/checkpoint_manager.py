import json
from pathlib import Path

from app.checkpoint.checkpoint import Checkpoint


class CheckpointManager:
    """
    Stores workflow checkpoints on disk.
    """

    ROOT = Path("checkpoints")

    def __init__(self):

        self.ROOT.mkdir(
            exist_ok=True,
        )

    def save(
        self,
        checkpoint: Checkpoint,
    ) -> None:

        path = self.ROOT / f"{checkpoint.workflow_id}.json"

        path.write_text(
            checkpoint.model_dump_json(
                indent=4,
            )
        )

    def load(
        self,
        workflow_id: str,
    ) -> Checkpoint | None:

        path = self.ROOT / f"{workflow_id}.json"

        if not path.exists():
            return None

        return Checkpoint.model_validate_json(
            path.read_text()
        )

    def delete(
        self,
        workflow_id: str,
    ) -> None:

        path = self.ROOT / f"{workflow_id}.json"

        if path.exists():
            path.unlink()