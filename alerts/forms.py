from django import forms
from django.core.exceptions import ValidationError

import phonenumbers


class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=100)

    def clean_phone(self):
        phone_raw = self.cleaned_data["phone"]
        try:
            phone = phonenumbers.parse(phone_raw, "UA")
        except phonenumbers.NumberParseException:
            raise ValidationError("Phone is invalid...")
        if not phonenumbers.is_valid_number(phone):
            raise ValidationError("Phone is invalid...")
        return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
