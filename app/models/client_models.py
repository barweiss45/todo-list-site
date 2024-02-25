#! /usr/bin/env/ python3

# from datetime import datetime, timezone
# from typing import Optional

from pydantic import BaseModel, Field

# from typing_extensions import Annotated


class ClientRequest(BaseModel):
    task: str = Field(..., example="Buy groceries", min_length=1)
    completed: bool = Field(default=False, example=False)
    create_date: str = Field(default=None)
