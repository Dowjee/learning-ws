import asyncio, websockets

async def echo(ws):
    async for msg in ws:
        await ws.send(f"echo: {msg}")


async def main():
    async with websockets.serve(echo,"0.0.0.0",8765):
        await asyncio.Future()

asyncio.run(main())