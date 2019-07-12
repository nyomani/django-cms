from django.shortcuts import render
from django.http import HttpResponse
from cms.models.pagemodel import Page
from cms.admin.pageadmin import AddPageForm

def edit_page(request,page_id=1):
    page = Page.objects.filter(pk=page_id)[0]
    print (page)
    return render(request,'ppln/page-editor.html',{'page' : page })

def list_page(request):
    pages = Page.objects.filter(is_page_type=False,metapage__page_type__group='ARTICLE')
    return render(request,'ppln/pages.html',{'items' : pages })
