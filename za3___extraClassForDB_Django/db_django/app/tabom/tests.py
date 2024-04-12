from django.db import IntegrityError, connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext

from tabom.article_service import *
from tabom.like_service import *
from tabom.models import Article, Like, User


class TestArticleService(TestCase):
    def test_get_article_list_should_prefetch_likes(self) -> None:
        # Given
        user = User.objects.create(name="user1")
        articles = [Article.objects.create(title=f"{i}") for i in range(1, 21)]
        Like.objects.create(user_id=user.id, article_id=articles[-1].id)

        # When
        result_articles = get_article_list(0, 10)

        # Then
        self.assertEqual(len(result_articles), 10)
        self.assertEqual(1, result_articles[0].like_set.count())
        self.assertEqual([a.id for a in reversed(articles[10:21])], [a.id for a in result_articles])

    def test_get_article_list_should_prefetch_like(self) -> None:
        # Given
        user = User.objects.create(name="test_user")
        articles = [Article.objects.create(title=f"{i}") for i in range(1, 21)]
        do_like(user.id, articles[-1].id)

        with CaptureQueriesContext(connection) as ctx:

            # When
            result_articles = get_article_list(0, 10)
            result_counts = [a.like_set.count() for a in result_articles]

            # Then
            self.assertEqual(len(result_articles), 10)
            self.assertEqual(1, result_counts[0])
            self.assertEqual(
                [a.id for a in reversed(articles[10:21])],
                [a.id for a in result_articles],
            )


class TestLikeService(TestCase):

    def test_a_user_can_undo_like(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")
        like = Like.objects.create(user_id=user.id, article_id=article.id)

        # When
        undo_like(user.id, article.id)

        # Then
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=like.id)

    def test_like_count_should_increase(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        do_like(user.id, article.id)

        # Then
        article = Article.objects.get(id=article.id)
        self.assertEqual(1, article.like_set.count())

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect
        like1 = do_like(user.id, article.id)
        with self.assertRaises(IntegrityError):
            like2 = do_like(user.id, article.id)

        # # Expect
        # like1 = do_like(user.id, article.id)
        # try:
        #     like2 = do_like(user.id, article.id)
        # except IntegrityError as e:
        #     print(e)

    def test_a_user_can_like_an_article(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        like = do_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)
