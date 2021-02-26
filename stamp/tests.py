from django.test import TestCase
from stamp.models import Diller, User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"login_user": "nickname", "username": "testname", "password1": "qwer", }
        response = self.client.post("/api/v1/stamps/user/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def setUp(self):
        Diller.objects.create(name="andrey", statistics_User="12341234")
        Diller.objects.create(name="sasha", statistics_User="0")

    def test_Dillers(self):
        andrey = Diller.objects.get(name="andrey")
        sasha = Diller.objects.get(name="sasha")
        response1 = self.client.post("/api/v1/stamps/diller/create/", andrey)
        response2 = self.client.post("/api/v1/stamps/diller/create/", sasha)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_201_CREATED)