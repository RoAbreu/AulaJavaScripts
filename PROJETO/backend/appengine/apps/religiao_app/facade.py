# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from religiao_app.commands import ListReligiaoCommand, SaveReligiaoCommand, UpdateReligiaoCommand, \
    ReligiaoPublicForm, ReligiaoDetailForm, ReligiaoShortForm


def save_religiao_cmd(**religiao_properties):
    """
    Command to save Religiao entity
    :param religiao_properties: a dict of properties to save on model
    :return: a Command that save Religiao, validating and localizing properties received as strings
    """
    return SaveReligiaoCommand(**religiao_properties)


def update_religiao_cmd(religiao_id, **religiao_properties):
    """
    Command to update Religiao entity with id equals 'religiao_id'
    :param religiao_properties: a dict of properties to update model
    :return: a Command that update Religiao, validating and localizing properties received as strings
    """
    return UpdateReligiaoCommand(religiao_id, **religiao_properties)


def list_religiaos_cmd():
    """
    Command to list Religiao entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListReligiaoCommand()


def religiao_detail_form(**kwargs):
    """
    Function to get Religiao's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ReligiaoDetailForm(**kwargs)


def religiao_short_form(**kwargs):
    """
    Function to get Religiao's short form. just a subset of religiao's properties
    :param kwargs: form properties
    :return: Form
    """
    return ReligiaoShortForm(**kwargs)

def religiao_public_form(**kwargs):
    """
    Function to get Religiao'spublic form. just a subset of religiao's properties
    :param kwargs: form properties
    :return: Form
    """
    return ReligiaoPublicForm(**kwargs)


def get_religiao_cmd(religiao_id):
    """
    Find religiao by her id
    :param religiao_id: the religiao id
    :return: Command
    """
    return NodeSearch(religiao_id)


def delete_religiao_cmd(religiao_id):
    """
    Construct a command to delete a Religiao
    :param religiao_id: religiao's id
    :return: Command
    """
    return DeleteNode(religiao_id)

