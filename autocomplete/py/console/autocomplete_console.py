#!/usr/bin/env python

import subprocess
import sys

CTRL_C = "\003"


def get_input():
    """Waits for a single character of input and returns it."""
    prev_state = subprocess.check_output("stty -g", shell=True)

    try:
        subprocess.call("stty raw -echo", shell=True)
        ch = sys.stdin.read(1)
        if ch == CTRL_C:
            sys.exit()
        return ch
    finally:
        subprocess.call("stty " + prev_state, shell=True)

    return None


if __name__ == '__main__':
    print "Waiting for input..."
    ch = get_input()

    print "Got input", ch
