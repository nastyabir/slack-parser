from slack import WebClient
import pandas as pd

client = WebClient(token='you need user token')


def get_user_list(channel_id):
    """
    Get user list from channel. Return list of user_ids
    """
    response = client.conversations_members(channel=channel_id)
    user_list = response['members']
    return user_list


def get_display_name(user_id):
    """
    Get display name with user_id. Return display_name as string
    """
    return client.users_profile_get(user=user_id)['profile']['display_name']


def get_user_email(user_id):
    """
    Get email with user_id. Return email as string
    """
    return client.users_profile_get(user=user_id)['profile']['email']


def get_conversations_history(channel_id):
    """
    Get conversations history from channel. Return list with messages
    """
    return client.conversations_history(channel=channel_id)['messages']


def ts_parse(ts):
    """
    Return timestamp with slack format
    """
    return ts[:10] + '.' + ts[-6:]


def get_list_of_reactions(history, ts):
    """
    Return dictionary with reaction as a key and list of users as a value
    """
    dict_of_reac = {}
    for row in range(len(history)):
        if history[row]['ts'] == ts:
            for i in range(len(history[row]['reactions'])):
                dict_of_reac[history[row]['reactions'][i]['name']] = history[row]['reactions'][i]['users']
    return dict_of_reac
