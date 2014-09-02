# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from religiao_app import facade
from routes.religiaos.admin import new, edit


def delete(_handler, religiao_id):
    facade.delete_religiao_cmd(religiao_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_religiaos_cmd()
    religiaos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.religiao_short_form()

    def short_religiao_dict(religiao):
        religiao_dct = short_form.fill_with_model(religiao)
        religiao_dct['edit_path'] = router.to_path(edit_path, religiao_dct['id'])
        religiao_dct['delete_path'] = router.to_path(delete_path, religiao_dct['id'])
        return religiao_dct

    short_religiaos = [short_religiao_dict(religiao) for religiao in religiaos]
    context = {'religiaos': short_religiaos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

