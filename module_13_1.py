import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    balls = 5
    for i in range(balls):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i+1} шар.')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman("Guts", 5))
    task2 = asyncio.create_task(start_strongman("Maito Gai", 4))
    task3 = asyncio.create_task(start_strongman("Levi", 3))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
