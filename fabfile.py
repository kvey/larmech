from fabric.api import *

@task
def localhost():
    env.hosts = ["localhost"]


@task
def prod():
    env.user = "root"
    env.hosts = ["104.236.174.221"]

@task
def deploy():
    """
    Deploy new code slug
    """
    run("source /virtualenv/larmech/bin/activate")
    local("mkdir -p /tmp/deploys")
    local("tar --exclude='*.git*' --exclude='./client' -zcvf /tmp/deploys/slug.tar.gz ./")
    run("mkdir -p /deploys /current_release")
    put("/tmp/deploys/slug.tar.gz", "/deploys/")
    run("tar -xvf /deploys/slug.tar.gz -C /current_release")
    run("ln -sf /current_release/larmech_nginx.conf /etc/nginx/sites-enabled")
    run("ln -sf /current_release/larmech_uwsgi.ini /etc/uwsgi/apps-enabled")
    sudo("/etc/init.d/uwsgi restart")
    sudo("/etc/init.d/nginx restart")


@task
def provision():
    """
    Provision a new machine
    """
    sudo("add-apt-repository ppa:fkrull/deadsnakes")
    sudo("apt-get update")
    sudo("apt-get install nginx")
    sudo("apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev")
    sudo("apt-get install python2.7 python-setuptools uwsgi uwsgi-plugin-python")
    sudo("/etc/init.d/nginx start")
    sudo("apt-get install build-essential")
    sudo("easy_install -U pip")
    sudo("pip install virtualenv")
    run("mkdir -p /virtualenv")
    with cd("/virtualenv"):
        run("virtualenv larmech")
    with cd("/virtualenv/larmech"):
        run("source bin/activate")



