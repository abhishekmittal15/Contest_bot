import asyncio

async def g(message):
    print(message)

async def f(message):
    await g(message)

asyncio.run(f("Hey"))
print("Bye")
