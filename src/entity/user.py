from framefox.core.orm.abstract_entity import AbstractEntity
from sqlmodel import JSON, Column, Field, Relationship


class User(AbstractEntity, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str = Field(nullable=False)
    email: str = Field(nullable=False)
    roles: list[str] = Field(default_factory=lambda: ["ROLE_USER"], sa_column=Column(JSON))
