from datetime import datetime
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI(title="待办事项 API", version="1.0.0")


# 定义状态枚举
class TodoStatus(str, Enum):
    未完成 = "未完成"
    已完成 = "已完成"
    已取消 = "已取消"


# 定义待办事项数据模型
class TodoCreate(BaseModel):
    title: str = Field(..., description="待办事项标题（必填）")
    content: Optional[str] = Field(None, description="待办事项内容（可选）")
    deadline: datetime = Field(..., description="截止时间（格式 YYYY-MM-DD HH:MM:SS）")
    status: TodoStatus = Field(TodoStatus.未完成, description="状态（默认为未完成）")


class TodoUpdate(BaseModel):
    status: TodoStatus = Field(..., description="新的状态")


class TodoResponse(BaseModel):
    id: int
    title: str
    content: Optional[str]
    deadline: datetime
    status: TodoStatus
    created_at: datetime
    updated_at: datetime


# 模拟数据库存储
todos_db = []
next_id = 1


@app.post("/api/todos", response_model=TodoResponse, summary="创建待办")
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = {
        "id": next_id,
        "title": todo.title,
        "content": todo.content,
        "deadline": todo.deadline,
        "status": todo.status,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    todos_db.append(new_todo)
    next_id += 1
    return new_todo


@app.get("/api/todos", response_model=List[TodoResponse], summary="查询所有待办")
def get_todos(status: Optional[TodoStatus] = Query(None, description="按状态筛选")):
    filtered_todos = todos_db
    if status:
        filtered_todos = [todo for todo in todos_db if todo["status"] == status]
    return filtered_todos


@app.get("/api/todos/{todo_id}", response_model=TodoResponse, summary="查询单个待办")
def get_todo(todo_id: int):
    for todo in todos_db:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="待办事项不存在")


@app.patch("/api/todos/{todo_id}/status", response_model=TodoResponse, summary="更新待办状态")
def update_todo_status(todo_id: int, update_data: TodoUpdate):
    for todo in todos_db:
        if todo["id"] == todo_id:
            todo["status"] = update_data.status
            todo["updated_at"] = datetime.now()
            return todo
    raise HTTPException(status_code=404, detail="待办事项不存在")


@app.delete("/api/todos/{todo_id}", summary="删除待办")
def delete_todo(todo_id: int):
    global todos_db
    initial_length = len(todos_db)
    todos_db = [todo for todo in todos_db if todo["id"] != todo_id]

    if len(todos_db) == initial_length:
        raise HTTPException(status_code=404, detail="待办事项不存在")

    return {"message": f"待办事项 {todo_id} 删除成功"}
