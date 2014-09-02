# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from autoajuda_app import facade
from routes.autoajudas.admin import new, edit


def delete(_handler, autoajuda_id):
    facade.delete_autoajuda_cmd(autoajuda_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_autoajudas_cmd()
    autoajudas = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.autoajuda_short_form()

    def short_autoajuda_dict(autoajuda):
        autoajuda_dct = short_form.fill_with_model(autoajuda)
        autoajuda_dct['edit_path'] = router.to_path(edit_path, autoajuda_dct['id'])
        autoajuda_dct['delete_path'] = router.to_path(delete_path, autoajuda_dct['id'])
        return autoajuda_dct

    short_autoajudas = [short_autoajuda_dict(autoajuda) for autoajuda in autoajudas]
    context = {'autoajudas': short_autoajudas,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

