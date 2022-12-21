#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Jeolpaul

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "24229815"))
    API_HASH = os.environ.get("API_HASH", "6d03e392b1200580a85ef243f83a48a5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "5818737155:AAFgEZ3p6PGaHmKqW3QcLEotCb_EsDba9xg") 
    CAPTION = os.environ.get("CAPTION", "Upload By Kshitij")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", "5523592151")
    SESSION = os.environ.get("SESSION", "AQCxt5WEiHqq8DH-glWcAMOp2PdgKXi4L8hEsL7FjnoCN-t9P9-ITdpSnylg1uPL4HO3cAjuSa-lM6p4SqDcn7liLhfgHawNZQOvMn15aZDwApQ_h-GOhCgdSEW_ZNiHHObNhKtwHf-3wwpg0fMJsmOvo5S23CrPa-zWpE1sYGiblwpE8FOs-5qeSmy5Z8NBvlehbFL-YnD0f3XoI8O6ew4yP_5ifvKExBIDCIPC4WccU3hj--uhNx1u73Bm8CQvQJgdnu2obfj4U_TQRC23CVQMfXhTLs2dNROcadTUB7Yl5MqtL2DS_82c_AhQeSsaWuOn7jBUg1p-1d9kPYEekBgYAAAAAUk7U9cA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
