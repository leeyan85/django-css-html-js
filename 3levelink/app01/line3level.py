
#coding:utf8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.
import json 
from area import city_dic, province_dic, dist_dic

def ThreeLevel(request):
    return render_to_response('app01/index.html')

            
def SelelectRegion(request):
    
    client_data = request.REQUEST
    level = client_data.get('level')
    if level == 'province':
        province = client_data.get('province')
        if province == 'all':
            provinces = province_dic
            return HttpResponse(json.dumps(provinces))
        elif len(province) == 0:
            print 'hello'
            #return HttpResponse(json.dumps(provinces))
    
    elif level == 'city':
        province_index = client_data.get('province')
        cities = city_dic[province_index]
        return HttpResponse(json.dumps(cities))
        
    elif level == 'dist':
        city_index = client_data.get('city')
        if len(dist_dic[city_index]) != 0:
            dists = json.dumps(dist_dic[city_index])
            return HttpResponse(dists)
        else:
            dists = {'dists':0}
            dists = json.dumps(dists)
            return HttpResponse(dists)

def RegionInfo(request):
    id = request.GET.get('province')
    print id
    message= province_dic[id]
    return HttpResponse(json.dumps(message))

    
    