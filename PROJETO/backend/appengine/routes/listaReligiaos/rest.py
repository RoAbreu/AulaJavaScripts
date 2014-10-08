# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from listaReligiao_app import facade


def index():
    cmd = facade.list_lista_religiaos_cmd()
    lista_religiao_list = cmd()
    short_form=facade.lista_religiao_short_form()
    lista_religiao_short = [short_form.fill_with_model(m) for m in lista_religiao_list]
    return JsonResponse(lista_religiao_short)


def save(**lista_religiao_properties):
    cmd = facade.save_lista_religiao_cmd(**lista_religiao_properties)
    return _save_or_update_json_response(cmd)


def update(lista_religiao_id, **lista_religiao_properties):
    cmd = facade.update_lista_religiao_cmd(lista_religiao_id, **lista_religiao_properties)
    return _save_or_update_json_response(cmd)


def delete(lista_religiao_id):
    facade.delete_lista_religiao_cmd(lista_religiao_id)()


def _save_or_update_json_response(cmd):
    try:
        lista_religiao = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.lista_religiao_short_form()
    return JsonResponse(short_form.fill_with_model(lista_religiao))

