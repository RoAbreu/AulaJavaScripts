# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from listaDicionarios_app import facade
from routes.listaDicionarioss import admin


@no_csrf
def index(lista_dicionarios_id):
    lista_dicionarios = facade.get_lista_dicionarios_cmd(lista_dicionarios_id)()
    detail_form = facade.lista_dicionarios_detail_form()
    context = {'save_path': router.to_path(save, lista_dicionarios_id), 'lista_dicionarios': detail_form.fill_with_model(lista_dicionarios)}
    return TemplateResponse(context, 'listaDicionarioss/admin/form.html')


def save(_handler, lista_dicionarios_id, **lista_dicionarios_properties):
    cmd = facade.update_lista_dicionarios_cmd(lista_dicionarios_id, **lista_dicionarios_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'lista_dicionarios': cmd.form}

        return TemplateResponse(context, 'listaDicionarioss/admin/form.html')
    _handler.redirect(router.to_path(admin))

