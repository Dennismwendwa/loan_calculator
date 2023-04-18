from django.urls import path
from . import views

urlpatterns = [
	path("", views.loan_interest, name = "loan_interest"),
	path("calender", views.calender_today, name = "calender_today"),
	path("compound", views.compound_interest, name = "compound_interest"),
]
