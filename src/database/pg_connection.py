from os.path import join, dirname
import ssl

import asyncpg


def get_ssl_ctx():
    ctx = ssl.create_default_context(cafile='')
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    return ctx


async def get_pool(db_url: str, setup=True, *args, **kwargs):
    """A wrapper function for asyncpg.create_pool"""
    pool = await asyncpg.create_pool(db_url, *args, **kwargs)
    if setup:
        await setup_db(pool)

    return pool


async def setup_db(pool):

    with open(join(dirname(__file__), 'setup_pg_database.sql'), 'r') as f:
        sql_query = f.read()

    async with pool.acquire() as conn:
        await conn.execute(sql_query)
