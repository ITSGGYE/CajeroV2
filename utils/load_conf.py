# -*- coding: utf-8 -*-

import ConfigParser


class Config:

    def getConfig(self, file, section):
        conf = ConfigParser.ConfigParser()
        conf.read(file)
        array = eval(conf.get(section, "documentos"), {}, {})
        if array:
            return array
        else:
            return None
