from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(resquest):
	return render(resquest, 'index.html')

def exibir(resquest, perfil_id):

	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil('Wagner Trindade', 'wtrindades@hotmail.com', '7777-7777', 'Google')

	if perfil_id == '2':
		perfil = Perfil('Lucia Elaine', 'luciel@hotmail.com', '1212-1212', 'Esperanca')

	return render(resquest, 'perfil.html', { "perfil" : perfil })