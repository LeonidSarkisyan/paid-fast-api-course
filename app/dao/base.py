from sqlalchemy import select, update, delete, insert

from app.database import async_session_maker
from app.dao.sqlmaker import create_select, create_delete, create_select_by_id
from app.dao.protect import check_protect


class BaseDAO:
    model = None
    parent_field = None
    protect: bool = None

    @classmethod
    async def get_all(cls, *filters):
        async with async_session_maker() as session:
            query = create_select(cls.model, *filters)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_by_id(cls, entity_id: int, user_id: int = 0):
        async with async_session_maker() as session:
            query = create_select_by_id(cls.model, entity_id, user_id)
            result = await session.execute(query)
            result = result.scalar()
            if check_protect(cls.protect, user_id, result.user_id):
                return result

    @classmethod
    async def delete_by_id(cls, entity_id: int, user_id: int = 0):
        async with async_session_maker() as session:
            stmt = create_delete(cls.model, entity_id, user_id)
            result = await session.execute(stmt)
            if user_id:
                result_user_id = result.scalar()
            return await check_protect(cls.protect, user_id, result_user_id)

