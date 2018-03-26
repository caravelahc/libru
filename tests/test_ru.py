from pathlib import Path

import sys

ROOT_PATH = Path(__file__).resolve().parent.parent

sys.path.append(str(ROOT_PATH))

from libru.libru import parse  # noqa


menu = [
    [
        'arroz branco e arroz integral',
        'feijão carioca e ervilha',
        'frango (sobrecoxa ou sassami empanado) (almoço) e quibe (jantar)',
        'farofa simples',
        'alface e pepino em conserva',
        'mamão'
    ],
    [
        'arroz branco e arroz integral',
        'feijão e lentilha',
        'sobrecoxa de frango (almoço) e iscas de carne com cebola (jantar)',
        'batata palha (almoço) e macarrão com e sem molho branco (jantar)',
        'beterraba e rúcula',
        'salada de frutas'
    ],
    [
        'arroz branco e arroz integral',
        'feijão e ervilha',
        'filé mignon suíno com cebola e pimentão (almoço)',
        'brócolis',
        'rabanete e acelga',
        'melão'
    ],
    [
        'arroz branco e arroz integral',
        'feijão carioca e lentilha',
        'sassami de frango empanado',
        'couve-flor',
        'chicória e pepino',
        'abacaxi'
    ],
    [
        'arroz branco e arroz integral',
        'feijão e lentilha',
        'estrogonofe de carne',
        'batata palha',
        'couve folha e cenoura',
        'kiwi',
    ],
    [
        'arroz branco e arroz integral',
        'feijão e ervilha',
        'picadinho de carne com cebola',
        'batata inglesa com ervas',
        'pepino e alface',
        'morango'
    ],
    [
        'arroz branco e arroz integral',
        'feijão carioca e lentilha',
        'iscas bovina ao molho barbecue',
        'abóbora cozida',
        'brócolis',
        'melão'
    ],
]


def test_ru():
    with open(ROOT_PATH / 'tests/ru.html') as mock_html:
        html = mock_html.read()

    for weekday in range(7):
        assert parse(html, weekday) == menu[weekday]
