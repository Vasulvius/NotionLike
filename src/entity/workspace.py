from sqlmodel import Field, JSON, Column, Relationship
from framefox.core.orm.abstract_entity import AbstractEntity


class Workspace(AbstractEntity, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=256, nullable=False)
    description: str = Field(max_length=256, nullable=False)
