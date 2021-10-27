import click
from binary_search import bin_find


@click.command()
@click.argument('arr', nargs=-1)
@click.option('--el', nargs=1)
@click.option('--bds', default=None, nargs=2, help='bounds of search', type=int)
def dec_bin_find(arr, el, bds):
    if x := bin_find(arr, el, bds):
        click.echo(f'Индекс элемента {bin_find(arr, el, bds)}')
    else:
        click.echo('Элемент не найден')


if __name__ == '__main__':
    dec_bin_find()
