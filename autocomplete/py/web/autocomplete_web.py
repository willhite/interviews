#!/usr/bin/env python3

# Install flask with:
#   pip install jinja2 flask

import flask
import json

app = flask.Flask(__name__)


@app.route("/")
def autocomplete():
    return flask.render_template(
        "autocomplete.html", prompt="Search Wikipedia:")


@app.route("/search")
def search():
    query = flask.request.args.get("q", None)
    index = None
    if query:
        index = binary_search(g_lines, query, 0, len(g_lines) - 1)
    res = []
    if index is not None:
        res = g_lines[index:index+10]
    results = json.dumps({"query": query, "results": res})

    
    resp = flask.Response(results)
    resp.headers["Content-Type"] = "application/json"
    return resp

def read_lines():
    f = open("/Users/dan/work/quip/interviews/autocomplete/wikipedia-latest-titles.csv", "r")
    lines = f.readlines()
    return sorted(lines)

g_lines = []

def binary_search(lines, prefix, start, last):
    if start < 0 or last < 0 or start >= len(lines) or last >= len(lines) or last < start:
        print("binary_search returning None, start: %s, last: %s, len(lines): %s" % (start, last, len(lines)))
        return None
    mid = ((last - start) // 2) + start
    s1 = lines[mid].lower()
    print("binary_search, prefix: %s, start: %s, last: %s, mid: %s, s1: %s" % (prefix, start, last, mid, s1))
    if start == last and not s1.startswith(prefix):
        return None

    if s1.startswith(prefix):
        if mid == 0 or not lines[mid-1].lower().startswith(prefix):
            return mid
        else:
            return binary_search(lines, prefix, start, mid-1)
    elif prefix > s1:
        return binary_search(lines, prefix, mid+1, last)
    else:
        return binary_search(lines, prefix, start, mid-1)
    

def find_start(prefix):
    if len(prefix) == 0:
        return -1
    return binary_search(0, len(lines) - 1)
    
    


if __name__ == '__main__':
    app.debug = True
    g_lines = read_lines()
    app.run()
