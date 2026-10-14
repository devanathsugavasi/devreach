from dataclasses import dataclass


@dataclass
class Invoice:
    gstin: str
    total: float


def parse(path):
    # TODO: support multi-page invoices
    raise NotImplementedError("fixture only")
