# poetry  
`bash shell`
```bash  
# poetry new [설치경로]  
poetry new .

# poetry 현재 설치현황  
poetry env info  

# poetry 가상환경에서 사용할 파이썬버전 변경  
# poetry env use [파이썬 설치경로]  
poetry env use 'C:/Users/khy51/AppData/Local/Programs/Python/Python311/python.exe'  

# poetry 가상환경 삭제  
poetry env remove python
# 만약 에러가 뜨면 poetry env list로 설치된 환경 확인하기  
poetry env list
>> practice-poetry-20240312-jTiFJC5E-py3.11 (Activated)
poetry env remove practice-poetry-20240312-jTiFJC5E-py3.11

```  

# 01 Django JWT (JWT)  
`bash shell`
```bash  
pip install PyJWT # venv
poetry add PyJWT # poetry
``` 
  

# 02 Django JWT (SimpleJWT)  

`bash shell`
```bash  
pip install djangorestframework-simplejwt # venv
poetry add djangorestframework-simplejwt # poetry
``` 

