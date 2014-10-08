# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from cristianismo_app import facade
from routes.cristianismos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'cristianismos/admin/form.html')


def save(_handler, cristianismo_id=None, **cristianismo_properties):
    cmd = facade.save_cristianismo_cmd(**cristianismo_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'cristianismo': cmd.form}

        return TemplateResponse(context, 'cristianismos/admin/form.html')
    _handler.redirect(router.to_path(admin))

