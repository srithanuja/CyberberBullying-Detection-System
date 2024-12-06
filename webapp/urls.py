"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('u_', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('u_', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('u_blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [


    path('', views.homepage, name="n_home"),
    path('u_signup/', views.signuppage, name="n_signup"),
    path('a_loginaction/', views.adminloginaction, name="a_loginaction"),
    path('u_loginaction/', views.userloginaction, name="n_loginaction"),
    path('u_userlogout/', views.userlogoutaction, name="n_slogout"),
    path('a_adminhome/', views.adminhomedef, name="a_adminhomedef"),
    path('a_training/', views.training, name="training"),
    path('a_testing/', views.testing, name="testing"),
    path('a_adminlogout/', views.adminlogoutdef, name="adminlogoutdef"),
    path('u_userhome/', views.userhomepage, name="n_shome"),
    path('u_viewprofile/', views.viewprofilepage, name="n_viewprofile"),
    path('u_fsearch/', views.fsearch, name="n_fsearch"),
    path('u_freqsend/', views.freqsend, name="n_freqsend"),
    path('u_viewfreq/', views.viewfreq, name="n_viewfreq"),
    path('u_reqreject/', views.reqreject, name="n_reqreject"),
    path('u_viewfrds/', views.viewfrds, name="n_viewfrds"),
    path('u_writepost/', views.writepost, name="n_writepost"),
    path('u_writepost2/', views.writepost2, name="n_writepost2"),
    path('u_ownwall/', views.ownwall, name="n_ownwall"),
    path('u_viewwall/', views.viewwall, name="n_viewwall"),
    path('d1svm/', views.d1svmdef, name="d1svm"),
    path('d1nn/', views.d1nndef, name="d1nn"),
    path('d1nb/', views.d1nbdef, name="d1nb"),
    path('d1rf/', views.d1rfdef, name="d1rf"),
    path('d2rf/', views.d2rfdef, name="d2rf"),
    path('d2svm/', views.d2svmdef, name="d2svm"),
    path('d2nn/', views.d2nndef, name="d2nn"),
    path('d2nb/', views.d2nbdef, name="d2nb"),

    path('d1testing/', views.d1testingdef, name="d1testing"),

    path('d2testing/', views.d2testingdef, name="d2testing"),
    path('results/', views.results, name="results"),
    path('viewgraph/<str:cat>/', views.viewgraph, name="viewgraph"),
    

    
]
