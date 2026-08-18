"""pytest configuration for Tools/tests.

The tools are plain scripts, not a package. This file puts <repo>/Tools on sys.path so
they import as modules (``import audio_lineage``, ``import bounce_tempo``) no matter where
pytest is launched from -- ``py -m pytest Tools/tests -q`` at the repo root is the
documented command. Nothing in the tools themselves is touched.

Fixtures:
    cv2             -- the OpenCV module, or a clean skip when opencv-python is not installed
    ffmpeg_on_path  -- skips cleanly when ffmpeg / ffprobe are not on PATH
Both exist for the one optional end-to-end video test; every other test is pure numpy.
"""
import shutil
import sys
from pathlib import Path

import pytest

TOOLS_DIR = Path(__file__).resolve().parents[1]  # <repo>/Tools
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "video: end-to-end test that writes a tiny synthetic clip (needs cv2 + ffmpeg); "
        "deselect with -m 'not video'",
    )


@pytest.fixture
def cv2():
    """OpenCV, or skip the requesting test if opencv-python is missing or will not import."""
    try:
        import cv2 as _cv2  # noqa: F401 -- optional dependency, imported lazily on purpose
    except ImportError as exc:  # ModuleNotFoundError, or a broken install (missing DLLs etc.)
        pytest.skip(f"opencv-python (cv2) unavailable ({exc}) - video test skipped")
    return _cv2


@pytest.fixture
def ffmpeg_on_path():
    """Skip the requesting test if ffmpeg or ffprobe is missing (bounce_tempo.frames needs both)."""
    missing = [exe for exe in ("ffmpeg", "ffprobe") if shutil.which(exe) is None]
    if missing:
        pytest.skip(f"{' and '.join(missing)} not on PATH - video test skipped")
