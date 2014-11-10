from django.shortcuts import render

from django.http.response import HttpResponse
from models import Image
import json
# Create your views here.

def upload_photo(request):
    if request.method == 'POST':
        image = request.FILES['photo']
        image = Image(photo=image,)
        image.save()
        print image
        ocr_text = 'Foo text'
        # Do tesseract OCR here and replace processed text result here.
        response_data=[{"response": ocr_text}]
        return HttpResponse(json.dumps(response_data), mimetype='application/json')
