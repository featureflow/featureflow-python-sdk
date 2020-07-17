#! /usr/bin/env python3
# -*- coding: utf-8 -*-


class User:
    def __init__(self, **user):
        """docstring for __init__"""
        self.key = user.get('key', "")
        self.attributes = user.get('attributes', {})
        self.session_attributes = user.get('sessionAttributes', {})
