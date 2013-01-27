from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField


class Tag(models.Model):
    name = models.CharField(verbose_name=_(u'Name'), max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Tag')
        verbose_name_plural = _(u'Tags')
