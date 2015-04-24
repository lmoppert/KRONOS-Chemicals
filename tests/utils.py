from django.test import TestCase
from model_mommy import mommy
from django.contrib.auth.models import User


class TestUsers(TestCase):
    def __init__(self):
        superadmin = mommy.make(
            User, username="superadmin", password="superadmin",
            is_staff=True, is_superuser=True, is_active=True,
        )
        admin = mommy.make(
            User, username="admin", password="admin",
            is_staff=True, is_superuser=False, is_active=True,
        )
        user = mommy.make(
            User, username="user", password="user",
            is_staff=False, is_superuser=False, is_active=True,
        )
        locked = mommy.make(
            User, username="locked", password="locked",
            is_staff=True, is_superuser=False, is_active=False,
        )

    def login(self, user):
        status =  self.client.login(
            username=user.username,
            password=user.password
        )
        return status
