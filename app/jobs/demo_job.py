import datetime
import logging


def demo_blocking_job():
    logging.info('[demo_blocking_job] running at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


async def demo_asyncio_job():
    logging.info('[demo_asyncio_job] running at ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
