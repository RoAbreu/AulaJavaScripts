# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from budismo_app import facade
from routes.budismos.admin import new, edit


def delete(_handler, budismo_id):
    facade.delete_budismo_cmd(budismo_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_budismos_cmd()
    budismos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.budismo_short_form()

    def short_budismo_dict(budismo):
        budismo_dct = short_form.fill_with_model(budismo)
        budismo_dct['edit_path'] = router.to_path(edit_path, budismo_dct['id'])
        budismo_dct['delete_path'] = router.to_path(delete_path, budismo_dct['id'])
        return budismo_dct

    short_budismos = [short_budismo_dict(budismo) for budismo in budismos]
    context = {'budismos': short_budismos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

