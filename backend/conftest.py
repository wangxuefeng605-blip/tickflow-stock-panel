import sys
from pathlib import Path

AI_SELECTOR = Path(__file__).parent / "ai_selector"

if str(AI_SELECTOR) not in sys.path:
    sys.path.insert(0, str(AI_SELECTOR))