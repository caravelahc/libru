from pathlib import Path

import sys

ROOT_PATH = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_PATH))

from libru.libru import parse  # noqa


menu = [
    [
        "carne bovina á portuguesa",
        "abóbora cozida (almoço)",
        "purê de batatas (jantar)",
        "repolho",
        "beterraba",
        "molho de ervas",
        "laranja",
    ],
    [
        "filé mignon suíno ao molho agridoce",
        "farofa simples",
        "alface",
        "cenoura",
        "molho de mostarda",
        "maçã",
    ],
    ["iscas de frango", "vagem cozida", "chicória", "rabanete", "vinagrete", "banana"],
    [
        "quibe",
        "couve-flor refogada",
        "acelga",
        "salada de soja em grãos",
        "molho de mostarda",
        "laranja",
    ],
    [
        "risoto de frango",
        "batata palha",
        "agrião",
        "pepino",
        "molho de ervas",
        "banana",
    ],
    [],
    [],
]


def test_ru():
    with open(ROOT_PATH / "tests/ru.html") as mock_html:
        html = mock_html.read()

    for weekday in range(7):
        assert parse(html, weekday) == menu[weekday]
