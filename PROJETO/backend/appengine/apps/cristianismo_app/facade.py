# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from cristianismo_app.commands import ListCristianismoCommand, SaveCristianismoCommand, UpdateCristianismoCommand, \
    CristianismoPublicForm, CristianismoDetailForm, CristianismoShortForm


def save_cristianismo_cmd(**cristianismo_properties):
    """
    Command to save Cristianismo entity
    :param cristianismo_properties: a dict of properties to save on model
    :return: a Command that save Cristianismo, validating and localizing properties received as strings
    """
    return SaveCristianismoCommand(**cristianismo_properties)


def update_cristianismo_cmd(cristianismo_id, **cristianismo_properties):
    """
    Command to update Cristianismo entity with id equals 'cristianismo_id'
    :param cristianismo_properties: a dict of properties to update model
    :return: a Command that update Cristianismo, validating and localizing properties received as strings
    """
    return UpdateCristianismoCommand(cristianismo_id, **cristianismo_properties)


def list_cristianismos_cmd():
    """
    Command to list Cristianismo entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCristianismoCommand()


def cristianismo_detail_form(**kwargs):
    """
    Function to get Cristianismo's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CristianismoDetailForm(**kwargs)


def cristianismo_short_form(**kwargs):
    """
    Function to get Cristianismo's short form. just a subset of cristianismo's properties
    :param kwargs: form properties
    :return: Form
    """
    return CristianismoShortForm(**kwargs)

def cristianismo_public_form(**kwargs):
    """
    Function to get Cristianismo'spublic form. just a subset of cristianismo's properties
    :param kwargs: form properties
    :return: Form
    """
    return CristianismoPublicForm(**kwargs)


def get_cristianismo_cmd(cristianismo_id):
    """
    Find cristianismo by her id
    :param cristianismo_id: the cristianismo id
    :return: Command
    """
    return NodeSearch(cristianismo_id)


def delete_cristianismo_cmd(cristianismo_id):
    """
    Construct a command to delete a Cristianismo
    :param cristianismo_id: cristianismo's id
    :return: Command
    """
    return DeleteNode(cristianismo_id)

