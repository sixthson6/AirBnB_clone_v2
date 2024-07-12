#!/usr/bin/python3
"""Deploy static
"""


import re
from fabric.api import run, env
import os


def do_deploy(archive_path):
    """transfer archive to remote
    unarchive and deploy
    """
    
    if os.path.exists(archive_path) is False:
        return False

    env.hosts = [
            '54.208.116.17',
            '416793-web-01',
            '54.165.202.243',
            '416793-web-02'
            ]
    env.user = 'ubuntu'
    env.key_filename = '~/.ssh/id_rsa'

    # file = web_static_20240711195239.tgz

    pattern = r' _[0-9]+'
    match = re.findall(pattern, archive_path)
    name = "web_static" + match

    with cd("/tmp"):
        a = put(local_path="{}".format(archive_path), remote_path="/data/web_static/releases/{}".format(name))
        unar = run("tar -xzvf /data/web_static/releases/{}".format(name))
        if unar.succeded is True:
            b = run("rm /data/web_static/releases/{}".format(name))
    c = run("rm -f /data/web_static/current")
    d = run("ln -s /data/web_static/releases/{} /data/web_static/current".format(name))

    if a.ok and b.ok and c.ok and d.ok:
        return True
    else:
        return False
