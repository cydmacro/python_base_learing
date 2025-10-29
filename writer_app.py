import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.ai_writer import AIWriter
import json


app = FastAPI()

ai_writer = AIWriter()


async def stream_response(query: str):
    async for chunk in ai_writer.run_stream(query):
        json_data = json.dumps({"text":chunk},ensure_ascii=False)
        yield f"data: {json_data}\n\n"



@app.get("/ai_writer")
async def ai_writer_stream(query: str):
   return StreamingResponse(
       stream_response(query), 
       media_type="text/event-stream",
       headers={"Access-Control-Allow-Origin": "*"}
       )

   
if __name__ == "__main__":
    uvicorn.run(app, port=8000)