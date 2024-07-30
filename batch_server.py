"""
Batch Processing Server

This server uses Starlette to handle incoming batch data and performs sentiment analysis using Hugging Face Transformers.

Usage:
  - Start serve with uvicorn batch_server:app

Example usage: 
    
    curl -X POST -H "Content-Type: application/json" -d '[{"text": "Stocks rallied and the British pound gained."}, {"text": "The economy showed significant growth."}, {"text": "Investors are optimistic about the market."}]' http://localhost:8000/

Example result: [{"label":"positive","score":0.898361325263977},{"label":"positive","score":0.948479950428009},{"label":"positive","score":0.6735053658485413}]

"""

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from transformers import pipeline
import asyncio

async def sentiment_analyzer(request):
    """
    Handle incoming stream data and perform sentiment analysis.

    Args:
        request (starlette.requests.Request): The incoming request object.

    Returns:
        JSONResponse: The response containing sentiment analysis results.
    """
    payload = await request.json()
    string = [item['text'] for item in payload]
    response_q = asyncio.Queue()
    await request.app.model_queue.put((string, response_q))
    # Collect all the outputs from the response queue
    outputs = []
    for _ in range(len(string)):
        output = await response_q.get()
        outputs.append(output)
    
    return JSONResponse(outputs)

async def server_loop(q):
    """
    Process the queue of items (texts) and perform sentiment analysis.

    Args:
        q (asyncio.Queue): The queue containing the items to process.
    """
    pipe = pipeline("sentiment-analysis", model='ProsusAI/finbert')
    while True:
        (texts, rq) = await q.get()
        outs = pipe(texts, truncation=True, max_length=512)
        for rq, out in zip([rq]*len(texts), outs):
            await rq.put(out)
        q.task_done()

app = Starlette(
    routes=[
        Route("/", sentiment_analyzer, methods=["POST"]),
    ],
)

@app.on_event("startup")
async def startup_event():
    """
    Set up the queue and start the background processing loop.
    """
    q = asyncio.Queue()
    app.model_queue = q
    asyncio.create_task(server_loop(q))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)