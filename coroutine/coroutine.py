import asyncio
import time


class CustomAwaitable:
    def __init__(self):
        pass

    def __await__(self):
        print("I'm doing a heavy IO wait.")
        return self._await_impl().__await__()
    
    async def _await_impl(self):
        await asyncio.sleep(5)
        return "coroutine done."

async def my_coroutine():
    print("Hello python coroutine module!")

    awaitable = CustomAwaitable()
    result = await awaitable
    print(result)

async def my_for_loop():
    for i in range(10):
        await asyncio.sleep(1)  # 使用 asyncio.sleep 替代 time.sleep
        print(i)

async def main():
    # 并发运行 my_coroutine 和 my_for_loop
    # await 一般等待需要IO(从网络，磁盘中读取数据)的函数
    await asyncio.gather(my_coroutine(), my_for_loop())

# asyncio.run 阻塞调用
asyncio.run(main())

print("all coroutine done.")
