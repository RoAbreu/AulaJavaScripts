# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from listaDicionarios_app import facade
from routes.listaDicionarioss.admin import new, edit


def delete(_handler, lista_dicionarios_id):
    facade.delete_lista_dicionarios_cmd(lista_dicionarios_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_lista_dicionarioss_cmd()
    lista_dicionarioss = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.lista_dicionarios_short_form()

    def short_lista_dicionarios_dict(lista_dicionarios):
        lista_dicionarios_dct = short_form.fill_with_model(lista_dicionarios)
        lista_dicionarios_dct['edit_path'] = router.to_path(edit_path, lista_dicionarios_dct['id'])
        lista_dicionarios_dct['delete_path'] = router.to_path(delete_path, lista_dicionarios_dct['id'])
        return lista_dicionarios_dct

    short_lista_dicionarioss = [short_lista_dicionarios_dict(lista_dicionarios) for lista_dicionarios in lista_dicionarioss]
    context = {'lista_dicionarioss': short_lista_dicionarioss,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

