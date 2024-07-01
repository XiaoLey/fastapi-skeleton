import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from app.jobs.demo_job import demo_blocking_job, demo_asyncio_job


def create_blocking_scheduler() -> BlockingScheduler:
    logging.info("BlockingScheduler initializing")
    scheduler: BlockingScheduler = BlockingScheduler()
    register_blocking_jobs(scheduler)
    return scheduler


def create_asyncio_scheduler() -> AsyncIOScheduler:
    logging.info("AsyncIOScheduler initializing")
    scheduler: AsyncIOScheduler = AsyncIOScheduler()
    register_asyncio_jobs(scheduler)
    return scheduler


def register_blocking_jobs(scheduler: BlockingScheduler):
    """
     Register blocking jobs
    """
    scheduler.add_job(demo_blocking_job, trigger='interval', seconds=5)


def register_asyncio_jobs(scheduler: AsyncIOScheduler):
    """
     Register asyncio jobs
    """
    scheduler.add_job(demo_asyncio_job, trigger='interval', seconds=5)
