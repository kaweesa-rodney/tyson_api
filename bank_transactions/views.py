from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Bank_transactions
from .serializers import BankTranSerializer
from rest_framework import permissions



# Create your views here.
class BankTransactions(ListCreateAPIView):

    serializer_class = BankTranSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(entry_user=self.request.user)


    def get_queryset(self):
        return Bank_transactions.objects.filter(entry_user=self.request.user)



class BankTransactionsDetail(RetrieveUpdateDestroyAPIView):

    serializer_class = BankTranSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
    

    def get_queryset(self):
        return Bank_transactions.objects.filter(entry_user=self.request.user)