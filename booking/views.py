"""Views for booking / appt app"""
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm


def booking(request):
    """Booking / appt app view for submission of form"""
    if request.method == 'GET':
        form = BookingForm()
    else:
        form = BookingForm(request.POST)
        if form.is_valid():
            subject = "Booking Request"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'requested_date': form.cleaned_data['requested_date'],
                'course': form.cleaned_data['course'],
                'coach': form.cleaned_data['coach'],
                'message': form.cleaned_data['additional_information'],
            }
            message = '\n'.join(map(str, body.values()))
            messages.success(request, 'Message sent successfully!')
            try:
                send_mail(subject, message, 'simplyswimming@gmail.com', [
                    'simplyswimming@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            messages.error(
                request, "Form not submitted. Please correct any errors")
            return render(request, 'booking.html', {'form': form})
    form = BookingForm()
    return render(request, "booking.html", {'form': form})
