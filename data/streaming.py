"""
连接oanda经纪商，产生流式数据
"""


import requests
import json

from camille.event.event import TickEvent


class StreamingForexPrices:
    def __init__(self, domain, access_token, accountID, pairs, events_queue):  # TODO: pairs 和 instrument
        """
        初始化流式数据生成器

        Parameters
        ----------
        domain: API的接口选择，分为practice账户和real-live账户
        access_token: oanda要求的authorization token
        accountID: 账户ID
        pairs: 指定货币pairs，工具
        events_queue: 事件队列
        """
        self.domain = domain
        self.access_token = access_token
        self.accountId = accountID
        self.pairs = pairs
        self.events_queue = events_queue

    def __