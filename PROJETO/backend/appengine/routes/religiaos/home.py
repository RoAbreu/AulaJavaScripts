# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from religiao_app import facade
from routes.religiaos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_religiaos_cmd()
    religiaos = cmd()
    public_form = facade.religiao_public_form()
    religiao_public_dcts = [public_form.fill_with_model(religiao) for religiao in religiaos]
    context = {'religiaos': religiao_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

