# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from aventura_app import facade
from routes.aventuras.admin import new, edit


def delete(_handler, avenura_id):
    facade.delete_avenura_cmd(avenura_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_avenuras_cmd()
    avenuras = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.avenura_short_form()

    def short_avenura_dict(avenura):
        avenura_dct = short_form.fill_with_model(avenura)
        avenura_dct['edit_path'] = router.to_path(edit_path, avenura_dct['id'])
        avenura_dct['delete_path'] = router.to_path(delete_path, avenura_dct['id'])
        return avenura_dct

    short_avenuras = [short_avenura_dict(avenura) for avenura in avenuras]
    context = {'avenuras': short_avenuras,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

