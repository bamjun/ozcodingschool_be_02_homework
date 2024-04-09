import concurrent.futures
import time


def task(name):
    time.sleep(0.5)
    return f"{name}의 작업이 완료되었습니다."

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:

        furture_name = { executor.submit(task, f"Task-{i}") : f"Task-{i}" for i in range(30) }
        print(furture_name)


        for future in concurrent.futures.as_completed(furture_name):
            name = furture_name[future]
            try:
                result = future.result()
                print(f"{name}의 결과 : {result}")
            except Exception as exc:
                print(f"{name}에서 에러 발생 : {exc}")