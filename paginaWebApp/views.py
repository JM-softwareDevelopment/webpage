# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
from .models import blog
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


recomendedFooter= blog.objects.filter( 
            Q(id=1) | Q(id=2)
            )

categoriesFooter = blog.objects.values('category').distinct()

def home(request):
    return render(request,'paginaWebApp/home.html')


def index(request):
    recomended= blog.objects.filter( 
            Q(id=1) | Q(id=2) | Q(id=3) | Q(id=4)
            )
    ctx={'recomended':recomended,'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
    return render(request,'paginaWebApp/index.html',ctx)


def nosotros(request):
    ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
    return render(request,'paginaWebApp/nosotros.html',ctx)


def productoServicio(request):
    ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
    return render(request,'paginaWebApp/productos-servicios.html',ctx)

def portafolio(request):
    ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
    return render(request,'paginaWebApp/portafolio.html',ctx)

def blogCentral(request, parametro=''):
    if not parametro:
        rquery=blog.objects.all().order_by('-date_created')
        p=Paginator(rquery,5)
        page=request.GET.get('page')
        pageInfo=p.get_page(page)
        currentpage=pageInfo.number
        totalpages=p.num_pages
        currentPlus2=currentpage+2
        if totalpages<=5:
            iterator=range(1,totalpages+1,1)
        elif totalpages>=5 and currentpage<=3:
            iterator=range(1,6,1)
        elif totalpages>=5 and currentpage>=4 and currentPlus2<=totalpages:
            iterator=range(currentpage-2,currentpage+3,1)
        else:
            iterator=range(totalpages-4,totalpages+1,1)

        popular= blog.objects.filter( 
            Q(id=1) | Q(id=2) | Q(id=3)
            )
        
        recomended= blog.objects.filter( 
            Q(id=1) | Q(id=5) | Q(id=6)
            )

        ctx={'pageInfo':pageInfo,'paginator':p,'iterator':iterator,'categoriesFooter':categoriesFooter,'popular':popular,'recomended':recomended,'recomendedFooter':recomendedFooter}
        return render(request,'paginaWebApp/blog_central.html',ctx)
    else:
        p=Paginator(blog.objects.filter(category=parametro).order_by('-date_created'),5)
        page=request.GET.get('page')
        pageInfo=p.get_page(page)
        currentpage=pageInfo.number
        totalpages=p.num_pages
        currentPlus2=currentpage+2
        if totalpages<=5:
            iterator=range(1,totalpages+1,1)
        elif totalpages>=5 and currentpage<=3:
            iterator=range(1,6,1)
        elif totalpages>=5 and currentpage>=4 and currentPlus2<=totalpages:
            iterator=range(currentpage-2,currentpage+3,1)
        else:
            iterator=range(totalpages-4,totalpages+1,1)
        
        categories = blog.objects.values('category').distinct()

        popular= blog.objects.filter( 
            Q(id=1) | Q(id=2) | Q(id=3)
            )

        ctx={'pageInfo':pageInfo,'paginator':p,'iterator':iterator,'categoriesFooter':categoriesFooter,'popular':popular,'recomendedFooter':recomendedFooter}
        return render(request,'paginaWebApp/blog_central.html',ctx)




def contacto(request):
    ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
    return render(request,'paginaWebApp/contacto.html',ctx)

def sap(request):
    ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
    return render(request,'paginaWebApp/sap.html',ctx)

def aspel(request):
    ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
    return render(request,'paginaWebApp/aspel.html',ctx)

def siigo(request):
    ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
    return render(request,'paginaWebApp/siigo.html',ctx)

def vendedores(request):
    return render(request,'paginaWebApp/control-vendedores.html')

def tesoreria(request):
    return render(request,'paginaWebApp/tesoreria.html')

def tickets(request):
    return render(request,'paginaWebApp/sistema-tickets.html')

def searched(request):
    if request.method == "POST" :
        searchedText = request.POST['searchInput']
        results= blog.objects.filter( 
            Q(body__icontains=searchedText) | Q(title__icontains=searchedText) | Q(subtitle__icontains=searchedText)
            )
        count = results.count()
        ctx={'searchedText':searchedText,'results':results,'count':count,'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
        return render(request,'paginaWebApp/search-results.html',ctx)
    else:
        ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter}
        return render(request,'paginaWebApp/search-results.html',ctx)


def blogPost(request,parametro):
    result= blog.objects.get(id=parametro)
    ctx={'recomendedFooter':recomendedFooter,'categoriesFooter':categoriesFooter,'result':result}
    return render(request,'paginaWebApp/blog-post.html',ctx)
