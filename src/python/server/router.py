import json

from fastapi import (FastAPI, Request, Response)

from config_dataclass import ConfigData
from worker_db import WorkerDB
from enums import FindByActionsEnum
from dep_funs import remove_file
from models import *
from fault_tolerancer import FaultTolerancer


app = FastAPI()
worker_db = WorkerDB(ConfigData.db_path)
fault_tolerancer = FaultTolerancer()


@app.get("/get_all_from_db")
async def get_all_from_db(request: Request):
    try:
        data = worker_db.get_all_from_db()
    except Exception as e:
        data = None
    return Response(content=json.dumps(data), media_type="application/json")


@app.post("/find_by")
async def find_by(request: Request, post_item: ActionInp):
    data = None

    if post_item.action == FindByActionsEnum.index.value:
        data = worker_db.find_by_id(int(post_item.inp))
    elif post_item.action == FindByActionsEnum.title.value:
        data = worker_db.find_by_title(post_item.inp)
    elif post_item.action == FindByActionsEnum.genre.value:
        data = worker_db.find_by_genre(post_item.inp)
    elif post_item.action == FindByActionsEnum.author.value:
        data = worker_db.find_by_author(post_item.inp)

    return Response(content=json.dumps(data), media_type="application/json")


@app.post("/add_item_to_db")
async def add_item_to_db(request: Request, post_item: DBModel):
    data = worker_db.add_item_to_db(post_item)
    if ConfigData.config_logging:
        fault_tolerancer.copy_db()
    return Response(content=json.dumps(data), media_type="application/json")


@app.put("/edit_by_index")
async def edit_by_index(request: Request, post_item: ItemIndex):
    data = worker_db.edit_by_index(post_item.index, post_item.item)
    if ConfigData.config_logging:
        fault_tolerancer.copy_db()
    return Response(content=json.dumps(data), media_type="application/json")


@app.put("/delete_by_index")
async def delete_by_index(request: Request, post_item: Index):
    data = None
    if not (post_item.index > worker_db.get_last_index() or post_item.index < 0):
        worker_db.delete_by_index(post_item.index)
        if ConfigData.config_logging:
            fault_tolerancer.copy_db()
        data = f"Item by index {post_item.index} deleted"
    return Response(content=json.dumps(data), media_type="application/json")


@app.delete("/delete_db")
async def delete_db(request: Request):
    data = None
    if remove_file(ConfigData.db_path) == 0:
        data = "File Removed"
    return Response(content=json.dumps(data), media_type="application/json")


@app.put("/restore_db")
async def restore_db(request: Request, post_item: Index):
    data = None
    if post_item.index < 11:
        data = fault_tolerancer.restore_db(post_item.index)
    return Response(content=json.dumps(data), media_type="application/json")
