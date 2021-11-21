from django.urls import path
from .views import FibonacciView, FibonacciListView

urlpatterns = [
    path('list', FibonacciListView.as_view(), name='fibonacci_list'),
    path('start', FibonacciView.as_view(), name='fibonacci_start'),
]
