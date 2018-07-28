# -*- coding: utf-8 -*-

import ConfigParser


class Config:

    def getConfig(self):
        conf = ConfigParser.ConfigParser()
        conf.read("config.ini")
        array = eval(conf.get("documentos", "documentos"), {}, {})
        if array:
            return array
        else:
            return None
