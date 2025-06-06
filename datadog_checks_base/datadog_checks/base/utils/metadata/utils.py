# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)


def is_primitive(obj):
    # https://github.com/python/cpython/blob/4f82a53c5d34df00bf2d563c2417f5e2638d1004/Lib/json/encoder.py#L357-L377
    return obj is None or isinstance(obj, (bytes, bool, float, int, str))
