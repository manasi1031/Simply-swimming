"""Booking/Appointment app view testcases"""
from django.test import TestCase


class TestBookingViews(TestCase):
    """Test Booking / Appt app view"""
    def test_booking(self):
        """Test booking / appt form view"""
        # response = self.client.get('/booking/')
        # self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'booking.html')
