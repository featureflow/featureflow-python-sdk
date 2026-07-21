# Example server

A tiny Flask app (`app.py`) that imports the SDK straight from this repo's source
(no build or install step) so you can manually exercise `Featureflow.evaluate()`
against a real Featureflow account from a browser.

## Run it

```bash
python3 -m pip install -r examples/server/requirements.txt
FEATUREFLOW_SERVER_KEY=srv-env-<your key> python3 examples/server/app.py
```

Open http://127.0.0.1:3456/ -- or hit the JSON endpoints directly:

- `GET /health`
- `GET /api/ready` -- `true` once the 30s poll loop has fetched flags at least once
- `GET /api/features` -- keys of every feature currently loaded from the API
- `GET /api/evaluate?feature=<key>&userId=<id>&role=&tier=`
- `GET /api/evaluate-all?userId=<id>&role=&tier=`

`PORT` overrides the default `3456`.

## Things to know before you click around

- This SDK has **no `baseUrl` override** (unlike the Node SDK) -- it always polls
  and reports events against `https://app.featureflow.io`. There's no way to point
  this example at staging, and no "disable events" switch either: every
  `/api/evaluate*` request here sends a real evaluation event to your account.
- `.value()`, `.is_()`, `.isOn()`, and `.isOff()` on the object returned by
  `evaluate()` each *independently* send an evaluation event -- they don't share
  or memoize one. `/api/evaluate` only calls `.value()` once and derives
  `isOn`/`isOff` from the returned string, so one page action fires one event,
  not three. Keep that in mind if you build on top of this example.
- The app reads `client._features` (a private attribute) to list known feature
  keys and drive "evaluate all" -- the SDK doesn't expose a public accessor for
  the loaded feature set yet.
- Polling starts the moment `Featureflow(api_key)` is constructed, on a background
  thread, every 30s. If the key is wrong, the SDK prints
  `PollingClient got error from API code ...` to stderr and `/api/ready` stays
  `false` forever.
