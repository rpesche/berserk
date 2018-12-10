# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timezone


def to_millis(dt):
    return dt.timestamp() * 1000


def datetime_from_seconds(ts):
    return datetime.fromtimestamp(ts, timezone.utc)


def datetime_from_millis(millis):
    return datetime_from_seconds(millis / 1000)


def inner_datetime_fromtimestamp(*keys):
    def convert(data):
        for k in keys:
            data[k] = datetime_from_seconds(data[k])
        return data
    return convert


def noop(arg):
    return arg
