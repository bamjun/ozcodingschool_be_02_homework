[교제 링크](https://visioneer.notion.site/Fast-API-5d29c06e54bf46f4a5f7103b28faa345)  

# fastapi-backend-class [노션](https://visioneer.notion.site/02-FastAPI-2a8992e398204e00a86dae0774ebd4f4)  
- install fast api  

  &darr; `fastapi-backend-class\` &darr; `bash shell`
  ```bash
  pip install fastapi
  ```

<br>

- install uvicorn

  &darr; `fastapi-backend-class\` &darr; `bash shell`
  ```bash
  pip install 'uvicorn[standard]'
  ```

<br>

- fastapi 파일 `main.py` 생성

  &darr; `fastapi-backend-class\` &darr; `bash shell`
  ```bash
  touch main.py
  ```

<br>  

- `main.py` 파일작성  

  &darr; `fastapi-backend-class\` &darr; `main.py`
  ```python
  from fastapi import FastAPI

  app = FastAPI()


  @app.get("/")
  def read_root():
      return {"Hello": "World"}

  @app.get("/items/{item_id}")
  def read_item(item_id: int, q: str = None):
      return {"item_id": item_id, "q": q}


  if __name__ == "__main__":
      import uvicorn
      uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level='DEBUG', reload=True)
  ```
<br>

- 서버 실행 하기  

  &darr; `fastapi-backend-class\` &darr; `bash shell`
  ```bash
  uvicorn main:app --reload
  ```

<br>

- 결과 확인  

> 브라우저를 열고 **`http://127.0.0.1:8000`**로 이동합니다. "Hello: World"라는 JSON 응답을 볼 수 있습니다. 또한 FastAPI는 자동으로 API 문서를 생성합니다. **`http://127.0.0.1:8000/docs`** 또는 **`http://127.0.0.1:8000/redoc`**으로 이동하여 API 문서를 볼 수 있습니다.

![alt text](images/markdown-image.png)  

![alt text](images/markdown-image-1.png)  

![alt text](images/markdown-image-2.png)  

<br>

- ## Swagger UI vs ReDoc 차이점

### **Swagger UI (`/docs`)**

- **Swagger UI**는 FastAPI와 함께 가장 일반적으로 사용되는 자동 생성 문서입니다.
- 사용자 친화적인 인터페이스를 제공하며, API의 각 경로와 가능한 요청 및 응답을 시각적으로 표시합니다.
- 실시간으로 API를 테스트하고 상호 작용할 수 있는 기능을 제공합니다. 예를 들어, API 엔드포인트에 대한 요청을 직접 보내고 응답을 받아볼 수 있습니다.
- 각 API 엔드포인트에 대한 파라미터, 요청 본문, 응답 스키마 등의 세부 사항을 볼 수 있습니다.

### **ReDoc (`/redoc`)**

- **ReDoc**은 좀 더 간결하고 정돈된 인터페이스를 제공하는 다른 형태의 문서화 도구입니다.
- Swagger UI보다 더 간단하고 읽기 쉬운 레이아웃을 제공합니다.
- 대규모 API에 적합하며, 복잡한 스키마를 가진 API를 좀 더 쉽게 탐색하고 이해할 수 있도록 도와줍니다.
- 실시간 API 테스트 기능은 제공하지 않습니다. 대신, 문서화에 더 초점을 맞추고 있습니다.

### **언제 어떻게 활용하나요?**

- **개발 및 테스트**: Swagger UI (**`/docs`**)는 API 개발 및 테스트 과정에서 매우 유용합니다. 개발자는 API의 각 부분을 실시간으로 테스트하고 결과를 즉시 확인할 수 있습니다.
- **문서화 및 프레젠테이션**: ReDoc (**`/redoc`**)은 API의 최종 사용자나 스테이크홀더들에게 API를 소개하거나 문서화하는 데 더 적합합니다. 그것은 깔끔하고 직관적인 인터페이스로 API의 구조와 기능을 명확하게 전달합니다.

결론적으로, Swagger UI와 ReDoc은 각기 다른 목적과 상황에 맞게 활용될 수 있으며, FastAPI에서 두 문서화 도구를 모두 제공하는 것은 개발자가 다양한 요구 사항과 선호도에 맞게 선택할 수 있게 합니다.

<br>

- 다양한 서버 실행 방법

1. **프로그래밍 방식으로 직접 실행하기:**
FastAPI 애플리케이션을 프로그램 내부에서 직접 실행하는 가장 일반적인 방법입니다.
    
    ```python
    import uvicorn
    
    if __name__ == "__main__":
        uvicorn.run("main:app", port=8000, log_level="info")
    ```
    
    - python main.py
    
    만약, 위 내용이 없다면
    
    ```bash
    > uvicorn main:app --port 8000 --log-level info
    ```
    
2. **Config와 Server 인스턴스 사용하기:**
더 많은 구성 옵션과 서버 수명 주기 제어가 필요할 때 사용합니다.
    
    ```python
    import uvicorn
    
    if __name__ == "__main__":
        config = uvicorn.Config("main:app", port=8000, log_level="info")
        server = uvicorn.Server(config)
        server.run()
    ```
    
3. **Gunicorn과 함께 사용하기:**
프로덕션 환경에서는 Gunicorn을 사용하는 것이 권장됩니다. Gunicorn은 프로세스 관리 및 부하 분산 기능을 제공합니다.
    
    ```
    gunicorn example:app -w 4 -k uvicorn.workers.UvicornWorker
    ```

# FastAPI APIRouter  

- `items.py` 파일생성.  

    &darr; `fastapi-backend-class\` &darr; `bash shell`
    ```bash
    touch items.py
    ```

- `items.py` 코드 작성.  

  &darr; `fastapi-backend-class\` &darr; `items.py`
  ```python
  from fastapi import APIRouter

  router = APIRouter()

  @router.get("/api/v1/items/{item_id}/", 
              status_code=200, 
              tags=["items", "payment"], 
              summary="특정 아이템 가져오기", 
              description="Item 모델에서 item_id 값을 가지고 특정 아이템 조회")
  def get_item(item_id: int):
      return {'items': item_id}
  ```

- `main.py` 에 items 라우터 추가하기  
- 



<br>  

<br>  

<br>  

<br>  

--- 
--- 
--- 

# 노트 

비동기와 데이터 검증. ?
페스트 아이피..

데이터검증..

파이덴틱..

직렬화. 자동화...

# 트렌트 체크..
앵귤러는 안쓰는추세...
[추세](https://trends.google.co.kr/trends/explore?date=today%205-y&geo=KR&q=fastapi,%20flask&hl=en)  
fast api vs fLask 지난 5년간...  
 FASTAPI  올라가는 추세..  


개발자들이 중요한거.. 깃.  스타수..  


MSA 구조 ?