from django.db.models import Prefetch, QuerySet

from tabom.models import Article, Like


def get_an_article(article_id: int) -> Article:
    return Article.objects.get(id=article_id)


def get_article_list(offset: int, limit: int) -> QuerySet[Article]:
    return Article.objects.order_by("-id")[offset : offset + limit]
