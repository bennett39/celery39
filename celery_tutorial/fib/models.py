from django.db import models


class Calculation(models.Model):
    """Track a calculation and its results"""
    EQUATION_FIBONACCI = 'FIB'
    EQUATIONS = ((EQUATION_FIBONACCI, 'Fibonacci'),)

    STATUS_PENDING = 'PENDING'
    STATUS_ERROR = 'ERROR'
    STATUS_SUCCESS = 'SUCCESS'
    STATUSES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_ERROR, 'Error'),
        (STATUS_SUCCESS, 'Success'),
    )

    equation = models.CharField(max_length=3, choices=EQUATIONS)
    input = models.IntegerField()
    output = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=STATUSES)
    message = models.CharField(max_length=110, blank=True)
