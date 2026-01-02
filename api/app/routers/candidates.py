from fastapi import APIRouter
from app.core.queue import task_queue
from app.core.tasks import send_candidate_notification

router = APIRouter(prefix="/candidates", tags=["Candidates"])

@router.post("/{candidate_id}/notify")
def notify_candidate(candidate_id: int):
    task_queue.enqueue(send_candidate_notification, candidate_id)
    return {"message": "Notification queued"}
