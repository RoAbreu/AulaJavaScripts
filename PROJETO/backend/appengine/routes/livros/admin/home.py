# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from livro_app import facade
from routes.livros.admin import new, edit

@no_csrf
def delete(_handler, livro_id):
    facade.delete_livro_cmd(livro_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    context = {'new_path': router.to_path(new)}
    return  TemplateResponse(context)

    cmd = facade.list_livros_cmd()
    livros = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.livro_short_form()

    def short_livro_dict(livro):
        livro_dct = short_form.fill_with_model(livro)
        livro_dct['edit_path'] = router.to_path(edit_path, livro_dct['id'])
        livro_dct['delete_path'] = router.to_path(delete_path, livro_dct['id'])
        return livro_dct

    short_livros = [short_livro_dict(livro) for livro in livros]
    context = {'livros': short_livros,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

