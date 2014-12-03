# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from livroNovo_app import facade
from routes.livroNovos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'livroNovos/admin/form.html')


def save(_handler, livro_novo_id=None, **livro_novo_properties):
    cmd = facade.save_livro_novo_cmd(**livro_novo_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'livro_novo': cmd.form}

        return TemplateResponse(context, 'livroNovos/admin/form.html')
    _handler.redirect(router.to_path(admin))

