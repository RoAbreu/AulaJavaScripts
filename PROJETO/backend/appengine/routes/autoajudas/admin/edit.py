# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from autoajuda_app import facade
from routes.autoajudas import admin


@no_csrf
def index(autoajuda_id):
    autoajuda = facade.get_autoajuda_cmd(autoajuda_id)()
    detail_form = facade.autoajuda_detail_form()
    context = {'save_path': router.to_path(save, autoajuda_id), 'autoajuda': detail_form.fill_with_model(autoajuda)}
    return TemplateResponse(context, 'autoajudas/admin/form.html')


def save(_handler, autoajuda_id, **autoajuda_properties):
    cmd = facade.update_autoajuda_cmd(autoajuda_id, **autoajuda_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'autoajuda': cmd.form}

        return TemplateResponse(context, 'autoajudas/admin/form.html')
    _handler.redirect(router.to_path(admin))

