import requests
from itertools import count
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

API_URL = 'https://covid-19.dataflowkit.com/v1/'
FLAG_URL = 'https://countryflagsapi.com/svg/'


def Home(request):
    return HttpResponse(
        """
            Please visit localhost/api/ for get details from api.
            For getting county details visit localhost/api/[county_name]
        """
    )


class CountryView(generics.ListAPIView):
    """
        For getting details of a county

        ### how its work
            1. get a country name from api exm: localhost/api/jaPan it will read japan as a country
            2. make it lower to avoid typo exm: jaPan => japan
            3. if its not match any country its return World summary as main api returns data
    """
    def get(self, request, country, *args, **kwargs):
        # get county name and make url path
        url = f'{API_URL}{country.lower()}'
        country_flag_url = f'{FLAG_URL}{country.lower()}'
        data = requests.get(url)
        flag = requests.get(country_flag_url)
        try:
            # make data to json format for better readability
            data = data.json()
        except:
            return Response({"Error: Please visit after some time later"})
        returning_data = {"data": data, "flag": flag}
        return Response(returning_data)


class GlobalView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        url = f'{API_URL}world'
        data = requests.get(url)
        try:
            # make data to json format
            data = data.json()
            print(data)
        except:
            return Response({"Error: Please visit after some time later"})
        return Response(data)
