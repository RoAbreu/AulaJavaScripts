# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from dicionarios_app import facade
from routes.dicionarioss.admin import new, edit


def delete(_handler, dicionarios_id):
    facade.delete_dicionarios_cmd(dicionarios_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_dicionarioss_cmd()
    dicionarioss = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.dicionarios_short_form()

    def short_dicionarios_dict(dicionarios):
        dicionarios_dct = short_form.fill_with_model(dicionarios)
        dicionarios_dct['edit_path'] = router.to_path(edit_path, dicionarios_dct['id'])
        dicionarios_dct['delete_path'] = router.to_path(delete_path, dicionarios_dct['id'])
        return dicionarios_dct

    short_dicionarioss = [short_dicionarios_dict(dicionarios) for dicionarios in dicionarioss]
    context = {'dicionarioss': short_dicionarioss,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

