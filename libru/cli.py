from libru import ru
from sys import argv

weekdays = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]


def fail(msg):
    print(msg)
    exit(1)


def parse_args():
    def parse_fail():
        fail(
            "dia invalido, deve ser entre 0 (segunda) e 6 (domingo)"
            " ou ser um de: {}".format(", ".join(weekdays))
        )

    if len(argv) < 2:
        return None

    day = argv[1]

    try:
        weekday = int(day)
        if not (0 <= weekday <= 6):
            parse_fail()
        return weekday
    except ValueError:
        try:
            return weekdays.index(
                day.strip().lower().replace("ç", "c").replace("á", "a")
            )
        except ValueError:
            parse_fail()


def cli():
    weekday = parse_args()

    menu = ru(weekday=weekday)

    if not menu:
        fail("cardápio indisponível")

    if weekday is None:
        print("hoje tem:")
    else:
        if isinstance(weekday, int):
            print("{} tem:".format(weekdays[weekday]))
        else:
            print("{} tem:".format(weekday))

    for item in menu:
        print("\u2022", item)


if __name__ == "__main__":
    cli()
