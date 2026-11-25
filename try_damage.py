# Таблица урона: кто сколько наносит кому (приём силой 1.0).
# Запуск: открой этот файл и нажми ▶ вверху справа.
# Вопрос себе: какое существо самое опасное? Кто бьёт сильнее всего и почему?

from creatures import creatures
from battle import calc_damage

for attacker in creatures:
    for defender in creatures:
        if attacker is defender:
            continue
        damage = calc_damage(attacker, defender)
        print(attacker["name"], "→", defender["name"], ":", damage, "урона")
    print()
