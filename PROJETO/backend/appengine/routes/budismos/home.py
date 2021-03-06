# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from budismo_app import facade
from routes.budismos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_budismos_cmd()
    budismos = cmd()
    public_form = facade.budismo_public_form()
    budismo_public_dcts = [public_form.fill_with_model(budismo) for budismo in budismos]
    context = {'budismos': budismo_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

