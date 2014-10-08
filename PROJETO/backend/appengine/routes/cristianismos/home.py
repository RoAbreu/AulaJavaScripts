# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from cristianismo_app import facade
from routes.cristianismos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_cristianismos_cmd()
    cristianismos = cmd()
    public_form = facade.cristianismo_public_form()
    cristianismo_public_dcts = [public_form.fill_with_model(cristianismo) for cristianismo in cristianismos]
    context = {'cristianismos': cristianismo_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

