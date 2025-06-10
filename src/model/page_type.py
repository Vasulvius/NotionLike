from enum import Enum


class PageType(str, Enum):
    """Types de pages disponibles"""

    DOCUMENT = "document"
    DATABASE = "database"
    KANBAN = "kanban"
    CALENDAR = "calendar"
