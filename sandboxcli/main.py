#!/usr/bin/env python
import click


@click.command(help='Simple click CLI')  # (1)
# (2)
@click.option('-n', '--name', 'name', type=str, help='your name', required=True)
@click.option('-l', '--last-name', 'last_name', type=str, help='your last name', default='Fujimoto', required=False)
def main(name, last_name):
    print('Your name is %s' % name)


if __name__ == '__main__':
    main()
