import pytest
from django.test import TestCase

# Create your tests here.
import requests


class Testcase:
    def setup_class(self):
        self.url = "http://127.0.0.1:8000/" + "testcase/"
        self.test_get_testcaselist_url = "http://127.0.0.1:6324/testcaselist"

    def test_get_testcaselist(self):
        r = requests.get(url=self.url)
        print(r.text)
        assert r.status_code == 200

    def test_get_testcase(self):
        r = requests.get(url=self.url, params={'id': 4})
        print(r.text)
        assert r.status_code == 200

    @pytest.mark.parametrize("nodeID", (['nodeID001', 'nodeID002', 'nodeID003', 'nodeID005']))
    def test_post(self, nodeID):
        data = {"nodeID": nodeID, 'remark': "今天天气真热！"}
        r = requests.post(url=self.url, data=data)
        print(r.text)

    def test_post2(self, ):
        data = {
            'params':
                {
                    "nodeID": 'nodeID123',
                    'remark': "今天天气真热！"
                }
        }
        r = requests.post(url=self.url, json=data)
        print(r.text)

    def test_put(self):
        data = {
            'id': '5',
            "nodeID": 'nodeID003',
            'remark': "修改了今天天气真l！",
            'priority':1,
            'status':1,
            'author':'zyy'
        }
        r = requests.put(url=self.url, json=data)
        print(r.text)

    def test_delete(self):
        data = {"nodeID": 'nodeID005'}
        data2 = {"id": '4'}
        r = requests.delete(url=self.url, params=data2)
        print(r.text)
