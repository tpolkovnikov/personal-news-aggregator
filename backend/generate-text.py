from __future__ import annotations
from yandex_cloud_ml_sdk import YCloudML
import os
from dotenv import load_dotenv

messages = [
    {
        "role": "system",
        "text": "Найди ошибки в тексте и исправь их",
    },
    {
        "role": "user",
        "text": """Ламинат подойдет для укладке на кухне или в детской 
комнате – он не боиться влаги и механических повреждений благодаря 
защитному слою из облицованных меламиновых пленок толщиной 0,2 мм и 
обработанным воском замкам.""",
    },
]


def main():
    # Load environment variables from a .env file if present
    load_dotenv()

    folder_id = os.getenv("folderID")
    api_key = os.getenv("API")

    iam = os.getenv("iamToken")
    

    if not folder_id or not api_key:
        raise RuntimeError(
            "Missing required environment variables: idKey (folder_id) and secretKey (API key)."
        )

    sdk = YCloudML(
        folder_id=folder_id,
        #auth=api_key,
        auth=iam,
    )

    result = (
        sdk.models.completions("yandexgpt").configure(temperature=0.5).run(messages)
    )

    for alternative in result:
        print(alternative)


if __name__ == "__main__":
    main()
