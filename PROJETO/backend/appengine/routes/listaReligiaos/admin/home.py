# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from listaReligiao_app import facade
from routes.listaReligiaos.admin import new, edit


def delete(_handler, lista_religiao_id):
    facade.delete_lista_religiao_cmd(lista_religiao_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_lista_religiaos_cmd()
    lista_religiaos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.lista_religiao_short_form()

    def short_lista_religiao_dict(lista_religiao):
        lista_religiao_dct = short_form.fill_with_model(lista_religiao)
        lista_religiao_dct['edit_path'] = router.to_path(edit_path, lista_religiao_dct['id'])
        lista_religiao_dct['delete_path'] = router.to_path(delete_path, lista_religiao_dct['id'])
        return lista_religiao_dct

    short_lista_religiaos = [short_lista_religiao_dict(lista_religiao) for lista_religiao in lista_religiaos]
    context = {'lista_religiaos': short_lista_religiaos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

