import click
import os
import crud

from pathlib import Path


@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context):
    notes_dir = 'C:/Users/user/Documents/Notes'
    if not os.path.exists(notes_dir):
       os.mkdir(notes_dir)

    
    ctx.obj = { 'notes_dir': Path(notes_dir) }


cli.add_command(crud.create)
cli.add_command(crud.list)
cli.add_command(crud.add)
cli.add_command(crud.show)
cli.add_command(crud.update)

if __name__ == "__main__":
    cli()