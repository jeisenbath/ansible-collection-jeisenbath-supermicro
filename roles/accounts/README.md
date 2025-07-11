jeisenbath.supermicro.accounts
=========

Manage users for Supermicro BMC using Redfish AccountService API

Role Variables
--------------

Role defaults/main.yml
```yaml
accounts_bmc_admin_user: "{{ bmc_admin_user }}"
accounts_bmc_admin_password: "{{ bmc_admin_password }}"
accounts_bmc_validate_certs: "{{ bmc_validate_certs }}"
accounts_bmc_force_basic_auth: "{{ bmc_force_basic_auth }}"
```

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - name: jeisenbath.supermicro.accounts
          accounts_bmc_user:
            - UserName: operator
              Password: "{{ vault_bmc_operator_password }}"
              RoleId: User
              Enabled: true
              Id: 3
```          

License
-------

GPL-3.0-or-later
