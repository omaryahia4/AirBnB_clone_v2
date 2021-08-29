#!/usr/bin/python3
"""Fabric script that generates a .tgz archive """
from datetime import datetime
from fabric.api import local


def do_pack():
    """script that generates a .tgz archive"""
    try:
        sysdate = datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        fn = "versions/web_static_{}.tgz".format(sysdate)
        local("tar -cvzf {} web_static".format(fn))
        return fn
    except BaseException:
        return None
