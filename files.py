#!/usr/bin/env python3
import os

def list_all_files(root='.'):
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            print(os.path.join(dirpath, fname))

if __name__ == '__main__':
    list_all_files()
