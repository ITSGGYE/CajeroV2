# -*- coding: utf-8 -*-

import logging


class Validations:

    def onlyDigits(self, input):
        if str.isdigit(input) or input == "":
            logging.warning(input)
            return True
        else:
            logging.warning(input)
            return False