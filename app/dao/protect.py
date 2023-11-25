

async def check_protect(protect: bool, user_id: int, result_user_id: int = 0) -> bool:
    if not protect or user_id == result_user_id:
        await session.commit()
        return True
    else:
        await session.rollback()
        return False
