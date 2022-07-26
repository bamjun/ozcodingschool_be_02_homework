- piping " | " 기호를 씀.  
 
![alt text](images/markdown-image.png)

- date 데이터 > tee > 복사데이터

![alt text](images/markdown-image-1.png)

- echo 는 타이핑만 입력 받음.  
  
![alt text](images/markdown-image-2.png)

- xargs 를 입력해서, 데이터 받게 가능.  

![alt text](images/markdown-image-3.png)

- xargs 를 이용해서, 텍스트 파일안에 있는 파일이름의 파일을 삭제가능.  
  
![alt text](images/markdown-image-4.png)  

![alt text](images/markdown-image-5.png)

- aliases [링크](https://linuxconfig.org/how-to-remove-alias-on-linux)

  ![alt text](images/markdown-image-6.png)

# LINUX File System

  - pwd  
    현재 디렉토리  

    ![alt text](images/markdown-image-7.png)
  
  - ls -F 현재 디렉토리상의 폴더는 '/' 파일은 '@'
  
    ![alt text](images/markdown-image-8.png)  
  
    ![alt text](images/markdown-image-9.png)

  - ls -l 자세한 정보  
    - 'd' 디렉토리  
    - 'r' 리드  
    - 'w' 라이트  
    - 'x' 실행가능한 권한 있음.  
    - 1번째 현재, 2번째 그룹멤버들, 3번째 다른 멤버들.  

    ![alt text](images/markdown-image-10.png)  

    ![alt text](images/markdown-image-11.png)  
    [링크](https://techbyexample.com/chmod-ow/)  
    ![alt text](images/markdown-image-12.png)  
    [링크](https://www.linkedin.com/pulse/day-5-task-linux-permissions-access-control-lists-maninder-singh/)  

  - ls -lh
    - 사이즈가 단위로 표시  
    
    ![alt text](images/markdown-image-13.png)

# cd 명령어  

  - cd [경로]  
  
   ![alt text](images/markdown-image-14.png)  
  
  - cd ~
    - 절대경로  
  
    ![alt text](images/markdown-image-15.png)  

  - ls -a  
    - 안보이는 경로 보임  
    
    ![alt text](images/markdown-image-16.png)  

  - /home/jun/docu/docu.txt
    - 절대경로    
  - jun/docu/docu.txt
    - 상대경로  
  
# File Extension  

  - file [파일이름]
    - 파일 정보 나타냄, 리눅스는 파일확장자 필요하지는 않음.  
  - image.png 확장자를 iamge.jpg 로 바꿔서 실행.  
    ![alt text](images/markdown-image-17.png)  
    ![alt text](images/markdown-image-18.png)  

# Wild Card  

  - '*' 전체 선택  
    - ls * 하위 전체 목록 출력  
      ![alt text](images/markdown-image-19.png)  

  - ls *.txt txt 확장자만 가져옴.  
    ![alt text](images/markdown-image-20.png)  

  - '?' 한글자만 선택  
    ![alt text](images/markdown-image-21.png)  

    ![alt text](images/markdown-image-22.png)  

    ![alt text](images/markdown-image-23.png)  

# touch , mkdir  

- touch  
  - 파일생성  
  ![alt text](images/markdown-image-24.png)  

- mkdir  
  - 폴더생성  
  ![alt text](images/markdown-image-25.png)  

  - mkdir [-p]
    - 경로상 폴더가 없어도 폴더 생성  
    ![alt text](images/markdown-image-26.png)  

# 명령어로 여러 파일을 한번에 생성하기  

- { } 사용해서 여러 파일을 한번에 생성할수 있음.  
  - { 1 }{ 2 } 여러번 사용해서 반복적으로 사용가능,  
  ![alt text](images/markdown-image-27.png)  
  ![alt text](images/markdown-image-28.png)  

- touch 를 사용해서, 폴더마다, 파일여러게 생성가능  
![alt text](images/markdown-image-29.png)  

# rm  
- 파일 삭제 하는 기능.  
  ![alt text](images/markdown-image-30.png)  

# 폴더 삭제하기  
- rm -r (폴더안에 있는 파일도 같이 삭제)  
![alt text](images/markdown-image-31.png)  

- rm -ri 대화형으로 y, n 선택해서 삭제 가능.  rm -i (대화형 삭제)  
![alt text](images/markdown-image-32.png)  

- rmdir
  - 폴더만 삭제기능  
  ![alt text](images/markdown-image-33.png)  

# 파일과폴더를 복사하기 (cp)  
- cp [원본위치] [복사본 위치]
![alt text](images/markdown-image-34.png)  

- cp [-p] 폴더 복사 기능  
![alt text](images/markdown-image-35.png)  

# 파일과 폴더의 이름변경 및 이동하기 (mv)
- mv [원본파일] [파일이동하거나 이름변경]  
![alt text](images/markdown-image-36.png)  

# nano를 이용한 파일 편집하기  
- nano [편집할 파일이름]  
![alt text](images/markdown-image-37.png)  
- 옵션에서 ^ 은 컨트롤 m 은 알트  

# locate 명령어 이용하기  
- 파일을 찾는 명령어.  

- 처음사용할때는 설치해야함.  
![alt text](images/markdown-image-38.png)  

![alt text](images/markdown-image-39.png)  

-파일 만들고 바로 locate 실행하면, 생성한 파일이 안나올수 있음.  
  - 크론이 경로를 업데이트 해야함.  
  - 강제로 업데이트 가능. updatedb 권한이 없다고나오면 sudo updatedb  
![alt text](images/markdown-image-40.png)  

# find 명령어 사용하기  
- 찾기 기능 find [찾을 파일]  
![alt text](images/markdown-image-41.png)  
- find는 데이터베이스에서찾는게 아니라서 느릴수있음. locate는 파일경로를 db에 저장해서 db에서 검색.  

# vi 편집기
- 확장자 없어도 열리고 어떤 종류의 파일이든 다열림.  
- vi [파일명] 파일이없으면 새로 생성됨.  
- 왼쪽아래 new라고 새로생긴파일 임을 알려줌.  
  ![alt text](images/markdown-image-42.png)  
- insert 눌러서 수정가능. esc 눌러서 기능 선택모드.  
  ![alt text](images/markdown-image-43.png)  

  ![alt text](images/markdown-image-44.png)


# tar.gz (리눅스용 압축 파일)
- tar 폴더를 묶는 용도  
- gz 압축만 가능.  
- 동시에 사용.  

![alt text](images/markdown-image-45.png)

![alt text](images/markdown-image-46.png)

# yum , apt 파일설치   
