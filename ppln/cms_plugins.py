from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import Candidate,Team,TeamPluginModel
from .page import ArticlePluginModel
from cms.models.pagemodel import Page
from django.http import Http404
from django.core.paginator import InvalidPage, Paginator

@plugin_pool.register_plugin
class PresidentialTallyPlugin(CMSPluginBase):
    modul =_("PresidentialTally")
    name = _("Presidentail Tally Plugin")
    render_template = "ppln/ppwp.html"
    cache = False

    def render(self, context, instance, placeholder):
        print(context['request'],instance)
        tallies= Candidate.objects.filter(election_type__code = 'PPWP', candidate_id__lt=1000).order_by('party__party_id','candidate_id')
        context.update({'candidates': tallies})
        return context

@plugin_pool.register_plugin
class ParliamentTallyPlugin(CMSPluginBase):
    modul =_("ParliamentTally")
    name = _("Parliament Tally Plugin")
    render_template = "ppln/dpr.html"
    cache = False

    def render(self, context, instance, placeholder):
        print(context['request'],instance)
        tallies= Candidate.objects.filter(election_type__code = 'DPR', candidate_id__lt=1000).order_by('party__party_id','candidate_id')
        context.update({'candidates': tallies})
        return context        

@plugin_pool.register_plugin
class TeamPlugin(CMSPluginBase):
    modul =_("Team")
    name = _("Team Plugin")
    render_template = "ppln/team.html"
    cache = False
    model = TeamPluginModel
    def render(self, context, instance, placeholder):
        group = instance.user_group.name
        team= Team.objects.filter(profile__groups__name__in = [group]).order_by('rank')
        context.update({'people': team})
        return context                

@plugin_pool.register_plugin
class ArticlePlugin(CMSPluginBase):
    modul =_("Articles")
    name = _("Articles Plugin")
    render_template = "ppln/pages.html"
    cache = False
    model = ArticlePluginModel
    def render(self, context, instance, placeholder):
        page_group = instance.page_group.group
        page_size = instance.item_perpage
        query_set = Page.objects.filter(is_page_type=False,publisher_is_draft=False,metapage__page_type__group=page_group)
        page = context['request'].GET.get('page') or 1
        paginator, page, queryset, is_paginated =self.paginate_queryset(page,query_set,page_size)
        context.update({'items' : queryset,
                        'paginator': paginator,
                        'page_obj': page,
                        'is_paginated':is_paginated,
                        'object_list':queryset
         })
        return context    

    def paginate_queryset(self, page,queryset,page_size):
        """Paginate the queryset, if needed."""
        paginator = Paginator(queryset, page_size)
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_('Page is not “last”, nor can it be converted to an int.'))
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage as e:
            raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
                'page_number': page_number,
                'message': str(e)
            })
