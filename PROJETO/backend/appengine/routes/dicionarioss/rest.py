# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from dicionarios_app import facade


def index():
    cmd = facade.list_dicionarioss_cmd()
    dicionarios_list = cmd()
    short_form=facade.dicionarios_short_form()
    dicionarios_short = [short_form.fill_with_model(m) for m in dicionarios_list]
    return JsonResponse(dicionarios_short)


def save(**dicionarios_properties):
    cmd = facade.save_dicionarios_cmd(**dicionarios_properties)
    return _save_or_update_json_response(cmd)


def update(dicionarios_id, **dicionarios_properties):
    cmd = facade.update_dicionarios_cmd(dicionarios_id, **dicionarios_properties)
    return _save_or_update_json_response(cmd)


def delete(dicionarios_id):
    facade.delete_dicionarios_cmd(dicionarios_id)()


def _save_or_update_json_response(cmd):
    try:
        dicionarios = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.dicionarios_short_form()
    return JsonResponse(short_form.fill_with_model(dicionarios))

