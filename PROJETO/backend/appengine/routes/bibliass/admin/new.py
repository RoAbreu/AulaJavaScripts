# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from biblias_app import facade
from routes.bibliass import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'bibliass/admin/form.html')


def save(_handler, biblias_id=None, **biblias_properties):
    cmd = facade.save_biblias_cmd(**biblias_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'biblias': cmd.form}

        return TemplateResponse(context, 'bibliass/admin/form.html')
    _handler.redirect(router.to_path(admin))

