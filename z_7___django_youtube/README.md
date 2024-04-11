# GITHUBE actions CI/CD 위한 새로운 repo에 올림. [repo 링크](https://github.com/bamjun/django-backend-youtube)  



[완성 깃](https://github.com/Meoyoug/django-backend-youtube/tree/main/app)  

[ec2 도커 설정](https://visioneer.notion.site/Deployment_-2-AWS-b28f79d23703424ab94a77becbf53921)  

[깃링크](https://github.com/Seopftware/django-backend-youtube2)  

# [교제 링크](https://visioneer.notion.site/Project1_Youtube-988b009559144545aa7e2ab4eb354d6c)  

Deployment_(2) AWS
Deployment Process
(1) IAM 유저 생성
(2) EC2 instance 생성 (Amazon Linux) -> Free tier
		- EC2 SSH 접속 -> Finger Print
(3) AWS EC2
	  - git, docker-compose 설치 & docker-compose up
​
IAM 생성
Users → Add users → Access Type(Password - Custom password)


EC2 키페어 생성
첫 번째 방법 - EC2 SSH key 생성

 
두 번째 방법 - AWS 배포 키 생성하기
윈도우 - Putty 활용
[AWS]EC2 - 윈도우에서 인스턴스 접속하기 (2/2) (tistory.com)
PuTTYgen을 사용한 .pem 파일의 .ppk 형식으로의 변환
.pem 파일을 Windows에서 사용할 수 있는 형식으로 변환하는 일반적인 방법은 PuTTYgen 도구를 사용하는 것입니다. PuTTYgen은 PuTTY SSH 클라이언트에 포함된 유틸리티로, .pem 파일을 PuTTY의 .ppk 포맷으로 변환하는 데 사용됩니다.
PuTTYgen 다운로드 및 실행:
PuTTYgen은 PuTTY 설치 시 함께 제공됩니다. PuTTY가 설치되어 있지 않다면, PuTTY 공식 웹사이트에서 다운로드할 수 있습니다.
PuTTYgen을 실행합니다.
.pem 파일 불러오기:
PuTTYgen에서 'Load' 버튼을 클릭합니다.
파일 탐색기에서 .pem 파일을 찾아 선택합니다. 기본적으로 PuTTYgen은 .ppk 파일만 표시하므로, 모든 파일 유형을 표시하도록 설정해야 합니다.
해당 .pem 파일을 불러옵니다.
.ppk 형식으로 저장:
파일을 성공적으로 불러오면, 'Save private key' 버튼을 클릭합니다.
비밀번호를 설정할 수 있으며, 이는 선택 사항입니다. 비밀번호 설정은 추가 보안을 제공합니다.
.ppk 파일로 저장할 위치와 파일 이름을 선택합니다.
.ppk 파일 사용:
이제 생성된 .ppk 파일을 PuTTY나 다른 SSH 클라이언트에서 사용할 수 있습니다.
Github 배포 키 생성하기 (EC2 에서 진행)
# EC2 서버 접속 후
> ssh-keygen -t ed25519 -b 4096
​
이 명령어는 SSH 키 쌍을 생성합니다. 여기서 t ed25519는 키의 유형을 ed25519로 지정합니다. ed25519는 공개 키 암호화에 사용되는 알고리즘으로, 효율성과 보안성이 뛰어납니다. 
이 명령어는 새로운 ed25519 키를 생성합니다. ed25519는 GitHub에 권장되는 키 유형입니다.

> cat ~/.ssh/id_ed25519.pub
​
이 명령어는 생성된 공개 키를 화면에 표시합니다. SSH 키 쌍에는 개인 키(id_ed25519)와 공개 키(id_ed25519.pub) 두 종류가 있습니다. 공개 키는 서버나 서비스(예: GitHub)에 등록하여 SSH를 통한 안전한 접속을 가능하게 합니다. 개인 키는 사용자의 컴퓨터에 안전하게 보관해야 합니다.

위 값을 github에 등록
Settings → Deploy keys → Add key


EC2 인스턴스
EC2 인스턴스 생성
Quick Start
Amazon Linux
key pair 선택
Allow HTTP trafffic

ssh-add id_rsa
​
SSH 개인 키(private key)를 SSH 인증 에이전트에 추가하는 명령어입니다. 사용자가 SSH 접속을 시도할 때마다 키의 비밀번호를 입력하지 않아도 되어 편리합니다.
리눅스 구성
Git 설치
> sudo yum install git -y
​
Amazon Linux 에 Git을 설치합니다. Git은 버전 관리 시스템으로, 프로젝트의 소스 코드 관리에 주로 사용됩니다.
Docker 설치 및 구성
Docker 설치
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
​
sudo amazon-linux-extras install docker -y: Docker를 설치합니다. Docker는 애플리케이션을 컨테이너화하여 개발, 배포, 실행을 용이하게 해주는 도구입니다.
sudo systemctl enable docker.service: Docker 서비스가 시스템 부팅시 자동으로 시작되도록 설정합니다.
sudo systemctl start docker.service: Docker 서비스를 시작합니다.
Docker 권한 부여
sudo usermod -aG docker ec2-user
​
ec2-user 사용자에게 Docker 그룹의 권한을 부여합니다. 이를 통해 ec2-user가 Docker 명령어를 사용할 수 있게 됩니다.
usermod: 이것은 사용자 계정을 수정하는 명령어입니다.
aG:
a (append) 옵션은 사용자를 그룹에 추가합니다. 이 옵션을 사용하지 않으면 사용자가 현재 속해 있는 다른 그룹에서 제거될 수 있습니다.
G 옵션은 사용자를 지정된 그룹(이 경우는 docker 그룹)에 추가하거나 기존 그룹에서 제거하는 데 사용됩니다.
docker: 이는 사용자가 추가될 그룹의 이름입니다. Docker를 설치한 후에, Docker 명령어를 sudo 없이 실행하기 위해 사용자를 docker 그룹에 추가하는 것이 일반적인 관행입니다.
ec2-user: 이는 수정될 사용자 계정의 이름입니다. Amazon EC2 인스턴스에서는 기본적으로 ec2-user라는 사용자 계정이 생성됩니다.
참고: 위 명령어 실행 후, exit 명령어를 사용하여 로그아웃하고 서버에 다시 연결해야 권한이 적용됩니다.
Docker Compose 설치
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
​
Docker Compose를 다운로드하고 설치합니다. Docker Compose는 여러 컨테이너를 함께 관리하고 실행하는 도구입니다.
최신 버전 확인을 위한 명령어
curl -s https://api.github.com/repos/docker/compose/releases/latest | grep tag_name
​
도커 컴포즈 실행 권한 부여
sudo chmod +x /usr/local/bin/docker-compose
​
sudo: 슈퍼유저(루트 유저) 권한으로 명령어를 실행합니다. 이는 시스템의 중요한 파일에 변경을 가할 때 필요합니다.
chmod: 'change mode'의 약자로, 파일이나 디렉토리의 권한을 변경하는 데 사용되는 명령어입니다.
+x: 실행 권한을 추가합니다. 이는 파일을 실행 가능한 프로그램으로 만들기 위해 필요합니다.
/usr/local/bin/docker-compose: 이 경로는 docker-compose 바이너리 파일의 위치를 나타냅니다.
다운로드한 Docker Compose 파일에 실행 권한을 부여합니다.
코드 복제(git clone)
git clone <project ssh url>
​
git clone <project ssh url>: Git을 사용하여 프로젝트의 소스 코드를 복제합니다. 여기서 <project ssh url>은 복제할 Git 저장소의 SSH 주소입니다.

참고: 서비스를 시작하기 전에 .env 파일을 생성해야 합니다.
cd django-backend-youtube
cp .env.sample .env
​

docker-compose 실행 관련 명령어
(1) 서비스 실행
docker-compose -f docker-compose-deploy.yml up -d
​
docker-compose -f docker-compose-deploy.yml up -d: Docker Compose를 사용하여 서비스를 백그라운드에서 실행합니다.
docker-compose: 이것은 Docker Compose 명령어를 호출하는 부분입니다. Docker Compose는 여러 컨테이너를 정의하고 실행하는 데 사용되는 도구입니다. 주로 docker-compose.yml 파일에 정의된 서비스, 네트워크, 볼륨 등을 관리합니다.
f docker-compose-deploy.yml: f 플래그는 사용할 Compose 파일을 지정합니다. 여기서는 docker-compose-deploy.yml 파일을 사용하라고 지시하고 있습니다. 이 파일에는 애플리케이션을 실행하는 데 필요한 설정이 들어 있습니다. 표준 이름인 docker-compose.yml 대신 다른 이름을 사용하려면 f 옵션으로 파일 이름을 지정해야 합니다.
up: 이 부분은 Compose 파일에 정의된 모든 서비스를 생성하고 시작하는 데 사용됩니다.
d: 이것은 "detached mode"를 의미합니다. 즉, 컨테이너를 백그라운드에서 실행하고 터미널을 즉시 반환하라는 의미입니다. 이 옵션 없이 실행하면 로그가 터미널에 계속 출력되고, 터미널 세션이 컨테이너 실행에 바인딩됩니다.
(2) 서비스 중지:
docker-compose -f docker-compose-deploy.yml down
​
docker-compose -f docker-compose-deploy.yml down: 실행 중인 서비스를 중지합니다.
데이터까지 모두 제거하려면
docker-compose -f docker-compose-deploy.yml down --volumes
​
로그 보기
docker-compose -f docker-compose-deploy.yml logs
​
docker-compose -f docker-compose-deploy.yml logs: 컨테이너의 로그를 보여줍니다. 실시간 로그 추적을 위해서는 명령어 끝에 f 옵션을 추가합니다.
업데이트
git pull origin
docker-compose -f docker-compose-deploy.yml build app
docker-compose -f docker-compose-deploy.yml up --no-deps -d app
​
git pull origin: 서버에 최신 코드 변경 사항을 끌어옵니다.
docker-compose -f docker-compose-deploy.yml build app: 최신 코드를 포함하여 앱 이미지를 재빌드합니다.
docker-compose -f docker-compose-deploy.yml up --no-deps -d app: 업데이트된 앱을 적용합니다.
추가작업
app/settings.py
맨 밑에 줄에 추가해주세요.
STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'
​
proxy/Dockerfile
FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="seopftware"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static

RUN mkdir -p /var/cache/nginx/client_temp && \
    chown -R nginx:nginx /var/cache/nginx

RUN touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

CMD ["/run.sh"]
​
proxy/run.sh
#!/bin/sh
set -e

# 'app' 서비스가 시작되기를 기다립니다.
until nc -z $APP_HOST $APP_PORT; do
    echo "Waiting for the 'app' service..."
    sleep 1
done

echo "'app' service is up - executing command"
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'

​
EC2에서 장고 프로젝트 폴더 이동 후
sudo docker-compose -f docker-compose-deploy.yml build
sudo docker-compose -f docker-compose-deploy.yml up
​
장고 코드 변경 후
docker-compose -f docker-compose-deploy.yml up --no-deps -d app
​
장고 코드 업데이트 후 빌드 과정없이 코드 변경된 것을 컨테이너가 반영할 수 있도록 해주는 명령어
docker-compose -f docker-compose-deploy.yml run --rm app sh -c 'python manage.py createsuperuser'