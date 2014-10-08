# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from listaDicionarios_app import facade


def index():
    cmd = facade.list_lista_dicionarioss_cmd()
    lista_dicionarios_list = cmd()
    short_form=facade.lista_dicionarios_short_form()
    lista_dicionarios_short = [short_form.fill_with_model(m) for m in lista_dicionarios_list]
    return JsonResponse(lista_dicionarios_short)


def save(**lista_dicionarios_properties):
    cmd = facade.save_lista_dicionarios_cmd(**lista_dicionarios_properties)
    return _save_or_update_json_response(cmd)


def update(lista_dicionarios_id, **lista_dicionarios_properties):
    cmd = facade.update_lista_dicionarios_cmd(lista_dicionarios_id, **lista_dicionarios_properties)
    return _save_or_update_json_response(cmd)


def delete(lista_dicionarios_id):
    facade.delete_lista_dicionarios_cmd(lista_dicionarios_id)()


def _save_or_update_json_response(cmd):
    try:
        lista_dicionarios = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.lista_dicionarios_short_form()
    return JsonResponse(short_form.fill_with_model(lista_dicionarios))

