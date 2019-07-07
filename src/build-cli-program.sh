#!/bin/bash

clang -fobjc-arc -framework AppKit ActiveApp.m -o ActiveApp
# xcrun -sdk macosx swiftc -framework AppKit ActiveApp.swift -o ActiveApp
