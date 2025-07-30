#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: ssm_host
short_description: Manages hosts in Supermicro Server Manager.
description:
    - Remove or discover hosts using Supermicro Server Manager API.
version_added: 1.2.0
author:
    - "Josh Eisenbath (@jeisenbath)"
options:
    state:
        description: Whether server should be present or absent in SSM.
        required: false
        type: str
        default: 'present'
        choices:
            - 'present'
            - 'absent'
    discovery_type:
        description:
            - Type of discovery for managed host.
            - Required if I(state=present).
        required: false
        type: str
        choices:
            - redfish
            - ipmi
            - agentless
            - agent_managed
    bmc_hostname:
        description:
            - IP Address or domain name for host to manage.
        required: true
        type: str
    bmc_user:
        description: Defines the user account to access BMC.
        required: false
        type: str
    bmc_password:
        description: Defines the password to access BMC.
        required: false
        type: str
    override:
        description:
            - Forces the Discovery API to override attributes of the discovered hosts.
            - Formatted as a single string, comma separated with format "<Attribute1>,<Value1>,<Attribute2>,<Value2>…"
            - e.g. I(override="check_interval,300,max_check_attempts,5")
            - 'Three attributes may be overridden: check_interval, retry_interval, max_check_attempts.'
            - 'More attributes are available to override if NM-enabled hosts are discovered I(detect_nm="true"):
                derated_ac_power, derated_dc_power, max_ps_output.'
        required: false
        type: str
    detect_nm:
        description: Directs the Discovery API to check if NM (Intel® Intelligent Power Node Manager) is installed on the discovered hosts.
        required: false
        type: str
        choices:
            - "true"
            - "false"
    clearPolicy:
        description: Forces the Discovery API to clear all existing policies on the NM of the discovered hosts.
        required: false
        type: str
        choices:
            - "true"
            - "false"
extends_documentation_fragment:
    - jeisenbath.supermicro.ssm_auth_options
requirements:
    - requests
'''

EXAMPLES = r'''
- name: Add a redfish host to SSM
  jeisenbath.supermicro.ssm_host:
    ssm_hostname: "{{ ssm_hostname }}"
    username: "{{ ssm_username }}"
    password: "{{ ssm_password }}"
    force_basic_auth: "true"
    bmc_hostname: "{{ bmc_hostname }}"
    state: present
    discovery_type: redfish
    bmc_user: "{{ bmc_user }}"
    bmc_password: "{{ bmc_password }}"
  delegate_to: localhost
'''

RETURN = r'''
host:
    description: Returned data from API request.
    returned: always
    type: dict
    sample: {
        "Address": "",
        "CurrentCheckAttempt": 1,
        "Description": "Firmware: ASPEED",
        "HostOID": 100,
        "IpmiAddress": "",
        "IpmiMacAddress": "",
        "LastCheck": "",
        "LastStateChange": "",
        "MaxCheckAttempts": 3,
        "Name": "",
        "ServiceAllInOneStatus": "",
        "ServiceAllInOneStatusCode": 1,
        "StateType": "",
        "Status": "",
        "StatusCode": 0,
        "StatusInformation": "",
        "Type": ""
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.jeisenbath.supermicro.plugins.module_utils.ssm import ssm_argument_spec
from ansible_collections.jeisenbath.supermicro.plugins.module_utils.hosts import Hosts


def main():
    argument_spec = ssm_argument_spec()
    argument_spec.update(
        state=dict(required=False, choices=['present', 'absent'], default='present', type='str'),
        discovery_type=dict(required=False, choices=['redfish', 'ipmi', 'agentless', 'agent_managed'], type='str'),
        bmc_hostname=dict(required=True, type='str'),
        bmc_user=dict(required=False, type='str'),
        bmc_password=dict(required=False, no_log=True, type='str'),
        override=dict(required=False, type='str'),
        detect_nm=dict(required=False, choices=['true', 'false'], type='str'),
        clearPolicy=dict(required=False, choices=['true', 'false'], type='str'),
    )
    module = AnsibleModule(
        argument_spec,
        supports_check_mode=True,
        required_if=[
            ('state', 'present', ['discovery_type', 'bmc_hostname']),
            ('discovery_type', 'redfish', ['bmc_user']),
        ]
    )

    changed = False
    getHost = {}
    try:
        ssmHosts = Hosts(
            module.params['ssm_hostname'],
            module.params['username'],
            module.params['password'],
            module.params['force_basic_auth'],
            module.params['ssm_https_port']
        )
        rc, hostList = ssmHosts.get_hosts()
        getHost = ssmHosts.get_host(hostList, module.params['bmc_hostname'])
    except Exception:
        module.fail_json(msg=f'Failed to connect to SSM API: Exception{str(Exception)}')
    if module.params['state'] == 'present':
        try:
            if not getHost:
                if not module.check_mode:
                    if module.params['discovery_type'] == 'redfish':
                        rc, data = ssmHosts.discover_redfish(
                            searchRange=module.params['bmc_hostname'],
                            bmcId=module.params['bmc_user'],
                            bmcPassword=module.params['bmc_password'],
                            override=module.params['override'],
                            detectNm=module.params['detect_nm'],
                            useDnsName='true',
                        )
                    rc, hostList = ssmHosts.get_hosts()
                    getHost = ssmHosts.get_host(hostList, module.params['bmc_hostname'])
                changed = True
        except Exception as e:
            module.fail_json(msg=f'Failed to add host. Exception: {e}')
    elif module.params['state'] == 'absent':
        try:
            if getHost:
                if not module.check_mode:
                    rc, data = ssmHosts.remove_host(getHost['HostOID'])
                changed = True
        except Exception as e:
            module.fail_json(msg=f'Failed to remove host. Exception: {e}')

    module.exit_json(changed=changed, host=getHost)


if __name__ == '__main__':
    main()
