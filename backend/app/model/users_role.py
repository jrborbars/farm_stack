from sqlalchemy import Column, String, table
from sqlmodel import SQLModel, Field, Relationship
from app.model.mixins import TimeMixin
from typing import Optional, List


class UsersRole(SQLModel, TimeMixin, table=True):
    __tablename__="user_role"
    id:Optional[str] = Field(None, primary_key=True, nullable=False)
    users_id : Optional[str] = Field(default=None,foreign_key="users.id", primary_key=True)
    role_id : Optional[str] = Field(default=None,foreign_key="role.id", primary_key=True)