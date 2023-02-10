from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import core.models

class HomeView(View):
    def get(self, *args, **kwargs):

        template_name = 'core/home.html'
        eventos = list(core.models.Evento.objects.values('id', 'nome', 'data', 'descricao', 'imagem').filter(status='S').order_by('data'))
        context = {
            'eventos': eventos
        }
        return render(self.request, template_name=template_name, context=context)

    def post(self, *args, **kwargs):
        return JsonResponse({}, safe=False)


class MapaView(View):
    def get(self, *args, **kwargs):
        template_name = 'core/mapa.html'
        context = {}
        return render(self.request, template_name=template_name, context=context)


class RoletaView(View):
    def get(self, *args, **kwargs):
        template_name = 'core/roleta.html'
        context = {
            'roleta': core.models.Configuracao.objects.all().filter(tipo='ROLETA').first()
        }
        return render(self.request, template_name=template_name, context=context)

    def post(self, *args, **kwargs):
        roleta = core.models.Configuracao.objects.all().filter(tipo='ROLETA').first()
        if roleta is None:
            roleta = core.models.Configuracao(
                tipo='ROLETA',
                valor='USADA'
            )
        else:
            roleta.valor = 'USADA'
        roleta.save()
        return JsonResponse({'status': True}, safe=False)


class MotivoView(View):
    def get(self, *args, **kwargs):
        template_name = 'core/motivo.html'
        context = {
            'motivos': core.models.Motivo.objects.values('tipo', 'nome', 'id')
        }
        return render(self.request, template_name=template_name, context=context)


class NomeView(View):
    def get(self, *args, **kwargs):
        template_name = 'core/nome.html'
        context = {}
        return render(self.request, template_name=template_name, context=context)


class RecadosView(View):
    def get(self, *args, **kwargs):
        template_name = 'core/recados.html'
        context = {}
        return render(self.request, template_name=template_name, context=context)