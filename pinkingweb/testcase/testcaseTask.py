# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 14:59
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : testcaseTask.py
# @Software: PyCharm
import pytest
import requests


class Testcase:
    def setup_class(self):
        self.url = "http://127.0.0.1:6324/"+"task/"

    def test_get_task(self):
        r = requests.get(url=self.url)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        data = {"remark": 'nodeID', 'report': "今天天气真热！"}
        r = requests.post(url=self.url, data=data)
        print(r.text)

    @pytest.mark.parametrize("nodeID", (['nodeID001', 'nodeID002', 'nodeID003', 'nodeID005']))
    def test_post1(self, nodeID):
        data = {"remark": nodeID, 'report': "今天天气真热！"}
        r = requests.post(url=self.url, data=data)
        print(r.text)