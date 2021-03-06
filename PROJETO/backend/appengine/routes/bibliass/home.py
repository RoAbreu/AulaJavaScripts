# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from biblias_app import facade
from routes.bibliass import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_bibliass_cmd()
    bibliass = cmd()
    public_form = facade.biblias_public_form()
    biblias_public_dcts = [public_form.fill_with_model(biblias) for biblias in bibliass]
    context = {'bibliass': biblias_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

