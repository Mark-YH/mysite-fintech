from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import connection
import fintech.QTS_SMA as SMA
import json


def get_stock_list(request):
    if request.method == 'GET':
        try:
            cursor = connection.cursor()
            sql = ("select `Symbol` from Fintech.Stocks")
            cursor.execute(sql)
            stocks = []
            for items in cursor.fetchall():
                stocks.append(items[0])
            return JsonResponse({'stock list': stocks})
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'database connection error'})
        return JsonResponse({'status': 'ok'})

    return JsonResponse({'status': 'fail'})


@require_http_methods(["POST"])
def recommend_sma(request):
    symbol = 'CSCO'
    body = json.loads(request.body)
    stock_data = get_stock_price(symbol, body['start'], body['end'])

    return JsonResponse(SMA.QTS(stock_data['price']))


def get_stock_price(symbol, start, end):
    try:
        cursor = connection.cursor()
        sql = ("select `Date`, `Adj Close` from Fintech.{} where `Date` between '{}' and '{}'") \
            .format(symbol, start, end)
        print(sql)
        cursor.execute(sql)
        data = {'date': [], 'price': []}
        for items in cursor.fetchall():
            date, price = items
            data['date'].append(date)
            data['price'].append(price)
        sql = ("select `Date`, `Adj Close` from Fintech.{} where `Date` < '{}' ORDER BY `Date` DESC limit 256") \
            .format(symbol, start)
        print(sql)
        cursor.execute(sql)
        data_training = {'date': [], 'price': []}
        for items in cursor.fetchall():
            date, price = items
            data_training['date'].append(date)
            data_training['price'].append(price)
        data_training['date'].reverse()
        data_training['price'].reverse()

        data_training['date'].extend(data['date'])
        data_training['price'].extend(data['price'])
        return data_training
    except Exception as e:
        return e


@require_http_methods(["POST"])
def custom(request):
    print(1)
    symbol = 'CSCO'
    try:
        print(request.body)
        body = json.loads(request.body)
    except Exception as e:
        print(e)
    stock_data = get_stock_price(symbol, body['start'], body['end'])
    print(3)
    strategy = {'buy1': body['buy1'], 'buy2': body['buy2'], 'sell1': body['sell1'], 'sell2': body['sell2']}
    print(4)
    holding_period, profit = SMA.fitness(stock_data['price'],
                                         [body['buy1'], body['buy2'], body['sell1'], body['sell2']])
    print(5)
    context = {'stock price': stock_data['price'][256:], 'holding period': holding_period, 'profit': profit,
               'strategy': strategy}
    return JsonResponse(context)
