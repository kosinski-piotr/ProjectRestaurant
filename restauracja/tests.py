from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from restauracja import views
from restauracja.models import RodzajDan
from rest_framework import status
from django.utils.http import urlencode
from django import urls

class RodzajDanTests(APITestCase):
    def post_rodzaj_dania(self, name):
        url = reverse(views.RodzajDanList.name)
        data = {'nazwa':name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_rodzaj_dania(self):
        new_rodzaj_dania_name = 'kolacja'
        response = self.post_rodzaj_dania(new_rodzaj_dania_name)
        print("PK {0}".format(RodzajDan.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert RodzajDan.objects.count() == 1
        assert RodzajDan.objects.get().name == new_rodzaj_dania_name

    def test_post_existing_rodzaj_dania_name(self):
        url = reverse(views.RodzajDanList.name)
        new_rodzaj_dania_name = 'Duplikat kolacja'
        data = {'nazwa':new_rodzaj_dania_name}
        response_one = self.post_rodzaj_dania(new_rodzaj_dania_name)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_rodzaj_dania(new_rodzaj_dania_name)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_rodzaj_dania_by_name(self):
        rodzaj_dania_name_one = 'kolacja'
        rodzaj_dania_name_two = 'kolacja1'
        self.post_rodzaj_dania(rodzaj_dania_name_one)
        self.post_rodzaj_dania(rodzaj_dania_name_two)
        filter_by_name = {'nazwa': rodzaj_dania_name_one}
        url= '{0}?{1}'.format(reverse(views.RodzajDanList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == rodzaj_dania_name_one

    def test_get_rodzaj_dania_collection(self):
        new_rodzaj_dania_name = 'Kolacja aa'
        self.post_rodzaj_dania(new_rodzaj_dania_name)
        url = reverse(views.RodzajDanList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == new_rodzaj_dania_name

    def test_update_rodzaj_dania(self):
        rodzaj_dania_name = 'kolacja'
        response = self.post_rodzaj_dania(rodzaj_dania_name)
        url = urls.reverse(views.RodzajDanDetail.name,None,{response.data['pk']})
        updated_rodzaj_dania_name = 'Nowa kolacja'
        data = {'name': updated_rodzaj_dania_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_rodzaj_dania_name

    def test_get_rodzaj_dania(self):
        rodzaj_dania_name = 'kolacja'
        response = self.post_rodzaj_dania(rodzaj_dania_name)
        url = urls.reverse(views.RodzajDanDetail.name,None,{response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['nazwa'] == rodzaj_dania_name
