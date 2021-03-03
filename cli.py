#!/usr/bin/env python3

import sys
from originizer import originize

originize(
    f"{sys.argv[1]}.png",
    f"{sys.argv[1]}.xml",
    f"{sys.argv[1]}.ora"
)
