"""Views for contactme app"""
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """Contactme app view for submission of form"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Enquiry"
            body = {
                'message': form.cleaned_data['message'],
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address']
            }
            message = "\n".join(body.values())
            messages.success(request, 'Thank you for the query. Message sent successfully!')

            try:
                send_mail(subject, message, 'simplyswimming@gmail.com', [
                    'simplyswimming@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            messages.error(
                request, "Form not submitted. Please correct any errors")
            return render(request, 'contact.html', {'form': form})
    form = ContactForm()
    return render(request, "contact.html", {'form': form})
