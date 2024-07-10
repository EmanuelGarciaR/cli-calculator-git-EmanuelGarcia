import click

from app.model import Calculator


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """A simple calculator."""
    
    ctx.obj = {"calculator_object": Calculator()}


@click.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
@click.pass_context
def add(ctx: click.Context, a: int, b: int) -> None:
    """Add two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.add(a, b)
    click.echo(result)


@click.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
@click.pass_context
def subtract(ctx: click.Context, a: int, b: int) -> None:
    """Add two numbers."""
    calculator = ctx.obj["calculator_object"]
    result = calculator.subtract(a, b)
    click.echo(result)


cli.add_command(add)
cli.add_command(subtract)
    