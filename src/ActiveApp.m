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
        NSArray *runningApps = [[NSWorkspace sharedWorkspace] runningApplications];
        for (NSRunningApplication *currApp in runningApps) {
            if ([currApp isActive]) {
                appName = [currApp localizedName];
                bundleID = [currApp bundleIdentifier];
                bundleURL = [currApp bundleURL];
                appPath = [NSString stringWithUTF8String: bundleURL.fileSystemRepresentation];
//                NSLog(@"\n%@\n%@\n%@", appName, bundleID, appPath);
                printf("%s\r%s\r%s", [appName UTF8String], [bundleID UTF8String], [appPath UTF8String]);
                return 0;
            }
        }
    }
    return 1;
}
