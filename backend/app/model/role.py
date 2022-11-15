from sqlalchemy import Column, String, table
from sqlmodel import SQLModel, Field, Relationship
from app.model.mixins import TimeMixin
from typing import Optional, List
from app.model.users_role import UsersRole
from app.model.users import Users


class Role(SQLModel, TimeMixin, table=True):
    __tablename__="role"
    id:Optional[str] = Field(None, primary_key=True, nullable=False)
    role_name:str
    users: List["Users"] = Relationship(back_populates="roles", link_model=UsersRole)