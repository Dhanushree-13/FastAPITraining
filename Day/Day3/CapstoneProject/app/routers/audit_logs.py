from fastapi import APIRouter

router = APIRouter()


@router.get("/audit-logs")
def get_audit_logs():
    return {"message": "Audit logs"}