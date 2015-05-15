from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite

# Create your views here.
def index(resquest):
	return render(resquest, 'index.html', { "perfis" : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(resquest)})

def exibir(resquest, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(resquest)
	ja_eh_contato = perfil in perfil_logado.contatos.all() 
	return render(resquest, 'perfil.html', { "perfil" : perfil, "perfil_logado" : perfil_logado , "ja_eh_contato" : ja_eh_contato})

def convidar(resquest, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(resquest)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

def aceitar(resquest, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

def get_perfil_logado(resquest):
	return Perfil.objects.get(id='1')