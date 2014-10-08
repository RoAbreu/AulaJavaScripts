# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from listaDidaticos_app import facade
from routes.listaDidaticoss import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'listaDidaticoss/admin/form.html')


def save(_handler, lista_didaticos_id=None, **lista_didaticos_properties):
    cmd = facade.save_lista_didaticos_cmd(**lista_didaticos_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'lista_didaticos': cmd.form}

        return TemplateResponse(context, 'listaDidaticoss/admin/form.html')
    _handler.redirect(router.to_path(admin))

