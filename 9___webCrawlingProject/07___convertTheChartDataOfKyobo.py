import pymysql, pass1, time, re, random, json
from datetime import datetime


conn = pymysql.connect(
    host="localhost",
    user="root",
    password=pass1.password(),
    db="booksminiproject",
    cursorclass=pymysql.cursors.DictCursor,
)

inputDate = datetime.now().strftime("%Y-%m-%d")
inputDate = "2024-02-13"


with conn.cursor() as cur:
    sql = "SELECT books.title, kyobo_ranking.kyoborank, kyobo_ranking.kyoboreview, kyobo_ranking.kyoboupdown FROM books join kyobo_ranking on books.isbn = kyobo_ranking.isbn where kyobo_ranking.inputdate = %s"
    cur.execute(sql, (inputDate))
    result = cur.fetchall()
    print(result)

    data = {"datasets": []}
    for x in result:
        if x["kyoboupdown"] < 0:
            index_kyoboupdown = f"⬇️{abs(int(x['kyoboupdown']))}"
        else:
            index_kyoboupdown = f"⬆️{x['kyoboupdown']}"

        data["datasets"].append(
            {
                "label": f"{x['kyoborank']}. {x['title']} {index_kyoboupdown}",
                "data": [
                    {"x": x['kyoborank'], "y": x['kyoboupdown'], "r": x['kyoboreview']},
                ],
                "borderColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.5)",
                "backgroundColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.5)",
            }
        )

    # 파일로 저장
    with open("data.js", "w", encoding="utf-8") as file:
        file.write(
            "const data = "
            + json.dumps(data, indent=2, ensure_ascii=False)
            + "; \n\nconst crawltime = "
            + json.dumps(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), indent=2, ensure_ascii=False)
            + ";"
        )
