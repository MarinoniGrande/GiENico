from django.urls import re_path, include

import core.views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^mapa$', core.views.MapaView.as_view(), name="mapa"),
    re_path(r'^roleta$', core.views.RoletaView.as_view(), name="roleta"),
    re_path(r'^nome$', core.views.NomeView.as_view(), name="nome"),
    re_path(r'^motivos$', core.views.MotivoView.as_view(), name="motivo"),
    re_path(r'^recados$', core.views.RecadosView.as_view(), name="recados"),
    re_path(r'^$', core.views.HomeView.as_view(), name="home"),

]
