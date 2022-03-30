import pytest
from click.testing import CliRunner

from sssdldapauth import cli

OBFUSCATED = (
    "AAAQABagVAjf9KgUyIxTw3A+HUfbig7N1+L0qtY4xAULt2GY"
    "HFc1B3CBWGAE9ArooklBkpxQtROiyCGDQH+VzLHYmiIAAQID"
)
DEOBFUSCATED = "Passw0rd"


@pytest.fixture()
def runner():
    return CliRunner(mix_stderr=False)


def test_valid(runner):
    result = runner.invoke(cli.root, ["deobfuscate", OBFUSCATED])

    assert result.exit_code == 0
    assert result.output == f"{DEOBFUSCATED}\n"


def test_invalid(runner):
    result = runner.invoke(cli.root, ["deobfuscate", "invalid"])

    assert result.exit_code == 1
    assert result.output == ""
    assert result.stderr == "unable to deobfuscate token\n"
