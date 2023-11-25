from typing import Optional, List

from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Rooms(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    services: Mapped[Optional[List[str]]] = mapped_column(JSON, nullable=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    image_id: Mapped[int]

    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
