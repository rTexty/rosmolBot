from typing import Annotated

from sqlalchemy import Column, BigInteger, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from database.database import Base


intpk = Annotated[int, mapped_column(BigInteger, primary_key=True)]


class Admins(Base):
    __tablename__ = "admins"

    user_id: Mapped[intpk]

    name: Mapped[str]

    direction: Mapped[str]


class Tasks(Base):
    __tablename__ = "tasks"
    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    task: Mapped[str] = mapped_column(String(150), nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
