# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from budismo_app import facade
from routes.budismos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'budismos/admin/form.html')


def save(_handler, budismo_id=None, **budismo_properties):
    cmd = facade.save_budismo_cmd(**budismo_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'budismo': cmd.form}

        return TemplateResponse(context, 'budismos/admin/form.html')
    _handler.redirect(router.to_path(admin))

