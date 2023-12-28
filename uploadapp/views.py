from django.shortcuts import render
from uploadapp.forms import UploadForm

# Create your views here.

def upload_image(req):
    if req.method == 'POST':
        form = UploadForm(req.POST, req.FILES)
        if form.is_valid:
            form.save()
            saved_object = form.instance
            return render(req, 'uploadapp/add_image.html', {'form': form, 'saved_object': saved_object })
    else:
        form = UploadForm()
    return render(req, 'uploadapp/add_image.html', { 'form': form })