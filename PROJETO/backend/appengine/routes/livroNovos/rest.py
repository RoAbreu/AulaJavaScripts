# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from livroNovo_app import facade

@login_not_required
@no_csrf
def index():
    cmd = facade.list_livro_novos_cmd()
    livro_novo_list = cmd()
    short_form=facade.livro_novo_short_form()
    livro_novo_short = [short_form.fill_with_model(m) for m in livro_novo_list]
    return JsonResponse(livro_novo_short)

@login_not_required
@no_csrf
def save(_resp, **livro_novo_properties):
    cmd = facade.save_livro_novo_cmd(**livro_novo_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def update(_resp, id, **livro_novo_properties):
    cmd = facade.update_livro_novo_cmd(id, **livro_novo_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def delete(id):
    facade.delete_livro_novo_cmd(id)()


def _save_or_update_json_response(_resp, cmd):
    try:
        livro_novo = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonUnsecureResponse({cmd.errors})
    short_form=facade.livro_novo_short_form()
    return JsonResponse(short_form.fill_with_model(livro_novo))

