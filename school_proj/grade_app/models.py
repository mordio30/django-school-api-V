from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Grade(models.Model):
    grade = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)]
    )
    a_subject = models.ForeignKey("subject_app.Subject", on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey("student_app.Student", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.a_subject.subject_name} - {self.grade}"