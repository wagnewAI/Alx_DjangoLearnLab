from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import CustomUser
from posts.models import Post, Comment, Like
from notifications.models import Notification

from django.contrib.auth import get_user_model
User = get_user_model()

class PostCommentTests(APITestCase):

    def setUp(self):
        # Create and authenticate a test user
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        url = reverse("post-list")
        data = {"title": "Test Post", "content": "This is a test post"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        Post.objects.create(author=self.user, title="A", content="B")
        url = reverse("post-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        post = Post.objects.create(author=self.user, title="Hello", content="World")
        url = reverse("comment-list")
        data = {"post": post.id, "content": "Nice post!"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class FeedTests(APITestCase):
    def setUp(self):
        self.a = User.objects.create_user(username='a', password='pw')
        self.b = User.objects.create_user(username='b', password='pw')
        self.c = User.objects.create_user(username='c', password='pw')
        # user a follows b
        self.a.following.add(self.b)
        # create posts
        Post.objects.create(author=self.b, title='B1', content='x')
        Post.objects.create(author=self.c, title='C1', content='y')
        self.client.force_authenticate(user=self.a)

    def test_feed_contains_only_followed_users_posts(self):
        url = reverse('feed')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        titles = [item['title'] for item in resp.data['results']]
        self.assertIn('B1', titles)
        self.assertNotIn('C1', titles)

    def test_like_post_creates_notification(self):
        post = Post.objects.create(author=self.user, title='Hello', content='World')
        other_user = User.objects.create_user(username='other', password='pw')
        self.client.force_authenticate(user=other_user)
        url = reverse('post-like', args=[post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 201)
    
    # Check notification exists
        self.assertTrue(Notification.objects.filter(recipient=self.user, actor=other_user, verb='liked your post').exists())
