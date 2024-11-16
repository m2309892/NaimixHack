from sqlalchemy import JSON, TIMESTAMP, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from datetime import datetime
from typing import TYPE_CHECKING

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.user import User


class ActionLogs(Base):
    __tablename__ = 'action_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP)
    action: Mapped[JSON] = mapped_column(JSON)

    user: Mapped["User"] = relationship()
