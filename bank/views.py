from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView




# Create your views here.
def home(request):
    return render(request, 'bank/home.html')


class IfscView(APIView):
    # ''' 
    # return response for query ./api/ifsc/{ifsc} 
    #
    #  if branch_with_ifsc exist:
    #        return branch json respone
    #   else:
    #        404 error
    # '''
    def get_object(self, ifsc):
        try:
            branch = Branch.objects.get(ifsc=ifsc)
            return branch
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, ifsc):
        branch = self.get_object(ifsc)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

class CityBankNameView(APIView):
    # '''
    # return: respone for query on endpoint ./api/branch/{bank_name}/}{city_name}
    # 
    # if branch in CITY of BANK exist:
        # return all matching query
    # else:
    #   return 404
    #    
    # '''
    def get_object(self, bank_name, city_name):
        try:
            branches = Branch.objects.filter(bank__name__icontains=bank_name, city__icontains=city_name)
            return branches
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request, bank_name, city_name):
        try:
            branches = self.get_object(bank_name, city_name)
            serializer = BranchSerializer(branches, many=True)
            return Response(serializer.data)
        except:
              return HttpResponse(status=status.HTTP_404_NOT_FOUND)
