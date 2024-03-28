from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/users',
                   tags=['users'],
                   responses={200: {"msg": "Success to get data"},
                              400: {"msg": "Not found"}},
                   )


# api/v1/users/{user_id}
@router.get("/{user_id}", 
            status_code=200, 
            tags=["items", "payment"], 
            summary="특정 아이템 가져오기", 
            description="Item 모델에서 item_id 값을 가지고 특정 아이템 조회")
def get_item(item_id: str):
    return {'items': item_id}