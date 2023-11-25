from typing import Optional
from datetime import date
from dataclasses import dataclass

from fastapi import FastAPI, Query, Depends

from pydantic import BaseModel

from app.bookings.router import router as router_bookings


app = FastAPI(title='Бронирование отелей')

app.include_router(router_bookings)


@dataclass
class HotelSearchArgs:
    location: str
    date_from: date
    date_to: date
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5)


@app.get('/hotels/{location}')
async def get_hotels(
    search_args: HotelSearchArgs = Depends()
):
    print(search_args)
    return search_args


class SBookingPost(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
async def add_booking(booking: SBookingPost):
    return booking
