#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2015 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2015-11-23
#

"""Run all scripts 10 times."""

from __future__ import print_function, unicode_literals, absolute_import

import os
import subprocess
import time

ITERATIONS = 10


def iter_scripts():
    """Yield active scripts."""
    dirpath = os.path.dirname(os.path.abspath(__file__))
    for name in os.listdir(dirpath):
        if name.startswith('active_') and name.endswith('.py'):
            yield os.path.join(dirpath, name)


def main():
    """Run benchmarks."""
    averages = {}
    for script in iter_scripts():

        name = os.path.splitext(os.path.basename(script))[0]
        cmd = [b'/usr/bin/python', script]
        times = []
        print(name)
        for i in range(ITERATIONS):
            s = time.time()
            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError as err:
                print('[ERROR] running "{}": {}'.format(name, err))
                continue
            d = time.time() - s
            times.append(d)
            print('[{:2d}/{:2d}] {:0.4f} secs'.format(i + 1, ITERATIONS, d))

        averages[name] = sum(times) / ITERATIONS

    averages = sorted([(v, k) for k, v in averages.items()])
    for d, n in averages:
        print('{:30s}{:0.4f} seconds average'.format(n, d))


if __name__ == '__main__':
    main()
