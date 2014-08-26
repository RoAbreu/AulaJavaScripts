# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from aventura_app import facade
from routes.aventuras import admin


@no_csrf
def index(avenura_id):
    avenura = facade.get_avenura_cmd(avenura_id)()
    detail_form = facade.avenura_detail_form()
    context = {'save_path': router.to_path(save, avenura_id), 'avenura': detail_form.fill_with_model(avenura)}
    return TemplateResponse(context, 'aventuras/admin/form.html')


def save(_handler, avenura_id, **avenura_properties):
    cmd = facade.update_avenura_cmd(avenura_id, **avenura_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'avenura': cmd.form}

        return TemplateResponse(context, 'aventuras/admin/form.html')
    _handler.redirect(router.to_path(admin))

