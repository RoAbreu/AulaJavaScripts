# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from cristianismo_app import facade


def index():
    cmd = facade.list_cristianismos_cmd()
    cristianismo_list = cmd()
    short_form=facade.cristianismo_short_form()
    cristianismo_short = [short_form.fill_with_model(m) for m in cristianismo_list]
    return JsonResponse(cristianismo_short)


def save(**cristianismo_properties):
    cmd = facade.save_cristianismo_cmd(**cristianismo_properties)
    return _save_or_update_json_response(cmd)


def update(cristianismo_id, **cristianismo_properties):
    cmd = facade.update_cristianismo_cmd(cristianismo_id, **cristianismo_properties)
    return _save_or_update_json_response(cmd)


def delete(cristianismo_id):
    facade.delete_cristianismo_cmd(cristianismo_id)()


def _save_or_update_json_response(cmd):
    try:
        cristianismo = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.cristianismo_short_form()
    return JsonResponse(short_form.fill_with_model(cristianismo))

