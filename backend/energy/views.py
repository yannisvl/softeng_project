from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Actualtotalload, Aggregatedgenerationpertype, Allocatedeicdetail, Areatypecode, Dayaheadtotalloadforecast, Mapcode, Productiontype, Resolutioncode, MyUser, UserStats
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models import F
from itertools import chain
import csv, io
from django.contrib import messages
from django.template import loader
from django.template import RequestContext
import os
from datetime import datetime
from django.utils.dateparse import parse_datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import connections
from django.db.utils import OperationalError
from .forms import UploadFileForm, SignUpForm
from collections import defaultdict
from itertools import zip_longest
import requests
from datetime import datetime
from django.contrib.auth.hashers import make_password

def test(request):
    return HttpResponse(str(request.META))
'''
def upload_file_ATL(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                i=0
                count_before= Actualtotalload.objects.all().count()
                for column in csv.reader(io_string, delimiter=';', quotechar="|"):
                    i+=1
                    x = Actualtotalload.objects.filter(id = column[0])
                    if x:
                        x.update(entitycreatedat=parse_datetime(column[1]), entitymodifiedat=parse_datetime(column[2]),\
                                 actiontaskid=column[3],status=column[4][:2],year=column[5],month=column[6],day=column[7],\
                                 datetime=column[8],areaname=column[9],updatetime=column[10],totalloadvalue=column[11],\
                                 areatypecodeid=Areatypecode.objects.get(pk=column[12]),mapcodeid=Mapcode.objects.get(pk=column[15]),\
                                 areacodeid=Allocatedeicdetail.objects.get(pk=column[13]),\
                                 resolutioncodeid=Resolutioncode.objects.get(pk=column[14]),rowhash=column[16])
                    else:
                        Actualtotalload.objects.create(
                        id=column[0],
                        entitycreatedat=parse_datetime(column[1]),
                        entitymodifiedat=parse_datetime(column[2]),
                        actiontaskid=column[3],
                        status=column[4][:2],
                        year=column[5],
                        month=column[6],
                        day=column[7],
                        datetime=column[8],
                        areaname=column[9],
                        updatetime=column[10],
                        totalloadvalue=column[11],
                        areatypecodeid=Areatypecode.objects.get(pk=column[12]),
                        mapcodeid=Mapcode.objects.get(pk=column[15]),
                        areacodeid=Allocatedeicdetail.objects.get(pk=column[13]),
                        resolutioncodeid=Resolutioncode.objects.get(pk=column[14]),
                        rowhash=column[16]
                        )
                count_after= Actualtotalload.objects.all().count()
                context={'totalRecordsInFile':i, 'totalRecordsImported':count_after-count_before, 'totalRecordsInDatabase':count_after}
                return JsonResponse(context)
            else:
                response = HttpResponse('400: Bad request\n')
                response.status_code = 400
                return response
        else:
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        response = HttpResponse('401: Not authorized\n')
        response.status_code = 401
        return response

def upload_file_ATL(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                fields=next(io_string)
                s=fields[:-1].split(';')
                d={}
                k=0
                
                for f in s:
                    d[f]=k
                    k+=1
                lines=data_set.split("\n")
                i=0
                count_before= Actualtotalload.objects.all().count()
                for column in csv.reader(io_string, delimiter=';', quotechar="|"):
                    i+=1
                    x = Actualtotalload.objects.filter(id = column[d['Id']])
                    if x:
                        x.update(
                             entitycreatedat=parse_datetime(column[d['EntityCreatedAt']]),                          entitymodifiedat=parse_datetime(column[d['EntityModifiedAt']]),
                                 actiontaskid=column[d['ActionTaskID']],status=column[d['Status']][:2],year=column[d['Year']],month=column[d['Month']],day=column[d['Day']], datetime=column[d['DateTime']],areaname=column[d['AreaName']],updatetime=column[d['UpdateTime']],totalloadvalue=column[d['TotalLoadValue']],
                                 areatypecodeid=Areatypecode.objects.get(pk=column[d['AreaTypeCodeId']]),mapcodeid=Mapcode.objects.get(pk=column[d['MapCodeId']]),
                                 areacodeid=Allocatedeicdetail.objects.get(pk=column[d['AreaCodeId']]),
                                 resolutioncodeid=Resolutioncode.objects.get(pk=column[d['ResolutionCodeId']]),rowhash=column[d['RowHash']])
                    else:
                    Actualtotalload.objects.create(
                        entitycreatedat=parse_datetime(column[d['EntityCreatedAt']]), entitymodifiedat=parse_datetime(column[d['EntityModifiedAt']]),\
                                 actiontaskid=column[d['ActionTaskID']],status=column[d['Status']][:2],year=column[d['Year']],month=column[d['Month']],day=column[d['Day']],\
                                 datetime=column[d['DateTime']],areaname=column[d['AreaName']],updatetime=column[d['UpdateTime']],totalloadvalue=column[d['TotalLoadValue']],\
                                 areatypecodeid=Areatypecode.objects.get(pk=column[d['AreaTypeCodeId']]),mapcodeid=Mapcode.objects.get(pk=column[d['MapCodeId']]),\
                                 areacodeid=Allocatedeicdetail.objects.get(pk=column[d['AreaCodeId']]),\
                                 resolutioncodeid=Resolutioncode.objects.get(pk=column[d['ResolutionCodeId']]),rowhash=column[d['RowHash']])
                count_after= Actualtotalload.objects.all().count()
                context={'totalRecordsInFile':i, 'totalRecordsImported':count_after-count_before, 'totalRecordsInDatabase':count_after}
                return JsonResponse(context)
            else:
                response = HttpResponse('400: Bad request\n')
                response.status_code = 400
                return response
        else:
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        response = HttpResponse('401: Not authorized\n')
        response.status_code = 401
        return response
'''

def upload_file_ATL(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                data_list=[]
                count_before= Actualtotalload.objects.all().count()
                i=0
                for column in csv.reader(io_string, delimiter=';', quotechar="|"):
                    i+=1
                    x = Actualtotalload.objects.filter(id = column[0])
                    if x:
                        x.update(entitycreatedat=parse_datetime(column[1]), entitymodifiedat=parse_datetime(column[2]),\
                                 actiontaskid=column[3],status=column[4][:2],year=column[5],month=column[6],day=column[7],\
                                 datetime=column[8],areaname=column[9],updatetime=column[10],totalloadvalue=column[11],\
                                 areatypecodeid=Areatypecode.objects.get(pk=column[12]),mapcodeid=Mapcode.objects.get(pk=column[15]),\
                                 areacodeid=Allocatedeicdetail.objects.get(pk=column[13]),\
                                 resolutioncodeid=Resolutioncode.objects.get(pk=column[14]),rowhash=column[16])
                    else:
                        data={
                        "id":column[0],
                        "entitycreatedat":parse_datetime(column[1]),
                        "entitymodifiedat":parse_datetime(column[2]),
                        "actiontaskid":column[3],
                        "status":column[4][:2],
                        "year":column[5],
                        "month":column[6],
                        "day":column[7],
                        "datetime":column[8],
                        "areaname":column[9],
                        "updatetime":column[10],
                        "totalloadvalue":column[11],
                        "areatypecodeid":Areatypecode.objects.get(pk=column[12]),
                        "mapcodeid":Mapcode.objects.get(pk=column[15]),
                        "areacodeid":Allocatedeicdetail.objects.get(pk=column[13]),
                        "resolutioncodeid":Resolutioncode.objects.get(pk=column[14]),
                        "rowhash":column[16]
                        }
                        data_list.append(Actualtotalload(**data))
                Actualtotalload.objects.bulk_create(data_list)
                count_after= Actualtotalload.objects.all().count()
                context={'totalRecordsInFile':i, 'totalRecordsImported':count_after-count_before, 'totalRecordsInDatabase':count_after}
                return JsonResponse(context)
            else:
                response = HttpResponse('400: Bad request\n')
                response.status_code = 400
                return response
        else:
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        response = HttpResponse('401: Not authorized\n')
        response.status_code = 401
        return response


'''
def upload_file_AGPT(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                i=0
                count_before= Aggregatedgenerationpertype.objects.all().count()
                for column in csv.reader(io_string, delimiter=';', quotechar="|"):
                    i+=1
                    x = Aggregatedgenerationpertype.objects.filter(id = column[0])
                    if x:
                        x.update(entitycreatedat=parse_datetime(column[1]),
                    entitymodifiedat=parse_datetime(column[2]),
                    actiontaskid=column[3],
                    status=column[4][:2],
                    year=column[5],
                    month=column[6],
                    day=column[7],
                    datetime=column[8],
                    areaname=column[9],
                    updatetime=column[10],
                    actualgenerationoutput=column[11],
                    actualconsuption=column[12],
                    areatypecodeid=Areatypecode.objects.get(pk=column[13]),
                    productiontypeid=Productiontype.objects.get(pk=column[17]),
                    resolutioncodeid=Resolutioncode.objects.get(pk=column[15]),
                    mapcodeid=Mapcode.objects.get(pk=column[16]),
                    areacodeid=Allocatedeicdetail.objects.get(pk=column[14]),
                    rowhash=column[18])
                    else:
                        Aggregatedgenerationpertype.objects.create(
                        id=column[0],
                        entitycreatedat=parse_datetime(column[1]),
                        entitymodifiedat=parse_datetime(column[2]),
                        actiontaskid=column[3],
                        status=column[4][:2],
                        year=column[5],
                        month=column[6],
                        day=column[7],
                        datetime=column[8],
                        areaname=column[9],
                        updatetime=column[10],
                        actualgenerationoutput=column[11],
                        actualconsuption=column[12],
                        areatypecodeid=Areatypecode.objects.get(pk=column[13]),
                        productiontypeid=Productiontype.objects.get(pk=column[17]),
                        resolutioncodeid=Resolutioncode.objects.get(pk=column[15]),
                        mapcodeid=Mapcode.objects.get(pk=column[16]),
                        areacodeid=Allocatedeicdetail.objects.get(pk=column[14]),
                        rowhash=column[18]
                        )
                count_after= Aggregatedgenerationpertype.objects.all().count()
                context={'totalRecordsInFile':i, 'totalRecordsImported':count_after-count_before, 'totalRecordsInDatabase':count_after}
                return JsonResponse(context)
        else:
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        response = HttpResponse('401: Not authorized\n')
        response.status_code = 401
        return response
'''
def upload_file_AGPT(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                i=0
                data_list=[]
                count_before= Aggregatedgenerationpertype.objects.all().count()
                for column in csv.reader(io_string, delimiter=';', quotechar="|"):
                    i+=1
                    x = Aggregatedgenerationpertype.objects.filter(id = column[0])
                    if x:
                        x.update(entitycreatedat=parse_datetime(column[1]),
                    entitymodifiedat=parse_datetime(column[2]),
                    actiontaskid=column[3],
                    status=column[4][:2],
                    year=column[5],
                    month=column[6],
                    day=column[7],
                    datetime=column[8],
                    areaname=column[9],
                    updatetime=column[10],
                    actualgenerationoutput=column[11],
                    actualconsuption=column[12],
                    areatypecodeid=Areatypecode.objects.get(pk=column[13]),
                    productiontypeid=Productiontype.objects.get(pk=column[17]),
                    resolutioncodeid=Resolutioncode.objects.get(pk=column[15]),
                    mapcodeid=Mapcode.objects.get(pk=column[16]),
                    areacodeid=Allocatedeicdetail.objects.get(pk=column[14]),
                    rowhash=column[18])
                    else:
                        data={
                        "id":column[0],
                        "entitycreatedat":parse_datetime(column[1]),
                        "entitymodifiedat":parse_datetime(column[2]),
                        "actiontaskid":column[3],
                        "status":column[4][:2],
                        "year":column[5],
                        "month":column[6],
                        "day":column[7],
                        "datetime":column[8],
                        "areaname":column[9],
                        "updatetime":column[10],
                        "actualgenerationoutput":column[11],
                        "actualconsuption":column[12],
                        "areatypecodeid":Areatypecode.objects.get(pk=column[13]),
                        "productiontypeid":Productiontype.objects.get(pk=column[17]),
                        "resolutioncodeid":Resolutioncode.objects.get(pk=column[15]),
                        "mapcodeid":Mapcode.objects.get(pk=column[16]),
                        "areacodeid":Allocatedeicdetail.objects.get(pk=column[14]),
                        "rowhash":column[18]
                        }
                        data_list.append(Aggregatedgenerationpertype(**data))
                Aggregatedgenerationpertype.objects.bulk_create(data_list)
                count_after= Aggregatedgenerationpertype.objects.all().count()
                context={'totalRecordsInFile':i, 'totalRecordsImported':count_after-count_before, 'totalRecordsInDatabase':count_after}
                return JsonResponse(context)
        else:
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        response = HttpResponse('401: Not authorized\n')
        response.status_code = 401
        return response

'''
def upload_file_DATLF(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                i=0
                count_before= Dayaheadtotalloadforecast.objects.all().count()
                for column in csv.reader(io_string, delimiter=';', quotechar="|"):
                    i+=1
                    x = Dayaheadtotalloadforecast.objects.filter(id = column[0])
                    if x:
                        x.update(entitycreatedat=parse_datetime(column[1]), entitymodifiedat=parse_datetime(column[2]),\
                                 actiontaskid=column[3],status=column[4][:2],year=column[5],month=column[6],day=column[7],\
                                 datetime=column[8],areaname=column[9],updatetime=column[10],totalloadvalue=column[11],\
                                 areatypecodeid=Areatypecode.objects.get(pk=column[12]),mapcodeid=Mapcode.objects.get(pk=column[15]),\
                                 areacodeid=Allocatedeicdetail.objects.get(pk=column[13]),\
                                 resolutioncodeid=Resolutioncode.objects.get(pk=column[14]),rowhash=column[16])
                    else:
                        Dayaheadtotalloadforecast.objects.create(
                        id=column[0],
                        entitycreatedat=parse_datetime(column[1]),
                        entitymodifiedat=parse_datetime(column[2]),
                        actiontaskid=column[3],
                        status=column[4][:2],
                        year=column[5],
                        month=column[6],
                        day=column[7],
                        datetime=column[8],
                        areaname=column[9],
                        updatetime=column[10],
                        totalloadvalue=column[11],
                        areatypecodeid=Areatypecode.objects.get(pk=column[12]),
                        mapcodeid=Mapcode.objects.get(pk=column[15]),
                        areacodeid=Allocatedeicdetail.objects.get(pk=column[13]),
                        resolutioncodeid=Resolutioncode.objects.get(pk=column[14]),
                        rowhash=column[16]
                        )
                count_after= Dayaheadtotalloadforecast.objects.all().count()
                context={'totalRecordsInFile':i, 'totalRecordsImported':count_after-count_before, 'totalRecordsInDatabase':count_after}
                return JsonResponse(context)
            else:
                response = HttpResponse('400: Bad request\n')
                response.status_code = 400
                return response
        else:
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        response = HttpResponse('401: Not authorized\n')
        response.status_code = 401
        return response
'''
def upload_file_DATLF(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['file']
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                i=0
                data_list=[]
                count_before= Dayaheadtotalloadforecast.objects.all().count()
                for column in csv.reader(io_string, delimiter=';', quotechar="|"):
                    i+=1
                    x = Dayaheadtotalloadforecast.objects.filter(id = column[0])
                    if x:
                        x.update(entitycreatedat=parse_datetime(column[1]), entitymodifiedat=parse_datetime(column[2]),\
                                 actiontaskid=column[3],status=column[4][:2],year=column[5],month=column[6],day=column[7],\
                                 datetime=column[8],areaname=column[9],updatetime=column[10],totalloadvalue=column[11],\
                                 areatypecodeid=Areatypecode.objects.get(pk=column[12]),mapcodeid=Mapcode.objects.get(pk=column[15]),\
                                 areacodeid=Allocatedeicdetail.objects.get(pk=column[13]),\
                                 resolutioncodeid=Resolutioncode.objects.get(pk=column[14]),rowhash=column[16])
                    else:
                        data={
                            "id":column[0],
                            "entitycreatedat":parse_datetime(column[1]),
                            "entitymodifiedat":parse_datetime(column[2]),
                            "actiontaskid":column[3],
                            "status":column[4][:2],
                            "year":column[5],
                            "month":column[6],
                            "day":column[7],
                            "datetime":column[8],
                            "areaname":column[9],
                            "updatetime":column[10],
                            "totalloadvalue":column[11],
                            "areatypecodeid":Areatypecode.objects.get(pk=column[12]),
                            "mapcodeid":Mapcode.objects.get(pk=column[15]),
                            "areacodeid":Allocatedeicdetail.objects.get(pk=column[13]),
                            "resolutioncodeid":Resolutioncode.objects.get(pk=column[14]),
                            "rowhash":column[16]
                        }
                        data_list.append(Dayaheadtotalloadforecast(**data))
                    #if i==10:break
                Dayaheadtotalloadforecast.objects.bulk_create(data_list)
                count_after= Dayaheadtotalloadforecast.objects.all().count()
                context={'totalRecordsInFile':i, 'totalRecordsImported':count_after-count_before, 'totalRecordsInDatabase':count_after}
                return JsonResponse(context)
            else:
                response = HttpResponse('400: Bad request\n')
                response.status_code = 400
                return response
        else:
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        response = HttpResponse('401: Not authorized\n')
        response.status_code = 401
        return response


def check_connection(request):
  if request.method == 'GET':
      db_conn = connections['default']
      try:
        c = db_conn.cursor()
      except OperationalError:
        context = {"status":"NOT OK"}
      else:
        context={"status":"OK"}
      return JsonResponse(context)
  else:
      response = HttpResponse('400: Bad request\n')
      response.status_code = 400
      return response
  
def reset_db(request):
  if request.method == "POST":
    Actualtotalload.objects.all().delete()
    Aggregatedgenerationpertype.objects.all().delete()
    Dayaheadtotalloadforecast.objects.all().delete() 
    MyUser.objects.exclude(username='admin').delete()
    return JsonResponse({"status":"OK"})
  else:
    response = HttpResponse('400: Bad request\n')
    response.status_code = 400
    return response 

def sign_up(request):
  if request.user.is_superuser:
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User created successfully\n')
        else:
            print("valid else")
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        print("post_else")
        response = HttpResponse('400: Bad request\n')
        response.status_code = 400
        return response
  else:
    response = HttpResponse('401: Not authorized\n')
    response.status_code = 401
    return response

def github(request):
    template = 'energy/github.html'
    user = {}
    if 'uname' in request.GET:
        username = request.GET['uname']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'energy/github.html', {'user': user})

def modify1(request, username):
    if request.user.is_superuser:
        if request.method == "GET":
            try:
                us = MyUser.objects.get(username = username)
                us2 = UserStats.objects.get(user_id = us.id)
            except:
                response = HttpResponse('403: No data\n')
                response.status_code = 403
                return response
            d = {}
            d['username'] = us.username
            d['email'] = us.email
            d['quota'] = us2.quota
            d['remainingquota'] = us2.remainingquota
            d['last_activity'] = us2.last_activity
            return JsonResponse(d, safe=False)
        elif request.method == "PUT":
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            us = MyUser.objects.filter(username=username)
            us2 = UserStats.objects.filter(user_id = us.values()[0]['id'])
            if 'email' in request.PUT:
                us.update(email=request.PUT.get('email'))
            else:
                response = HttpResponse('39834908')
                return response
            if 'quota' in request.PUT:
                us2.update(quota=request.PUT.get('quota'), remainingquota=request.PUT.get('quota'))
            else:
                response = HttpResponse('398345664908')
                return response
            if 'passw' in request.PUT:
                us.update(password=make_password(request.PUT.get('passw')))
            else:
                response = HttpResponse('39843453734908')
                return response
            return HttpResponse('Successfully Modified\n')
        else:
            response = HttpResponse('400: Bad request\n')
            response.status_code = 400
            return response
    else:
        response = HttpResponse('401: Not authorized\n')
        response.status_code = 401
        return response

def query1a(request, name_of_area, resol, y, m, d):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Actualtotalload.objects.filter(areaname=name_of_area, year=y, month=m, day=d, resolutioncodeid=r.id).values('areaname', 'areatypecodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'totalloadvalue', 'updatetime', 'mapcodeid')
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["resolutioncodeid"] = Resolutioncode.objects.get(pk=d["resolutioncodeid"]).resolutioncodetext
        d["Source"]="entso-e"
        d["Dataset"]="ActualTotalLoad"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"] = d.pop("areatypecodeid")
        d["MapCode"] = d.pop("mapcodeid")
        d["ResolutionCode"] = d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["DateTimeUTC"]=d.pop("datetime")
        d["ActualTotalLoadValue"]=d.pop("totalloadvalue")
        d["UpdateTimeUTC"]=d.pop("updatetime")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query1b(request, name_of_area, resol, y, m):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Actualtotalload.objects.filter(areaname=name_of_area, year=y, month=m, resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day').\
    order_by('day').annotate(totalload=Sum('totalloadvalue'))
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = resol
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="ActualTotalLoad"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["ActualTotalLoadByDayValue"]=d.pop("totalload")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query1c(request, name_of_area, resol, y):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Actualtotalload.objects.filter(areaname=name_of_area, year=y, resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month').\
    order_by('month').annotate(totalload=Sum('totalloadvalue'))
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = resol
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="ActualTotalLoad"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["ActualTotalLoadByYearValue"]=d.pop("totalload")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query2a1(request, name_of_area, resol, prod_type, y, m, d):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    p = Productiontype.objects.get(productiontypetext=prod_type)
    l = Aggregatedgenerationpertype.objects.filter(areaname=name_of_area, year=y, month=m, day=d, productiontypeid=p.id, resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'actualgenerationoutput', 'updatetime', 'mapcodeid', 'productiontypeid')
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = Resolutioncode.objects.get(pk=d["resolutioncodeid"]).resolutioncodetext
        d["productiontypeid"] = Productiontype.objects.get(pk=d["productiontypeid"]).productiontypetext
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="AggregatedGenerationPerType"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["DateTimeUTC"]=d.pop("datetime")
        d["ProductionType"]=d.pop("productiontypeid")
        d["ActualGenerationOutputValue"]=d.pop("actualgenerationoutput")
        d["UpdateTimeUTC"]=d.pop("updatetime")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query2b1(request, name_of_area, resol, prod_type, y, m):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    p = Productiontype.objects.get(productiontypetext=prod_type)
    l = Aggregatedgenerationpertype.objects.filter(areaname=name_of_area, year=y, month=m, productiontypeid=p.id, resolutioncodeid=r.id).\
 values('areaname','mapcodeid','areatypecodeid','year','month','day','productiontypeid','resolutioncodeid').order_by('day').annotate(actualgen=Sum('actualgenerationoutput'))
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response    
    for d in l:
        d["resolutioncodeid"] = resol
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["productiontypeid"] = Productiontype.objects.get(pk=d["productiontypeid"]).productiontypetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="AggregatedGenerationPerType"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["ProductionType"]=d.pop("productiontypeid")
        d["ActualGenerationOutputValue"]=d.pop("actualgen")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query2c1(request, name_of_area, resol, prod_type, y):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    p = Productiontype.objects.get(productiontypetext=prod_type)
    l = Aggregatedgenerationpertype.objects.filter(areaname=name_of_area, year=y, productiontypeid=p.id, resolutioncodeid=r.id).\
 values('areaname','mapcodeid','areatypecodeid','year','month','productiontypeid','resolutioncodeid').order_by('month').annotate(actualgen=Sum('actualgenerationoutput'))
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = resol
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["productiontypeid"] = Productiontype.objects.get(pk=d["productiontypeid"]).productiontypetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="AggregatedGenerationPerType"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["ProductionType"]=d.pop("productiontypeid")
        d["ActualGenerationOutputValue"]=d.pop("actualgen")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query2a2(request, name_of_area, resol, y, m, d):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Aggregatedgenerationpertype.objects.filter(areaname=name_of_area, year=y, month=m, day=d, resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'actualgenerationoutput', 'updatetime', 'mapcodeid', 'productiontypeid')
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = Resolutioncode.objects.get(pk=d["resolutioncodeid"]).resolutioncodetext
        d["productiontypeid"] = Productiontype.objects.get(pk=d["productiontypeid"]).productiontypetext
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="AggregatedGenerationPerType"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["DateTimeUTC"]=d.pop("datetime")
        d["ProductionType"]=d.pop("productiontypeid")
        d["ActualGenerationOutputValue"]=d.pop("actualgenerationoutput")
        d["UpdateTimeUTC"]=d.pop("updatetime")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query2b2(request, name_of_area, resol, y, m):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Aggregatedgenerationpertype.objects.filter(areaname=name_of_area, year=y, month=m, resolutioncodeid=r.id).\
    values('areaname','mapcodeid','areatypecodeid','year','month','day','productiontypeid','resolutioncodeid').order_by('day').\
    annotate(actualgen=Sum('actualgenerationoutput'))
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = resol
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["productiontypeid"] = Productiontype.objects.get(pk=d["productiontypeid"]).productiontypetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="AggregatedGenerationPerType"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["ProductionType"]=d.pop("productiontypeid")
        d["ActualGenerationOutputValue"]=d.pop("actualgen")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query2c2(request, name_of_area, resol, y):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Aggregatedgenerationpertype.objects.filter(areaname=name_of_area, year=y, resolutioncodeid=r.id).\
 values('areaname','mapcodeid','areatypecodeid','year','month','productiontypeid','resolutioncodeid').order_by('month').annotate(actualgen=Sum('actualgenerationoutput'))
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = resol
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["productiontypeid"] = Productiontype.objects.get(pk=d["productiontypeid"]).productiontypetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="AggregatedGenerationPerType"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["ProductionType"]=d.pop("productiontypeid")
        d["ActualGenerationOutputValue"]=d.pop("actualgen")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query3a(request, name_of_area, resol, y, m, d):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Dayaheadtotalloadforecast.objects.filter(areaname=name_of_area, year=y, month=m, day=d, resolutioncodeid=r.id).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'totalloadvalue', 'updatetime')
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["resolutioncodeid"] = Resolutioncode.objects.get(pk=d["resolutioncodeid"]).resolutioncodetext
        d["Source"]="entso-e"
        d["Dataset"]="DayAheadTotalLoadForecast"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"] = d.pop("areatypecodeid")
        d["MapCode"] = d.pop("mapcodeid")
        d["ResolutionCode"] = d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["DateTimeUTC"]=d.pop("datetime")
        d["DayAheadTotalLoadForecastValue"]=d.pop("totalloadvalue")
        d["UpdateTimeUTC"]=d.pop("updatetime")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query3b(request, name_of_area, resol, y, m):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Dayaheadtotalloadforecast.objects.filter(areaname=name_of_area, year=y, month=m, resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day').\
    order_by('day').annotate(totalload=Sum('totalloadvalue'))
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = resol
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="DayAheadTotalLoadForecast"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["DayAheadTotalLoadForecastValue"]=d.pop("totalload")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query3c(request, name_of_area, resol, y):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l = Dayaheadtotalloadforecast.objects.filter(areaname=name_of_area, year=y, resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month').\
    order_by('month').annotate(totalload=Sum('totalloadvalue'))
    if (len(l)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l:
        d["resolutioncodeid"] = resol
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["Source"]="entso-e"
        d["Dataset"]="DayAheadTotalLoadForecast"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"]=d.pop("areatypecodeid")
        d["MapCode"]=d.pop("mapcodeid")
        d["ResolutionCode"]=d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["DayAheadTotalLoadForecastValue"]=d.pop("totalload")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l[0].keys())
    for d in l:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l), safe=False, content_type='application/json')

def query4a(request, name_of_area, resol, y, m, d):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l1 = Actualtotalload.objects.filter(areaname=name_of_area, year=y, month=m, day=d, resolutioncodeid=r.id).\
    annotate(realtotalload=F('totalloadvalue')).\
    values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'realtotalload')
    l2 = Dayaheadtotalloadforecast.objects.filter(areaname=name_of_area, year=y, month=m, day=d, resolutioncodeid=r.id).\
    values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'totalloadvalue')
    l3 = [{**u, **v} for u,v in zip(l1,l2)]
    if (len(l3)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l3:
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["resolutioncodeid"] = Resolutioncode.objects.get(pk=d["resolutioncodeid"]).resolutioncodetext
        d["Source"]="entso-e"
        d["Dataset"]="ActualvsForecast"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"] = d.pop("areatypecodeid")
        d["MapCode"] = d.pop("mapcodeid")
        d["ResolutionCode"] = d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["DateTimeUTC"]=d.pop("datetime")
        d["DayAheadTotalLoadForecastValue"]=d.pop("totalloadvalue")
        d["ActualTotalLoadValue"] = d.pop("realtotalload")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l3[0].keys())
    for d in l3:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l3), safe=False, content_type='application/json')

def query4b(request, name_of_area, resol, y, m):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l1 = Actualtotalload.objects.filter(areaname=name_of_area, year=y, month=m, resolutioncodeid=r.id).annotate(realtotalload=F('totalloadvalue')).annotate(realtotalload=Sum('realtotalload')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'realtotalload')
    l2 = Dayaheadtotalloadforecast.objects.filter(areaname=name_of_area, year=y, month=m, resolutioncodeid=r.id).annotate(totalload=Sum('totalloadvalue')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'day', 'datetime', 'totalloadvalue')
    l3 = [{**u, **v} for u, v in zip(l1, l2)]
    if (len(l3)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l3:
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["resolutioncodeid"] = Resolutioncode.objects.get(pk=d["resolutioncodeid"]).resolutioncodetext
        d["Source"]="entso-e"
        d["Dataset"]="ActualvsForecast"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"] = d.pop("areatypecodeid")
        d["MapCode"] = d.pop("mapcodeid")
        d["ResolutionCode"] = d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["Day"]=d.pop("day")
        d["DateTimeUTC"]=d.pop("datetime")
        d["DayAheadTotalLoadForecastValue"]=d.pop("totalloadvalue")
        d["ActualTotalLoadValue"] = d.pop("realtotalload")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l3[0].keys())
    for d in l3:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l3), safe=False, content_type='application/json')

def query4c(request, name_of_area, resol, y):
    if (not request.user.is_superuser):
        userstat = UserStats.objects.filter(user_id = request.user.id)
        uservals = userstat.values()[0]
        dmy = uservals['last_activity']
        k = datetime.now()
        curtime = datetime(k.year, k.month, k.day)
        if (not (dmy.day == curtime.day and dmy.month == curtime.month and dmy.year == curtime.year)):
            userstat.update(remainingquota = uservals['quota'])
        uservals = userstat.values()[0]
        currquota = uservals['remainingquota']
        if currquota > 0:
            currquota -= 1
            userstat.update(remainingquota = currquota, last_activity = curtime)
        else:
            response = HttpResponse('402: Out of quota')
            response.status_code = 402
            return response
    output_format = request.GET.get('format')
    r = Resolutioncode.objects.get(resolutioncodetext=resol)
    l1 = Actualtotalload.objects.filter(areaname=name_of_area, year=y, resolutioncodeid=r.id).annotate(realtotalload=F('totalloadvalue')).order_by('month').annotate(realtotalload=Sum('realtotalload')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year', 'month', 'realtotalload')
    l2 = Dayaheadtotalloadforecast.objects.filter(areaname=name_of_area, year=y, resolutioncodeid=r.id).annotate(totalload=Sum('totalloadvalue')).values('areaname', 'areatypecodeid', 'mapcodeid', 'resolutioncodeid', 'year','month', 'totalloadvalue')
    l3 = [{**u, **v} for u, v in zip(l1, l2)]
    if (len(l3)==0):
        response=HttpResponse('403: No data')
        response.status_code=403
        return response
    for d in l3:
        d["areatypecodeid"] = Areatypecode.objects.get(pk=d["areatypecodeid"]).areatypecodetext
        d["mapcodeid"] = Mapcode.objects.get(pk=d["mapcodeid"]).mapcodetext
        d["resolutioncodeid"] = Resolutioncode.objects.get(pk=d["resolutioncodeid"]).resolutioncodetext
        d["Source"]="entso-e"
        d["Dataset"]="ActualvsForecast"
        d["AreaName"]=d.pop("areaname")
        d["AreaTypeCode"] = d.pop("areatypecodeid")
        d["MapCode"] = d.pop("mapcodeid")
        d["ResolutionCode"] = d.pop("resolutioncodeid")
        d["Year"]=d.pop("year")
        d["Month"]=d.pop("month")
        d["DayAheadTotalLoadForecastValue"]=d.pop("totalloadvalue")
        d["ActualTotalLoadValue"] = d.pop("realtotalload")
    response1 = HttpResponse(content_type='text/csv')
    writer = csv.writer(response1)
    writer.writerow(l3[0].keys())
    for d in l3:
        writer.writerow(d.values())
    if output_format=='csv':
        return response1
    else:
        return JsonResponse(list(l3), safe=False, content_type='application/json')
