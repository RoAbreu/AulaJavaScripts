# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from budismo_app import facade


def index():
    cmd = facade.list_budismos_cmd()
    budismo_list = cmd()
    short_form=facade.budismo_short_form()
    budismo_short = [short_form.fill_with_model(m) for m in budismo_list]
    return JsonResponse(budismo_short)


def save(**budismo_properties):
    cmd = facade.save_budismo_cmd(**budismo_properties)
    return _save_or_update_json_response(cmd)


def update(budismo_id, **budismo_properties):
    cmd = facade.update_budismo_cmd(budismo_id, **budismo_properties)
    return _save_or_update_json_response(cmd)


def delete(budismo_id):
    facade.delete_budismo_cmd(budismo_id)()


def _save_or_update_json_response(cmd):
    try:
        budismo = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.budismo_short_form()
    return JsonResponse(short_form.fill_with_model(budismo))

