from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(resquest):
	return render(resquest, 'index.html')

def exibir(resquest, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)

	return render(resquest, 'perfil.html', { "perfil" : perfil })