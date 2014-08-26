# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from litnacional_app import facade


def index():
    cmd = facade.list_litnacionals_cmd()
    litnacional_list = cmd()
    short_form=facade.litnacional_short_form()
    litnacional_short = [short_form.fill_with_model(m) for m in litnacional_list]
    return JsonResponse(litnacional_short)


def save(**litnacional_properties):
    cmd = facade.save_litnacional_cmd(**litnacional_properties)
    return _save_or_update_json_response(cmd)


def update(litnacional_id, **litnacional_properties):
    cmd = facade.update_litnacional_cmd(litnacional_id, **litnacional_properties)
    return _save_or_update_json_response(cmd)


def delete(litnacional_id):
    facade.delete_litnacional_cmd(litnacional_id)()


def _save_or_update_json_response(cmd):
    try:
        litnacional = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.litnacional_short_form()
    return JsonResponse(short_form.fill_with_model(litnacional))

