#! /usr/bin/env/ python3

# from datetime import datetime, timezone
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel, Field, ValidationError

# from typing_extensions import Annotated


class CreateTask(BaseModel):

    task: str = Field(..., example="Buy groceries", min_length=1)
    completed: bool = Field(default=False, example=False)
    create_date: str = Field(default=None)


class CompleteTask(BaseModel):
    task: str = Field(..., example="Buy groceries", min_length=1)
    completed: bool = Field(default=False, example=False)
    complete_date: str = Field(default=None)


class ClientResponse:
    """Standard outbound response"""
    success: bool = Field(...)
    message: Optional[Union[str, Dict[str, Any]]]
