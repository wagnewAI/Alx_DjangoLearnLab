from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='u1', password='pw1')
        self.user2 = User.objects.create_user(username='u2', password='pw2')
        self.client.force_authenticate(user=self.user1)

    def test_follow_and_unfollow(self):
        follow_url = reverse('follow-user', kwargs={'user_id': self.user2.id})
        unfollow_url = reverse('unfollow-user', kwargs={'user_id': self.user2.id})

        resp = self.client.post(follow_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn(self.user2, self.user1.following.all())

        resp2 = self.client.post(unfollow_url)
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
        self.assertNotIn(self.user2, self.user1.following.all())
