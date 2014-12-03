# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from livro_app import facade

@login_not_required
@no_csrf
def index():
    cmd = facade.list_livros_cmd()
    livro_list = cmd()
    short_form=facade.livro_short_form()
    livro_short = [short_form.fill_with_model(m) for m in livro_list]
    return JsonResponse(livro_short)
    #return JsonUnsecureResponse(livro_short)

@login_not_required
@no_csrf
def save(_resp, **livro_properties):
    cmd = facade.save_livro_cmd(**livro_properties)
    return _save_or_update_json_response(cmd, _resp)

@login_not_required
@no_csrf
def update(_resp, livro_id, **livro_properties):
    cmd = facade.update_livro_cmd(livro_id, **livro_properties)
    return _save_or_update_json_response(cmd, _resp,)

@login_not_required
@no_csrf
def delete(livro_id):
    facade.delete_livro_cmd(livro_id)

@login_not_required
@no_csrf
def _save_or_update_json_response(cmd, _resp):
    try:
        livro = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    short_form=facade.livro_short_form()
    return JsonResponse(short_form.fill_with_model(livro))

