# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
from ansible.module_utils.basic import env_fallback

try:
    import requests
    HAS_REQUESTS = True
    requests.packages.urllib3.disable_warnings()
except ImportError:
    HAS_REQUESTS = False
except Exception:
    raise Exception


def ssm_argument_spec():
    return dict(
        ssm_hostname=dict(fallback=(env_fallback, ['SSM_HOSTNAME']), required=False, type='str'),
        ssm_https_port=dict(required=False, default='8443', type='str'),
        username=dict(fallback=(env_fallback, ['SSM_USERNAME']), required=False, type='str'),
        password=dict(fallback=(env_fallback, ['SSM_PASSWORD']), required=False, type='str', no_log=True),
        force_basic_auth=dict(required=False, default=False, type='bool'),
    )


class SSM:

    def __init__(self, ssm_hostname: str, username: str, password: str, force_basic_auth: bool = False, ssm_https_port: str = '8443'):
        self.ssm_hostname = ssm_hostname
        self.ssm_https_port = ssm_https_port
        self.force_basic_auth = force_basic_auth
        self.apiUrl = f'https://{self.ssm_hostname}:{self.ssm_https_port}/SSMWeb/api'
        self.username = username
        self.password = password
        try:
            if not force_basic_auth:
                self.token = self.get_auth_token()
                self.headers = {'Authorization': f'Bearer {self.token}', 'Accept': 'application/json'}
                apiResp = requests.get(f'{self.apiUrl}', headers=self.headers, verify=False)
            else:
                self.headers = {'Accept': 'application/json'}
                apiResp = requests.get(f'{self.apiUrl}', auth=(self.username, self.password), headers=self.headers, verify=False)
            respJson = json.loads(apiResp.text)
            if respJson['Code'] != 200:
                raise Exception(f'HTTP {respJson["Code"]}: API url is not reachable.')
            _testAuthCode, _testAuthResp = self.get_hosts()
            if _testAuthCode != 200:
                raise Exception(f'HTTP {_testAuthCode}: Authorization failed.')
        except Exception:
            raise Exception

    def get_auth_token(self):
        oauthUrl = f'{self.apiUrl}/oauth/token'
        oauthData = {'grant_type': 'client_credentials'}
        oauthDataJson = json.dumps(oauthData)
        response = requests.post(oauthUrl, auth=(self.username, self.password), data=oauthDataJson, verify=False)
        responseJson = json.loads(response.text)
        if responseJson['Code'] == 401:
            raise Exception("Unauthorized")

        oauthToken = responseJson['access_token']
        return oauthToken

    def get_hosts(self):
        if self.force_basic_auth:
            resp = requests.get(f'{self.apiUrl}/hosts', auth=(self.username, self.password), headers=self.headers, verify=False)
        else:
            resp = requests.get(f'{self.apiUrl}/hosts', headers=self.headers, verify=False)
        respJson = json.loads(resp.text)

        return respJson['Code'], respJson['Data']
    
    def get_host(self, hosts, hostname):
        for host in hosts:
            if host['Name'] == hostname:
                return host
    
    def get_task(self, taskId):
        if self.force_basic_auth:
            resp = requests.get(f'{self.apiUrl}/tasks/{taskId}', auth=(self.username, self.password), headers=self.headers, verify=False)
        else:
            resp = requests.get(f'{self.apiUrl}/tasks/{taskId}', headers=self.headers, verify=False)
        respJson = json.loads(resp.text)

        return respJson['Code'], respJson['Data']
