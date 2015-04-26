from django.core.exceptions import ValidationError


def RatingValidator(value):
    if value is not None and (value < 1 or value > 5):
        raise ValidationError("Rating can't be lower than 1 or higher thane 5")