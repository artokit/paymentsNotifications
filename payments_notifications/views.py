from django.http import JsonResponse
from django.shortcuts import render
import telebot
import json
from django.views.decorators.csrf import csrf_exempt
import hashlib
from django.shortcuts import redirect

TOKEN = '6797138607:AAGsgLq0i3j3i2zpoPhKX5UzJopSCWDdrk4'
POSTBACK_ID = -1002011453442

bot = telebot.TeleBot(TOKEN, parse_mode=None)

import logging

logging.basicConfig(
    filename="/home/c/cq29540/eqwr/public_html/paymentsNotifications/payments_notifications/logs.log",
    format='[%(asctime)s] | %(levelname)s | %(message)s',
    filemode='a',
    level=logging.INFO
)
# logging.FATAL

logger = logging.getLogger('Telegram Bot')


@csrf_exempt
def index(request):
    # bot.send_message(POSTBACK_ID, str(request.GET))
    # bot.send_message(POSTBACK_ID, request.dict())
    d = request.POST.dict()
    logging.info(d)
    s = f'{d["notification_type"]}&{d["operation_id"]}&{d["amount"]}&{d["currency"]}&{d["datetime"]}&{d["sender"]}&{d["codepro"]}&aXY53ygxstezC8olKmJSnUDs&{d["label"]}'
    h = hashlib.sha1(s.encode()).hexdigest()
    # bot.send_message(POSTBACK_ID, str(d))
    # if h == d['sha1_hash']:
    bot.send_message(POSTBACK_ID, f'yoomoney:{d["label"]}:{d["amount"]}')
    #for i in request.POST:
    #    bot.send_message(POSTBACK_ID, i)
    # bot.send_message(POSTBACK_ID, "t")
    return JsonResponse({'message': 'success'})


@csrf_exempt
def crypt_payment(request):
    d = json.loads(request.body.decode())
    if d['status'] in ('paid', 'paid_over'):
        bot.send_message(POSTBACK_ID, f'cryptomus:{d["order_id"]}:{d["amount"]}')
    # bot.send_message(POSTBACK_ID, request.body)
    return JsonResponse({'message': "success"})


@csrf_exempt
def paypal(request):
    logging.info(request.GET)
    bot.send_message(POSTBACK_ID, f'paypal:{request.GET["token"]}:{request.GET["paymentId"]}:{request.GET["PayerID"]}')
    return redirect('https://t.me/test_cryptomus_bot')
