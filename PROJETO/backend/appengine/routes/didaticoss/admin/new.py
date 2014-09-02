# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from didaticos_app import facade
from routes.didaticoss import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'didaticoss/admin/form.html')


def save(_handler, didaticos_id=None, **didaticos_properties):
    cmd = facade.save_didaticos_cmd(**didaticos_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'didaticos': cmd.form}

        return TemplateResponse(context, 'didaticoss/admin/form.html')
    _handler.redirect(router.to_path(admin))

