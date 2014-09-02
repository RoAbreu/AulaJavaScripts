# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from dicionarios_app import facade
from routes.dicionarioss import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'dicionarioss/admin/form.html')


def save(_handler, dicionarios_id=None, **dicionarios_properties):
    cmd = facade.save_dicionarios_cmd(**dicionarios_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'dicionarios': cmd.form}

        return TemplateResponse(context, 'dicionarioss/admin/form.html')
    _handler.redirect(router.to_path(admin))

