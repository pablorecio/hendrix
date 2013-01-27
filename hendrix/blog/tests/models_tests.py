from django.test import TestCase

from ..models import Tag


class TagTestCase(TestCase):

    def test_unicode(self):
        tag_1 = Tag.objects.create(name="Metal")
        self.assertEqual(unicode(tag_1), u"Metal")
        self.assertEqual(str(tag_1), "Metal")

        tag_2 = Tag.objects.create(name="Rock & Roll")
        self.assertEqual(unicode(tag_2), u"Rock & Roll")
        self.assertEqual(str(tag_2), "Rock & Roll")

    def test_slug(self):
        tag_1 = Tag.objects.create(name="Metal")
        self.assertEqual(tag_1.slug, "metal")

        tag_2 = Tag.objects.create(name="Rock & Roll")
        self.assertEqual(tag_2.slug, "rock-roll")

        tag_3 = Tag.objects.create(name="Metal")
        self.assertEqual(tag_3.slug, "metal-2")
