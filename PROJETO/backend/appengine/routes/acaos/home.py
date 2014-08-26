# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from acao_app import facade
from routes.acaos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_acaos_cmd()
    acaos = cmd()
    public_form = facade.acao_public_form()
    acao_public_dcts = [public_form.fill_with_model(acao) for acao in acaos]
    context = {'acaos': acao_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

