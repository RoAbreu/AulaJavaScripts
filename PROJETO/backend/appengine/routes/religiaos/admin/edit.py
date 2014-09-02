# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from religiao_app import facade
from routes.religiaos import admin


@no_csrf
def index(religiao_id):
    religiao = facade.get_religiao_cmd(religiao_id)()
    detail_form = facade.religiao_detail_form()
    context = {'save_path': router.to_path(save, religiao_id), 'religiao': detail_form.fill_with_model(religiao)}
    return TemplateResponse(context, 'religiaos/admin/form.html')


def save(_handler, religiao_id, **religiao_properties):
    cmd = facade.update_religiao_cmd(religiao_id, **religiao_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'religiao': cmd.form}

        return TemplateResponse(context, 'religiaos/admin/form.html')
    _handler.redirect(router.to_path(admin))

