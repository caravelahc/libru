# libru

Fetches today's menu from [RU's page](http://ru.ufsc.br/ru/)

Example usage:
```python
from libru import ru

ru()
# [
#     'arroz branco e arroz integral',
#     'feijão carioca e lentilha',
#     'sassami de frango empanado',
#     'couve-flor',
#     'chicória e pepino',
#     'abacaxi',
# ]
```

Also exposes a command-line utility:
```
$ ru
hoje tem:
• arroz branco e arroz integral
• feijão carioca e lentilha
• sassami de frango empanado
• couve-flor
• chicória e pepino
• abacaxi
```

You can also specify the weekday:
```python
ru(weekday=0) # monday
```
And:
```bash
$ ru 0
$ ru segunda
```
