"""alston URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from gccsa_csbg_survey import views as gccsa_views
from gccsa_csbg_survey.forms import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', gccsa_views.about, name = 'about'),
    url(r'^about/', gccsa_views.about, name = 'about'),
    url(r'^requirement/', gccsa_views.requirement, name = 'requirement'),
    
    url(r'^information/$', gccsa_views.InformationWizard.as_view(
        [HeadOfHousehold,
         Household,
         HeadOfHouseholdMemberInfo,
         HouseholdMemberDemographicsInfo]), name = 'information'),

    url(r'^householdmember/', gccsa_views.householdmember, name = 'householdmember'),
    url(r'^handle404/$', gccsa_views.handler404, name = '404'),
]