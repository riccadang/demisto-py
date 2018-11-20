#!/usr/bin/env python2.7

# example
# Upload a new widget to the available widget library
#
# Author:       Slavik Markovich
# Version:      1.0
#

import json
import argparse
import demisto


def p(what):
    if verbose:
        print(what)


def options_handler():
    parser = argparse.ArgumentParser(
        description='Upload a new widget to Demisto')
    parser.add_argument(
        'key', help='The API key to access the server')
    parser.add_argument(
        'server', help='The server URL to connect to')
    parser.add_argument(
        'widget', help='The new widget JSON file')
    parser.add_argument('-q', '--quiet', action='store_false',
                        dest='verbose', help="no extra prints")
    options = parser.parse_args()
    global verbose
    verbose = options.verbose
    return options


def main():
    options = options_handler()
    c = demisto.DemistoClient(options.key, options.server)
    with open(options.widget, 'r') as widget_file:
        widget_data = widget_file.read()
        res = c.req('POST', 'widgets', json.loads(widget_data))
        if res.status_code != 200:
            raise RuntimeError('Error uploading widget - %d (%s)' %
                               (res.status_code, res.reason))
        p('Widget successfully uploaded')


if __name__ == '__main__':
    main()
