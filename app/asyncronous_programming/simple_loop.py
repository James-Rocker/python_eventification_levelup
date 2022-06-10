import asyncio

# A future is something that has no yet been done
# Asyncio has an AbstractEventLoop class where we can pass methods with the future as an argument
# e.g. has it run forever, run until complete, stop etc


async def task_ex(n):
   print("Processing {}".format(n))


async def generator_task():
   for i in range(10):
      asyncio.ensure_future(task_ex(i))  # wraps the routine in a future for the ensure_future function
   print("Tasks Completed")

loop = asyncio.get_event_loop()
loop.run_until_complete(generator_task())  # runs until a future is complete, regardless of what that future is
loop.close()

# question, is there a way to verify the future object?
