# Alfred AppScripts Workflow #

List, search and run/open AppleScripts for the active application.

![](https://raw.githubusercontent.com/deanishe/alfred-appscripts/master/demo.gif)

## Download ##

The workflow can be downloaded from [GitHub](https://github.com/deanishe/alfred-appscripts/releases) or from [Packal](http://www.packal.org/workflow/appscripts).

## Usage ##

- `.as [query]` — Show/search list of AppleScripts for the active application
	+ `↩` — Run the selected script
	+ `⌘+↩` — Open the selected script in AppleScript Editor
	+ `⌥+↩` — Reveal the selected script in Finder

## Where are these scripts? ##

The workflow will search in the following directories. `<app_name>` is the name of the application, e.g. `BBEdit` or `OmniFocus`, and `<bundle_id>` is the application's bundle ID, e.g. `com.barebones.bbedit` or `com.omnigroup.OmniFocus2`.

- `~/Library/Scripts/Applications/<app_name>`. This is the directory used by FastScripts.
- `~/Library/Scripts/Applications/<bundle_id>`
- `~/Library/Application Scripts/<app_name>`
- `~/Library/Application Scripts/<bundle_id>`
- `~/Library/Application Support/<app_name>/Scripts`
- `~/Library/Application Support/<bundle_id>/Scripts`
- `~/Library/Containers/<bundle_id>/Data/Library/Application Support/<app_name>/Scripts`

Any `*.scpt` or `*.applescript` files found within the appropriate directory for the currently-active application will be shown.

## Licence, thanks ##

The workflow code and the bundled [Alfred-Workflow library](https://github.com/deanishe/alfred-workflow) are both licensed under the [MIT Licence](http://opensource.org/licenses/MIT).

The workflow icon ([source](http://destegabry.deviantart.com/art/AppleScript-Folder-79793515)), by [destegabry](http://destegabry.deviantart.com/), is licensed under the [Creative Commons Attribution-Noncommercial 3.0 License](http://creativecommons.org/licenses/by-nc/3.0/).
