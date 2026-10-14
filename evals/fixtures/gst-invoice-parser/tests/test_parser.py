from pathlib import Path

import pytest

from gstparse import parse

REAL = Path(__file__).parent / "fixtures" / "real_invoices"


@pytest.mark.parametrize("pdf", sorted(REAL.glob("*.pdf")))
def test_parses_real_invoices(pdf):
    invoice = parse(pdf)
    assert invoice.gstin
