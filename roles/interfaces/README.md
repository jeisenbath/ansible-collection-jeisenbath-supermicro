jeisenbath.bios.interfaces
=========

Configure a Supermicro BMC EthernetInterface using redfish APIs

Role Variables
--------------

Role defaults in defaults/main.yml:
```yaml
interfaces_bmc_admin_user: "{{ bmc_admin_user }}"
interfaces_bmc_admin_password: "{{ bmc_admin_password }}"
interfaces_bmc_validate_certs: "{{ bmc_validate_certs }}"
interfaces_bmc_force_basic_auth: "{{ bmc_force_basic_auth }}"
```

Define interfaces_ethernet_interface as below to configure EthernetInterface/1
```yaml
interfaces_ethernet_interface:
  HostName: "{{ inventory_hostname_short }}"
  IPProtocolStatus: IPv4 # Valid values are IPv4, IPv6, Dual
  StaticNameServers:
    - "{{ main_dns_server }}"
    - "{{ secondary_dns_server }}"
  LANInterface: Dedicated # Valid values are Dedicated, Failover, Shared
```

Example Playbook
----------------

```yaml
    - hosts: servers
      roles:
        - name: jeisenbath.supermicro.interfaces
          interfaces_ethernet_interface:
            HostName: "{{ inventory_hostname_short }}"
            IPProtocolStatus: IPv4
            StaticNameServers:
              - "{{ main_dns_server }}"
              - "{{ secondary_dns_server }}"
            LANInterface: Dedicated
```

License
-------

GPT-3.0-or-later
