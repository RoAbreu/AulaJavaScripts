# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from listaDidaticos_app import facade
from routes.listaDidaticoss.admin import new, edit


def delete(_handler, lista_didaticos_id):
    facade.delete_lista_didaticos_cmd(lista_didaticos_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_lista_didaticoss_cmd()
    lista_didaticoss = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.lista_didaticos_short_form()

    def short_lista_didaticos_dict(lista_didaticos):
        lista_didaticos_dct = short_form.fill_with_model(lista_didaticos)
        lista_didaticos_dct['edit_path'] = router.to_path(edit_path, lista_didaticos_dct['id'])
        lista_didaticos_dct['delete_path'] = router.to_path(delete_path, lista_didaticos_dct['id'])
        return lista_didaticos_dct

    short_lista_didaticoss = [short_lista_didaticos_dict(lista_didaticos) for lista_didaticos in lista_didaticoss]
    context = {'lista_didaticoss': short_lista_didaticoss,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

