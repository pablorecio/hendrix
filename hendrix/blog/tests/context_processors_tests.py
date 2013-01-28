from django.test import TestCase
from django.test.client import Client

from ..models import Link


class LinksContextProcessorTestCase(TestCase):
    def setUp(self):
        super(LinksContextProcessorTestCase, self).setUp()
        self.client = Client()

    def test_empty_links(self):
        with self.assertNumQueries(1):
            response = self.client.get("/")
            self.assertEqual(response.context["links"].count(), 0)

    def test_links(self):
        with self.assertNumQueries(4):
            link_1 = Link.objects.create(
                title="About", url="/about", weight=2)
            link_2 = Link.objects.create(
                title="Google", url="http://www.google.com", weight=1)
            link_3 = Link.objects.create(
                title="Links", url="/links", weight=3)

            response = self.client.get("/")
            self.assertEqual(response.context["links"].count(), 3)

            links = response.context["links"]
            self.assertEqual(link_2, links[0])
            self.assertEqual(link_1, links[1])
            self.assertEqual(link_3, links[2])
