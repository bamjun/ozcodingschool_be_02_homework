## Flask 기본 세션 모듈에서 제공하는 함수

**`session`** 객체는 사용자의 브라우저에 저장된 쿠키와 연결되어 있으며, 사전(dictionary) 형태로 작동하여 세션 데이터를 저장하고 접근합니다. 

**(1) `session`에 데이터 저장하기**

**데이터 추가**: **`session`** 객체에 새로운 키와 값을 추가할 수 있습니다.

```python
session['username'] = 'john'
```

**(2)`session`에서 데이터 가져오기**

**데이터 읽기**: **`session`** 객체에서 키를 사용하여 데이터를 읽을 수 있습니다.

```python
username = session['username']
```

**`get` 메소드 사용**: 키가 존재하지 않을 경우 **`None`**을 반환하도록 **`get`** 메소드를 사용할 수 있습니다.

```python
username = session.get('username')
```

**(3) `session`에서 데이터 제거하기**

**데이터 삭제**: **`pop`** 메소드를 사용하여 특정 키와 그에 대응하는 값을 세션에서 제거할 수 있습니다.

```python
session.pop('username', None)
```

**세션 클리어**: **`clear`** 메소드를 사용하여 세션의 모든 데이터를 제거할 수 있습니다.

```python
session.clear()
```

- 특정 사용자와 관련된 모든 세션 데이터를 서버 측에서 삭제하는 데 사용
    
    주로 사용자가 로그아웃할 때, 사용자와 관련된 모든 세션 데이터를 삭제함.
    

**(4) 세션 유지 기간 설정**

**`permanent`** 속성을 **`True`**로 설정하여 세션의 유지 기간을 **`PERMANENT_SESSION_LIFETIME`** 설정값에 따라 조정 가능

**app.py**

```python
from datetime import timedelta

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 예: 7일
```

**routes/user.py**

```python
@app.route('/login', methods=['POST'])
def login():
    session['username'] = 'your_username'
    session.permanent = True  # 세션 유지 기간을 활성화
    return redirect(url_for('secret'))
```