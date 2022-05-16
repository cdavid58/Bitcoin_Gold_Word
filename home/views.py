from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .send_email import send_email_client

def Home(request):

	if request.is_ajax():
		message = ""
		try:
			Client(
				name = request.GET['name'],
				phone = request.GET['phone'],
				email = request.GET['email'],
				address = request.GET['address']
			).save()
			send_email_client(str(request.GET['name']),str(request.GET['phone']),str(request.GET['email']),str(request.GET['address']))
			message = "Registro Exitoso"
		except Exception as e:
			if 'phone' in str(e):
				message = "El número de teléfono ya esta registrado"
			elif 'email' in str(e):
				message = "El email ya esta registrado"
		return HttpResponse(message)

	return render(request,'index.html')