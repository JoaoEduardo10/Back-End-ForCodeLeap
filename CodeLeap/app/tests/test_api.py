from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from app.models import Careers
import json


class CodeLeapApiTestCase(APITestCase):

    def setUp(self):
        self.careersTest = Careers.objects.create(
            username = "joão eduardo", 
            title = "Test",
            content = "created Test"
        )

        self.valid_payload = {
            'username': 'joao ',
            'content': "Apenas um test",
            'title': 'Test',
        }

        self.invalid_payload = {
            'content': "Apenas um test",
            'title': 'Test',
        }

        self.update_payload = {
            'content': "Apenas um test update",
            'title': 'Update Test',
        }

    def test_it_should_return_a_list_of_users(self):
        url = reverse("create_and_get_careers");

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_created_careers(self):
        url = reverse("create_and_get_careers");

        response = self.client.post(url, data=json.dumps(self.valid_payload), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_an_error_may_return_when_trying_to_create_a_careers(self):
        url = reverse("create_and_get_careers");

        response = self.client.post(url, data=json.dumps(self.invalid_payload), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_should_update(self):
        url = reverse("update_delete_careers", kwargs={"id": self.careersTest.pk});

        response = self.client.patch(url,data=json.dumps(self.invalid_payload), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotEqual(self.careersTest, response.data)

    def test_not_should_update(self):
        url = reverse("update_delete_careers", kwargs={"id": self.careersTest.pk});

        response = self.client.patch(url,data=json.dumps({}), content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertNotEqual(self.careersTest, response.data)

    def test_should_delete(self):
        url = reverse("update_delete_careers", kwargs={"id": self.careersTest.pk});

        url_get = reverse("create_and_get_careers");

        response = self.client.delete(url)

        response_get = self.client.get(url_get)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {})
        self.assertEqual(len(response_get.data), 0)

    def test_not_should_delete(self):
        url = reverse("update_delete_careers", kwargs={"id": 9});

        url_get = reverse("create_and_get_careers");


        response = self.client.delete(url)

        response_get = self.client.get(url_get)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response_get.data), 1)

    
    



