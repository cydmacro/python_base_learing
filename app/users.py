from fastapi import APIRouter, HTTPException,Depends, Header
from pydantic import BaseModel
def verify_token(token: str = Header(...)):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return token

router = APIRouter(
    prefix="/api/users/v1",
    tags=["用户管理"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(verify_token)]
)



class UserCreate(BaseModel):
    username: str
    password: str

@router.post("/register", status_code=200,dependencies=[Depends(verify_token)])
async def register(user: UserCreate):
    """用户注册接口"""
    # 实际应保存到数据库
    return {"message": "用户创建成功", "username": user.username}

@router.get("/{user_id}")
async def get_user(user_id: int):
    if user_id > 100:
        raise HTTPException(404, "用户不存在")
    return {"user_id": user_id, "name": "虚拟用户"}

@router.get("/list")
async def list_users():
    return [{"id": 1, "name": "alice"},{"id": 2, "name": "jack"}]
