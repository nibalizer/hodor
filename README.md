Hodor
=====


Hodor doesn't speak much english, the only thing he can do is make you a vm. Hodor doesn't care


Usage:


```shell
$: python hodor.py 
Manager envvars:ca-ymq-1 running task FlavorList
Manager envvars:ca-ymq-1 ran task FlavorList in 2.01990008354s
Manager envvars:ca-ymq-1 running task GlanceImageList
Manager envvars:ca-ymq-1 ran task GlanceImageList in 1.39872288704s
Manager envvars:ca-ymq-1 running task KeypairList
Manager envvars:ca-ymq-1 ran task KeypairList in 0.179165840149s
Manager envvars:ca-ymq-1 running task ServerCreate
Manager envvars:ca-ymq-1 ran task ServerCreate in 0.59867978096s
Manager envvars:ca-ymq-1 running task ServerGet
Manager envvars:ca-ymq-1 ran task ServerGet in 0.309627056122s


$ nova list | grep hodor
| d316b42b-694c-429c-accd-5a4c0745635e | hodor-b7717c31-b76b-49de-a25c-7698e4c03289 | BUILD  | spawning   | NOSTATE     |                       |
```




History
=======


This grew out of the hodor shell script in nibalizer's dotfiles: https://github.com/nibalizer/dotfiles/blob/master/local/bin/hodor



Installation
============



Hodor will probably always require shade from git.

Hodor uses oscc(http://docs.openstack.org/developer/os-client-config/) and a clouds.yaml


Destroying hodor machines
=========================


```shell
nova list | awk '/hodor/ { print $4}' | xargs nova delete
```



