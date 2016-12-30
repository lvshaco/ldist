#!/usr/bin/env python
#_*_ coding:utf-8 _*_

hostvars = {
    'vps':       { 'ansible_host': '45.76.205.94',  'ansible_port': 22 },
    'qzdev_lxj': { 'ansible_host': '127.0.0.1',     'ansible_port': 19860 },
    'qzdev_game':{ 'ansible_host': '192.168.1.220', 'ansible_port': 22 },
    'qzdev_jie': { 'ansible_host': '192.168.1.221', 'ansible_port': 22 },
    'qzdev_jie2':{ 'ansible_host': '192.168.1.223', 'ansible_port': 22 },
    'qzdev_db':  { 'ansible_host': '192.168.1.200', 'ansible_port': 22 },
    'qzs3':      { 'ansible_host': '42.51.11.49',   'ansible_port': 22 },
    'qzs4':      { 'ansible_host': '42.51.11.196',   'ansible_port': 22 },
}

auth_dev = [
    '~/.ssh/id_rsa_coolsoft.pub',
    '~/.ssh/id_rsa_jie.pub',
]
user_vps = [
    { 'name': 'lxj', 'password': 'vps1986', 'authorized': ['~/.ssh/id_rsa_lvshaco.pub'] },
    { 'name': 'hpj', 'password': 'vps1986', 'authorized': ['~/.ssh/id_rsa_hpj.pub'] },
]
user_coolsoft = [
    { 'name': 'game', 'password': '123456', 'authorized': auth_dev },
]
user_out = [
    { 'name': 'game', 'password': 'ABcd#adfa#*(#!*(*&Y*', 'authorized': auth_dev },
]
user_39 = [
    { 'name': 'game', 'password': 'ABcd#adfa#*(#!*(*&Y*', 'authorized': auth_dev },
]
groups = {
    'vps': {
        'hosts': [ 'vps' ],
        'vars': { 'sshuser': user_vps },
        },
    'coolsoft': {
        'hosts': [ 'qzdev_lxj', 'qzdev_game', 'qzdev_jie', 'qzdev_jie2', 'qzdev_db' ],
        'vars': { 'sshuser': user_coolsoft, 'ssh_enable_password_login': True },
        },
    'out': {
        'hosts': [ 'qzbuilder' ],
        'vars': { 'sshuser': user_out },
        },
    '39': {
        'hosts': [ 'qzcs', 'qzios', 'qzs1', 'qzs3', 'qzs4' ],
        'vars': { 'sshuser': user_39 },
        },
    '_meta': { 'hostvars': hostvars }
    }

def gen(is_root):
    if not is_root:  # use ~/.ssh/config
        groups['_meta']['hostvars'] = {}
    import inventory
    inventory.gen(groups)

################################################
# ssh_disable_key_login      # default undefined
# ssh_enable_password_login  # default undefined
# ssh_user                   # ssh users
