# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from religiao_app import facade


def index():
    cmd = facade.list_religiaos_cmd()
    religiao_list = cmd()
    short_form=facade.religiao_short_form()
    religiao_short = [short_form.fill_with_model(m) for m in religiao_list]
    return JsonResponse(religiao_short)


def save(**religiao_properties):
    cmd = facade.save_religiao_cmd(**religiao_properties)
    return _save_or_update_json_response(cmd)


def update(religiao_id, **religiao_properties):
    cmd = facade.update_religiao_cmd(religiao_id, **religiao_properties)
    return _save_or_update_json_response(cmd)


def delete(religiao_id):
    facade.delete_religiao_cmd(religiao_id)()


def _save_or_update_json_response(cmd):
    try:
        religiao = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.religiao_short_form()
    return JsonResponse(short_form.fill_with_model(religiao))

