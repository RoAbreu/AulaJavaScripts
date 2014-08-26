# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from litnacional_app import facade
from routes.litnacionals.admin import new, edit


def delete(_handler, litnacional_id):
    facade.delete_litnacional_cmd(litnacional_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_litnacionals_cmd()
    litnacionals = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.litnacional_short_form()

    def short_litnacional_dict(litnacional):
        litnacional_dct = short_form.fill_with_model(litnacional)
        litnacional_dct['edit_path'] = router.to_path(edit_path, litnacional_dct['id'])
        litnacional_dct['delete_path'] = router.to_path(delete_path, litnacional_dct['id'])
        return litnacional_dct

    short_litnacionals = [short_litnacional_dict(litnacional) for litnacional in litnacionals]
    context = {'litnacionals': short_litnacionals,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

