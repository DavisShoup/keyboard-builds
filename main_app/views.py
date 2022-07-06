from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
S3_BASE_URL = 'https://s3.amazonaws.com/'
BUCKET = 'keyboardbuilds-ds'
from .models import Keyboard, Photo


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def keyboards_index(request):
    keyboards = Keyboard.objects.all()
    return render(request, 'keyboards/index.html', { 'keyboards': keyboards })

@login_required
def keyboard_detail(request, keyboard_id):
    keyboard = Keyboard.objects.get(id=keyboard_id)
    return render(request, 'keyboards/detail.html', { 'keyboard': keyboard })

class KeyboardCreate(LoginRequiredMixin, CreateView):
    model = Keyboard
    fields = ['name', 'keyboard', 'switch', 'keycaps']
    success_url = '/keyboards/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class KeyboardUpdate(LoginRequiredMixin, UpdateView):
    model = Keyboard
    fields = ['name', 'keyboard', 'switch', 'keycaps']

class KeyboardDelete(LoginRequiredMixin, DeleteView):
    model = Keyboard
    success_url = '/keyboards/'

@login_required
def add_photo(request, keyboard_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, keyboard_id=keyboard_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', keyboard_id=keyboard_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)