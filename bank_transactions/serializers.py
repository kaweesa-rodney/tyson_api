from ast import Mod
from rest_framework.serializers import ModelSerializer
from .models import Bank_transactions


class BankTranSerializer(ModelSerializer):

    class Meta:
        model = Bank_transactions

        fields = ['entry_user', 'tran_id', 'amount', 'entry_date', 'payment_method']