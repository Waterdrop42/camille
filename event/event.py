"""
Event
-----
TickEvent：
SignalEvent：
OrderEvent：
"""


class Event:
    pass


class TickEvent(Event):
    def __init__(self, instrument, time, bid, ask):
        """
        初始化TickEvent

        Parameters
        ----------
        instrument: 外汇工具，e.g. GBP_USD
        time: 当前Tick的时间戳
        bid: 对应买价
        ask: 对应卖价
        """
        self.type = 'TICK'
        self.instrument = str(instrument)
        self.time = str(time)
        self.bid = str(bid)
        self.ask = str(ask)

    def __repr__(self):
        return 'Type: {}, Instrument: {}, Time: {}, Bid: {}, Ask: {}'.format(
            self.type, self.instrument, self.time, self.bid, self.ask
        )


class SignalEvent(Event):
    def __init__(self, instrument, time, order_type, side):  # TODO: time参数，
        """
        初始化SignalEvent

        Parameters
        ----------
        instrument: 外汇工具，e.g. GBP_USD
        time: 当前Tick的时间戳
        order_type: 下单类型。市价单：'MARKET'，限价单：'LIMIT'
        side：交易方向，'BUY' or 'SELL'
        """
        self.type = 'SIGNAL'
        self.instrument = str(instrument)
        self.time = str(time)
        self.order_type = str(order_type)
        self.side = str(side)

    def __repr__(self):
        return 'Type: {}, Instrument: {}, Time: {}, OrderType: {}, Side: {}'.format(
            self.type, self.instrument, self.time, self.order_type, self.side
        )


class OrderEvent(Event):
    def __init__(self, instrument, units, order_type):
        """
        初始化OrderEvent， TODO: 现在的API下单没有side参数了，在Portfolio中注意要改变方向

        Parameters
        ----------
        instrument: 外汇工具。e.g. GBP_USD
        units: 交易数量。若为正数，则为买入，若为负数，则为卖出
        order_type: 下单类型。市价单：'MARKET'，限价单：'LIMIT'
        """
        self.type = 'ORDER'
        self.instrument = str(instrument)
        self.units = str(units)
        self.order_type = str(order_type)

    def __repr__(self):
        return 'Type: {}, Instrument: {}, Units: {}, OrderType: {}'.format(
            self.type, self.instrument, self.units, self.order_type
        )




