from django.shortcuts import render

from django.http.response import HttpResponse
from datetime import datetime

from models import Image
import json
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from pdir import pdir

import subprocess

@csrf_exempt
def upload_photo(request):
    if request.method == 'POST':
        image = request.FILES['photo']

        img = Image(photo=image,)
        img.save()
        path =  img.photo.path

        t1 = datetime.now()     # For profiling performance
        # Do tesseract OCR here and replace processed text result here.
        cmd = "tesseract " + path + " out && cat out.txt"
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        t2 = datetime.now()     # For profiling performance
        ocr_microseconds = (t2 - t1).microseconds                 # Total time spent by server in performing OCR on local image
        output = p.stdout.read()

        #XXX One way is to load file from file system. More efficient would be to directly used the bytes in the memory.

        response_data=[{"response": output, "ocr_microseconds": ocr_microseconds}]
        return HttpResponse(json.dumps(response_data), content_type='application/json')
