from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import ShortURL
from .forms import CreateNewShortURL
from datetime import datetime
import random, string

# Create your views here.
def home(request):
    if request.method == "POST":
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            d = datetime.now()
            s = ShortURL(original_url=original_website, short_url=random_chars, time_date_created=d)
            s.save()
            return render(request, 'index.html', {'chars':random_chars})
    else:
        form=CreateNewShortURL()
        context={'form': form}
        return render(request, 'index.html', context)