# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from litnacional_app import facade
from routes.litnacionals import admin


@no_csrf
def index(litnacional_id):
    litnacional = facade.get_litnacional_cmd(litnacional_id)()
    detail_form = facade.litnacional_detail_form()
    context = {'save_path': router.to_path(save, litnacional_id), 'litnacional': detail_form.fill_with_model(litnacional)}
    return TemplateResponse(context, 'litnacionals/admin/form.html')


def save(_handler, litnacional_id, **litnacional_properties):
    cmd = facade.update_litnacional_cmd(litnacional_id, **litnacional_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'litnacional': cmd.form}

        return TemplateResponse(context, 'litnacionals/admin/form.html')
    _handler.redirect(router.to_path(admin))

