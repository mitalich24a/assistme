import hashlib
import subprocess
import sys
from pathlib import Path


class PackageManager:
    """
    Ensures Python dependencies from requirements.txt are installed.
    """

    CACHE_DIR = Path(".bootstrap")
    CACHE_FILE = CACHE_DIR / "requirements.sha256"

    @classmethod
    def ensure_requirements(cls) -> None:

        requirements = Path("requirements.txt")

        if not requirements.exists():
            raise FileNotFoundError("requirements.txt not found.")

        current_hash = hashlib.sha256(
            requirements.read_bytes()
        ).hexdigest()

        cls.CACHE_DIR.mkdir(exist_ok=True)

        if cls.CACHE_FILE.exists():

            previous_hash = cls.CACHE_FILE.read_text()

            if previous_hash == current_hash:
                print("✓ Python packages already installed.")
                return

        print("Installing Python dependencies...")

        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "-r",
                str(requirements),
            ]
        )

        cls.CACHE_FILE.write_text(current_hash)

        print("✓ Dependencies installed.")