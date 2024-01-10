""""
to test the categories  api
"""

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient



CREATE_CATEGORY = reverse('category:create')

class CategoriesAPiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
    

    def test_create_category(self):
        payload = {

            'category_name': 'Test Category',
            'category_name_id': 123,
            'category_image_url': 'https://png.pngtree.com/png-clipart/20190516/original/pngtree-healthy-food-png-image_3776802.jpg',
            'is_active': True,
            'is_deleted': False,
            'created_by': 1,
            'updated_by': 1,

        }

        response = self.client.post(CREATE_CATEGORY, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Data inserted successfully')

