from django.urls import path
from django.conf.urls  import url
from . import views

# urls
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^api/ifsc/(?P<ifsc>[A-Za-z]{4}\w{7})$', views.IfscView.as_view(), name='Ifsc'),
    url(r'^api/branch/(?P<bank_name>.*)/(?P<city_name>.*)$', views.CityBankNameView.as_view(), name='city_bank_name'),
    
]