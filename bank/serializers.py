from .models import Bank, Branch
from rest_framework import serializers

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    bank = serializers.CharField(source='bank.name', read_only=True)
    class Meta:
        model = Branch
        fields = ["ifsc","address","city","state","bank"]
