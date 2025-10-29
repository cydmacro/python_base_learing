from fastapi import APIRouter

router = APIRouter(
    prefix="/api/product/v1",
    tags=["商品管理"],
    responses={404: {"description": "Not found"}},
    dependencies=[]
)


@router.get("/search", summary="商品搜索")
async def search_products(q: str,min_price: float = None,max_price: float = None):
    # 实现搜索逻辑
    return {"message": "搜索成功"}

@router.get("/{product_id}", summary="获取商品详情")
async def get_product_details(product_id: int):
    return {"id": product_id}