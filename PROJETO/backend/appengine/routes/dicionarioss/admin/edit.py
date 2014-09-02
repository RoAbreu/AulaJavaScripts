# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from dicionarios_app import facade
from routes.dicionarioss import admin


@no_csrf
def index(dicionarios_id):
    dicionarios = facade.get_dicionarios_cmd(dicionarios_id)()
    detail_form = facade.dicionarios_detail_form()
    context = {'save_path': router.to_path(save, dicionarios_id), 'dicionarios': detail_form.fill_with_model(dicionarios)}
    return TemplateResponse(context, 'dicionarioss/admin/form.html')


def save(_handler, dicionarios_id, **dicionarios_properties):
    cmd = facade.update_dicionarios_cmd(dicionarios_id, **dicionarios_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'dicionarios': cmd.form}

        return TemplateResponse(context, 'dicionarioss/admin/form.html')
    _handler.redirect(router.to_path(admin))

