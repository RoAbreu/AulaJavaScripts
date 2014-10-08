# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from cristianismo_app import facade
from routes.cristianismos import admin


@no_csrf
def index(cristianismo_id):
    cristianismo = facade.get_cristianismo_cmd(cristianismo_id)()
    detail_form = facade.cristianismo_detail_form()
    context = {'save_path': router.to_path(save, cristianismo_id), 'cristianismo': detail_form.fill_with_model(cristianismo)}
    return TemplateResponse(context, 'cristianismos/admin/form.html')


def save(_handler, cristianismo_id, **cristianismo_properties):
    cmd = facade.update_cristianismo_cmd(cristianismo_id, **cristianismo_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'cristianismo': cmd.form}

        return TemplateResponse(context, 'cristianismos/admin/form.html')
    _handler.redirect(router.to_path(admin))

