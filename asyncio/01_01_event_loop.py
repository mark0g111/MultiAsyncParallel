import asyncio


async def tick():
    print('tick')
    await asyncio.sleep(1)
    print('tock')


async def main():
    await asyncio.gather(tick(), tick(), tick())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        print('coroutines have finished')
    finally:
        loop.close()
        print('loop is closed')
