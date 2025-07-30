# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r"""
options:
    ssm_hostname:
        description:
          - Hostname or IP Address of the Supermicro Server Manager.
          - If not defined in the task, the value of E(SSM_HOSTNAME) will be used instead.
        required: false
        type: str
    username:
        description:
          - The username to authenticate with to the Supermicro Server Manager web API.
          - If not defined in the task, the value of E(SSM_USERNAME) will be used instead.
        required: false
        type: str
    password:
        description:
          - The password to authenticate with to the Supermicro Server Manager web API.
          - If not defined in the task, the value of E(SSM_PASSWORD) will be used instead.
        required: false
        type: str
    force_basic_auth:
        description:
            - Whether or not to use basic auth instead of OAUTH.
        required: false
        type: bool
        default: False
    ssm_https_port:
        description:
            - The port on which the SSM API is listening on.
        required: false
        type: str
        default: '8443'
"""
