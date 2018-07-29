# -*- coding: utf-8 -*-

import json


class LoadJson:

    def read(self, file):

        with open(file) as json_file:
            data = json.load(json_file)

            if data:
                return data
            else:
                None
