# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from livro_app import facade
from routes.livros import admin


@no_csrf
def index(livro_id):
    livro = facade.get_livro_cmd(livro_id)()
    detail_form = facade.livro_detail_form()
    context = {'save_path': router.to_path(save, livro_id), 'livro': detail_form.fill_with_model(livro)}
    return TemplateResponse(context, 'livros/admin/form.html')


def save(_handler, livro_id, **livro_properties):
    cmd = facade.update_livro_cmd(livro_id, **livro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'livro': cmd.form}

        return TemplateResponse(context, 'livros/admin/form.html')
    _handler.redirect(router.to_path(admin))

