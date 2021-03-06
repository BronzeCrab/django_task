from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Appointment
import datetime

# Create your views here.


class AppointmentForm(forms.Form):
        # just dummy docs names
    VIKTOROVA = 'Viktorova'
    IVANOVA = 'Ivanova'
    DOCS_NAMES = (
        (VIKTOROVA, 'Viktorova'),
        (IVANOVA, 'Ivanova'),
    )
    doc_name = forms.ChoiceField(choices=DOCS_NAMES)
    visit_date = forms.DateField(label='When will you come?')
    visit_time = forms.TimeField(label='At what time?')
    client_name = forms.CharField(label='What is your full name?')

appointment_form = AppointmentForm(auto_id=False)


def index(request):
    return render(
        request,
        'clinic/index.html',
        {
            'form': appointment_form,
        }
    )


def all_apps(request):
    if request.user.is_authenticated():
        appointments = Appointment.objects.all()
        return render(
            request,
            'clinic/all_apps.html',
            {
                'appointments': appointments,
            }
        )
    else:
        messages.add_message(request, messages.ERROR,
                             'You cant accesss')
        return redirect('home')


def newappointment(request):
    a = Appointment()
    a.doc_name = request.POST['doc_name']
    a.visit_date = request.POST['visit_date']
    a.visit_time = request.POST['visit_time']
    # first of all i must check if somebody
    # want to see doctor today but that time has
    # already passed, so it's impossible

    # what time is now
    now = datetime.datetime.now()
    time_now = now.strftime("%H:%M")
    date_now = now.strftime("%Y-%m-%d")
    # check if current time is alredy passed
    if a.visit_date == date_now and (int(time_now[0:2]) >
        int(a.visit_time[0:2]) or (int(time_now[0:2]) == int(a.visit_time[0:2])
        and int(time_now[3:5]) > int(a.visit_time[3:5]))):
        messages.add_message(request, messages.ERROR,
                             'Please specify another time, because, \
                                 that time is already passed')
        return redirect('home')

    # === olf stuff, done that using js pickers ===
    # if (int(a.visit_time[0:2]) > 17 or
    # 	int(a.visit_time[0:2]) == 17 and int(a.visit_time[3:5]) != 0):
    # 	messages.add_message(request, messages.ERROR,
    # 	 					 'Our docs working till 18:00, Please\
    # 	 					  specify another time, because\
    # 	 					  appontment will last for hour')
    # === olf stuff, done that using js pickers ===

    # check date and time, querying all apps with that date,
    # time and docs_name:
    try:
        apps_count_same_doc = Appointment.objects.filter(
            doc_name=a.doc_name).count()
        apps_count_same_date = Appointment.objects.filter(
            visit_date=a.visit_date).count()
        apps_count_same_time = Appointment.objects.filter(
            visit_time=a.visit_time).count()
        if (apps_count_same_date and apps_count_same_time
                and apps_count_same_doc):
            messages.add_message(request, messages.ERROR,
                                 'Please specify another doc, another time or date, \
                             	 Cause this doc is busy at that time')
            return redirect('home')
    # if we caught exception like it ok to go further
    # just no entities in db yet
    except Appointment.DoesNotExist:
        pass
        # checking for length of visitor's name
    if len(request.POST['client_name'].split()) >= 3:
        a.client_name = request.POST['client_name']
    else:
        messages.add_message(request, messages.ERROR,
                             'Please specify your full name')
        return redirect('home')
    # saving appontment to db
    a.save()
    messages.add_message(
        request,
        messages.SUCCESS,
        'Your appointment was added')
    return redirect('home')
