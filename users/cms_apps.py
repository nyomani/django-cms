from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
class django_login(CMSApp):
    app_name = "users"
    name = _("LOGIN")
    def get_urls(self, page=None, language=None, **kwargs):
        return ["users.urls"]
apphook_pool.register(django_login)  # register the application