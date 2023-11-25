from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings


router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования']
)


@router.get('/')
async def get_bookings():
    return await BookingDAO.get_all(Bookings.user_id == user.id)

