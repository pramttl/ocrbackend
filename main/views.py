from django.shortcuts import render

from django.http.response import HttpResponse
from models import Image
import json
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_photo(request):
    if request.method == 'POST':
        image = request.FILES['photo']

        #XXX Now convert image file to OpenCV Image type
        #image = Image(photo=image,)
        #image.save()

        #XXX One way is to load file from file system. More efficient would be to directly used the bytes in the memory.

        #XXX Use Tesseract API to convert get UTF text from image.

        ocr_text = 'Foo text'
        # Do tesseract OCR here and replace processed text result here.
        response_data=[{"response": ocr_text}]
        return HttpResponse(json.dumps(response_data), content_type='application/json')
