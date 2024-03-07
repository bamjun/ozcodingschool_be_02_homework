from pysql import connection
from repository import ArticleRepository


def test_article_repository_create_article() -> None:
    # Given
    author = "test_author"
    body = "test_body"

    # When
    article = ArticleRepository.create(author, body)

    # Then
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT id, author, body, modified_at, created_at FROM articles WHERE id={article['id']}",
        )
    assert cursor.rowcount == 1
    result_article = cursor.fetchone()
    assert result_article
    assert result_article["id"] == article["id"]
    assert result_article["author"] == author
    assert result_article["body"] == body
