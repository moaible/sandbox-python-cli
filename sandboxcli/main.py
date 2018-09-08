#!/usr/bin/env python
import click

from commands import command


@click.command(help='Simple click CLI')
@click.option('-n', '--name', 'name', type=str, help='your name', required=False)
@click.option('-l', '--last-name', 'last_name', type=str, help='your last name', default='moaible', required=False)
def main(name, last_name):
    print('Your name is %s' % name)
    ret = command.execute(["ls"])
    print(ret.value)


if __name__ == '__main__':
    main()
