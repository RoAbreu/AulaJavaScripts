# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from acao_app import facade
from routes.acaos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'acaos/admin/form.html')


def save(_handler, acao_id=None, **acao_properties):
    cmd = facade.save_acao_cmd(**acao_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'acao': cmd.form}

        return TemplateResponse(context, 'acaos/admin/form.html')
    _handler.redirect(router.to_path(admin))

