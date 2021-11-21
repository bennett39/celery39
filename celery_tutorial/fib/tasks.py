from celery_tutorial.celery import app
from .models import Calculation


@app.task(bind=True)
def fibonacci_task(self, calculation_id):
    calculation = Calculation.objects.get(id=calculation_id)

    def fib(n):
        if n < 2:
            return 1
        return fib(n - 2) + fib(n - 1)

    try:
        calculation.output = fib(calculation.input)
        calculation.status = Calculation.STATUS_SUCCESS
    except Exception as e:
        calculation.status = Calculation.STATUS_ERROR
        calculation.message = str(e)[:110]

    calculation.save()
