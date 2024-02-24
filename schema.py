#! /usr/bin/env python3

from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional
from typing_extensions import Annotated

tz = timezone.utc


class BaseToDo(BaseModel):
    task: str = Field(..., example="Buy groceries", min_length=1)
    completed: bool = Field(default=False, example=False)
    create_date: datetime = Field(default_factory=datetime.now(tz).astimezone().isoformat())


class CreateToDo(BaseToDo):
    pass


class Modify(BaseToDo):
    pass