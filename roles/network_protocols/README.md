jeisenbath.supermicro.network_protocols
=========

Configure Supermicro BMC NetworkProtocols using Redfish APIs

Role Variables
--------------

Defaults in defaults/main.yml
```yaml
network_protocols_bmc_admin_user: "{{ bmc_admin_user }}"
network_protocols_bmc_admin_password: "{{ bmc_admin_password }}"
network_protocols_bmc_validate_certs: "{{ bmc_validate_certs }}"
network_protocols_bmc_force_basic_auth: "{{ bmc_force_basic_auth }}"
network_protocols_ntp_enabled: false
network_protocols_snmp2_enabled: false
network_protocols_snmp2_community_strings: []
network_protocols_ssh_enabled: true
```

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - name: jeisenbath.supermicro.network_protocols
          network_protocols_ntp_enabled: true
          network_protocols_ntp_servers:
            - 0.us.pool.ntp.org
            - 1.us.pool.ntp.org
          network_protocols_snmp2_enabled: true
          network_protocols_snmp2_community_strings:
            - AccessMode: Limited
              CommunityString: community
              Name: snmp2ro
          network_protocols_ssh_enabled: false
```

License
-------

GPT-3.0-or-later
