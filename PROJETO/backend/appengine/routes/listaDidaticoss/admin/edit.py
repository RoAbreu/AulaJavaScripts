# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from listaDidaticos_app import facade
from routes.listaDidaticoss import admin


@no_csrf
def index(lista_didaticos_id):
    lista_didaticos = facade.get_lista_didaticos_cmd(lista_didaticos_id)()
    detail_form = facade.lista_didaticos_detail_form()
    context = {'save_path': router.to_path(save, lista_didaticos_id), 'lista_didaticos': detail_form.fill_with_model(lista_didaticos)}
    return TemplateResponse(context, 'listaDidaticoss/admin/form.html')


def save(_handler, lista_didaticos_id, **lista_didaticos_properties):
    cmd = facade.update_lista_didaticos_cmd(lista_didaticos_id, **lista_didaticos_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'lista_didaticos': cmd.form}

        return TemplateResponse(context, 'listaDidaticoss/admin/form.html')
    _handler.redirect(router.to_path(admin))

