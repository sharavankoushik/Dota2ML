import smtplib, os
from email.mime.text import MIMEText
from email.utils import formatdate
from datetime import datetime
from dota2py import data

def print_match_history(gmh_result):
    '''Print a summary of a list of matches.'''
    for match in gmh_result['matches']:
        match_id = match['match_id']
        start_time = datetime.fromtimestamp(int(match['start_time']))
        print('Match %d - %s' % (match_id, start_time))

def get_game_mode_string(game_mode_id):
    '''Return a human-readable string for a game_mode id.'''
    try:
        return data.GAME_MODES['dota_game_mode_%s' % game_mode_id]
    except KeyError:
        return 'Unknown mode %s' % game_mode_id
