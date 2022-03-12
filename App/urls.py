from django.urls import path
from . import views
urlpatterns = [

    path('index',views.programs),
    path('html',views.function1),
    path('google',views.function2),
    path('facebook',views.function3)

]
