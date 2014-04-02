#!/usr/bin/python
__all__ = ['MAJOR', 'MINOR', 'RELEASE', 'VERSION']


MAJOR = 0
MINOR = 0
RELEASE = 1

VERSION = "%s.%s.%s" % (MAJOR, MINOR, RELEASE)

if __name__ == '__main__':
    print VERSION
