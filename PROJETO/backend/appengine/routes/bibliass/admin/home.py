# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from biblias_app import facade
from routes.bibliass.admin import new, edit


def delete(_handler, biblias_id):
    facade.delete_biblias_cmd(biblias_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_bibliass_cmd()
    bibliass = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.biblias_short_form()

    def short_biblias_dict(biblias):
        biblias_dct = short_form.fill_with_model(biblias)
        biblias_dct['edit_path'] = router.to_path(edit_path, biblias_dct['id'])
        biblias_dct['delete_path'] = router.to_path(delete_path, biblias_dct['id'])
        return biblias_dct

    short_bibliass = [short_biblias_dict(biblias) for biblias in bibliass]
    context = {'bibliass': short_bibliass,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

