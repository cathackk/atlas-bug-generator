import json
import random

import click


def _load_data(fn):
    data = json.load(open(fn))
    ts = [
        template['keys']
        for template in data['templates'].values()
        for _ in range(template['prob'])
    ]
    ps = data['parts']
    return ts, ps


templates, parts = _load_data("data.json")


def gen():
    return " ".join(
        random.choice(parts[key])
        for key in random.choice(templates)
    )


@click.command()
@click.argument('count', type=int, default=10)
def main(count: int = 10):
    for _ in range(count):
        print("- " + gen())


if __name__ == '__main__':
    main()
