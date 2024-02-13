# aws

- 리전확인하기  
<img src="images/awsmain.png">

# ec2  
  - 인스턴스 생성하기  

# 윈도우에서 ec2 접속하기  
<a href="https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/putty.html">putty 설명</a>  
  - putty 다운로드 
  - putty 커널 실행프로그램  
  - puttygen pem키 to ppk (putty용 키로 변환)  
  <img src='images/puttygen.png'>  
  - 로드에서 확장자 모드로 선택한다음, putty용 키로 변환할 .pem 선택  
  - 제너레이트 클릭
  <img src='images/putty-1.png'>  
  - host Name에 ec2 인스턴스 퍼블릭 ip 입력 포트 22  
  <img src='images/putty-2.png'>  
  - 왼쪽창에 coonection > ssh > auth > credentials > browse클릭 후 변환한 키 선택  
  - 오픈 클릭 후 login as 나타나면, ubuntu 입력  

# 리눅스 커널 명령어  
  - ls  
    - 현재 경로 나타남.  
    ```bash  
    ls  
    ```  

  - cd [폴더명]
    - 폴더 이동  
    ```bash  
    cd home
    # 하위폴더인 home 으로 이동  
    cd ..  
    # 상위폴더로 이동  
    cd ~ 
    # home 디렉토리로 이동  
    ```
  - pwd  
    - 현재 위치한 폴더 보여줌  
    ```bash  
    pwd  
    # /home/ubuntu 이런식으로 현재경로 표시  
    ```

# elastic IP 탄력적 IP  
  - 사용중인 ec2 가 문제가 생길때 빠르게 대처할수 있음.  
  - EC2 메뉴에서 오른쪽 메뉴에서 한글일경우, 네트워크 및 보안 > 탄력적 IP > 주환색 탄력적 IP 주소 할당 > 할당  
  - 생성된 탄력적 ip 주소 클릭 후 생성한 인스턴스 설정해주기.  
  - 설정안된 탄력적 IP 주소는 과금 됨..  
  - 탄력적 IP 주소 와 기존 인스턴스 IP로 둘 다 사용해서 커널 접속 가능.  
  - 탄력적IP 주소 사용안해서, 탄력적IP주소 연결해제 했을시, 탄력적IP주소 릴리스 눌러서 완전히 삭제해야 과금안됨.  
  - 릴리스 안하고 1시간 경과시, 과금  
  <img src='images/elasticip.png'>  