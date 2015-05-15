from django.shortcuts import render, redirect
from perfis.models import Perfil

# Create your views here.
def index(resquest):
	return render(resquest, 'index.html', { "perfis" : Perfil.objects.all()})

def exibir(resquest, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)

	return render(resquest, 'perfil.html', { "perfil" : perfil })

def convidar(resquest, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(resquest)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

def get_perfil_logado(resquest):
	return Perfil.objects.get(id=1)