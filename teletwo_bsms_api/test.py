#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .core import TeleTwoAPI

"""
partner_login, partner_password, sender_name
"""

TeleTwoAPI('partner_login', 'partner_password', 'sender_name').send_message('+79999999999', 'Немного мессаджа')
