#!/usr/bin/python3
"""Deploy static
"""


import re
from fabric.api import *
import os


env.hosts = [
        '54.208.116.17',
        '54.165.202.243'
        ]
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """transfer archive to remote
    unarchive and deploy
    """
    
    if os.path.exists(archive_path) is False:
        return False

    # file = web_static_20240711195239.tgz

    pattern = r' _[0-9]+'
    match = re.findall(pattern, archive_path)
    name = "web_static" + match

    put(archive_path, "/tmp")
    run("sudo mkdir -p /data/web_static/releases/{}".format(name))

    unar = run("sudo tar -xzvf /tmp/{}.tgz -C /data/web_static/releases/web_static_{}/".format(name))
    if unar.succeded is True:
            b = run("sudo rm /tmp/{}".format(name))

    run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name))

    run('sudo rm -rf /data/web_static/releases/{}/web_static'.format(name))

    c = run("sudo rm -f /data/web_static/current")
    d = run("sudo ln -s /data/web_static/releases/{} /data/web_static/current".format(name))

    if a.ok and b.ok and c.ok and d.ok:
        return True
    else:
        return False
