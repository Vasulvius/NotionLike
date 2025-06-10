from typing import Any, Dict

from framefox.core.orm.abstract_entity import AbstractEntity
from sqlmodel import JSON, Column, Field, Relationship

from src.model.block_type import BlockType


class Block(AbstractEntity, table=True):
    id: int | None = Field(default=None, primary_key=True)
    block_type: BlockType = Field(default=BlockType.PARAGRAPH)
    content: Dict[str, Any] = Field(sa_column=Column(JSON))
    position: int = Field(nullable=False)
