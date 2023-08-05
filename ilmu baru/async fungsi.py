'''
penggunaan asyncio di gunakan untuk mengeksekusi perinyah sebelum penggunaan wait
'''

import asyncio


async def count():
    print("One")
    print(2)
    for i in range(10):
        print(i)
    await asyncio.sleep(2)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
