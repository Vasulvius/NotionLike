from framefox.core.orm.abstract_entity import AbstractEntity
from sqlmodel import JSON, Column, Field, Relationship

from src.model.page_type import PageType


class Page(AbstractEntity, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=256, nullable=False)
    content: str = Field(max_length=256, nullable=True)
    page_type: PageType = Field(default=PageType.DOCUMENT)
