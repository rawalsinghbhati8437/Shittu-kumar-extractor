#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7722678913:AAHrBdtInOhhInrMjnmlMWl_QZPI1IPoXEQ")
    API_ID = int(os.environ.get("API_ID", "16494736"))
    API_HASH = os.environ.get("API_HASH", "2cb7fa5859e2de684e3e10d9c049621a")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6214273135")
