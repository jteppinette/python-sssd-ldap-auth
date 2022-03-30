import sys

import click

import sssdldapauth


@click.group()
def root():
    pass


@root.command()
@click.argument("token")
def deobfuscate(token):
    try:
        password = sssdldapauth.deobfuscate(token)
    except Exception:
        click.echo("unable to deobfuscate token", err=True)
        sys.exit(1)

    click.echo(password)
