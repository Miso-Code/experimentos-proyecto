import math
import random

from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse

from ..services.nutritional_plan import NutritionalPlanService

router = APIRouter(
    prefix="/nutritional-plan",
    tags=["nutritional-plan"],
    responses={404: {"description": "Not found"}},
)


@router.post("/{user_id}/notify-caloric-intake")
async def notify_caloric_intake(user_id: str, alert_service: NutritionalPlanService = Depends()):
    alert_service.notify_caloric_intake(user_id)
    return JSONResponse(status_code=200, content={"message": "Notification sent successfully"})
