from django.shortcuts import render
from rango.models import Category, Page

# Create your views here.

from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict )

def about(request):
    context_dict = {'boldmessage':"Rango"}
    return render(request,'rango/about.html',context_dict)

def new_page(request):
    context_dict = {'variable_name': "I'm a New Page"}
    return render(request, 'rango/newpage.html', context_dict)

def category(request, category_name_slug):
    context_dic ={}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dic ['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dic ['pages'] = pages
        context_dic ['category'] =category
    except Category.DoesNotExist:
        pass

    return render(request,'rango/category.html',context_dic)