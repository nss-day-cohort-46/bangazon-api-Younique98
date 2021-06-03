from bangazonreports.views.customers.favoritedsellersbycustomers import favoritesellersbycustomers_list
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('reports/favoritedsellersbycustomers',
         favoritesellersbycustomers_list),

]
