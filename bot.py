#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from config import Config
from pyrogram import Client as PMVBot
from pyrogram import filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    PMVBot = PMVBot(
        "Shell Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        in_memory=True,
    
      PMVBot.run()
