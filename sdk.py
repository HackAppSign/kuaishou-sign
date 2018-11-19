#! -*- coding:utf-8 -*-
import os
import sys

class AbstractSign(object):
    def work(self, url, payload):
        pass
    
class OnlineKuaishouSign(AbstractSign):
    def work(self, url, payload):
        pass
   
class OfflineKuaishouSign(AbstractSign):
    def work(self, url, payload):
        pass

class KuaishouSdk(object):
    def __init__(self, signer):
        self.signer = signer
    
    def feed_hot(self):
        pass
    
    def feed_nearby(self, lat, lon):
        pass
    
    def list_reply(self, id):
        pass
    
    def like(self, id):
        pass
    
    def reply(self, content):
        pass
    
    def download(self, id):
        pass
    
if __name__ == '__main__':
    ks = KuaishouSdk(OnlineKuaishouSign())
    
