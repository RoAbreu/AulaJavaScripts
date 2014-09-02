# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from litestrangeira_app import facade
from routes.litestrangeiras import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'litestrangeiras/admin/form.html')


def save(_handler, litestrangeira_id=None, **litestrangeira_properties):
    cmd = facade.save_litestrangeira_cmd(**litestrangeira_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'litestrangeira': cmd.form}

        return TemplateResponse(context, 'litestrangeiras/admin/form.html')
    _handler.redirect(router.to_path(admin))

