from django.core.exceptions import ValidationError
import re

def validate_subject_format(value):
    if not value.istitle():
        raise ValidationError("Subject must be in title case format.")

def validate_professor_name(value):
    if not re.match(r"^Professor [A-Z][a-z]+$", value):
        raise ValidationError('Professor name must be in the format "Professor Adam".')