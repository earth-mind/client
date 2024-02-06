# import click

# JSON_RPC_ENDPOINT = ""

# @click.group()
# def cli():
#     pass


import click

# @click.command()
# @click.option("--count", default=1, help="Number of greetings.")
# @click.option("--name", prompt="Your name", help="The person to greet.")
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for _ in range(count):
#         click.echo(f"Hello, {name}!")

# if __name__ == '__main__':
#     hello()

# Comandos
# earthmind miners list
# earthmind miners add --account "0x0......"
# earthmind miners remove --account "0x0......"
# earthmind validators list
# earthmind validators add --account "0x0......"
# earthmind validators remove --account "0x0......"
# earthmind miners start
# earthmind validators start

@click.group()
def cli():
    pass

@cli.group()
def miners():
    pass

@miners.command()
def list():
    click.echo("List of miners")

@miners.command()
@click.option("--account", help="Account to add")
def add(account):
    click.echo(f"Add miner with account {account}")

@miners.command()
@click.option("--account", help="Account to remove")
def remove(account):
    click.echo(f"Remove miner with account {account}")

@cli.group()
def validators():
    pass

@validators.command()
def list():
    click.echo("List of validators")

@validators.command()
@click.option("--account", help="Account to add")
def add(account):
    click.echo(f"Add validator with account {account}")

@validators.command()
@click.option("--account", help="Account to remove")
def remove(account):
    click.echo(f"Remove validator with account {account}")

@miners.command()
def start():
    click.echo("Start miners")

@validators.command()
def start():
    click.echo("Start validators")

if __name__ == '__main__':
    cli()