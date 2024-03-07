from typing import Any

from pysql import connection


class ArticleRepository:

    @classmethod
    def create(cls, author: str, body: str) -> dict[str, Any]:
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO articles (author, body) VALUES ('{author}', '{body}'); ")
            connection.commit()
        return {
            "id": cursor.lastrowid,
            "author": author,
            "body": body,
        }
