from datetime import datetime
from sqlalchemy import TIMESTAMP, FetchedValue
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import event


class Base(DeclarativeBase):
    pass


# region Traits
class HasDates:
    """
    Создаёт поля "created_at" и "updated_at"
    Автоматически обновляет поле "updated_at"
    """
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default='NOW()')
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default='NOW()', onupdate=datetime.now)




# endregion
