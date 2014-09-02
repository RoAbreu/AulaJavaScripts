# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from litinfantojuv_app import facade
from routes.litinfantojuvs import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_litinfantojuvs_cmd()
    litinfantojuvs = cmd()
    public_form = facade.litinfantojuv_public_form()
    litinfantojuv_public_dcts = [public_form.fill_with_model(litinfantojuv) for litinfantojuv in litinfantojuvs]
    context = {'litinfantojuvs': litinfantojuv_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

