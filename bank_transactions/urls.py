from django.urls import path
from .views import BankTransactions, BankTransactionsDetail

urlpatterns = [
    path('', BankTransactions.as_view()),
    path('<int:id>', BankTransactionsDetail.as_view()),
]