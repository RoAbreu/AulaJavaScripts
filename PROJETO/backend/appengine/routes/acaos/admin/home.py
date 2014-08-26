# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from acao_app import facade
from routes.acaos.admin import new, edit


def delete(_handler, acao_id):
    facade.delete_acao_cmd(acao_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_acaos_cmd()
    acaos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.acao_short_form()

    def short_acao_dict(acao):
        acao_dct = short_form.fill_with_model(acao)
        acao_dct['edit_path'] = router.to_path(edit_path, acao_dct['id'])
        acao_dct['delete_path'] = router.to_path(delete_path, acao_dct['id'])
        return acao_dct

    short_acaos = [short_acao_dict(acao) for acao in acaos]
    context = {'acaos': short_acaos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

