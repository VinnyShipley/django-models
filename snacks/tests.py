from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        reviewer = get_user_model().objects.create(username="tester",password="tester")
        Snack.objects.create(name="rake", reviewer=reviewer)

    def test_list_page_status_code(self):
        url = reverse('Snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('Snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'Snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('Snack_list')
        response = self.client.get(url)
        Snacks = response.context['object_list']
        self.assertEqual(len(Snacks), 1)
        self.assertEqual(Snacks[0].name, "rake")
        self.assertEqual(Snacks[0].rating, 0)
        self.assertEqual(Snacks[0].reviewer.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('Snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('Snack_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'Snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('Snack_detail',args=(1,))
        response = self.client.get(url)
        Snack = response.context['Snack']
        self.assertEqual(Snack.name, "rake")
        self.assertEqual(Snack.rating, 0)
        self.assertEqual(Snack.reviewer.username, "tester")