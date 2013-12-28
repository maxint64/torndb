#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Sample database connection config file.

    Added by maxint64
"""

from collections import defaultdict
conf = defaultdict(dict)

#default connection config
conf["default"]["host"] = "localhost"
conf["default"]["database"] = "database"
conf["default"]["user"] = "user"
conf["default"]["password"] = "password"
conf["default"]["max_idle_time"] = 7*3600
conf["default"]["connect_timeout"] = 0
conf["default"]["time_zone"] = "+0:00" 

#of course you could extend this config as your need
#
#conf["backup"]["host"] = "localhost"
#conf["backup"]["database"] = "database"
#conf["backup"]["user"] = "user"
#conf["backup"]["password"] = "password"
#conf["backup"]["max_idle_time"] = 7*3600
#conf["backup"]["connect_timeout"] = 0
#conf["backup"]["time_zone"] = "+0:00" 
#
#conf["test"]["host"] = "localhost"
#conf["test"]["database"] = "database"
#conf["test"]["user"] = "user"
#conf["test"]["password"] = "password"
#conf["test"]["max_idle_time"] = 7*3600
#conf["test"]["connect_timeout"] = 0
#conf["test"]["time_zone"] = "+0:00" 
