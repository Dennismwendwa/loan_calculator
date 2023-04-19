from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
import pytz
import calendar
from calendar import HTMLCalendar

# Create your views here.
#def current_datetime(request):
#	now_time = datetime.now()
#	print(now_time)
#
#	return render(request, "interest/index.html", {
#			'now_time': now_time,
#			})


def loan_interest(request):

	localTimeZone = pytz.timezone("Africa/Nairobi")
	timeInNairobi = datetime.now(localTimeZone)
	now_time = timeInNairobi.strftime("%H:%M:%S")

	time = 0 #default value
	simple_interest = 0 #defoult value
	
	if request.method == 'POST':
		
		principle      = int(request.POST['principle'])
		interest_rate  = float(request.POST['interest_rate'])
		time           = int(request.POST['time'])

		simple_interest = round((principle * interest_rate * time), 2)

	
	return render(request, "interest/index.html", {
		'now_time': now_time,

		'time': time,
		'simple_interest': simple_interest,

#'simple_interest': simple_interest,
})

def calender_today(request):
	now = datetime.now()
	localTimeZone = pytz.timezone("Africa/Nairobi")
	timeInNairobi = datetime.now(localTimeZone)

	current_time = timeInNairobi.strftime("%I:%M %p") # %I : %M : %S
	year = now.year
	month = now.month

	cal = HTMLCalendar().formatmonth(year, month)
	cal = cal.replace('<td', '<td style="padding: 10px;"') #changing padding

	current_calendar = calendar.HTMLCalendar()
# adding padding to calendar table
	calendar_html = current_calendar.formatyear(year)


	return render(request, "interest/calender.html", {
		'cal': cal,
		'current_time': current_time,
		'calendar_html': calendar_html,

	})
def Compound_interest_func(principal, interest_rate, years, compounds_per_year):
	total_compounds = years * compounds_per_year
	interest_per_compound = interest_rate / compounds_per_year
	total_interest = round(principal * ((1 + interest_per_compound) ** total_compounds - 1), 2)
	total_amount = round(principal + total_interest, 2)

	return total_amount, total_interest
	

def compound_interest(request):
	results = 0
	total_interest = 0
	years = 0

	if request.method == 'POST':
		principal = float(request.POST['principle'])
		interest_rate = float(request.POST['interest_rate'])
		years = int(request.POST['time'])
		compounds_per_year = 12

		results, total_interest = Compound_interest_func(principal, interest_rate, years, 
				compounds_per_year)


	return render(request, "interest/compound.html", {
			'results': results,
			'total_interest': total_interest,
			'years': years,
			})
