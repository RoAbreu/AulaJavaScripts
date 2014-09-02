# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from dicionarios_app import facade
from routes.dicionarioss import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_dicionarioss_cmd()
    dicionarioss = cmd()
    public_form = facade.dicionarios_public_form()
    dicionarios_public_dcts = [public_form.fill_with_model(dicionarios) for dicionarios in dicionarioss]
    context = {'dicionarioss': dicionarios_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

