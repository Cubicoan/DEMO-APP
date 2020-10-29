"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexPage, name="index"),

    path('one_to_two/<str:pk>', views.moveOneToTwo, name="one_to_two"),

    path('two_to_one/<str:pk>', views.moveTwoToOne, name="two_to_one"),
    path('two_to_three/<str:pk>', views.moveTwoToThree, name="two_to_three"),

    path('three_to_two/<str:pk>', views.moveThreeToTwo, name="three_to_two"),
    path('three_to_four/<str:pk>', views.moveThreeToFour, name="three_to_four"),

    path('four_to_three/<str:pk>', views.moveFourToThree, name="four_to_three"),
    path('four_to_five/<str:pk>', views.moveFourToFive, name="four_to_five"),

    path('five_to_four/<str:pk>', views.moveFiveToFour, name="five_to_four"),
]
