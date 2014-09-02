# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from litinfantojuv_app import facade
from routes.litinfantojuvs import admin


@no_csrf
def index(litinfantojuv_id):
    litinfantojuv = facade.get_litinfantojuv_cmd(litinfantojuv_id)()
    detail_form = facade.litinfantojuv_detail_form()
    context = {'save_path': router.to_path(save, litinfantojuv_id), 'litinfantojuv': detail_form.fill_with_model(litinfantojuv)}
    return TemplateResponse(context, 'litinfantojuvs/admin/form.html')


def save(_handler, litinfantojuv_id, **litinfantojuv_properties):
    cmd = facade.update_litinfantojuv_cmd(litinfantojuv_id, **litinfantojuv_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'litinfantojuv': cmd.form}

        return TemplateResponse(context, 'litinfantojuvs/admin/form.html')
    _handler.redirect(router.to_path(admin))

