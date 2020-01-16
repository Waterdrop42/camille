"""
data的抽象类
"""


from abc import ABC, abstractmethod


class DataHandler(ABC):
    """
    DataHandler是一个抽象基类，给所有继承DataHandler子类提供接口（包括历史回测和实盘交易）

    提供这样一个抽象基类的目的在于使得每一个继承此基类的子类都输出同样格式的"tick"数据，并将
    这些数据传入事件队列
    """
    def _set_up_prices_dict(self):
        prices_dict = dict(
            [(p, {'bid': None, 'ask': None, 'time': None}) for p in self.pairs]
        )
        inv_price_dict = dict(
            [('%s_%s' % (p[-3:], p[:3]), {'bid': None, 'ask': None, 'time': None}) for p in self.pairs]
        )
