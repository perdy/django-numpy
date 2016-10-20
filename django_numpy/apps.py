# -*- coding: utf-8 -*-
"""Django application config module.
"""

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoNumpy(AppConfig):
    name = 'django_numpy'
    verbose_name = _('Django Numpy')
