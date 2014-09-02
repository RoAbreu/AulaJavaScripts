# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from litestrangeira_app import facade
from routes.litestrangeiras.admin import new, edit


def delete(_handler, litestrangeira_id):
    facade.delete_litestrangeira_cmd(litestrangeira_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_litestrangeiras_cmd()
    litestrangeiras = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.litestrangeira_short_form()

    def short_litestrangeira_dict(litestrangeira):
        litestrangeira_dct = short_form.fill_with_model(litestrangeira)
        litestrangeira_dct['edit_path'] = router.to_path(edit_path, litestrangeira_dct['id'])
        litestrangeira_dct['delete_path'] = router.to_path(delete_path, litestrangeira_dct['id'])
        return litestrangeira_dct

    short_litestrangeiras = [short_litestrangeira_dict(litestrangeira) for litestrangeira in litestrangeiras]
    context = {'litestrangeiras': short_litestrangeiras,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

