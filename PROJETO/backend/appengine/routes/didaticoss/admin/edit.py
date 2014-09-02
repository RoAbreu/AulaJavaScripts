# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from didaticos_app import facade
from routes.didaticoss import admin


@no_csrf
def index(didaticos_id):
    didaticos = facade.get_didaticos_cmd(didaticos_id)()
    detail_form = facade.didaticos_detail_form()
    context = {'save_path': router.to_path(save, didaticos_id), 'didaticos': detail_form.fill_with_model(didaticos)}
    return TemplateResponse(context, 'didaticoss/admin/form.html')


def save(_handler, didaticos_id, **didaticos_properties):
    cmd = facade.update_didaticos_cmd(didaticos_id, **didaticos_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'didaticos': cmd.form}

        return TemplateResponse(context, 'didaticoss/admin/form.html')
    _handler.redirect(router.to_path(admin))

