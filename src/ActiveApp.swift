//
//  ActiveApp.swift
//
//  Created by Dean Jackson on 23/11/2015.
//  Copyright © 2019 Dean Jackson. All rights reserved.
//

import AppKit

if let app = NSWorkspace.shared.frontmostApplication {
  print("\(app.localizedName!)")
  print("\(app.bundleIdentifier!)")
  print("\(app.bundleURL!.path)", terminator: "")
}
