from pydantic import (BaseModel,
                      conint,
                      field_serializer)
from datetime import datetime


class DBModel(BaseModel):
    title: str
    author: list
    genre: list
    year: int
    width: conint(gt=0)
    height: conint(gt=0)
    cover: str
    source: str
    buy_date: str
    read_date: str
    rating: int

    @field_serializer('buy_date', 'read_date')
    @classmethod
    def convert_date(cls, v: str) -> datetime:
        return datetime.strptime(v, "%d-%m-%Y")


class ActionInp(BaseModel):
    action: int
    inp: str


class Index(BaseModel):
    index: int


class ItemIndex(BaseModel):
    item: DBModel
    index: conint(ge=0)
