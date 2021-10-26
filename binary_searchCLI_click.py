import click
from binary_search import bin_find


@click.command()
@click.argument('arr', nargs=-1)
@click.option('--el', nargs=1)
@click.option('--bds', default=None, nargs=2, help='Number of greetings.', type=int)
def dec_bin_find(arr, el, bds):
    click.echo(f'Индекс элемента {bin_find(arr, el, bds)}')


if __name__ == '__main__':
    dec_bin_find()
