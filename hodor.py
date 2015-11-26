#!/usr/bin/env python


import os
import shade
import uuid



if __name__ == "__main__":

    shade.simple_logging(debug=True)

    user = os.getlogin()

    #cloud = shade.openstack_cloud(cloud='nibz-vexxhost')
    cloud = shade.openstack_cloud()

    flavor = cloud.get_flavor_by_ram(512)

    image = cloud.get_image('Ubuntu 14.04.3 LTS')

    key = cloud.search_keypairs(name_or_id=user)

    server_name = "hodor-" + str(uuid.uuid4())

    cloud.create_server( server_name, image['id'], flavor['id'], key_name=key[0]['id'])


