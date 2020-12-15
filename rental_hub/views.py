from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, UserManager
import bcrypt
import requests

# CREATE
def index(request):
    return render(request, 'index.html')

def main(request):
    # if 'user_id' not in request.session:
    return render(request, 'main.html')

def register(request):
    if request.method == "GET":
        return redirect('/main')
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
    return render(request, 'login.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def markets(request):
    return render(request,'market.html')

# UPDATE

# def update(request):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     user = User.objects.get(id=request.session['user_id'])
#     context = {
#         'user': user
#     }
#     return render(request, 'myaccount.html', context)

# DELETE

# def delete_market(request):
#         market = Market.objects.filter().delete
#         return redirect('/profile')


def rent_estimate(request):
    url = "https://realtymole-rental-estimate-v1.p.rapidapi.com/rentalPrice"

    querystring = {
        "address":"",
        "bedrooms":"",
        "bathrooms":"",
        "propertyType":"",
        "squareFootage":"",
        "compCount":"5"}

    headers = {
        'x-rapidapi-key': "9005cdaf4dmsha7aa0f6d73dc67bp10d25djsn5aa317647eb0",
        'x-rapidapi-host': "realtymole-rental-estimate-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)