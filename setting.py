ENVIRONMENTS = {
    'streaming': {
        'real': 'https://stream-fxtrade.oanda.com',
        'practice': 'https://stream-fxpractice.oanda.com',
        'sandbox': 'https://stream-sandbox.oanda.com'
    },
    'api': {
        'real': 'https://api-fxtrade.oanda.com',
        'practice': 'https://api-fxpractice.oanda.com',
        'sandbox': 'https://api-sandbox.oanda.com'
    }
}

DOMAIN = 'practice'
STREAM_DOMAIN = ENVIRONMENTS['streaming'][DOMAIN]
API_DOMAIN = ENVIRONMENTS['api'][DOMAIN]
ACCESS_TOKEN = '5b669c93c07fefe15aca3e93c488a218-66827942e84d879f3453111f7d524420'
ACCOUNT_ID = '101-011-13116840-007'
