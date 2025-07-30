# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import time
try:
    import requests
    HAS_REQUESTS = True
    requests.packages.urllib3.disable_warnings()
except ImportError:
    HAS_REQUESTS = False
except Exception:
    raise Exception
from ansible_collections.jeisenbath.supermicro.plugins.module_utils.ssm import SSM
# from plugins.module_utils.ssm import SSM


class Hosts(SSM):
    def __init__(self, ssm_hostname: str, username: str, password: str, force_basic_auth: bool = False, ssm_https_port: str = '8443'):
        super().__init__(ssm_hostname, username, password, force_basic_auth, ssm_https_port)

    def discover_redfish(self, searchRange: str, bmcPassword: str,
                         override: str = None, bmcId: str = None, detectNm: str = None,
                         clearPolicy: str = None, useDnsName: str = None):

        data = {'search_range': searchRange, 'bmc_password': bmcPassword}
        if override:
            data['override'] = f'override={override}'
        if bmcId:
            data['bmc_id'] = bmcId
        if detectNm:
            data['detect_nm'] = detectNm
        if clearPolicy:
            data['clear_policy'] = clearPolicy
        if useDnsName:
            data['use_dns_name'] = useDnsName
        while True:
            timeout = 60
            sleepWait = 1
            totalWait = 0
            if self.force_basic_auth:
                resp = requests.post(
                    f'{self.apiUrl}/hosts/discovery/redfish',
                    auth=(self.username, self.password),
                    headers=self.headers,
                    data=data,
                    verify=False)
            else:
                resp = resp = requests.post(
                    f'{self.apiUrl}/hosts',
                    headers=self.headers,
                    data=data,
                    verify=False)
            if json.loads(resp.text):
                break
            elif totalWait >= timeout:
                break
            else:
                totalWait = totalWait + sleepWait
                time.sleep(sleepWait)
        respJson = json.loads(resp.text)
        while True:
            timeout = 60
            sleepWait = 1
            totalWait = 0
            taskRc, taskResp = self.get_task(respJson['Data']['TaskID'])
            if taskResp['Status'] != 'RUNNING':
                break
            elif totalWait >= timeout:
                break
            else:
                totalWait = totalWait + sleepWait
                time.sleep(sleepWait)

        return taskRc, taskResp
    
    def remove_host(self, hostOid):
        while True:
            timeout = 60
            sleepWait = 1
            totalWait = 0
            if self.force_basic_auth:
                resp = requests.delete(
                    f'{self.apiUrl}/hosts/{hostOid}',
                    auth=(self.username, self.password),
                    headers=self.headers,
                    verify=False)
            else:
                resp = requests.delete(
                    f'{self.apiUrl}/hosts/{hostOid}',
                    headers=self.headers,
                    verify=False)
            if json.loads(resp.text):
                break
            elif totalWait >= timeout:
                break
            else:
                totalWait = totalWait + sleepWait
                time.sleep(sleepWait)
        respJson = json.loads(resp.text)
        return respJson['Code'], respJson['Data']
        #while True:
        #    timeout = 120
        #    sleepWait = 3
        #    totalWait = 0
        #    taskRc, taskResp = self.get_task(respJson['Data']['TaskID'])
        #    if taskResp['Status'] != 'RUNNING':
        #        break
        #    elif totalWait >= timeout:
        #        break
        #    else:
        #        totalWait = totalWait + sleepWait
        #        time.sleep(sleepWait)

        #return taskRc, taskResp
