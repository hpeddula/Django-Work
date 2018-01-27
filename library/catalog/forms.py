from django import forms

from django.core.exceptions import  ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a valid data between now and 4 books")

    def clean_renewal_date(self):
        data = self.cleanded_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(_('Invalid Date - Date in the past'))

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data
