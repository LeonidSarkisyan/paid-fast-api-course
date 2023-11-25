from app.dao.base import BaseDAO
from app.bookings.models import Bookings


class BookingDAO(BaseDAO):
    model = Bookings
    parent_field = Bookings.room_id
    protect = True
