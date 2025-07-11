jeisenbath.supermicro.managers
=========

Configure Supermicro BMC settings in the /redfish/v1/Managers/1 Redfish API

Role Variables
--------------

```yaml
managers_bmc_admin_user: "{{ bmc_admin_user }}"
managers_bmc_admin_password: "{{ bmc_admin_password }}"
managers_bmc_validate_certs: "{{ bmc_validate_certs }}"
managers_bmc_force_basic_auth: "{{ bmc_force_basic_auth }}"
managers_timezone: (UTC+00:00) Coordinated Universal Time # Valid timezones can be found at /redfish/v1/Managers/1/TimeZoneName@Redfish.AllowableValues
```

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - name: jeisenbath.supermicro.managers
          managers_timezone: (UTC-06:00) Central Time (US & Canada)
```

License
-------

GPL-3.0-or-later
