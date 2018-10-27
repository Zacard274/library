import redis

from config import REDIS


def get_redis():
    return redis.StrictRedis(host=REDIS['host'], port=REDIS['port'])


_redis = get_redis()
