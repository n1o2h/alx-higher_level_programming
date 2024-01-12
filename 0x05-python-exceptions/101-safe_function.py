#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct
    except Exception as e:
        import sys
        print(f"Exception: {e}", file=sys.stderr)
