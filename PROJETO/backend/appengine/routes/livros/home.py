# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from livro_app import facade
from routes.livros import admin, rest


@login_not_required
@no_csrf
def index():

    context = {'rest_list_path': router.to_path(rest.index),
               'rest_delete_path': router.to_path(rest.delete),
               'rest_save_path': router.to_path(rest.save)}
    return TemplateResponse(context)

