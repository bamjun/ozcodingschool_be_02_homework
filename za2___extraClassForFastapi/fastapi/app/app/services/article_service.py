import asyncio

from app.dtos.article_and_comments_response import (ArticleAndCommentsResponse,
                                                    CommentResponse)
from app.models.article import Article
from app.models.comment import Comment


async def service_get_article_and_comments(
    article_id: str,
) -> ArticleAndCommentsResponse:

    # async def service_get_article_and_comments(article_id: str) -> ArticleAndCommentsResponse:

    """
    dict 데신 dto 쓰는 경우
    return dict[str, Any] -> 외부 http 요청을 해서 그 결과되는 json 을 그대로 린턴하는 경우
    딕셔너리를 리턴하는 경우는 없어야함. > dto 나 객체 리턴


    N+1 문제 해결 방법

    article = Article.get_by_id(article_id)
     --> select * from articles where id = article_id
    for c in article.comments:
        print(c)

        프리패치 > for 문으로 쿼리 돌리는거를 방지.

    article = await Article.get_one_by_id(article_id)
    comments = await Comment.get_all_by_article_id(article_id)
    """

    article, comments = await asyncio.gather(
        Article.get_one_by_id(article_id),
        Comment.get_all_by_article_id(article_id),
    )

    return ArticleAndCommentsResponse(
        id=article.id,
        author=article.author,
        title=article.title,
        body=article.body,
        comments=tuple(
            CommentResponse(id=comment.id, author=comment.author, body=comment.body)
            for comment in comments
        ),
    )
