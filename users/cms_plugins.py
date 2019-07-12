from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
@plugin_pool.register_plugin
class LoginPlugin(CMSPluginBase):
    modul =("LoginPlugin")
    name = ("Login Plugin")
    render_template = "users/login.html"
    cache = False

    def render(self, context, instance, placeholder):
        form=auth_views.LoginView.as_view()
      #  form = auth_forms.AuthenticationForm()
        context.update({'form': form})
        return context        
