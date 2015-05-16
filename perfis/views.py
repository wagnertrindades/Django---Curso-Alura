from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def index(resquest):
	return render(resquest, 'index.html', { "perfis" : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(resquest)})

@login_required
def exibir(resquest, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(resquest)
	ja_eh_contato = perfil in perfil_logado.contatos.all() 
	return render(resquest, 'perfil.html', { "perfil" : perfil, "perfil_logado" : perfil_logado , "ja_eh_contato" : ja_eh_contato})

@permission_required('perfis.add_convite', raise_exception=True)
@login_required
def convidar(resquest, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(resquest)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')

@login_required
def aceitar(resquest, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

@login_required
def get_perfil_logado(resquest):
	return resquest.user.perfil