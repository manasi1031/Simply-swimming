"""Forms for Appointment/Booking app"""
from django import forms
# from course.models import Course
# from coaches.models import Coach


class BookingForm(forms.Form):
    """Booking form to register for a course"""
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    # course = forms.ModelChoiceField(
    #     queryset=Course.objects.filter(status=1),
    #     empty_label="(Please select a course)")
    # coach = forms.ModelChoiceField(
    #     queryset=Coach.objects.filter(status=1),
    #     empty_label="(Please select a coach)")
    requested_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))
    additional_information = forms.CharField(
        widget=forms.Textarea, required=False)
