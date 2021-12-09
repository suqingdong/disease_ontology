import click
from fuzzywuzzy.process import extractBests
from prettytable import PrettyTable


def fuzzy_query(text, terms, **kwargs):
    choices = terms.keys()
    result = extractBests(text, choices, **kwargs)
    if not result:
        click.secho(f'no result for query text: "{text}" (with kwargs = {kwargs})', err=True, fg='yellow')
        return False
    best_match = result[0]
    click.secho(f'best matched term: "{best_match[0]}" [Score={best_match[1]}] [DOID={terms[best_match[0]]}]', err=True, fg='green')
    if best_match[1] < 90:
        click.secho('the score is too low, maybe you should try again with another name', err=True, fg='yellow')
    if best_match[1] < 95:
        click.secho('Partially matched terms are as follows:', err=True, fg='yellow')
        table = PrettyTable(['Index', 'Score', 'DOID', 'Term'])
        for idx, term in enumerate(result, 1):
            table.add_row([idx, term[1], terms.get(term[0]), term[0]])
        table.align['Term'] = 'l'
        table.align['DOID'] = 'l'
        click.secho(str(table), err=True, fg='green')

    return terms[best_match[0]]
