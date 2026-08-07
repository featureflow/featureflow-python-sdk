# Contributing

Thanks for your interest in improving the Featureflow Python SDK.

## Development setup

Clone with submodules — the conformance suite consumes a shared test specification:

```bash
git clone --recurse-submodules https://github.com/featureflow/featureflow-python-sdk.git
cd featureflow-python-sdk
python3 -m pip install -e ".[test]"
```

If you already have a clone without the submodule, run `git submodule update --init`.

## Running the tests

```bash
# Unit tests
python3 -m unittest discover -s test -t .

# Cross-SDK conformance suite (behave)
python3 -m behave
```

The `features/*.feature` files are symlinks into `testbed/`, the
[featureflow-sdk-testbed](https://github.com/featureflow/featureflow-sdk-testbed)
submodule shared by every Featureflow server SDK. Evaluation behaviour — bucketing,
rule matching, condition operators — must stay identical across SDKs, so:

- **Do not edit or copy the `.feature` files in this repo.** Behaviour changes start
  in the testbed repository, then each SDK updates its submodule pointer.
- Step definitions in `features/steps/` are the only conformance code owned here.
- The suite fails if the testbed contains a feature file this SDK neither runs nor
  explicitly skips (see `behave.ini` for the skip tags and the reasoning per tag).

## Pull requests

- Target the `main` branch.
- Add or update tests for any behaviour change. If the change affects evaluation
  semantics, it belongs in the testbed first (see above).
- Keep the public API surface (`Featureflow`, `User`, the `Evaluate` methods) stable;
  breaking changes need discussion in an issue first.

## Releasing (maintainers)

Releases are published to [PyPI as `featureflow-sdk`](https://pypi.org/project/featureflow-sdk/)
by GitHub Actions using [trusted publishing](https://docs.pypi.org/trusted-publishers/)
— there are no API tokens to manage, and releases can only be published through CI.

1. Bump `version` in `setup.py` and merge to `main`.
2. Create a GitHub release with tag `v<version>` (e.g. tag `v0.2.1` for version
   `0.2.1`). Write user-facing release notes — they are the changelog.
3. Publishing the release triggers `.github/workflows/publish.yml`, which:
   - runs the unit tests and the conformance suite on the supported Python versions;
   - verifies the release tag matches the `setup.py` version, and fails if not;
   - builds the sdist and wheel;
   - publishes to PyPI via OIDC through the `pypi` GitHub environment.
4. Confirm the new version is live on [PyPI](https://pypi.org/project/featureflow-sdk/)
   and that `pip install --upgrade featureflow-sdk` installs it.

If the workflow fails before the publish step, nothing has been uploaded: fix the
problem on `main`, move the tag to the fixed commit, and re-publish the release.
A version that has been uploaded to PyPI can never be reused — if a bad build ships,
release a new patch version rather than trying to replace the files.
