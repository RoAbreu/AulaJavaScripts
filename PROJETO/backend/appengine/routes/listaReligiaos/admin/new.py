# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from listaReligiao_app import facade
from routes.listaReligiaos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'listaReligiaos/admin/form.html')


def save(_handler, lista_religiao_id=None, **lista_religiao_properties):
    cmd = facade.save_lista_religiao_cmd(**lista_religiao_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'lista_religiao': cmd.form}

        return TemplateResponse(context, 'listaReligiaos/admin/form.html')
    _handler.redirect(router.to_path(admin))

