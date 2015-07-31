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

from __future__ import print_function, unicode_literals, absolute_import

import os
import subprocess

from workflow import Workflow, ICON_WARNING, ICON_INFO, ICON_ERROR


HELP_URL = 'https://github.com/deanishe/alfred-appscripts#alfred-appscripts-workflow'

UPDATE_SETTINGS = {
    'github_slug': 'deanishe/alfred-appscripts'
}

# Application-specific scripts are stored in subdirectories of this folder
# named after the respective application, e.g. "Safari" scripts are in
# ~/Library/Scripts/Applications/Safari
APP_SCRIPT_DIRECTORIES = [
    os.path.expanduser('~/Library/Scripts/Applications/{app_name}'),
    os.path.expanduser('~/Library/Scripts/Applications/{bundle_id}'),
    os.path.expanduser('~/Library/Application Scripts/{app_name}'),
    os.path.expanduser('~/Library/Application Scripts/{bundle_id}'),
    os.path.expanduser('~/Library/Application Support/{app_name}/Scripts'),
    os.path.expanduser('~/Library/Application Support/{bundle_id}/Scripts'),
    os.path.expanduser('~/Library/Containers/{bundle_id}/Data/Library'
                       '/Application Support/{app_name}/Scripts'),
]

# Acceptable extensions for AppleScripts
SCRIPT_EXTENSIONS = ['.scpt', '.applescript']

# Icon for an update
ICON_UPDATE = 'update-available.icns'

# AppleScript snippet to return ``name\npath`` of the frontmost app
AS = """\
tell application "System Events"
    set appPath to (path to frontmost application)
    set posixPath to POSIX path of appPath
    set appName to name of the first process whose frontmost is true
    set bundleId to bundle identifier of (info for appPath)
    appName & return & bundleId & return & posixPath
end tell
"""


class ScriptRunner(object):
    """Encapsulates the functionality of this workflow.

    Start the application with:

        wf = Workflow()
        app = ScriptRunner()
        wf.run(app.run)

    """

    def __init__(self):
        self.wf = None

    def run(self, wf):
        """Main script entry point.

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

        if wf.update_available:
            wf.add_item('A new version is available',
                        '↩ or ⇥ to install update',
                        autocomplete='workflow:update',
                        icon=ICON_UPDATE)

        app_name, bundle_id, app_path = self.get_frontmost_app()
        if not app_name:
            self.show_error("Couldn't get name of frontmost application")
            return 1
        scripts = self.get_scripts_for_app(app_name, bundle_id)
        if not scripts:
            self.show_warning('No scripts for {}'.format(app_name))
            return 0

        if query:
            scripts = wf.filter(query, scripts,
                                key=lambda x: os.path.basename(x),
                                min_score=30)

        if not scripts:
            self.show_warning('No matching scripts')
            return 0

        for script in scripts:
            title = os.path.splitext(os.path.basename(script))[0]
            wf.add_item(
                title,
                'Run this script',
                arg=script,
                valid=True,
                icon=app_path,
                icontype='fileicon',
            )
        wf.send_feedback()

    def get_frontmost_app(self):
        """Return ``(name, bundle_id, path)`` of frontmost application."""
        output = self.wf.decode(
            subprocess.check_output(['osascript', '-e', AS]))
        app_name, bundle_id, app_path = [s.strip() for s in output.split('\r')]
        self.wf.logger.debug('frontmost app : %r | %r | %r',
                             app_name, bundle_id, app_path)
        return app_name, bundle_id, app_path

    def show_error(self, title, subtitle=''):
        """Show Alfred result with ``title`` and ``subtitle`` with
        an error icon and send feedback to Alfred.

        """

        self.show_message(title, subtitle, ICON_ERROR)
        self.wf.send_feedback()

    def show_warning(self, title, subtitle=''):
        """Show Alfred result with ``title`` and ``subtitle`` with
        a warning icon and send feedback to Alfred.

        """

        self.show_message(title, subtitle, ICON_WARNING)
        self.wf.send_feedback()

    def show_message(self, title, subtitle='', icon=ICON_INFO):
        """Show Alfred result with ``title`` and ``subtitle`` with
        specified icon, but do not send feedback to Alfred.

        """

        self.wf.add_item(title, subtitle, icon=icon)

    def get_scripts_for_app(self, app_name, bundle_id):
        """Return list of AppleScripts in `APP_SCRIPT_DIRECTORIES`.

        :param app_name: Name of applications (as shown in Menu Bar)
        :type app_name: ``unicode``
        :returns: List of paths to AppleScripts
        :rtype: ``list``

        """

        def _wrapper():
            return self._get_scripts_for_app(app_name, bundle_id)

        return wf.cached_data('appscripts-{0}'.format(bundle_id),
                              _wrapper, max_age=30)

    def _get_scripts_for_app(self, app_name, bundle_id):
        """Return list of AppleScripts in `APP_SCRIPT_DIRECTORIES`.

        :param app_name: Name of applications (as shown in Menu Bar)
        :type app_name: ``unicode``
        :returns: List of paths to AppleScripts
        :rtype: ``list``

        """

        scriptdirs = []
        for dirpath in APP_SCRIPT_DIRECTORIES:
            scriptdirs.append(dirpath.format(app_name=app_name,
                                             bundle_id=bundle_id))

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
                    path = os.path.join(root, filename)
                    wf.logger.debug('Script : %r', path)
                    scripts.append(path)
        self.wf.logger.debug(
            '{} scripts found for app {!r}'.format(len(scripts), app_name))
        return scripts


if __name__ == '__main__':
    wf = Workflow(update_settings=UPDATE_SETTINGS,
                  help_url=HELP_URL)
    app = ScriptRunner()
    wf.run(app.run)
