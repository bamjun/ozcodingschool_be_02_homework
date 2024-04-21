#!"C:\Program Files\Git\git-bash.exe"
set -euo pipefail


# export COLOR_GREEN='\e[0;32m'
# export COLOR_NC='\e[0m' # No Color



# 녹색 색상 코드 정의
export COLOR_GREEN="\033[0;32m"

# 색상 초기화 코드 정의 (색상을 기본값으로 되돌림)
export COLOR_RESET="\033[0m"




# 일반 색상
COLOR_BLACK="\033[0;30m"
COLOR_RED="\033[0;31m"
COLOR_GREEN="\033[0;32m"
COLOR_YELLOW="\033[0;33m"
COLOR_BLUE="\033[0;34m"
COLOR_MAGENTA="\033[0;35m"
COLOR_CYAN="\033[0;36m"
COLOR_WHITE="\033[0;37m"

# 밝은 색상
COLOR_BRIGHT_BLACK="\033[0;90m"
COLOR_BRIGHT_RED="\033[0;91m"
COLOR_BRIGHT_GREEN="\033[0;92m"
COLOR_BRIGHT_YELLOW="\033[0;93m"
COLOR_BRIGHT_BLUE="\033[0;94m"
COLOR_BRIGHT_MAGENTA="\033[0;95m"
COLOR_BRIGHT_CYAN="\033[0;96m"
COLOR_BRIGHT_WHITE="\033[0;97m"


# 일반 배경 색상
BACKGROUND_BLACK="\033[0;40m"
BACKGROUND_RED="\033[0;41m"
BACKGROUND_GREEN="\033[0;42m"
BACKGROUND_YELLOW="\033[0;43m"
BACKGROUND_BLUE="\033[0;44m"
BACKGROUND_MAGENTA="\033[0;45m"
BACKGROUND_CYAN="\033[0;46m"
BACKGROUND_WHITE="\033[0;47m"

# 밝은 배경 색상
BACKGROUND_BRIGHT_BLACK="\033[0;100m"
BACKGROUND_BRIGHT_RED="\033[0;101m"
BACKGROUND_BRIGHT_GREEN="\033[0;102m"
BACKGROUND_BRIGHT_YELLOW="\033[0;103m"
BACKGROUND_BRIGHT_BLUE="\033[0;104m"
BACKGROUND_BRIGHT_MAGENTA="\033[0;105m"
BACKGROUND_BRIGHT_CYAN="\033[0;106m"
BACKGROUND_BRIGHT_WHITE="\033[0;107m"

COLOR_RED_ON_BLACK="\033[0;31;40m"

COLOR_RED_ON_WHITE="\033[0;31;47m"

# 빨간 글자와 검은 배경으로 텍스트 출력
echo -e "${BACKGROUND_GREEN}This is red text on a black background${COLOR_RESET}"

# echo "${COLOR_GREEN}You are good to go!${COLOR_NC}"
echo -e "${COLOR_GREEN}${COLOR_RED_ON_BLACK}You are good to go!${COLOR_RESET}"
echo -e "${COLOR_GREEN}You are good to go!${COLOR_RESET}"

echo -e "${COLOR_GREEN}You are good to go!"

echo -e "weoifjwefio${COLOR_RESET}"

if [ -z "${GIT_PS1_SHOWCONFLICTSTATE+x}" ]; then
    GIT_PS1_SHOWCONFLICTSTATE=''  # 또는 기본값 설정
fi
