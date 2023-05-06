#!/usr/bin/env python3

import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

print("VF1=I AM VF1")
print("VF2=I AM VF2")

logging.info('VF_ERR=I AM VF_ERR')
logging.error('I am just a simple error message.')
