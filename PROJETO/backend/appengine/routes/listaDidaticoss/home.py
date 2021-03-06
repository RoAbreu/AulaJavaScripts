# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from listaDidaticos_app import facade
from routes.listaDidaticoss import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_lista_didaticoss_cmd()
    lista_didaticoss = cmd()
    public_form = facade.lista_didaticos_public_form()
    lista_didaticos_public_dcts = [public_form.fill_with_model(lista_didaticos) for lista_didaticos in lista_didaticoss]
    context = {'lista_didaticoss': lista_didaticos_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

