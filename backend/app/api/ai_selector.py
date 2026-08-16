from fastapi import APIRouter

router = APIRouter(
    prefix="/ai-selector",
    tags=["AI Selector"]
)


@router.get("/health")
def health():
    return {
        "status": "ok",
        "module": "ai_selector"
    }
