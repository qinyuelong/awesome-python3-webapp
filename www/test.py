#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
from models import User, Blog, Comment
import asyncio




# def test():
#     yield from orm.create_pool(loop = loop, user='www-data', password='www-data', database='awesome')
#
#     u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
#
#     yield from u.save()
#
#
# for x in test():
#     pass
#



async def test(loop):
    await orm.create_pool(loop = loop, user='www-data', password='www-data', db='awesome')

    u = User(name='Test中文', email='test333@example.com', password='1234567890', image='about:blank')

    await u.save()
    # await orm.destory_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()