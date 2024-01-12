#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as e:
        import sys
        print(f"Exception: {e}", file=sys.stderr)
