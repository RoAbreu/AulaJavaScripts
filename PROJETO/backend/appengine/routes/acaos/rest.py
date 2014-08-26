# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from acao_app import facade


def index():
    cmd = facade.list_acaos_cmd()
    acao_list = cmd()
    short_form=facade.acao_short_form()
    acao_short = [short_form.fill_with_model(m) for m in acao_list]
    return JsonResponse(acao_short)


def save(**acao_properties):
    cmd = facade.save_acao_cmd(**acao_properties)
    return _save_or_update_json_response(cmd)


def update(acao_id, **acao_properties):
    cmd = facade.update_acao_cmd(acao_id, **acao_properties)
    return _save_or_update_json_response(cmd)


def delete(acao_id):
    facade.delete_acao_cmd(acao_id)()


def _save_or_update_json_response(cmd):
    try:
        acao = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.acao_short_form()
    return JsonResponse(short_form.fill_with_model(acao))

