from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
