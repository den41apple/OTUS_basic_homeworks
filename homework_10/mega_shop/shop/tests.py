from http import HTTPStatus

from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from shop.models import Category


class TestCategoriesTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.category = Category.objects.create(
            name="category_name",
            description="some description",
        )

    @classmethod
    def tearDownClass(cls):
        cls.category.delete()

    def test_get_category(cls):
        qs = Category.objects.filter(~Q(name="default"))
        category = qs.get()
        cls.assertEqual(category.pk, cls.category.pk)

    def test_queryset(cls):
        queryset = Category.objects.filter(~Q(archived=True)).order_by("id").all()
        url = reverse("shop:categories")
        response = cls.client.get(url)
        response_object_list = response.context_data["category_list"]
        cls.assertQuerySetEqual(queryset, response_object_list)


class IndexViewTestCase(TestCase):
    def test_status(cls):
        url = reverse("shop:index")
        response = cls.client.get(url)
        cls.assertEqual(response.status_code, HTTPStatus.OK)
        cls.assertTemplateUsed(response, "shop/index.html")

    def test_async_mode_is_off(cls):
        url = reverse("shop:index")
        response = cls.client.get(url)
        cls.assertEqual(response.context_data["view"].view_is_async, False)
