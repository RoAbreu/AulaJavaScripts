# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from listaReligiao_app import facade
from routes.listaReligiaos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_lista_religiaos_cmd()
    lista_religiaos = cmd()
    public_form = facade.lista_religiao_public_form()
    lista_religiao_public_dcts = [public_form.fill_with_model(lista_religiao) for lista_religiao in lista_religiaos]
    context = {'lista_religiaos': lista_religiao_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

