from django.shortcuts import render, redirect
from django.views import View

from .models import Calculation
from .tasks import fibonacci_task


class FibonacciView(View):
    def get(self, request):
        """Show a form to start a calculation"""
        return render(request, 'fib/start.html')

    def post(self, request):
        """Process a form & start a Fibonacci calculation"""
        n = request.POST['fib_number']
        calculation = Calculation.objects.create(
            equation=Calculation.EQUATION_FIBONACCI,
            input=int(n),
            status=Calculation.STATUS_PENDING,
        )
        fibonacci_task.delay(calculation.id)

        return redirect('fibonacci_list')


class FibonacciListView(View):
    def get(self, request):
        """Show a list of past calculations"""
        context = {'calculations': Calculation.objects.all()}
        return render(request, 'fib/list.html', context=context)
