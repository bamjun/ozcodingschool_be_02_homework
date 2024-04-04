import os
import psutil

# 현재 파이썬 프로그램의 pid를 얻습니다.
current_pid = os.getpid()

# 실행 중인 모든 프로세스에 대해 반복합니다.
for proc in psutil.process_iter():
    try:
        # 프로세스 정보를 가져오는데 성공하면,
        if proc.pid == current_pid:
            # 현재 프로세스의 이름을 출력합니다.
            print(f"Process Name: {proc.name()}")
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

