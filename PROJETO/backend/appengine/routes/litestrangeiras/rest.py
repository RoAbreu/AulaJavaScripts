# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from litestrangeira_app import facade


def index():
    cmd = facade.list_litestrangeiras_cmd()
    litestrangeira_list = cmd()
    short_form=facade.litestrangeira_short_form()
    litestrangeira_short = [short_form.fill_with_model(m) for m in litestrangeira_list]
    return JsonResponse(litestrangeira_short)


def save(**litestrangeira_properties):
    cmd = facade.save_litestrangeira_cmd(**litestrangeira_properties)
    return _save_or_update_json_response(cmd)


def update(litestrangeira_id, **litestrangeira_properties):
    cmd = facade.update_litestrangeira_cmd(litestrangeira_id, **litestrangeira_properties)
    return _save_or_update_json_response(cmd)


def delete(litestrangeira_id):
    facade.delete_litestrangeira_cmd(litestrangeira_id)()


def _save_or_update_json_response(cmd):
    try:
        litestrangeira = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.litestrangeira_short_form()
    return JsonResponse(short_form.fill_with_model(litestrangeira))

