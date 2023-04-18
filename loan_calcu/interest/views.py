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
	localTimeZone = pytz.timezone("Africa/Nairobi")
	timeInNairobi = datetime.now(localTimeZone)

	current_time = timeInNairobi.strftime("%I:%M %p") # %I : %M : %S
	year = 2021
	month = 9
	#month = month.title() or capitalize()
	#convert month from name to number
	#month_number = list(calendar.month_name).index(month)

	cal = HTMLCalendar().formatmonth(year, month)
	

	return render(request, "interest/calender.html", {
		'cal': cal,
		'current_time': current_time,

	})

def compound_interest(request):
	

	return render(request, "interest/compound.html", {})





