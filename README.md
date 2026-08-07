# featureflow-python-sdk
[![][dependency-img]][dependency-url]

> Python SDK for the featureflow feature management platform

Get your Featureflow account at [featureflow.io](http://www.featureflow.io)

## Get Started

The easiest way to get started is to follow the [Featureflow quick start guides](http://docs.featureflow.io/docs)


## Installation
The SDK is available on [PyPI as `featureflow-sdk`][pypi-url].

You can either add it as a dependency or install it globally.

```
python -m pip install featureflow-sdk
```

## Usage

**Create one `Featureflow` client for the lifetime of your application and share it.**
The constructor starts background threads that poll Featureflow for flag configuration
and batch evaluation events back to the server. Constructing a client per request (or
per evaluation) spawns new threads and re-downloads your flags every time — create it
once at startup, then call `evaluate()` on that single instance as often as you like;
evaluation is local and cheap.

```python
import os

from featureflow import Featureflow, User

# Once, at application startup. Use your server environment key (sdk-srv-env-...).
featureflow = Featureflow(os.environ["FEATUREFLOW_SERVER_KEY"])


def show_my_feature(user_id):
    user = User(key=user_id, attributes={"tier": "gold"})

    if featureflow.evaluate("my-cool-feature", user).isOn():
        print("I'm enabled")
```

In a web application, create the client at startup and reuse it across requests —
see [examples/server](examples/server) for how the Flask example does exactly this.

For multivariate flags, check a specific variant or read the evaluated value:

```python
evaluated = featureflow.evaluate("checkout-flow", user)

if evaluated.is_("variant-b"):
    ...

print(evaluated.value())  # e.g. "variant-b", or "off"
```

## Example server

See [examples/server](examples/server) for a small Flask app you can run locally to
manually test evaluations against your Featureflow account from a browser.

[pypi-url]: https://pypi.org/project/featureflow-sdk/
[dependency-url]: https://www.featureflow.io
[dependency-img]: https://www.featureflow.io/wp-content/uploads/2016/12/featureflow-web.png

