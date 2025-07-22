jeisenbath.supermicro.ssm_install
=========

Install Supermicro Server Manager.

Requirements
------------

Requires ansible.posix collection if running firewalld.

Role Variables
--------------

These three variables are required to define and have no defaults
```yaml
ssm_install_installer_bundle_path:
ssm_install_file:
ssm_install_web_admin_password:
```

role defaults/main.yml
```yaml
ssm_install_parent_dir: /opt/Supermicro
ssm_install_use_firewalld: true
# ssm needs to be installed with root priviledge. Change these to set file ownership for another user/group.
ssm_install_user: root
ssm_install_group: root
# ssm install property vars
ssm_install_chosen_install_feature_list: SSMServer,SSMWeb
ssm_install_use_default_jvm: 'Yes'
ssm_install_installed_jvm_path: /usr/java/jdk17.0.10/jre/bin/java # set if use_default_jvm is set to No
ssm_install_server_web_http_port: 8080
ssm_install_server_web_https_port: 8443
ssm_install_server_email_smtp: mail.localdomain.com
ssm_install_server_email_sender: localhost@localdomain.com
ssm_install_server_email_username: localhost
ssm_install_server_email_password: changeme
ssm_install_server_email_smtp_port: 25
ssm_install_server_email_smtp_security: none
ssm_install_server_default_contact: your.name@your-domain.com
ssm_install_use_server_default_db: 'Yes'
ssm_install_server_create_db: 'Yes'
ssm_install_server_db: # define if not installing default database
  type: PostgreSQL
  name: ssm
  port: 5432
  ip: your-DB-IP
  username: your-DB-Account
  password: your-DB-password
```

Example Playbook
----------------

The following example playbook would be a standard install with all required variables.

```yaml
- hosts: ssm-server.domain.com
  roles:
    - role: jeisenbath.supermicro.ssm_install
      ssm_install_installer_bundle_path: /home/ansible/SSM_6.1.0_build.1267_linux.zip
      ssm_install_file: SSMInstaller_6.1.0_build.1267_linux_x64_20250512164814.bin
      ssm_install_web_admin_password: "{{ vaulted_ssm_admin_password }}
```

License
-------

GPL-3.0-or-later
