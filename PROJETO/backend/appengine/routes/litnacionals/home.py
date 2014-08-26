# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from litnacional_app import facade
from routes.litnacionals import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_litnacionals_cmd()
    litnacionals = cmd()
    public_form = facade.litnacional_public_form()
    litnacional_public_dcts = [public_form.fill_with_model(litnacional) for litnacional in litnacionals]
    context = {'litnacionals': litnacional_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

