from django.shortcuts import render

from django.http.response import HttpResponse
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

        cmd = "tesseract " + path + " out && cat out.txt"
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        output = p.stdout.read()

        #XXX One way is to load file from file system. More efficient would be to directly used the bytes in the memory.

        #XXX Use Tesseract API to convert get UTF text from image.

        ocr_text = 'Foo text'
        # Do tesseract OCR here and replace processed text result here.
        response_data=[{"response": output}]
        return HttpResponse(json.dumps(response_data), content_type='application/json')
