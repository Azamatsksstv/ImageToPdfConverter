import os
from PIL import Image
from src import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html')


def convert_to_pdf(request):
    if request.method == 'POST' and request.FILES['photo']:
        photo = request.FILES['photo']
        image = Image.open(photo)
        pdf_path = os.path.join(settings.MEDIA_ROOT, 'converted.pdf')
        try:
            image.save(pdf_path, 'PDF', resolution=100.0)
        except Exception as e:
            return HttpResponse(f'Error converting image to PDF: {e}')

        # Redirect the user to the index page with a link to the converted PDF
        pdf_url = os.path.join(settings.MEDIA_URL, 'converted.pdf')
        print(pdf_url)
        print("hey")
        # b = T
        if not os.path.exists(pdf_path):
            return HttpResponse(f'PDF file not found at {pdf_path}')
        return render(request, 'index.html', {'pdf_url': pdf_url, 'tf': True})
    else:

        return redirect('index')
