# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from listaDidaticos_app import facade


def index():
    cmd = facade.list_lista_didaticoss_cmd()
    lista_didaticos_list = cmd()
    short_form=facade.lista_didaticos_short_form()
    lista_didaticos_short = [short_form.fill_with_model(m) for m in lista_didaticos_list]
    return JsonResponse(lista_didaticos_short)


def save(**lista_didaticos_properties):
    cmd = facade.save_lista_didaticos_cmd(**lista_didaticos_properties)
    return _save_or_update_json_response(cmd)


def update(lista_didaticos_id, **lista_didaticos_properties):
    cmd = facade.update_lista_didaticos_cmd(lista_didaticos_id, **lista_didaticos_properties)
    return _save_or_update_json_response(cmd)


def delete(lista_didaticos_id):
    facade.delete_lista_didaticos_cmd(lista_didaticos_id)()


def _save_or_update_json_response(cmd):
    try:
        lista_didaticos = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.lista_didaticos_short_form()
    return JsonResponse(short_form.fill_with_model(lista_didaticos))

