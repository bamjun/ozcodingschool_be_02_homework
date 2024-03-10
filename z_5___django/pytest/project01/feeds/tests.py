from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed

from users.models import User

class FeedAPITestCast(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

        self.feed1 = Feed.objects.create(user=self.user, title='Titlt1')
        self.feed2 = Feed.objects.create(user=self.user, title='Titlt2')
        self.feed3 = Feed.objects.create(user=self.user, title='Titlt3')

    def test_get_all_feeds(self):
        url = reverse('all_feeds')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)





