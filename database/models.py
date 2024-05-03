from typing import Annotated

from sqlalchemy import Column, BigInteger, String, Text, Boolean, ForeignKey, text
from sqlalchemy.orm import relationship, mapped_column, Mapped

from database.database import Base



class Admins(Base):
    __tablename__ = "admins"

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    name: Mapped[str]

    direction: Mapped[str]

    manager: Mapped[bool] = mapped_column(default=False, nullable=True)

    username: Mapped[str] = mapped_column(Text, nullable=True)


class Tasks(Base):
    __tablename__ = "tasks"
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    task: Mapped[str] = mapped_column(String(150), primary_key=True, nullable=True)
    is_completed: Mapped[bool] = mapped_column(default=False)
    username: Mapped[str] = mapped_column(Text, nullable=True)
    creator: Mapped[str] = mapped_column(Text, nullable=True)
