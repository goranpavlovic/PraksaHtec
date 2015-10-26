from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from usermanagement.models import Musician
from django.test.client import encode_multipart, RequestFactory


# Create your tests here.
class SampleTest(APITestCase):

    def setUp(self):
        self.musician = Musician(first_name="Bora", last_name="Fedorov")
        self.musician.save()

    def doCleanups(self):
        pass

    def test_create_item(self):
        print "----------our first test--------"
        # response = self.client.get("/country")
        data = {
                'first_name': 'nekoime',
                'last_name': 'nekoprezime',
                'id': self.musician.id,
                'country': 'nekazemlja'

            }
        content = encode_multipart('BoUnDaRyStRiNg', data)
        content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
        response = self.client.post("/country", content, content_type=content_type)
        self.musician.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.musician.country, response.data.get('country'))
        self.assertEqual(self.musician.last_name, response.data.get('last_name'))

    # def test_false_test(self):

        # self.assertEqual(True, False)


