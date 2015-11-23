//
//  ActiveApp.swift
//
//  Created by Dean Jackson on 23/11/2015.
//  Copyright © 2015 Dean Jackson. All rights reserved.
//

import Foundation
import AppKit

let runningApps = NSWorkspace.sharedWorkspace().runningApplications
for currApp in runningApps {
    if currApp.active {
        print(currApp.localizedName!, terminator: "\r")
        print(currApp.bundleIdentifier!, terminator: "\r")
        print(String.fromCString(currApp.bundleURL!.fileSystemRepresentation)!, terminator: "")
    }
}
