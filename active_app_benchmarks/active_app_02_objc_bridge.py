#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2015 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2015-11-23
#

"""Get app info with AppKit via objc bridge."""

from __future__ import print_function, unicode_literals, absolute_import

import time
import unicodedata

from AppKit import NSWorkspace


def decode(s):
    """Decode bytestring to Unicode."""
    if isinstance(s, str):
        s = unicode(s, 'utf-8')
    elif not isinstance(s, unicode):
        raise TypeError("str or unicode required, not {}".format(type(s)))
    return unicodedata.normalize('NFC', s)


def get_frontmost_app():
    """Return (name, bundle_id and path) of frontmost application.

    Raise a `RuntimeError` if frontmost application cannot be
    determined.

    """
    for app in NSWorkspace.sharedWorkspace().runningApplications():
        if app.isActive():
            app_name = app.localizedName()
            bundle_id = app.bundleIdentifier()
            app_path = app.bundleURL().fileSystemRepresentation()

            return (app_name, bundle_id, app_path)

    else:
        raise RuntimeError("Couldn't get frontmost application.")


if __name__ == '__main__':
    s = time.time()
    get_frontmost_app()
    d = time.time() - s
