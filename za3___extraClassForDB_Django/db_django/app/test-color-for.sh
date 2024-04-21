#!/bin/bash

# 색상 초기화
COLOR_RESET="\033[0m"

# 일반 색상과 색상 코드
declare -A colors
colors=(
    [COLOR_BLACK]="\033[0;30m"
    [COLOR_RED]="\033[0;31m"
    [COLOR_GREEN]="\033[0;32m"
    [COLOR_YELLOW]="\033[0;33m"
    [COLOR_BLUE]="\033[0;34m"
    [COLOR_MAGENTA]="\033[0;35m"
    [COLOR_CYAN]="\033[0;36m"
    [COLOR_WHITE]="\033[0;37m"
    [COLOR_BRIGHT_BLACK]="\033[0;90m"
    [COLOR_BRIGHT_RED]="\033[0;91m"
    [COLOR_BRIGHT_GREEN]="\033[0;92m"
    [COLOR_BRIGHT_YELLOW]="\033[0;93m"
    [COLOR_BRIGHT_BLUE]="\033[0;94m"
    [COLOR_BRIGHT_MAGENTA]="\033[0;95m"
    [COLOR_BRIGHT_CYAN]="\033[0;96m"
    [COLOR_BRIGHT_WHITE]="\033[0;97m"
    [ZZZ]="\033[38;5;9m\033[48;5;7m"
)

# 색상 출력
for color_name in "${!colors[@]}"; do
    color_code="${colors[$color_name]}"
    echo -e "${color_code}This is $color_name ${COLOR_RESET}"
    echo "$color_name: ${colors[$color_name]}"
done
