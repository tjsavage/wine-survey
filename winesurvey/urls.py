"""winesurvey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from survey import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/submit_survey/', views.api_submit_survey, name='api_submit_survey'),
    path('api/get_ab_test/', views.api_get_ab_test, name='api_get_ab_test'),
    path('api/submit_ab_results/', views.api_submit_ab_results, name='api_submit_ab_results'),
    path('csv/question_responses/', views.csv_question_responses, name='csv_question_responses'),
    path('csv/ab_responses/', views.csv_ab_responses, name='csv_ab_responses'),
    path('csv/wine_items/', views.csv_wine_items, name='csv_wine_items'),
    path('admin/', admin.site.urls),
]
