# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from litinfantojuv_app import facade
from routes.litinfantojuvs.admin import new, edit


def delete(_handler, litinfantojuv_id):
    facade.delete_litinfantojuv_cmd(litinfantojuv_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_litinfantojuvs_cmd()
    litinfantojuvs = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.litinfantojuv_short_form()

    def short_litinfantojuv_dict(litinfantojuv):
        litinfantojuv_dct = short_form.fill_with_model(litinfantojuv)
        litinfantojuv_dct['edit_path'] = router.to_path(edit_path, litinfantojuv_dct['id'])
        litinfantojuv_dct['delete_path'] = router.to_path(delete_path, litinfantojuv_dct['id'])
        return litinfantojuv_dct

    short_litinfantojuvs = [short_litinfantojuv_dict(litinfantojuv) for litinfantojuv in litinfantojuvs]
    context = {'litinfantojuvs': short_litinfantojuvs,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

