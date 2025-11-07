from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import time
import asyncio
import base64
from openai import OpenAI

app = FastAPI()

client = OpenAI(
    api_key = "api_key" #cannot show
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/get_openai")
async def get_openai(file: UploadFile = File(...)):
    image_data = await file.read()
    base64_image = base64.b64encode(image_data).decode("utf-8")
    start = time.time()
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "照片內匡起來的號誌是什麼，直接跟我講答案就好。"
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jepg;base64,{base64_image}"}
                    }
                ],
            }
        ]
    )
    print("open ai費時：", time.time()-start)
    return response.choices[0].message.content