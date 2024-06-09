import os
import sys
import logging
import requests
import urllib
import urllib.request
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
from linebot.models import RichMenu, RichMenuArea, RichMenuBounds, RichMenuSize, URIAction
from linebot.models import CameraAction, CameraRollAction
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage, ImageSendMessage, VideoSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent, FlexSendMessage
)
from linebot.models.actions import PostbackAction

from linebot.exceptions import (LineBotApiError, InvalidSignatureError)
from sql import insert_json_chooseDuration, choose_duration, choose_priority, insert_hour_duration, confirm_task, \
    create_task, task_created
import pymysql.cursors

conn = pymysql.connect(host='tododbpy.c94g44mqus56.ap-northeast-1.rds.amazonaws.com',
                    user='admin',
                    password = '1qaz2wsx',
                    db='Tododb',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

# LINEBOTと接続するための記述
# 環境変数からLINEBotのチャンネルアクセストークンとシークレットを読み込む
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

# 無いならエラー
if channel_secret is None:
    logger.error('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    logger.error('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

# apiとhandlerの生成（チャンネルアクセストークンとシークレットを渡す）
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

shota_id = "U216e9f3bb4781422a3d3af51e0697dd3"


# Lambdaのメインの動作
def lambda_handler(event, context):
    print(event)
    # 認証用のx-line-signatureヘッダー
    signature = event["headers"]["x-line-signature"]
    body = event["body"]

    # リターン値の設定
    ok_json = {"isBase64Encoded": False,
               "statusCode": 200,
               "headers": {},
               "body": ""}
    error_json = {"isBase64Encoded": False,
                  "statusCode": 500,
                  "headers": {},
                  "body": "Error"}

    # 例外処理としての動作
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        logger.error("Got exception from LINE Messaging API: %s\n" % e.handle_message)
        for m in e.error.details:
            logger.error("  %s: %s" % (m.property, m.handle_message))
        return error_json
    except InvalidSignatureError:
        return error_json

    return ok_json


# 以下でWebhookから送られてきたイベントをどのように処理するかを記述する

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    send_message = event.message.text
    print(event)
    display_name = 'None'
    if isinstance(event.source, SourceUser):
        profile = line_bot_api.get_profile(event.source.user_id)
        user_id = event.source.user_id
        display_name = profile.display_name

    else:
        print("user profile can't not use")

    if send_message == "New Task" and isinstance(event.source, SourceUser):
        bubble_string = """{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "New Task",
            "weight": "bold",
            "color": "#555555",
            "align": "center",
            "size": "xl"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "height": "1px",
                "backgroundColor": "#aaaaaa",
                "offsetTop": "7px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "position": "absolute",
                "width": "0%",
                "height": "3px",
                "backgroundColor": "#aaaaaa",
                "offsetTop": "6px"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "14px",
                    "height": "14px",
                    "backgroundColor": "#08C656",
                    "cornerRadius": "7px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "width": "10px",
                    "height": "10px",
                    "backgroundColor": "#aaaaaa",
                    "cornerRadius": "5px"
                  }
                ],
                "position": "absolute",
                "width": "100%",
                "justifyContent": "space-between",
                "alignItems": "center"
              }
            ],
            "height": "14px"
          },
          {
            "type": "separator"
          }
        ],
        "spacing": "lg"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Type task before title yours",
            "size": "xl",
            "color": "#555555"
          },
          {
            "type": "text",
            "text": "Ex) Task learn SQL",
            "color": "#aaaaaa"
          }
        ],
        "spacing": "md"
      }
    ],
    "spacing": "xl"
  }
}
"""
        message = FlexSendMessage(alt_text="Type Your Task", contents=json.loads(bubble_string))
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif send_message[:len("Task ")] == "Task " and isinstance(event.source, SourceUser):
        #ex) send_message = "Task learn SQL"
        user_task = send_message.replace("Task ","")
        #user_task = "learn SQL"
        if user_task.isalpha():
            bubble = insert_json_chooseDuration(user_task)
        message = FlexSendMessage(alt_text="Type Your Task", contents= bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )

@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data[-len("Duration + Date"):] == 'Duration + Date':
        line_bot_api.reply_message(
            event.reply_token,
            (TextSendMessage(text='Duration + Date'))
        )
    elif event.postback.data[-len("Duration"):] == 'Duration':
        data_list = event.postback.data.split(",")
        title = data_list[0]
        bubble =  insert_hour_duration(title)
        message = FlexSendMessage(alt_text="Choose Minutes", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif event.postback.data[-len("Duration + Date"):] == 'Start + End':
        line_bot_api.reply_message(
            event.reply_token,
            (TextSendMessage(text='Start + End'))
        )
    elif event.postback.data[-len(" hour"):] == " hour":
        dataList = event.postback.data.split(",")
        name = dataList[0]
        hour_duraiton = dataList[1].replace(" hour", "")
        # hour_duration = 1 or other seleciton.
        if hour_duraiton.isdigit():
            bubble = choose_duration(name, hour_duraiton)

            message = FlexSendMessage(alt_text="Choose Minutes", contents=bubble)
            line_bot_api.reply_message(
                event.reply_token,
                message
            )
    elif event.postback.data[-len(" mins"):] == " mins":
        dataList = event.postback.data.split(",")
        name = dataList[0]
        hour_duraiton = dataList[1].replace(" hour", "")
        minutes_duraiton = dataList[2].replace(" mins", "")
        # hour_duration = 1 or other seleciton.
        if hour_duraiton.isdigit():
            bubble = choose_priority(name, hour_duraiton,minutes_duraiton)

            message = FlexSendMessage(alt_text="Choose your priority", contents=bubble)
            line_bot_api.reply_message(
                event.reply_token,
                message
            )

    elif event.postback.data[:len("[INSERT]")] == "[INSERT]":
        dataList = event.postback.data.split(",")
        name = dataList[0].replace("[INSERT]","")
        hour_duraiton = dataList[1].replace(" hour", "")
        minutes_duraiton = dataList[2].replace(" mins", "")
        priority = dataList[3]

        bubble = confirm_task(name, hour_duraiton,minutes_duraiton,priority)

        message = FlexSendMessage(alt_text="Confirm Task", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif event.postback.data[:len("[confirmed]")] == "[confirmed]":
        dataList = event.postback.data.split(",")
        name = dataList[0].replace("[confirmed]","")
        hour_duraiton = dataList[1].replace(" hour", "")
        minutes_duraiton = dataList[2].replace(" mins", "")
        priority = dataList[3]

        bubble = task_created(name, hour_duraiton, minutes_duraiton, priority)

        create_task(conn,name,hour_duraiton,minutes_duraiton,priority,event.source.user_id)

        line_bot_api.reply_message(
            event.reply_token,
            (TextSendMessage(text='Task confirmed'))
        )

    elif event.postback.data[:len("[View Task]")] == "[View Task]":
        dataList = event.postback.data.split(",")
        name = dataList[0].replace("[View Task]", "")
        hour_duraiton = dataList[1].replace(" hour", "")
        minutes_duraiton = dataList[2].replace(" mins", "")
        priority = dataList[3]

        bubble = task_created(name, hour_duraiton, minutes_duraiton, priority)

        line_bot_api.reply_message(
            event.reply_token,
            (TextSendMessage(text='View Task'))
        )


@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='登録して頂きありがとうごいます！Boost Your To-DayのLINE公式アカウントです。\n\n下記Menuから今日のドリンクメニューやクーポン、お問い合わせ、ホームページのリンクがご確認頂けます。\n\n自動会話botと連携しており、チャットで話しかけると返答が返ってきます。\n\nぜひご活用頂ければ幸いです。'))
