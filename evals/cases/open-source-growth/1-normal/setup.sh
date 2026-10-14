#!/bin/bash
# Copy the fixture repository into the eval workspace (current directory).
set -euo pipefail
cp -R "$(dirname "$0")/../../../fixtures/gst-invoice-parser/." .
