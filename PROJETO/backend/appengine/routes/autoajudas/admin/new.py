# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from autoajuda_app import facade
from routes.autoajudas import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'autoajudas/admin/form.html')


def save(_handler, autoajuda_id=None, **autoajuda_properties):
    cmd = facade.save_autoajuda_cmd(**autoajuda_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'autoajuda': cmd.form}

        return TemplateResponse(context, 'autoajudas/admin/form.html')
    _handler.redirect(router.to_path(admin))

