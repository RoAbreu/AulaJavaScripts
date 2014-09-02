# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from litestrangeira_app import facade
from routes.litestrangeiras import admin


@no_csrf
def index(litestrangeira_id):
    litestrangeira = facade.get_litestrangeira_cmd(litestrangeira_id)()
    detail_form = facade.litestrangeira_detail_form()
    context = {'save_path': router.to_path(save, litestrangeira_id), 'litestrangeira': detail_form.fill_with_model(litestrangeira)}
    return TemplateResponse(context, 'litestrangeiras/admin/form.html')


def save(_handler, litestrangeira_id, **litestrangeira_properties):
    cmd = facade.update_litestrangeira_cmd(litestrangeira_id, **litestrangeira_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'litestrangeira': cmd.form}

        return TemplateResponse(context, 'litestrangeiras/admin/form.html')
    _handler.redirect(router.to_path(admin))

