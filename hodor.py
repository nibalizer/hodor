#!/usr/bin/env python


import os
import shade
import uuid
import sys
import random
import time
import paramiko


def filter_images(images):
    new_images = []
    for i in images:
        if "(PV)" in i.name:
            continue
        if "OnMetal" in i.name:
            continue

        new_images.append(i)

    return new_images


if __name__ == "__main__":

    shade.simple_logging(debug=False)
    print "HODOR, make vm"

    user = os.getlogin()

    clouds = shade.openstack_clouds()
    cloud = random.choice(clouds)
    print "HODOR, using {0}-{1}".format(cloud.name, cloud.region_name)

    flavor = cloud.get_flavor_by_ram(512)

    images = filter_images(cloud.list_images())

    ubuntus = [i for i in images if 'Ubuntu' in i.name]
    trustys = [i for i in ubuntus if '14.04' in i.name]
    xenials = [i for i in ubuntus if '16.04' in i.name]
    print "HODOR, using image: {0}".format(trustys[0].name)
    print "HODOR, image id is {0}".format(trustys[0].id)

    image = cloud.get_image(trustys[0].name)

    key = cloud.search_keypairs(name_or_id=user)

    server_name = "hodor-" + str(uuid.uuid4())

    cloud.create_server(server_name, image['id'], flavor['id'], key_name=key[0]['id'])
    server = cloud.get_server(server_name)
    while True:
        print "HODOR, cloud slow"
        time.sleep(2)
        server = cloud.get_server(server_name)
        if len(server.addresses) > 0:
            break

    # either the first addr is ipv4 or ipv6
    if server.addresses['public'][0]['version'] == 4:
        ip = server.addresses['public'][0]['addr']
    else:
        ip = server.addresses['public'][1]['addr']
    print "HODOR, ip is {0}".format(ip)

    try:
        client = paramiko.client.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username='ubuntu')
        stdin, stdout, stderr = client.exec_command('ls -l')
    except:
        print "Paramiko failed"
        print "ssh ubuntu@{0}".format(ip)
