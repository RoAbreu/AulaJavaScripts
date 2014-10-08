# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from listaDicionarios_app import facade
from routes.listaDicionarioss import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_lista_dicionarioss_cmd()
    lista_dicionarioss = cmd()
    public_form = facade.lista_dicionarios_public_form()
    lista_dicionarios_public_dcts = [public_form.fill_with_model(lista_dicionarios) for lista_dicionarios in lista_dicionarioss]
    context = {'lista_dicionarioss': lista_dicionarios_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

