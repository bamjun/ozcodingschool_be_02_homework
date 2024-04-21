#!"C:\Program Files\Git\git-bash.exe"
set -euo pipefail


# export COLOR_GREEN='\e[0;32m'
# export COLOR_NC='\e[0m' # No Color



# 녹색 색상 코드 정의
export COLOR_GREEN="\033[0;32m"

# 색상 초기화 코드 정의 (색상을 기본값으로 되돌림)
export COLOR_RESET="\033[0m"


echo "Run black"
poetry run black .

echo "Run isort"
poetry run isort .

echo "Run mypy"
poetry run mypy .

echo "Run tests"
python manage.py test


# echo "${COLOR_GREEN}You are good to go!${COLOR_NC}"
echo -e "${COLOR_GREEN}You are good to go!${COLOR_RESET}"
echo -e "${COLOR_GREEN}You are good to go!${COLOR_RESET}"

if [ -z "${GIT_PS1_SHOWCONFLICTSTATE+x}" ]; then
    GIT_PS1_SHOWCONFLICTSTATE=''  # 또는 기본값 설정
fi

