from django.db import models
from django.utils.translation import ugettext_lazy as _

from markymark.fields import MarkdownField


class Post(models.Model):

    content = MarkdownField(_('Content'))

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __unicode__(self):
        return u'{0}'.format(self.id)
