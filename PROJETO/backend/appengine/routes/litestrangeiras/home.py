# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from litestrangeira_app import facade
from routes.litestrangeiras import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_litestrangeiras_cmd()
    litestrangeiras = cmd()
    public_form = facade.litestrangeira_public_form()
    litestrangeira_public_dcts = [public_form.fill_with_model(litestrangeira) for litestrangeira in litestrangeiras]
    context = {'litestrangeiras': litestrangeira_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

