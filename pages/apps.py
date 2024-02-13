from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PagesConfig(AppConfig):
    name = "pages"
    default_auto_field = "django.db.models.AutoField"
    verbose_name = _("Pages")
