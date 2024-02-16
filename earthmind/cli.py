import click

@click.group()
def cli():
    pass

@cli.group()
def miners():
    pass

@cli.group()
def validators():
    pass

@cli.group()
def aggregator():
    pass

# Miners commands
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

@miners.command()
def run():
    click.echo("Run miners")

# Validators commands
@validators.command()
def list():
    click.echo("List of validators")

@validators.command()
@click.option("--account", help="Account to add")
def add(account):
    click.echo(f"Add validator with account {account}")
    validator.add(account)

@validators.command()
@click.option("--account", help="Account to remove")
def remove(account):
    click.echo(f"Remove validator with account {account}")

@validators.command()
def run():
    click.echo("Start validators")

# Aggregator commands
@aggregator.command()
def run():
    click.echo("Start aggregator")
    
if __name__ == '__main__':
    cli()

# Como agrego un unit test para los comandos?
# Como agrego un unit test para la funcion validator.add()?
# Por que el integration test requiere una transaction a una blockchain no?
