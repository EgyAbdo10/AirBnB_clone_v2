#!/usr/bin/python3
"""this file is for deploying code to my servers"""
from fabric.api import *
import os


env.hosts = ["ubuntu@100.25.144.102", "ubuntu@34.207.58.33"]


def do_deploy(archive_path):
    """deploy code to remote servers"""
    if not os.path.exists(archive_path):
        return False
    put(local_path=archive_path, remote_path="/tmp/")
    archive_name = archive_path.split("/")[-1][:-4]  # without extension
    run(f"mkdir -p /data/web_static/releases/{archive_name}")
    run(f"""tar -xzf /tmp/{archive_name}.tgz -C
         /data/web_static/releases/{archive_name}""")
    run(f"rm /tmp/{archive_name}.tgz")
    run(f"rm -rf /data/web_static/current")
    sudo(
        f"""
        ln -s /data/web_static/releases/{archive_name}/
         /data/web_static/current
        """
        )
    return True
