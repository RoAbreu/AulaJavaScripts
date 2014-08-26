# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from litnacional_app import facade
from routes.litnacionals import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'litnacionals/admin/form.html')


def save(_handler, litnacional_id=None, **litnacional_properties):
    cmd = facade.save_litnacional_cmd(**litnacional_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'litnacional': cmd.form}

        return TemplateResponse(context, 'litnacionals/admin/form.html')
    _handler.redirect(router.to_path(admin))

