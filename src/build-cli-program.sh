#!/bin/bash

clang -fobjc-arc -framework Foundation -framework AppKit ActiveApp.m -o ActiveApp
# xcrun -sdk macosx swiftc -framework Foundation -framework AppKit ActiveApp.swift -o ActiveApp
