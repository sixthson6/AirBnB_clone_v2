<<<<<<< HEAD
=======
#!/usr/bin/python3
""" Make an archive
"""

import datetime
import os
from fabric.api import local


def do_pack():
    """
    making an archinve from airbnb folder
    """
    now = datetime.datetime.now()
    name = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.tgz'
    res = local("tar cvzf {} ./web_static/*".format(name))
    local("mkdir -p versions")
    local("mv {} versions".format(name))

    if res.failed is True:
        return None

    abs_path = os.path.abspath(name)
    return abs_path
>>>>>>> de4db2c088b56d8fcb97b00ddea3cd394c697d21
