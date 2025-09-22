from fastapi import APIRouter, HTTPException, Request
import os
import requests

router = APIRouter()

YANDEX_GPT_API_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
IAM_TOKEN = os.getenv("iamToken")
FOLDER_ID = os.getenv("FOLDER_ID")  # Укажите ваш folder_id в .env

@router.post("/gpt/send_message")
async def send_message(request: Request):
    """
    Эндпоинт для отправки сообщения в Yandex GPT и получения ответа.
    Ожидает JSON с ключом 'message'.
    """
    data = await request.json()
    message = data.get("message")
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    headers = {
        "Authorization": f"Bearer {IAM_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt/latest",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": 100
        },
        "messages": [
            {"role": "user", "text": message}
        ]
    }

    response = requests.post(YANDEX_GPT_API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    result = response.json()
    return {"result": result}
