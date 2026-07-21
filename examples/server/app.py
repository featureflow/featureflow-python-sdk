#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example server: a small Flask app that uses this repo's SDK straight from source
(no build/install step needed) so you can manually exercise Featureflow.evaluate()
against a real Featureflow account from a browser.

    FEATUREFLOW_SERVER_KEY=srv-env-xxxxxxxxx python3 examples/server/app.py

Open http://127.0.0.1:3456/ -- or use the JSON API below. See README.md in this
directory for the endpoint list and a few things worth knowing before you click
around (this SDK always talks to https://app.featureflow.io, no staging override,
and every evaluate call below sends a real event to your account).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from flask import Flask, Response, jsonify, request
except ImportError:
    print(
        'Flask is required to run this example. Install it with:\n'
        '  python3 -m pip install -r examples/server/requirements.txt',
        file=sys.stderr,
    )
    sys.exit(1)

from featureflow import Featureflow, User

API_KEY = os.environ.get('FEATUREFLOW_SERVER_KEY', '').strip()
if not API_KEY:
    print(
        'Set FEATUREFLOW_SERVER_KEY to your Featureflow server API key.\n'
        'Example:\n'
        '  FEATUREFLOW_SERVER_KEY=srv-env-xxxxxxxxx python3 examples/server/app.py',
        file=sys.stderr,
    )
    sys.exit(1)

PORT = int(os.environ.get('PORT', '3456'))

client = Featureflow(API_KEY)

app = Flask(__name__)


def build_user(user_id, role, tier):
    return User(
        key=user_id,
        attributes={'role': role or 'pvt_tester', 'tier': tier or 'gold'},
    )


@app.get('/health')
def health():
    return jsonify(status='ok')


@app.get('/')
def index():
    return Response(INDEX_HTML, mimetype='text/html')


@app.get('/api/ready')
def ready():
    # No public isReady()/config accessor on this SDK yet -- _features is the
    # in-memory store PollingClient replaces every 30s once it can reach the API.
    return jsonify(ready=bool(client._features))


@app.get('/api/features')
def features():
    return jsonify(features=sorted(client._features.keys()))


@app.get('/api/evaluate')
def evaluate():
    feature = (request.args.get('feature') or '').strip()
    if not feature:
        return jsonify(error='Query parameter "feature" is required'), 400

    user_id = (request.args.get('userId') or 'anonymous').strip()
    role = (request.args.get('role') or '').strip()
    tier = (request.args.get('tier') or '').strip()

    user = build_user(user_id, role, tier)
    evaluated = client.evaluate(feature, user)
    # .value(), .is_(), .isOn() and .isOff() each independently send an evaluation
    # event -- call only one per request here or you'll multiply event volume.
    value = evaluated.value()

    return jsonify(
        feature=feature,
        user=user.toJSON(),
        value=value,
        isOn=value == 'on',
        isOff=value == 'off',
    )


@app.get('/api/evaluate-all')
def evaluate_all():
    user_id = (request.args.get('userId') or 'anonymous').strip()
    role = (request.args.get('role') or '').strip()
    tier = (request.args.get('tier') or '').strip()

    user = build_user(user_id, role, tier)
    results = {
        key: client.evaluate(key, user).value()
        for key in sorted(client._features.keys())
    }

    return jsonify(user=user.toJSON(), features=results)


@app.errorhandler(404)
def not_found(_e):
    return jsonify(error='Not found'), 404


INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Featureflow Python SDK -- example server</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 42rem; margin: 2rem auto; padding: 0 1rem; }
    label { display: block; margin-top: 0.75rem; }
    input { width: 100%; max-width: 24rem; padding: 0.25rem 0.5rem; }
    pre { background: #f4f4f4; padding: 0.75rem; overflow: auto; }
    .ok { color: #0a0; } .err { color: #c00; }
    table { border-collapse: collapse; width: 100%; max-width: 32rem; }
    th, td { text-align: left; padding: 0.25rem 0.75rem 0.25rem 0; border-bottom: 1px solid #ddd; font-family: ui-monospace, monospace; }
    th { font-family: system-ui, sans-serif; }
  </style>
</head>
<body>
  <h1>Featureflow Python SDK -- example server</h1>
  <p>Uses the SDK straight from this repo's source (no build step). Set <code>FEATUREFLOW_SERVER_KEY</code> before starting -- see this directory's README for details and caveats.</p>
  <p>Ready: <strong id="ready">&hellip;</strong></p>
  <label>Feature key <input id="feature" type="text" value="harness-demo" placeholder="my-feature-key" /></label>
  <label>User id <input id="userId" type="text" value="harness-user" placeholder="user id" /></label>
  <label>Role attribute <input id="role" type="text" value="pvt_tester" placeholder="role" /></label>
  <label>Tier attribute <input id="tier" type="text" value="gold" placeholder="tier" /></label>
  <p><button type="button" id="go">Evaluate</button></p>
  <h2>Result</h2>
  <pre id="out">&mdash;</pre>
  <h2>User sent to server</h2>
  <pre id="userJson">&mdash;</pre>
  <h2>Raw JSON</h2>
  <pre id="raw">&mdash;</pre>
  <h2>All known features</h2>
  <p><button type="button" id="refreshAll">Re-evaluate all</button> <span id="allStatus"></span></p>
  <table>
    <thead><tr><th>Feature key</th><th>Variant</th></tr></thead>
    <tbody id="allRows"><tr><td colspan="2">&mdash;</td></tr></tbody>
  </table>
  <script>
  (function () {
    var readyEl = document.getElementById('ready');
    var outEl = document.getElementById('out');
    var rawEl = document.getElementById('raw');
    var userJsonEl = document.getElementById('userJson');
    function get(path) { return fetch(path).then(function (r) { return r.json(); }); }
    function refreshReady() {
      get('/api/ready').then(function (d) {
        readyEl.textContent = d.ready ? 'yes' : 'not yet / polling (up to 30s)';
        readyEl.className = d.ready ? 'ok' : '';
      }).catch(function () { readyEl.textContent = 'error'; readyEl.className = 'err'; });
    }
    refreshReady();
    setInterval(refreshReady, 5000);
    function escapeHtml(s) {
      return String(s).replace(/[&<>"']/g, function (c) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
      });
    }
    var allRowsEl = document.getElementById('allRows');
    var allStatusEl = document.getElementById('allStatus');
    function loadAll() {
      var u = document.getElementById('userId').value.trim() || 'anonymous';
      var r = document.getElementById('role').value.trim();
      var t = document.getElementById('tier').value.trim();
      allStatusEl.textContent = 'loading…';
      get('/api/evaluate-all?userId=' + encodeURIComponent(u) + '&role=' + encodeURIComponent(r) + '&tier=' + encodeURIComponent(t)).then(function (d) {
        var keys = Object.keys(d.features).sort();
        if (!keys.length) {
          allRowsEl.innerHTML = '<tr><td colspan="2">(no features loaded yet -- check FEATUREFLOW_SERVER_KEY and wait for polling)</td></tr>';
        } else {
          allRowsEl.innerHTML = keys.map(function (k) {
            return '<tr><td>' + escapeHtml(k) + '</td><td>' + escapeHtml(d.features[k]) + '</td></tr>';
          }).join('');
        }
        allStatusEl.textContent = keys.length + ' feature(s) for user "' + u + '"';
        allStatusEl.className = '';
      }).catch(function () {
        allStatusEl.textContent = 'request failed';
        allStatusEl.className = 'err';
      });
    }
    document.getElementById('refreshAll').onclick = loadAll;
    loadAll();
    document.getElementById('go').onclick = function () {
      var f = document.getElementById('feature').value.trim();
      var u = document.getElementById('userId').value.trim() || 'anonymous';
      var r = document.getElementById('role').value.trim();
      var t = document.getElementById('tier').value.trim();
      var q = '/api/evaluate?feature=' + encodeURIComponent(f) + '&userId=' + encodeURIComponent(u) +
        '&role=' + encodeURIComponent(r) + '&tier=' + encodeURIComponent(t);
      get(q).then(function (d) {
        if (d.error) {
          outEl.textContent = d.error;
          outEl.className = 'err';
          return;
        }
        outEl.className = '';
        outEl.textContent = 'value: ' + d.value + '\\nisOn: ' + d.isOn + ', isOff: ' + d.isOff;
        userJsonEl.textContent = JSON.stringify(d.user, null, 2);
        rawEl.textContent = JSON.stringify(d, null, 2);
      }).catch(function () {
        outEl.textContent = 'Request failed';
        outEl.className = 'err';
      });
    };
  })();
  </script>
</body>
</html>
"""

if __name__ == '__main__':
    print(
        f'Featureflow Python SDK example server listening on http://127.0.0.1:{PORT}/\n'
        '  GET  /health  GET  /api/ready  GET  /api/features\n'
        '  GET  /api/evaluate?feature=<key>&userId=<id>&role=&tier=\n'
        '  GET  /api/evaluate-all?userId=<id>&role=&tier=\n'
        '  This SDK always polls/reports against https://app.featureflow.io (no baseUrl override) --\n'
        '  every evaluate call above sends a real event to your account.\n'
    )
    app.run(host='127.0.0.1', port=PORT)
