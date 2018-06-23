"""testingCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^elements', views.elements.index, name='element_index'),
    url(r'^elements/create', views.elements.create, name='element_create'),
    url(r'^elements/<int:element_id>', views.elements.show, name='element_show'),
    url(r'^elements/<int:element_id>/delete', views.elements.show, name='element_delete'),
    url(r'^elements/<int:element_id>/update', views.elements.show, name='element_update'),

    url(r'^pages', views.pages.index, name='page_index'),
    url(r'^pages/create', views.pages.create, name='page_create'),
    url(r'^pages/<int:page_id>', views.pages.show, name='page_show'),
    url(r'^pages/<int:page_id>/delete', views.pages.show, name='page_delete'),
    url(r'^pages/<int:page_id>/update', views.pages.show, name='page_update'),

    url(r'^components', views.components.index, name='component_index'),
    url(r'^components/create', views.components.create, name='component_create'),
    url(r'^components/<int:component_id>', views.components.show, name='component_show'),
    url(r'^components/<int:component_id>/delete', views.components.show, name='component_delete'),
    url(r'^components/<int:component_id>/update', views.components.show, name='component_update'),
]

