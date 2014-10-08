# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from biblias_app import facade


def index():
    cmd = facade.list_bibliass_cmd()
    biblias_list = cmd()
    short_form=facade.biblias_short_form()
    biblias_short = [short_form.fill_with_model(m) for m in biblias_list]
    return JsonResponse(biblias_short)


def save(**biblias_properties):
    cmd = facade.save_biblias_cmd(**biblias_properties)
    return _save_or_update_json_response(cmd)


def update(biblias_id, **biblias_properties):
    cmd = facade.update_biblias_cmd(biblias_id, **biblias_properties)
    return _save_or_update_json_response(cmd)


def delete(biblias_id):
    facade.delete_biblias_cmd(biblias_id)()


def _save_or_update_json_response(cmd):
    try:
        biblias = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.biblias_short_form()
    return JsonResponse(short_form.fill_with_model(biblias))

