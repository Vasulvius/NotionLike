from enum import Enum


class BlockType(str, Enum):
    """Types de blocs disponibles"""

    PARAGRAPH = "paragraph"
    HEADING_1 = "heading_1"
    HEADING_2 = "heading_2"
    HEADING_3 = "heading_3"
    BULLETED_LIST = "bulleted_list"
    NUMBERED_LIST = "numbered_list"
    TODO = "todo"
    QUOTE = "quote"
    CODE = "code"
    IMAGE = "image"
    DIVIDER = "divider"
