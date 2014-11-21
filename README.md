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
=====

Start the server

    python manage.py runserver

Send FILE as a post request to `/`

    # If running locally this is your defauly post endpoint.
    http://localhost:8000/

File POST parameter name is `photo`.

For clarification see examples/post_test.py which shows how to emulate the post with Python. The same thing can also be done with other languages
very easily.