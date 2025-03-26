from django.db import models
from django.core.exceptions import ValidationError
from .validators import (
    validate_subject_format,
    validate_professor_name,
)

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True, validators=[validate_subject_format])
    professor = models.CharField(max_length=100, default="Professor Cahan", validators=[validate_professor_name])
    
    def add_a_student(self, student):
        if self.students.count() >= 30:
            raise ValidationError("This subject is full!")
        self.students.add(student)

    def drop_a_student(self, student):
        if self.students.count() <= 0:
            raise ValidationError("This subject is empty!")
        self.students.remove(student)
        Grade.objects.filter(student=student, a_subject=self).delete()

    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count()} students"