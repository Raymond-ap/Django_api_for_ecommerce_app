from django.http import JsonResponse, request
from django.shortcuts import render

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def APIOVERVIEW(request):
    pass