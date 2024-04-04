import psutil


for proc in psutil.process_iter():
    
    ps_name = proc.name()
    # #전체 프로세서 프린터
    # print(ps_name)
    # 특정 프로세서 프린터
    if "chrome" in ps_name:
        print(ps_name, proc.pid)
