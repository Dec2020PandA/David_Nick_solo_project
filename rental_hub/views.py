from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, UserManager
import bcrypt

# CREATE
def index(request):
    return render(request, 'index.html')

def main(request):
    if 'user_id' not in request.session:
        return redirect('/main')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'main.html', context)

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        return redirect('/main')

# READ

def login(request):
    if request.method == "GET":
        return redirect('/login')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/login')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/main')

def logout(request):
    request.session.clear()
    return redirect('/')



# def markets
#     pass

# UPDATE

# def update(request):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     user = User.objects.get(id=request.session['user_id'])
#     context = {
#         'user': user
#     }
#     return render(request, 'myaccount.html', context)

# def create_quote(request):
#     if request.method == 'POST':
#         errors = Quote.objects.validate(request.POST)
#         if errors:
#             for e in errors.values():
#                 messages.error(request, e)
#             return redirect('/quotes')
#         quote = Quote.objects.create(author=request.POST['author'],quote_field=request.POST['content'], poster=User.objects.get(id=request.session['user_id']))
#     return redirect('/quotes')

# DELETE

# def delete_market(request):
#         market = Market.objects.filter().delete
#         return redirect('/profile')

