//
//  ActiveApp.m
//
//  Created by Dean Jackson on 23/11/2015.
//  Copyright © 2015 Dean Jackson. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <AppKit/AppKit.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSString *appName;
        NSString *bundleID;
        NSURL *bundleURL;
        NSString *appPath;
        NSRunningApplication *currApp = [[NSWorkspace sharedWorkspace] frontmostApplication];
        appName = [currApp localizedName];
        bundleID = [currApp bundleIdentifier];
        bundleURL = [currApp bundleURL];
        appPath = [NSString stringWithUTF8String: bundleURL.fileSystemRepresentation];
        printf("%s\n%s\n%s", [appName UTF8String], [bundleID UTF8String], [appPath UTF8String]);
        return 0;
    }
    return 1;
}
