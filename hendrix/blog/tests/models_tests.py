from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Entry, Link, Tag


class TagTestCase(TestCase):

    def test_unicode(self):

        with self.assertNumQueries(4):
            tag_1 = Tag.objects.create(name="Metal")
            self.assertEqual(unicode(tag_1), u"Metal")
            self.assertEqual(str(tag_1), "Metal")

            tag_2 = Tag.objects.create(name="Rock & Roll")
            self.assertEqual(unicode(tag_2), u"Rock & Roll")
            self.assertEqual(str(tag_2), "Rock & Roll")

    def test_slug(self):
        with self.assertNumQueries(7):
            tag_1 = Tag.objects.create(name="Metal")
            self.assertEqual(tag_1.slug, "metal")
            tag_2 = Tag.objects.create(name="Rock & Roll")
            self.assertEqual(tag_2.slug, "rock-roll")
            tag_3 = Tag.objects.create(name="Metal")
            self.assertEqual(tag_3.slug, "metal-2")


class LinkTestCase(TestCase):

    def test_unicode(self):
        with self.assertNumQueries(2):
            link_1 = Link.objects.create(title="About", url="/about")
            self.assertEqual(unicode(link_1), u"About - </about>")
            self.assertEqual(str(link_1), "About - </about>")

            link_2 = Link.objects.create(title="Google", url="http://www.google.com")
            self.assertEqual(unicode(link_2), u"Google - <http://www.google.com>")
            self.assertEqual(str(link_2), "Google - <http://www.google.com>")

    def test_weight(self):
        with self.assertNumQueries(6):
            link_1 = Link.objects.create(
                title="About", url="/about", weight=2)
            link_2 = Link.objects.create(
                title="Google", url="http://www.google.com", weight=1)
            link_3 = Link.objects.create(
                title="Links", url="/links", weight=3)

            links = Link.objects.all()
            self.assertEqual(link_2, links[0])
            self.assertEqual(link_1, links[1])
            self.assertEqual(link_3, links[2])

    def test_is_external(self):
        with self.assertNumQueries(3):
            link_1 = Link.objects.create(
                title="About", url="/about", weight=2)
            link_2 = Link.objects.create(
                title="Google", url="http://www.google.com", weight=1)
            link_3 = Link.objects.create(
                title="Links", url="/links", weight=3)

            self.assertFalse(link_1.is_external)
            self.assertTrue(link_2.is_external)
            self.assertFalse(link_3.is_external)


class EntryTestCase(TestCase):

    def setUp(self):
        super(EntryTestCase, self).setUp()
        self.user = User.objects.create(username="test")

    def test_unicode(self):
        with self.assertNumQueries(2):
            entry = Entry.objects.create(
                title="Testing entry",
                body="This is the body",
                created_by=self.user
            )
            self.assertEqual(
                unicode(entry),
                u"%s - Testing entry" % date.today().strftime("%Y/%m/%d")
            )
            self.assertEqual(
                str(entry),
                "%s - Testing entry" % date.today().strftime("%Y/%m/%d")
        )
