# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from autoajuda_app import facade
from routes.autoajudas import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_autoajudas_cmd()
    autoajudas = cmd()
    public_form = facade.autoajuda_public_form()
    autoajuda_public_dcts = [public_form.fill_with_model(autoajuda) for autoajuda in autoajudas]
    context = {'autoajudas': autoajuda_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

