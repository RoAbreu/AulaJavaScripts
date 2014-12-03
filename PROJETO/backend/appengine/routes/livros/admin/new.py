# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from livro_app import facade
from routes.livros import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'livros/admin/form.html')


def save(_handler, livro_id=None, **livro_properties):
    cmd = facade.save_livro_cmd(**livro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'livro': cmd.form}

        return TemplateResponse(context, 'livros/admin/form.html')
    _handler.redirect(router.to_path(admin))

