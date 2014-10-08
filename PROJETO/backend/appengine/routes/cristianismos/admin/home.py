# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from cristianismo_app import facade
from routes.cristianismos.admin import new, edit


def delete(_handler, cristianismo_id):
    facade.delete_cristianismo_cmd(cristianismo_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_cristianismos_cmd()
    cristianismos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.cristianismo_short_form()

    def short_cristianismo_dict(cristianismo):
        cristianismo_dct = short_form.fill_with_model(cristianismo)
        cristianismo_dct['edit_path'] = router.to_path(edit_path, cristianismo_dct['id'])
        cristianismo_dct['delete_path'] = router.to_path(delete_path, cristianismo_dct['id'])
        return cristianismo_dct

    short_cristianismos = [short_cristianismo_dict(cristianismo) for cristianismo in cristianismos]
    context = {'cristianismos': short_cristianismos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

