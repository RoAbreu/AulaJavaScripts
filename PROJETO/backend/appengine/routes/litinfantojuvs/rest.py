# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from litinfantojuv_app import facade


def index():
    cmd = facade.list_litinfantojuvs_cmd()
    litinfantojuv_list = cmd()
    short_form=facade.litinfantojuv_short_form()
    litinfantojuv_short = [short_form.fill_with_model(m) for m in litinfantojuv_list]
    return JsonResponse(litinfantojuv_short)


def save(**litinfantojuv_properties):
    cmd = facade.save_litinfantojuv_cmd(**litinfantojuv_properties)
    return _save_or_update_json_response(cmd)


def update(litinfantojuv_id, **litinfantojuv_properties):
    cmd = facade.update_litinfantojuv_cmd(litinfantojuv_id, **litinfantojuv_properties)
    return _save_or_update_json_response(cmd)


def delete(litinfantojuv_id):
    facade.delete_litinfantojuv_cmd(litinfantojuv_id)()


def _save_or_update_json_response(cmd):
    try:
        litinfantojuv = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.litinfantojuv_short_form()
    return JsonResponse(short_form.fill_with_model(litinfantojuv))

