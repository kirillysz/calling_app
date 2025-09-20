from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Integer, String

from auth_service.db.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto", index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)

    phone: Mapped[str] = mapped_column(String, nullable=False)
    verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
