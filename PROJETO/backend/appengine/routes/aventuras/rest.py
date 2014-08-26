# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from aventura_app import facade


def index():
    cmd = facade.list_avenuras_cmd()
    avenura_list = cmd()
    short_form=facade.avenura_short_form()
    avenura_short = [short_form.fill_with_model(m) for m in avenura_list]
    return JsonResponse(avenura_short)


def save(**avenura_properties):
    cmd = facade.save_avenura_cmd(**avenura_properties)
    return _save_or_update_json_response(cmd)


def update(avenura_id, **avenura_properties):
    cmd = facade.update_avenura_cmd(avenura_id, **avenura_properties)
    return _save_or_update_json_response(cmd)


def delete(avenura_id):
    facade.delete_avenura_cmd(avenura_id)()


def _save_or_update_json_response(cmd):
    try:
        avenura = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.avenura_short_form()
    return JsonResponse(short_form.fill_with_model(avenura))

