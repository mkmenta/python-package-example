#!/usr/bin/env bash
rm -R build/docs
sphinx-apidoc -o docs/ helloworld/
sphinx-build -M html docs/ build/docs/