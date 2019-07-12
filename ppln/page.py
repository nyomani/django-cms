from django.db import models
from cms.extensions import PageExtension
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.pagemodel import Page
from cms.models import CMSPlugin

class PageGroup (models.Model):
    group = models.CharField(max_length=32)

    def __str__(self):
        return self.group


class MetaPage(PageExtension):
    image = models.ImageField(upload_to='page-icons',null=True,blank=True)
    page_type=models.ForeignKey(PageGroup,default=0,on_delete=models.CASCADE)
    page_summary = HTMLField()

    def __str__(self):
        return self.page_type.group

class ArticlePluginModel(CMSPlugin):
    page_group = models.ForeignKey(PageGroup,on_delete=models.CASCADE)
    item_perpage = models.IntegerField(default=6)
    def __str__(self):
        return self.page_group.group
