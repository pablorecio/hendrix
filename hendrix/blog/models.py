from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField


class WeightMixin(models.Model):
    weight = models.IntegerField(
        verbose_name=_(u'Weight'),
        help_text=_(u'For proper ordering with it\'s siblings'),
        default=0
    )


class Tag(models.Model):
    name = models.CharField(verbose_name=_(u'Name'), max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Tag')
        verbose_name_plural = _(u'Tags')


class Link(WeightMixin, models.Model):
    title = models.CharField(verbose_name=_(u'Title'), max_length=100)
    url = models.CharField(
        verbose_name=_(u'URL'),
        max_length=400,
        help_text=_(u'Relative if you want an internal link, full link otherwise')
    )

    def __unicode__(self):
        return u'%s - <%s>' % (self.title, self.url)

    class Meta:
        verbose_name = _(u'Link')
        verbose_name_plural = _(u'Links')
        ordering = ["weight"]
