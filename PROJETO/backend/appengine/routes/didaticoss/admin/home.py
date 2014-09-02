# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from didaticos_app import facade
from routes.didaticoss.admin import new, edit


def delete(_handler, didaticos_id):
    facade.delete_didaticos_cmd(didaticos_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_didaticoss_cmd()
    didaticoss = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.didaticos_short_form()

    def short_didaticos_dict(didaticos):
        didaticos_dct = short_form.fill_with_model(didaticos)
        didaticos_dct['edit_path'] = router.to_path(edit_path, didaticos_dct['id'])
        didaticos_dct['delete_path'] = router.to_path(delete_path, didaticos_dct['id'])
        return didaticos_dct

    short_didaticoss = [short_didaticos_dict(didaticos) for didaticos in didaticoss]
    context = {'didaticoss': short_didaticoss,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

