from bangazonreports.views.customers.favoritedsellersbycustomers import favoritedsellersbycustomers_list
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('reports/favoritedsellersbycustomers',
         favoritedsellersbycustomers_list),

]
