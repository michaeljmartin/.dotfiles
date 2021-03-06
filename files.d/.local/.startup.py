# mostly stolen from:
# https://nedbatchelder.com/blog/201904/startuppy.html

print("(.startup.py)")

import collections, datetime, itertools, math, os, pprint, re, sys, time
print("(imported collections, datetime, itertools, math, os, pprint, re, sys, time)")

pp = pprint.pprint

# A function for pasting code into the repl.
def paste():
    import textwrap
    exec(textwrap.dedent(sys.stdin.read()), globals())

# Readline and history support
def hook_up_history():
    try:
        # Not sure why this module is missing in some places, but deal with it.
        import readline
    except ImportError:
        print("No readline, use ^H")
    else:
        import atexit
        import os
        import rlcompleter

        history_path = os.path.expanduser(
            "~/.pyhistory{0}".format(sys.version_info[0])
        )

        def save_history(history_path=history_path):
            import readline
            readline.write_history_file(history_path)

        if os.path.exists(history_path):
            readline.read_history_file(history_path)

        atexit.register(save_history)

# Don't do history stuff if we are IPython, it has its own thing.
is_ipython = 'In' in globals()
if not is_ipython:
    hook_up_history()

# Get rid of globals we don't want.
del is_ipython, hook_up_history
