# created by Chris Jackson as a test

import asyncio
import random


async def coroutine(id):

    process_time = random.randint(1, 5)

    print('starting task number {}'.format(id))

    await asyncio.sleep(process_time)

    print('task number: {}, process time: {}'.format(id, process_time))


async def main():
    tasks = []

    task_list = [1, 2, 3, 4, 5]

    for i in task_list:
        tasks.append(asyncio.ensure_future(coroutine(i)))

    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
