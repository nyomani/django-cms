from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .forms import PersonForm

@plugin_pool.register_plugin
class VoterPlugin(CMSPluginBase):
    modul =_("RegistrationForm")
    name = _("Registration Form Plugin")
    render_template = "voter/add_person.html"
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']

        if request.method == "POST":
            form = PersonForm(data=request.POST)
            person = form.save()
            instance.render_template="voter/person-detail.html"
            context.update({'person': person})

        else:
            form = PersonForm
            context.update({'form': form})
        return context