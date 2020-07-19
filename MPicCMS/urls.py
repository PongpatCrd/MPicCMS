"""MPicCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import cms.views as cms

urlpatterns = [
    path('', cms.index, name="home"),
    path('login', cms._login, name="login"),
    path('logout', cms._logout, name="logout"),
    path('movie_cms', cms.mpic_movie_imp_cms, name="movie_cms"),
    path('customer_cms', cms.mpic_customer_imp_cms, name="customer_cms"),
    path('report_render/<str:report_code>', cms.report_render, name="report_render"),
    path('create_or_update/mpic_movie_imp_cms_edit_data', cms.mpic_movie_imp_cms_edit_data, name="mpic_movie_imp_cms_edit_data"),
    path('create_or_update/mpic_customer_imp_cms_edit_data', cms.mpic_customer_imp_cms_edit_data, name="mpic_customer_imp_cms_edit_data"),
    path('delete/mpic_customer_imp_cms_delete', cms.mpic_customer_imp_cms_delete, name="mpic_customer_imp_cms_delete"),
    path('delete/mpic_movie_imp_cms_delete', cms.mpic_movie_imp_cms_delete, name="mpic_movie_imp_cms_delete"),
    path('download/download_example_import_movie_file', cms.download_example_import_movie_file, name="download_example_import_movie_file"),
    path('download/download_example_import_customer_file', cms.download_example_import_customer_file, name="download_example_import_customer_file"),
    path('import/import_mpic_movie_imp_cms', cms.import_mpic_movie_imp_cms, name="import_mpic_movie_imp_cms"),
    path('import/import_mpic_customer_imp_cms', cms.import_mpic_customer_imp_cms, name="import_mpic_customer_imp_cms")
]
