# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from livroNovo_app import facade
from routes.livroNovos import admin


@no_csrf
def index(livro_novo_id):
    livro_novo = facade.get_livro_novo_cmd(livro_novo_id)()
    detail_form = facade.livro_novo_detail_form()
    context = {'save_path': router.to_path(save, livro_novo_id), 'livro_novo': detail_form.fill_with_model(livro_novo)}
    return TemplateResponse(context, 'livroNovos/admin/form.html')


def save(_handler, livro_novo_id, **livro_novo_properties):
    cmd = facade.update_livro_novo_cmd(livro_novo_id, **livro_novo_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'livro_novo': cmd.form}

        return TemplateResponse(context, 'livroNovos/admin/form.html')
    _handler.redirect(router.to_path(admin))

