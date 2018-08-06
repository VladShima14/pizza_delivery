from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.sessions.models import Session
from pizza_app_auth.models import CustomUser


class TestLoginView(TestCase):
    @classmethod
    def setUp(cls): # создаём пользователся
        cls.password = 'test'
        cls.user = CustomUser(
            username='test',
            email='test@mail.com'
        )
        cls.user.set_password(cls.password)
        cls.user.save()
        cls.client = Client()

    def test_incorrect_login(self): # проверка неправильного входа
        url = reverse('auth_app:login')
        response = self.client.post(url, {
            'username': self.user.username,
            'password': 'wrong-password', # неправильный пароль
        }, follow=True)

        # self.assertEquals(response.status_code, 200)
        # self.assertIn('Please enter a correct username and password',
        #               str(response.content)
        #               )
        assert response.status_code == 200
        assert Session.objects.all().count() == 0

    def test_correct_login(self):
        url = reverse('auth_app:login')
        response = self.client.post(url, {
            'username': self.user.username,
            'password': self.password,
        }, follow=True)

        assert response.status_code == 200
        assert Session.objects.all().count() == 1


class TestRegisterUser(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def test_register(self):
        url = reverse('auth_app:register')
        username = 'test_user'
        response = self.client.post(url, {
            "username": username,
            "password1": "pass1234",
            "password2": "pass1234",
        }, follow=True)

        assert response.status_code == 200
        self.assertTrue(CustomUser.objects.get(username=username))
