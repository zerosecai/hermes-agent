"""Kuma alias for the ``hermes_cli`` package.

This module installs itself as an alias for ``hermes_cli`` so that
``from kuma_cli.main import main`` (and any other submodule) resolves
to the same code as the canonical ``hermes_cli`` import path. No
existing ``hermes_cli`` imports are affected.

The mechanism is the standard ``sys.modules`` swap:

1. Python imports ``kuma_cli`` and runs this ``__init__`` once.
2. We import the real ``hermes_cli`` package.
3. We replace ``sys.modules['kuma_cli']`` with the ``hermes_cli``
   module object. Subsequent ``import kuma_cli.<sub>`` lookups use
   ``hermes_cli.__path__`` and find the real submodule.

Used in the wild by ``six``, parts of ``attrs``, and others.
"""

import sys as _sys

import hermes_cli as _hermes_cli

_sys.modules[__name__] = _hermes_cli
