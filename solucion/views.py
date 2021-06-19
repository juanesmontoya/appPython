from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona

# Create your views here.
def index(request):
	return render(request, 'index.html')

def create(request):
	if request.method == 'GET':
		form = PersonaForm()
		context = {'form': form }		
	else:
		form = PersonaForm(request.POST)
		context = {'form': form }
		if form.is_valid():
			form.save()
			return redirect('index')
	return render(request, 'create.html', context)

def consulta(request):
	personas = Persona.objects.all()	
	context = {'personas':personas}
	return render(request, 'consulta.html', context)