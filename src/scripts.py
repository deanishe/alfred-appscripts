#!/usr/bin/env python
# encoding: utf-8
#
# Copyright © 2014 deanishe@deanishe.net
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2014-04-07
#

"""
"""

from __future__ import print_function, unicode_literals

import sys
import os
import subprocess

# Make workflow library importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                'alfred-workflow-1.4.zip'))

from workflow import Workflow, ICON_WARNING, ICON_INFO, ICON_ERROR

# Application-specific scripts are stored in subdirectories of this folder
# named after the respective application, e.g. "Safari" scripts are in
# ~/Library/Scripts/Applications/Safari
APP_SCRIPT_DIRECTORY = os.path.expanduser('~/Library/Scripts/Applications')
APP_SUPPORT_DIRECTORY = os.path.expanduser('~/Library/Application Support')

# Acceptable extensions for AppleScripts
SCRIPT_EXTENSIONS = ['.scpt', '.applescript']

# AppleScript snippet to return ``name\npath`` of the frontmost app
AS = """\
tell application "System Events"
    set appPath to POSIX path of (path to frontmost application)
    set appName to name of the first process whose frontmost is true
    appName & return & appPath
end tell"""


class ScriptRunner(object):

    def __init__(self):
        self.wf = None

    def run(self, wf):
        """Main script

        - Get frontmost app
        - Get list of scripts for that app
        - Filter list by query if there is one
        - Show list of available scripts or warning if
          none match query/were found

        """

        self.wf = wf

        query = None
        if wf.args:
            query = wf.args[0].strip()

        app_name, app_path = self.get_frontmost_app()
        if not app_name:
            self.show_error("Couldn't get name of frontmost application")
            return 1
        scripts = self.get_scripts_for_app(app_name)
        if not scripts:
            self.show_warning('No scripts for {}'.format(app_name))
            return 0

        if query:
            scripts = self.wf.filter(query, scripts,
                                     key=lambda x: os.path.basename(x))

        if not scripts:
            self.show_warning('No matching scripts')
            return 0

        for script in scripts:
            title = os.path.splitext(os.path.basename(script))[0]
            self.wf.add_item(title,
                             'Run this script',
                             arg=script,
                             valid=True,
                             icon=app_path,
                             icontype='fileicon'
                             )
        self.wf.send_feedback()

    def get_frontmost_app(self):
        """Return ``(name, path)`` of frontmost application"""
        output = self.wf.decode(
            subprocess.check_output(['osascript', '-e', AS]))
        app_name, app_path = [s.strip() for s in output.split('\r')]
        self.wf.logger.debug('frontmost app : {!r} [{!r}]'.format(app_name,
                                                                  app_path))
        return app_name, app_path

    def show_error(self, title, subtitle=''):
        """
        Show Alfred result with ``title`` and ``subtitle`` with
        an error icon and send feedback to Alfred

        """

        self.show_message(title, subtitle, ICON_ERROR)
        self.wf.send_feedback()

    def show_warning(self, title, subtitle=''):
        """
        Show Alfred result with ``title`` and ``subtitle`` with
        a warning icon and send feedback to Alfred

        """

        self.show_message(title, subtitle, ICON_WARNING)
        self.wf.send_feedback()

    def show_message(self, title, subtitle='', icon=ICON_INFO):
        """
        Show Alfred result with ``title`` and ``subtitle`` with
        specified icon, but do not send feedback to Alfred

        """

        self.wf.add_item(title, subtitle, icon=icon)

    def get_scripts_for_app(self, app_name):
        """
        Return list of AppleScripts in
        ~/Library/Scripts/Application/<app_name> and
        ~/Library/Application Support/<app_name>/Scripts.

        :param app_name: Name of applications (as shown in Menu Bar)
        :type app_name: ``unicode``
        :returns: List of paths to AppleScripts
        :rtype: ``list``
        """
        scriptdirs = [os.path.join(APP_SCRIPT_DIRECTORY, app_name),
                      os.path.join(APP_SUPPORT_DIRECTORY, app_name, 'Scripts')]

        scripts = []
        for scriptdir in scriptdirs:
        # scriptdir = os.path.join(APP_SCRIPT_DIRECTORY, app_name)
            if not os.path.isdir(scriptdir):
                self.wf.logger.debug(
                    'App script directory does not exists : {!r}'.format(
                        scriptdir))
                continue
            for root, dirnames, filenames in os.walk(scriptdir):
                for filename in filenames:
                    ext = os.path.splitext(filename)[1]
                    if ext.lower() not in SCRIPT_EXTENSIONS:
                        continue
                    scripts.append(os.path.join(root, filename))
        self.wf.logger.debug(
            '{} scripts found for app {!r}'.format(len(scripts), app_name))
        return scripts


if __name__ == '__main__':
    wf = Workflow()
    app = ScriptRunner()
    wf.run(app.run)
