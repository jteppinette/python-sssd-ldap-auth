import pytest

from sssdldapauth.deobfuscate import deobfuscate

OBFUSCATED = (
    "AAAQABagVAjf9KgUyIxTw3A+HUfbig7N1+L0qtY4xAULt2GY"
    "HFc1B3CBWGAE9ArooklBkpxQtROiyCGDQH+VzLHYmiIAAQID"
)
DEOBFUSCATED = "Passw0rd"


def test_valid():
    assert deobfuscate(OBFUSCATED) == DEOBFUSCATED


@pytest.mark.parametrize("token", ["invalid", "", None])
def test_invalid(token):
    with pytest.raises(Exception):
        deobfuscate(token)
