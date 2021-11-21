from celery_tutorial.celery import app
from .models import Calculation


def fib(n):
    """Calculate the Nth fibonacci number"""
    if n < 0:
        raise ValueError('Negative numbers are not supported')
    elif n == 0:
        return 0
    elif n <= 2:
        return 1

    return fib(n - 2) + fib(n - 1)


@app.task(bind=True)
def fibonacci_task(self, calculation_id):
    """Perform a calculation & update the status"""
    calculation = Calculation.objects.get(id=calculation_id)

    try:
        calculation.output = fib(calculation.input)
        calculation.status = Calculation.STATUS_SUCCESS
    except Exception as e:
        calculation.status = Calculation.STATUS_ERROR
        calculation.message = str(e)[:110]

    calculation.save()
