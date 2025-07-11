jeisenbath.supermicro.bios
=========

Update and apply BIOS settings for a Supermicro server through the Redfish API

Role Variables
--------------

Defaults defined in defaults/main.yml
```yaml
bios_bmc_admin_user: "{{ bmc_admin_user }}"
bios_bmc_admin_password: "{{ bmc_admin_password }}"
bios_bmc_validate_certs: "{{ bmc_validate_certs }}"
bios_bmc_force_basic_auth: "{{ bmc_force_basic_auth }}"
bios_apply_pending: false
bios_reset: false
bios_reset_type: GracefulRestart
```

Optional variables
```yaml
bios_attributes: # Dictionarey of BIOS Attribute Names and Values
```

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - role: jeisenbath.supermicro.bios
          bios_apply_pending: true
          bios_attributes:
            PowerTechnology#2800: "Disable"
            EnableMonitorMWAIT#083D: "Disable"
            CPUC6Report#0840: "Disable"
            EnhancedHaltState(C1E)#0841: "Disable"
            PackageCState#0843: "C0/C1 state"
          tags: bios
```

License
-------

GPL-3.0-or-later
