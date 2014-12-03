# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from livroNovo_app import facade
from routes.livroNovos.admin import new, edit


def delete(_handler, livro_novo_id):
    facade.delete_livro_novo_cmd(livro_novo_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_livro_novos_cmd()
    livro_novos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.livro_novo_short_form()

    def short_livro_novo_dict(livro_novo):
        livro_novo_dct = short_form.fill_with_model(livro_novo)
        livro_novo_dct['edit_path'] = router.to_path(edit_path, livro_novo_dct['id'])
        livro_novo_dct['delete_path'] = router.to_path(delete_path, livro_novo_dct['id'])
        return livro_novo_dct

    short_livro_novos = [short_livro_novo_dict(livro_novo) for livro_novo in livro_novos]
    context = {'livro_novos': short_livro_novos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

