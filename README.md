```
# run ./foot init first
# see in `ap` script
# adduser
ansible-playbook -i i_byroot.py user_byroot.yml -k -l
ansible-playbook -i i.py user.yml -K -l

# vps
ansible-playbook -i i.py vps.yml -K -l

# web
# tags: sql,code,crontab
ansible-playbook -i i.py web.yml -K -l

# qaweb1
# tags: shacobin,code
ansible-playbook -i i.py qaweb1.yml -K -l

# qzserver
ansible-playbook -i hosts server.yml -K -t dev -l       # 部署开发环境
ansible-playbook -i hosts server.yml -K -t init -l      # 部署新服
ansible-playbook -i hosts server.yml -K -t reinit -l    # 清数据库重新开服
ansible-playbook -i hosts server.yml -K -t upgrade -l   # 更新重启
ansible-playbook -i hosts server.yml -K -t hotfix -l    # 热更新
ansible-playbook -i hosts server.yml -K -t reloadres -l # 更新资源 
ansible-playbook -i hosts server.yml -K -t gateopen -l  # 对外开放
ansible-playbook -i hosts server.yml -K -t gatelimit -l # 限制开放
ansible-playbook -i hosts server.yml -K -t dumpdb -l    # 导出数据
ansible-playbook -i hosts server.yml -K -t importdb -l  # 导入数据

# graylog
ansible-playbook -i host/hosts graylog.yml -K -b --become-method=su -l
```

todo:
serice: enabled=yes always changed
