# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from religiao_app import facade
from routes.religiaos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'religiaos/admin/form.html')


def save(_handler, religiao_id=None, **religiao_properties):
    cmd = facade.save_religiao_cmd(**religiao_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'religiao': cmd.form}

        return TemplateResponse(context, 'religiaos/admin/form.html')
    _handler.redirect(router.to_path(admin))

