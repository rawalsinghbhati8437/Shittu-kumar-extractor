#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7822801684:AAE4y0ETMqA12Y8xakRofTfWIsEG3IGXhYw")
    API_ID = int(os.environ.get("API_ID", "20114039"))
    API_HASH = os.environ.get("API_HASH", "87297b8f3cc8fc9bbce591ad30da5896")
    AUTH_USERS = os.environ.get("AUTH_USERS", "8172163893")
