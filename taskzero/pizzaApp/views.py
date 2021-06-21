from django.db.models.fields import DateTimeField
from django.http import response
from djongo import models
from pizzaApp.models import Pizza
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class Pizza_Info(APIView):
    def post(self,format=None):
        plist = Pizza.objects.values()
        response_dict = {"Pizzas": plist}
        return Response(response_dict, status=200)

class Create_Pizza(APIView):
    def post(self,request,format=None):
        data_f = request.data
        
        apType = str(data_f['pType']).lower()
        apSize = str(data_f['pSize']).lower()
        apTops = str(data_f['pTops']).lower()

        if(apType!="regular" and apType!="square"):
            response_dict = {"Status": "failure"}
            return Response(response_dict, status=401)

        toppings=""

        top = apTops.split(',')

        top.sort()

        for i in top:
            i = i.strip()
            toppings = toppings+i+","
        
        
        apkey = apType+apSize+toppings
        
        try:
            ar = Pizza.objects.create(pizType=apType,pizSize=apSize,pTops=toppings, pkey=apkey)
            
            response_dict = {"Status": "success"}
            return Response(response_dict, status=200)
        except:
            response_dict = {"Status": "failure"}
            return Response(response_dict, status=401)


class EditOrDelete_Pizza(APIView):
    def post(self,request,format=None):
        data_f = request.data
        
        if(data_f["process"]=="edit"):
            try:
                pe = Pizza.objects.filter(pkey=data_f['pkey'])
            except:
                response_dict = {"Status":"failure"}
                return Response(response_dict, status=404)
            
            
            pe.update(pizType = str(data_f["pType"]).lower())  
            
            pe.update(pizSize = str(data_f["pSize"]).lower())  
        
            pe.update(pTops = str(data_f["pTops"]).lower())  

            pe.update(pkey = str(data_f["pType"]+data_f["pSize"]+data_f["pTops"]).lower())

            response_dict = {"Status": "success"}
            return Response(response_dict, status=200)

        elif(data_f["process"]=="delete"):
            try:
                pe = Pizza.objects.filter(pkey=data_f['pkey'])
                pe.delete()
                response_dict = {"Status": "success"}
                return Response(response_dict, status=200)
            except:
                response_dict = {"Status": "failure"}
                return Response(response_dict, status=200)

        else:
            response_dict = {"Status": "wrong input"}
            return Response(response_dict, status=400)

class Filter_Pizza(APIView):
    def post(self,request,format=None):
        data_f = request.data
        
        abt = Pizza.objects.values()

        diction = dict()
        diction2 = dict()
        diction3 = dict()

        for i in abt:
            try:
                diction[i["pizType"]["pizSize"]]=diction[i["pizType"]["pizSize"]]+[i["pizSize"]]
                diction[i["pizType"]["pTops"]]=diction[i["pizType"]["pTops"]]+[i["pTops"]]

                diction2[i["pizSize"]["pizType"]]=diction2[i["pizSize"]["pizType"]]+[i["pizType"]]
                diction2[i["pizSize"]["pTops"]]=diction2[i["pizSize"]["pTops"]]+[i["pTops"]]

                diction3[i["pTops"]["pizSize"]]=diction3[i["pTops"]["pizSize"]]+[i["pizSize"]]
                diction3[i["pTops"]["pizType"]]=diction3[i["pTops"]["pizType"]]+[i["pizType"]]
                
            except:
                diction[i["pizType"]]={"pizSize":[i["pizSize"]],"pTops":[i["pTops"]]}
                diction2[i["pizSize"]]={"pizType":[i["pizType"]],"pTops":[i["pTops"]]}
                diction3[i["pTops"]]={"pizSize":[i["pizSize"]],"pizType":[i["pizType"]]}

        



        response_dict = {"bytype": diction, "bysize": diction2, "bytops":diction3}
        return Response(response_dict, status=200)
       
