Django API Backend for OCR using tesseract
===========================================

Requirements
------------

`tesseract-ocr` engine from Google installed and available on command line.

Installation
------------

    cd ocrbackend

    pip install -r requirements.txt
    # You might want to run this with the sudo if you are not using a virtual environment

    python manage.py migrate

Usage
-----

Start the server

    python manage.py runserver

Send FILE as a post request to `/`

    # If running locally this is your defauly post endpoint.
    http://localhost:8000/

File POST parameter name is `photo`.

For clarification see examples/post_test.py which shows how to emulate the post with Python. The same thing can also be done with other languages
very easily.

Sample Input/Output
-------------------

#### Example 1: via curl (on bash CLI)

    curl -F "photo=@/path/to/ocrbackend/examples/sample-image.jpg" localhost:8000/

Sample response:

    [{"response": "The quick brown fox\njumped over the 5\nlazy dogs!\n\n"}]


#### Example 2: via python

    # From inside ocrbackend/examples directory where sample-image.jpg is present
    url = 'http://localhost:8000'
    files = {'photo': open('sample-image.jpg', 'rb')}
    r = requests.post(url, files=files, data={})
    print r.text

Sample response:

    [{"response": "The quick brown fox\njumped over the 5\nlazy dogs!\n\n", "ocr_microseconds": 65467}]


#### Example 3: via java

    #TODO


Output Summary
--------------

The output is a  JSON which contains the OCRed text for the input file and the amount of time in microseconds
taken to do the OCR computation.