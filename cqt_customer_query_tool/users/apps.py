from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "cqt_customer_query_tool.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import cqt_customer_query_tool.users.signals  # noqa: F401
        except ImportError:
            pass
