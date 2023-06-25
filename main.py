from fastapi import FastAPI, Depends, Request, HTTPException
from pydantic import BaseModel
from typing import List
from linebot import ( LineBotApi, WebhookHandler, WebhookParser)
from linebot.models import ( MessageEvent, ImageMessage, TextMessage, TextSendMessage,)
from linebot.exceptions import (InvalidSignatureError)
import os

app = FastAPI()

CHANNEL_SECRET = os.environ["CHANNEL_SECRET"]
CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# リクエストのデータ構造を定義
class LineWebhook(BaseModel):
    destination: str
    events: List[dict]

@app.post("/callback/")
async def callback(webhook_data: LineWebhook):
    # Webhookイベントの信憑性を確認
    for event in webhook_data.events:
        if event["type"] == "message":
            if event["message"]["type"] == "image":
                line_bot_api.reply_message(
                    event["replyToken"],
                    TextSendMessage(text="画像を受け取りました"))
            elif event["message"]["type"] == "text":
                line_bot_api.reply_message(
                    event["replyToken"],
                    TextSendMessage(text=event["message"]["text"]))

    # 動作した際は200レスポンスを返す
    return {"status": "OK"}