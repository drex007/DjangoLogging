from django.shortcuts import render
from django.http import HttpResponse
import logging

# Create your views here.
logger = logging.getLogger("main")

def index(request):
    try:
        1/0
    except Exception as e:
        logger.info(f"This is the log message {e}")
    return HttpResponse("<h1>Hi!!!!!!!! Django<h1/>")