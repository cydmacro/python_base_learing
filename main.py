
import asyncio
import time
import httpx
from typing import Union
from fastapi import FastAPI, HTTPException,Header,Request,Depends
from fastapi.responses import JSONResponse
from app import users,products
import uvicorn
from fastapi.responses import StreamingResponse
def verify_token(token: str = Header(...)):
    if token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return token

#app = FastAPI(dependencies=[Depends(verify_token)])
app = FastAPI()
app.include_router(users.router)
app.include_router(products.router)


#定义一个依赖项
def common_params(query: str=None,page: int=1):
    print("common_params 执行了")
    page = page+1
    return {"query": query, "page": page}


#定义路由使用依赖项
@app.get("/dependency_example")
async def dependency_example(params: dict = Depends(common_params)):
    print("dependency_example 执行了")
    return params



class DatabaseSession:
    def __init__(self):
        self.session = "模拟数据库连接"
    
    def close(self):
        print("关闭数据库连接")

def get_db():
    db = DatabaseSession()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/")
async def get_users(db: DatabaseSession = Depends(get_db)):
    return {"db_session": db.session}



class Pagination:
    def __init__(self,page: int=1,size:int=10):
        print("Pagination  __init__ 执行了")
        self.page = page
        self.size = size

@app.get("/pagination")
async def pagination(pagination: Pagination=Depends()):
    print("pagination 接口 执行了")
    return {"page": pagination.page, "size": pagination.size}







for route in app.routes:
    print(route.path, route.methods)


if __name__ == '__main__':
    uvicorn.run(app,port=8001)







# from pydantic import BaseModel, Field,field_validator

# # 用户注册模型
# class UserRegister(BaseModel):
#     username: str          # 必填字段
#     password: str 
    
#     @field_validator("password")
#     def validate_password(cls, v):
#         if len(v) < 8:
#             raise ValueError("至少 8 个字符")
#         if not any(c.isupper() for c in v):
#             raise ValueError("至少一个大写字母")
#         return v
    
# @app.post("/register",tags=["用户管理"])
# async def register(user: UserRegister):
#     # 注册逻辑
#     return {"message": "注册成功","username": user.username}






# class Product(BaseModel):
#     name: str
#     price: float
#     description: Union[str, None] = None
#     tax: Union[float, None] = None


# @app.post("/create_product",tags=["商品管理"])
# async def create_product(product: Product):
#     # 产品数据
#     #return product.model_dump()
#     return product








# #定义一个异步函数
# async def fetch_data(url : str):
#     async with httpx.AsyncClient() as client:
#         resp = await client.get(url)
#         return resp.json()
    

# #定义一个接口获取聚合数据
# @app.get("/get_data")
# async def get_data():
#     start_time = time.time()
#     urls = [
#         "https://api-v2.cydh.net/api/teacher/v1/list",
#         "https://api-v2.cydh.net/api/funny/v1/get_funny",
#         "https://api-v2.cydh.net/api/page_item/v1/list?type=HOME_CATEGORY_BOTTOM",
#         "http://127.0.0.1:8000/test1",
#         "http://127.0.0.1:8000/test2"
#     ]
#     tasks = [fetch_data(url) for url in urls]
    
#     result = await asyncio.gather(*tasks)

#     print(f"总耗时：{time.time() - start_time}秒")
#     return result
    

# @app.get("/test1")
# def test1():
#     print("test1 执行")
#     time.sleep(3)
#     return {"status": "test1 done"}

# @app.get("/test2")
# def test2():
#     print("test2 执行")
#     time.sleep(3)
#     return {"status": "test2 done"}




# # 同步路由执行（顺序阻塞）
# @app.get("/sync_func")
# def sync_endpoint():
#     # 模拟耗时操作
#     print("开始任务1")  # 立即执行
#     time.sleep(3)      # 阻塞3秒
#     print("开始任务2")  # 3秒后执行
#     return {"status": "done"}

# # 异步执行（非阻塞切换）
# @app.get("/async_func")
# async def async_endpoint():  # 异步接口
#     # 必须使用异步库
#     print("开始任务A")   # 立即执行
#     await asyncio.sleep(3)  # 释放控制权,异步等待
#     print("开始任务B")   # 3秒后恢复执行
#     return {"status": "done"}







# @app.get("/")
# def read_root():
#     return {"Hello": "World cydh.net"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int):  # 自动类型转换和验证
#     return {"item_id": item_id}

# @app.post("/items/")
# def create_item(item: dict):
#     return {"item": item}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: dict):
#     return {"item_id": item_id, "updated_item": item}

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     return {"status": "deleted", "item_id": item_id}


# @app.get("/header")
# def header(item_id: int, token: str = Header("token")):
#     return {"item_id": item_id, "token": token}
    

# #获取全部请求头
# @app.get("/request_headers")
# def request_headers(request: Request):
#     return dict(request.headers)


# #自定义响应头
# @app.get("/custom_response_headers")
# def custom_response_headers():
#    content = {"message": "Hello, World! 学习python"}
#    headers = {"X-Custom-Header": "Custom Value cydh.net"}
#    return JSONResponse(content=content, headers=headers,status_code=300)



# from fastapi import  status,Response

# @app.get("/status_code", status_code=200)
# def create_item(name: str):
#     if name == "Foo":
#         return Response(status_code=status.HTTP_404_NOT_FOUND)
#     return {"name": name}





