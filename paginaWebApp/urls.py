# -*- coding: utf-8 -*-
from django.urls import path
from paginaWebApp import views


urlpatterns = [
    path('home/', views.home,name='home'),
    path('index/', views.index,name='index'),
    path('nosotros/', views.nosotros,name='nosotros'),
    path('productos_Servicios/', views.productoServicio,name='productos_Servicios'),
    path('portafolio/', views.portafolio,name='portafolio'),
    path('blog/', views.blogCentral,name='blogCentral'),
    path('blog/<parametro>', views.blogCentral,name='blogCentralCategoria'),
    path('contacto/', views.contacto,name='contacto'),
    path('medianasEmpresas/', views.sap,name='sap'),
    path('pequenasEmpresas/', views.aspel,name='aspel'),
    path('microsEmpresas/', views.siigo,name='siigo'),
    path('p-vendedores/', views.vendedores,name='control-vendedores'),
    path('p-tesoreria/', views.tesoreria,name='tesoreria'),
    path('p-tickets/', views.tickets,name='tickets'),
    path('search-result/', views.searched,name='searched'),
    path('blog-post/<int:parametro>', views.blogPost,name='blogPost'),
    
]


