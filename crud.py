import click
import os
import random
import re


@click.command('create')
@click.option('--title', prompt="Enter your note name", help="Note nomini yozish kerak")
@click.pass_context
def create(ctx: click.Context, title: str):
    with open(f"{ctx.obj['notes_dir']}/{title}.txt", 'w') as file:
        file.write("-- TASKS --")

    
    click.echo(f"New note: {title}")



@click.command('list')
@click.pass_context
def list(ctx: click.Context) -> None:
    files = [file for file in os.listdir(ctx.obj['notes_dir']) if os.path.isfile(os.path.join(ctx.obj['notes_dir'], file))]
    
    for file in files:
        click.echo("-- ALL NOTES --")
        click.echo(f"-- {file.split('.')[0]}")


@click.command('add')
@click.option('--note', prompt="Ishlatmoqchi bo'lgan note nomini yozing", help="Note nomini yozish kerak")
@click.option('--task', prompt="Taskni yozing")
@click.pass_context
def add(ctx: click.Context, note: str, task: str):
    file_path = f"{ctx.obj['notes_dir']}/{note}.txt"
    isFile = os.path.exists(file_path)
    if not isFile:
        return click.echo("NOTE NOT FOUND")
    
    with open(file_path, "r") as file:
        tasks = file.read()
        with open(file_path, 'w') as file:
            file.write(f"{tasks}\n[{random.randint(1000, 9999)}]: {task} -- FALSE")

    return click.echo(f"{tasks}\n[{random.randint(1000, 9999)}]: {task} -- FALSE"+"\n\n-- TASK ADDED SUCCESSFULLY --")
    

@click.command('show')
@click.option('--note', prompt="O'zgartirmoqchi bo'lgan note nomini yozing", help="Note nomini yozish kerak")
@click.pass_context
def show(ctx: click.Context, note):
    file_path = f"{ctx.obj['notes_dir']}/{note}.txt"
    isFile = os.path.exists(file_path)
    if not isFile:
        return click.echo("NOTE NOT FOUND")
    
    with open(file_path, "r") as file:
        tasks = file.read()
        for task in tasks.split('\n'):
            click.echo(task)



@click.command('update')
@click.option('--note', prompt="O'zgartirmoqchi bo'lgan note nomini yozing", help="Note nomini yozish kerak")
@click.option('--idx', prompt="TaskId yozing", help="Task aydisini yozish yozish kerak")
@click.option('--status', prompt="Status yozing", help="O'zgartirmoqchi bo'lgan statusingizni yozing")
@click.pass_context
def update(ctx: click.Context, note, status, idx):
    file_path = f"{ctx.obj['notes_dir']}/{note}.txt"
    isFile = os.path.exists(file_path)
    if not isFile:
        return click.echo("NOTE NOT FOUND")
    

    with open(file_path, "r") as file:
        tasks = file.read().split('\n')
        for task_id, task in enumerate(tasks):
            match = re.search(r'\[(\d+)\]:', task)
            if match:
                id = match.group(1)
                if id == idx:
                    tasks.remove(task)
                    tasks.insert(task_id, task.replace('FALSE', status))
                    with open(file_path, 'w') as f:
                        f.write("\n".join(tasks))                   
                    return click.echo("\n".join(tasks) + "\n\n--TASK UPDATED --")

        return click.echo("TASK NOT FOUND")    
            
           


