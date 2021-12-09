from pathlib import Path
import click
import pickle

from disease_ontology import version_info, DEFAULT_DB_PATH
from disease_ontology.util import parse_version, parse_term, get_iter_lines
from disease_ontology.util import fuzzy_query


@click.group(help=version_info['desc'])
@click.option('-d', '--dbfile',
              help='the database file path',
              default=str(DEFAULT_DB_PATH),
              envvar='DO_DB_PATH',
              show_default=True)
@click.version_option(version=version_info['version'],
                      prog_name=version_info['prog'])
@click.pass_context
def cli(ctx, **kwargs):
    ctx.obj = {
        'dbfile': Path(kwargs['dbfile'])
    }
    click.secho(f'dbfile: {kwargs["dbfile"]}', fg='yellow', err=True)


@click.command(
    no_args_is_help=True,
    help='get the DOID from database'
)
@click.argument('text', required=True, nargs=-1)
@click.option('-l', '--limit', help='maximum for the number of terms', type=int, default=5)
@click.option('-s', '--score-cutoff', help='Optional argument for score threshold', type=float, default=0)
@click.pass_obj
def query(obj, **kwargs):
    dbfile = obj.get('dbfile')
    text = ' '.join(kwargs['text'])

    if not dbfile.exists():
        click.secho(f'dbfile not exists: {dbfile}', err=True, fg='red')
        exit(1)

    click.secho(f'query string: "{text}"', err=True, fg='green')
    data = pickle.load(dbfile.open('rb'))
    fuzzy_query(text, data['terms'], limit=kwargs['limit'], score_cutoff=kwargs['score_cutoff'])


@click.command(
    help='build/update the database',
)
@click.option('-o', '--obo', help='the source file of doid.obo')
@click.pass_obj
def build(obj, **kwargs):
    dbfile = obj.get('dbfile')

    obo_file = kwargs['obo']
    lines = get_iter_lines(obo_file)

    data = {}
    data['data_version'] = parse_version(lines)
    data['terms'] = {term['name']: term['id'] for term in parse_term(lines)}
    data['term_count'] = len(data['terms'])

    click.secho('data_version: {data_version}\nterm_count: {term_count}'.format(
        **data), fg='green', err=True)

    with dbfile.open('wb') as out:
        pickle.dump(data, out)
    click.secho(f'build database file: {dbfile}')


@click.command(
    help='show the version of database'
)
@click.pass_obj
def version(obj):
    dbfile = obj.get('dbfile')
    if not dbfile.exists():
        click.secho(f'dbfile not exists: {dbfile}', fg='red')
        exit(1)
    data = pickle.load(dbfile.open('rb'))
    data_version = data.get('data_version')
    term_count = len(data['terms'])
    click.secho(f'data_version:\t{data_version}\nterm_count:\t{term_count}', err=True, fg='cyan')



def main():
    cli.add_command(query)
    cli.add_command(build)
    cli.add_command(version)
    cli()


if __name__ == "__main__":
    main()
