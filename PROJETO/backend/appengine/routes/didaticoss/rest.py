# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from didaticos_app import facade


def index():
    cmd = facade.list_didaticoss_cmd()
    didaticos_list = cmd()
    short_form=facade.didaticos_short_form()
    didaticos_short = [short_form.fill_with_model(m) for m in didaticos_list]
    return JsonResponse(didaticos_short)


def save(**didaticos_properties):
    cmd = facade.save_didaticos_cmd(**didaticos_properties)
    return _save_or_update_json_response(cmd)


def update(didaticos_id, **didaticos_properties):
    cmd = facade.update_didaticos_cmd(didaticos_id, **didaticos_properties)
    return _save_or_update_json_response(cmd)


def delete(didaticos_id):
    facade.delete_didaticos_cmd(didaticos_id)()


def _save_or_update_json_response(cmd):
    try:
        didaticos = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.didaticos_short_form()
    return JsonResponse(short_form.fill_with_model(didaticos))

