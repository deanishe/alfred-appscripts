
Alfred AppScripts Workflow
==========================

List, search and run/open AppleScripts for the active application. You can also specify directories that contain scripts that will always be shown, regardless of the active application.

![][demo]


Download
--------

**Note:** Version 3.0 and above are not compatible with Alfred 2.

The workflow can be downloaded from [GitHub][gh-releases] or from [Packal][packal].


Usage
-----

- `.as [<query>]` — Show/search list of AppleScripts for the active application
	- `↩` — Run the selected script.
	- `⌘+↩` — Open the selected script in Script Editor.
	- `⌥+↩` — Reveal the selected script in Finder.
- `appscripts [<query>]` — Show workflow configuration.
    - `Help` – Open this file in your browser.
    - `(No) Update Available` — Whether or not the workflow can be updated. Action the item to update or force an update check.
    - `Search Directories Recursively` – Whether the script directories should be searched recursively. Use with some caution.
    - `Edit Script Directories` — Open the configuration file in your default editor. The file contains a detailed description of how it works.
    - `Reset to Defaults` — Delete configuration and cache files.


Where are these scripts?
------------------------

The workflow comes with a default set of directories. These are defined in a settings file that you can edit yourself. Use the `Edit Script Directories` option in the configuration (keyword `appscripts`) to open the file in your editor.

These are the default directories. `{app_name}` will be replaced with the name of the currently active application, e.g. `BBEdit` or `OmniFocus`, and `{bundle_id}` with the application's bundle ID, e.g. `com.barebones.bbedit` or `com.omnigroup.OmniFocus2`:

- `~/Library/Scripts/Applications/{app_name}`
- `~/Library/Scripts/Applications/{bundle_id}`
- `~/Library/Application Scripts/{app_name}`
- `~/Library/Application Scripts/{bundle_id}`
- `~/Library/Application Support/{app_name}/Scripts`
- `~/Library/Application Support/{bundle_id}/Scripts`
- `~/Library/Containers/{bundle_id}/Data/Library/Application Support/{app_name}/Scripts`

Any `*.scpt`, `*.applescript` or `*.scptd` (script bundle) files found within the above directories will be shown.

If you add a directory path that doesn't contain `{app_name}` or `{bundle_id}`, it will match every application and the scripts will always be shown. See the settings file (`AppScript Directories.txt`) for more information.


Bug reports, feature requests
-----------------------------

Please use [GitHub issues][gh-issues] to report bugs or request features. Alternatively, you can post in the [Alfred Forum thread][forum-thread].


Licence, thanks
---------------

The workflow code and the bundled [Alfred-Workflow][alfred-workflow] and [docopt][docopt] libraries are all licensed under the [MIT Licence][mit-licence].

The workflow icon ([source][icon]), by [destegabry][destegabry], is licensed under the [Creative Commons Attribution-Noncommercial 3.0 License][cc-licence].

The other icons are from [Font Awesome][font-awesome] by [Dave Gandy][dave-gandy], and released under the [SIL OFL 1.1 licence][sil-licence].


[gh-issues]: https://github.com/deanishe/alfred-appscripts/issues
[forum-thread]: http://www.alfredforum.com/topic/4218-appscripts
[alfred-workflow]: https://github.com/deanishe/alfred-workflow
[icon]: http://destegabry.deviantart.com/art/AppleScript-Folder-79793515
[destegabry]: http://destegabry.deviantart.com/
[cc-licence]: http://creativecommons.org/licenses/by-nc/3.0/
[mit-licence]: http://opensource.org/licenses/MIT
[font-awesome]: http://fortawesome.github.io/Font-Awesome/
[dave-gandy]: https://twitter.com/davegandy
[sil-licence]: http://scripts.sil.org/OFL
[docopt]: https://github.com/docopt/docopt
[gh-releases]: https://github.com/deanishe/alfred-appscripts/releases
[packal]: http://www.packal.org/workflow/appscripts
[demo]: https://raw.githubusercontent.com/deanishe/alfred-appscripts/master/demo.gif "Animated demonstration of AppScripts"
