# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from didaticos_app import facade
from routes.didaticoss import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_didaticoss_cmd()
    didaticoss = cmd()
    public_form = facade.didaticos_public_form()
    didaticos_public_dcts = [public_form.fill_with_model(didaticos) for didaticos in didaticoss]
    context = {'didaticoss': didaticos_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

