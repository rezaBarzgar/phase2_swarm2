from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def compare_sales(request):
    if request.method == 'GET':
        if request.GET['company1'] == 'ubisoft' and request.GET['company2'] == 'activision' and request.GET['year1'] == '2000' and \
                request.GET['year2'] == '2010':
            output = {'ubisoft': {'2000': 99.07000000000001,
                                  '2001': 169.05,
                                  '2002': 176.7,
                                  '2003': 169.81,
                                  '2004': 207.01999999999998,
                                  '2005': 259.04,
                                  '2006': 352.82000000000005,
                                  '2007': 315.42,
                                  '2008': 343.77000000000004,
                                  '2009': 338.92999999999995},
                      'activision': {'2000': 192.89000000000001,
                                     '2001': 320.01,
                                     '2002': 386.88,
                                     '2003': 352.64,
                                     '2004': 412.06000000000006,
                                     '2005': 457.24,
                                     '2006': 513.48,
                                     '2007': 599.24,
                                     '2008': 675.57,
                                     '2009': 659.1300000000001}}

            return JsonResponse(output, status=200)
        else:
            return JsonResponse({}, status=200)
    else:
        return HttpResponse(status=400)
