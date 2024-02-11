# 교보문고. yes24 크롤링 데이터 활용해서 차트 만들기
> 교보문고, yes24에서 각각 일간베스트 도서 크롤링 후 크롤링 데이터를 활용해서 비교 차트 웹페이지 만들기  

<br>  

# 2024.02.07. ~


### 가이드 페이지 [링크](https://legend-palm-1f1.notion.site/0e70a019c8154103907fb13c8b6ee121)  

---  
# $$\Huge\color{purple}\fbox{\Huge \color{pink}{TODO LIST}}$$  
- DB 스키마 구조 설계  
  - 고유 책 ID인 ISBN으로 테이블 묶음.
    ```diff
    - 2024 02 07 완료  
    ```    
    <img src="images/sqlmap.png" width='500px'>  
  - 스키마 다시 만들어야 할듯...
    - > 교보문고 크롤링완료하고 워크벤치 확인과정에서, 문제점 발견..  
    교보문고 크롤링완료하고 yes24크롤링 후 데이터를 저장해야하는데, 한곳의 테이블에 교보문고와 yes24 데이터를  
    저장하는게 비효율이고, 오류가 발생할 가능성이 많을꺼 같아서, price와 ranking 테이블을 교보와 yes24테이블로 각각 만들어야할듯..  
      ```diff
      + 수정 2024 02 08  
      - 완료 2024 02 08  
      ```  
      <img src="images/sql_schema.png" width='500px'>  
      <img src="images/sqlmap2.png" width='500px'>  
  <br>
- 교보문고 크롤링 하기  
  - ~~yes24는 주간평균데이터만 제공하므로 비교를 위해 교보무고 주간~~```일간``` 데이터 가져오기  
    - 
    ```diff
    - 2024 02 07 완료  
    ```    
    <img src="images/sqlworkbench.png" width='500px'>  
  - > 매일 크롤링 하는과정에서 동일한 책은 books 테이블에 데이터 삽입 하지 않도록 수정  
  db에서 select count(*) as a from books where isbn = isbn 으로 중복확인  
    ```diff
    + 추가 2024 02 08 
    - 완료 2024 02 08  
    ```    
    <img src="images/kyobo_crawl.png" width='500px'>  
  <br>    
- yes24 크롤링 하기  
  - 데이터 크롤링.  
    ```diff
    - 완료 2024 02 08  
    ```    
  <img src="images/sqlworkbench_yes24.png" width='500px'>  
  <br>
- mysql 데이터 베이스에 저장  
  ```diff
  - 완료 2024 02 08  
  ```    
  <br>

- 교보문고, yes24 데이터 평균값 average 테이블에 저장  
  ```diff  
  - 완료 2024 02 10  
  ```  
  <img src="images/sqlaverage.png" width='500px'>  

  <br>

- flask 웹페이지 연동  
  - mysql 연동  
    ```diff  
    - 완료 2024 02 08  
    ```  
    <img src="images/cmdflaskdb.png" width='500px'>  
    <br>  

  - 부트스트렙을 활용해서 크롤링데이터 출력하기  
  - chart js 를 활용해서 차트 만들기  
  <br>
- aws window server에서 가동하게 구현하기  
  - aws lightsail windows server 개설하기  
    - 
    ```diff
    - 2024 02 07 완료  
    ```    
    <img src="images/awsweb.png" width='500px'>  
  - RDP를 활용해서 윈도우즈 메인컴에 서버컴 리모트 연동하기  
    - 
    ```diff
    - 2024 02 07 완료  
    ```    
    <img src="images/RDP_icon.png" width='500px'>  
    <img src="images/awswindow.png" width='500px'>  
  - aws ubuntu 개설  
    - 윈도우 환경에서 mysql 셀레니움 개발해서, aws 윈도우 서버로 하려고 했으나, 웹 개설할때 어려울꺼같아서, 우분투로 변경  
    - 셀레니움 코드 통합하기  
    ```diff  
    완료 2024 02 11  
    ```  
    <img src="images/ubuntu.jpg" width='500px'>  

    - mysql 설치 & 크롤링 코드 연동하기    

    - flask 설치 & 코드 연동하기   

  - mysql 연동  
  - 파이썬 크롤링 스크립트 매일 1회 실행하게 하기.  
  - flask 실행하기  
  - ~~~윈도우용~~~ nginx 설치  
  - 웹 개설 하기  


  # ㅠㅠ

  - 우분투에서 플라스크 실행중..

  - 크롤링 파일 크롤링이 끝까지 안되고, 자꾸 중간에 멈추는 문제발생. 
    - 총 100개 크롤링 중 10개 끝날때마다, 셀레니움 재시작하게 코드 만들어서 해결..  
    ```diff  
    - 완료 2024 02 11  
    ```  
    