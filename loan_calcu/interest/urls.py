from django.urls import path
from . import views

urlpatterns = [
	path("", views.loan_interest, name = "loan_interest"),
]
