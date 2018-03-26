from libru import ru


def cli():
    menu = ru()

    if not menu:
        print('cardápio de hoje indisponível')
        exit(1)
    else:
        print('hoje tem:')

        for item in menu:
            print('\u2022', item)


if __name__ == '__main__':
    cli()
