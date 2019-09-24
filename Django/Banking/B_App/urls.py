#from django.contrib.auth.views import login
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.Home, name="Home"),
    path("Sign_Up2/", views.Sign_Up2, name="register"),
    path("Transactions/", views.transaction, name="Transaction"),
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
