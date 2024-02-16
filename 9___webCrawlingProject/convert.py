import pymysql, time, re, random, json, pass1
from datetime import datetime

print(f"convert data - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


conn = pymysql.connect(
    host="localhost",
    user="root",
    password=pass1.password(),
    db="booksminiproject",
    cursorclass=pymysql.cursors.DictCursor,
)

# inputDate = datetime.now().strftime("%Y-%m-%d")
# inputDate = "2024-02-13"

with conn.cursor() as cur:
    sql = "SELECT DISTINCT inputdate FROM kyobo_price ORDER BY inputdate DESC LIMIT 1;"
    cur.execute(sql)
    inputDate = cur.fetchone()['inputdate']


    sql = "SELECT books.title, kyobo_ranking.kyoborank, kyobo_ranking.kyoboreview, kyobo_ranking.kyoboupdown, kyobo_price.kyobourl FROM books join kyobo_ranking on books.isbn = kyobo_ranking.isbn join kyobo_price on kyobo_price.isbn = books.isbn where kyobo_ranking.inputdate = %s and kyobo_price.inputdate = %s"
    cur.execute(sql, (inputDate, inputDate))
    result = cur.fetchall()
    # print(result)

    data = {"datasets": []}
    for x in result:
        index_kyoboupdown = x["kyoboupdown"]
        index_review = x['kyoboreview']

        if index_kyoboupdown < 0:
            index_kyoboupdown_tip = f"⬇️{abs(int(index_kyoboupdown))}"
        else:
            index_kyoboupdown_tip = f"⬆️{index_kyoboupdown}"
            if index_kyoboupdown > 54:
                index_kyoboupdown = 54
            elif index_kyoboupdown > 49:
                index_kyoboupdown = 49
            elif index_kyoboupdown < -54:
                index_kyoboupdown = -54
            elif index_kyoboupdown < -49:
                index_kyoboupdown = -49

        data["datasets"].append(
            {
                "label": f"{x['kyoborank']}. {x['title']} {index_kyoboupdown_tip} 리뷰 : {index_review}",
                "data": [
                    {"x": x['kyoborank'], "y": index_kyoboupdown, "r": index_review, "link": x['kyobourl']},
                ],
                "borderColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.5)",
                "backgroundColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.5)",
            }
        )

    conn.close()

# 파일로 저장
with open(pass1.savepath(), "w", encoding="utf-8") as file:
    file.write(
        "const data = "
        + json.dumps(data, indent=2, ensure_ascii=False)
        + "; \n\nconst crawltime = "
        + json.dumps(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), indent=2, ensure_ascii=False)
        + ";"
    )