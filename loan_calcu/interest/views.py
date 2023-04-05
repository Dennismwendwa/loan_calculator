from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def loan_interest(request):

	if request.method == 'POST':
		
		principle      = int(request.POST['principle'])
		interest_rate  = float(request.POST['interest_rate'])
		time           = int(request.POST['time'])

		simple_interest = round((principle * interest_rate * time), 2)

	
	return render(request, "interest/index.html", {

				'simple_interest': simple_interest,
				})
