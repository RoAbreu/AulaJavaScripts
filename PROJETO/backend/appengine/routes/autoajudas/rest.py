# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from autoajuda_app import facade


def index():
    cmd = facade.list_autoajudas_cmd()
    autoajuda_list = cmd()
    short_form=facade.autoajuda_short_form()
    autoajuda_short = [short_form.fill_with_model(m) for m in autoajuda_list]
    return JsonResponse(autoajuda_short)


def save(**autoajuda_properties):
    cmd = facade.save_autoajuda_cmd(**autoajuda_properties)
    return _save_or_update_json_response(cmd)


def update(autoajuda_id, **autoajuda_properties):
    cmd = facade.update_autoajuda_cmd(autoajuda_id, **autoajuda_properties)
    return _save_or_update_json_response(cmd)


def delete(autoajuda_id):
    facade.delete_autoajuda_cmd(autoajuda_id)()


def _save_or_update_json_response(cmd):
    try:
        autoajuda = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.autoajuda_short_form()
    return JsonResponse(short_form.fill_with_model(autoajuda))

