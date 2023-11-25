from sqlalchemy import select, update, delete, insert


def create_select(model, *filters):
    if filters:
        query = select(model).filter(*filters)
    else:
        query = select(model)
    return query


def create_select_by_id(model, entity_id: int, user_id: int):
    query = select(model).where(model.id == entity_id)
    return query


def create_delete(model, entity_id: int, user_id: int):
    if user_id:
        stmt = delete(model).returning(model.user_id).where(model.id == entity_id)
    else:
        stmt = delete(model).where(model.id == entity_id)
    return stmt
