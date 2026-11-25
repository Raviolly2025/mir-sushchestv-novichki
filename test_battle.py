# ПРОВЕРКА ЭТАПА 4 · ДВИЖОК БОЯ (трек «Новички»)
# Запуск: открой этот файл и нажми ▶ вверху справа.

passed = 0
failed = 0


def check(condition, what):
    global passed, failed
    if condition:
        passed += 1
        print("  ✅", what)
    else:
        failed += 1
        print("  ❌", what)


def safe(function, *args):
    """Вызывает функцию и не падает, если в ней ошибка."""
    try:
        return function(*args)
    except Exception as error:
        return "ошибка: " + type(error).__name__


print("Проверяю battle.py...\n")
try:
    from battle import element_multiplier, calc_damage
    import battle
except Exception as error:
    print("❌ Файл battle.py не запускается:", type(error).__name__, "-", error)
    raise SystemExit

print("Множитель стихии:")
cases = [
    ("fire", "nature", 2.0, "огонь против природы"),
    ("nature", "water", 2.0, "природа против воды"),
    ("water", "fire", 2.0, "вода против огня"),
    ("nature", "fire", 0.5, "природа против огня"),
    ("fire", "water", 0.5, "огонь против воды"),
    ("fire", "fire", 1.0, "огонь против огня"),
]
for attacker, defender, expected, text in cases:
    got = safe(element_multiplier, attacker, defender)
    check(got == expected, text + " → " + str(expected) + " (у тебя: " + str(got) + ")")

print("\nУрон:")
fire_cat = {"name": "Искрохвост", "element": "fire", "attack": 12, "defense": 4}
leaf = {"name": "Листик", "element": "nature", "attack": 9, "defense": 8}
drop = {"name": "Капля", "element": "water", "attack": 11, "defense": 5}

damage_cases = [
    (fire_cat, leaf, 1.0, 16, "Искрохвост бьёт Листика: 12×1×2=24, 24−8=16"),
    (fire_cat, drop, 1.0, 1, "Искрохвост бьёт Каплю: 12×1×0.5=6, 6−5=1"),
    (drop, fire_cat, 1.5, 29, "Капля бьёт Искрохвоста приёмом 1.5: 11×1.5×2=33, 33−4=29"),
    (leaf, drop, 1.0, 13, "Листик бьёт Каплю: 9×1×2=18, 18−5=13"),
    (leaf, fire_cat, 1.0, 1, "Листик бьёт Искрохвоста: 9×1×0.5=4.5 → 4, 4−4=0 → минимум 1"),
]
for attacker, defender, power, expected, text in damage_cases:
    got = safe(calc_damage, attacker, defender, power)
    check(got == expected, text + " (у тебя: " + str(got) + ")")

print("\n⭐ Бонус (is_super_effective):")
f = getattr(battle, "is_super_effective", None)
if f is not None:
    results = [safe(f, fire_cat, leaf) is True, safe(f, fire_cat, drop) is False, safe(f, leaf, leaf) is False]
    if all(results):
        print("  ⭐ is_super_effective работает")
    else:
        print("  · is_super_effective пока не работает (это бонус)")

print("\nИтог:", passed, "пройдено,", failed, "не пройдено.")
if failed == 0:
    print("🎉 Движок боя работает! Открой try_damage.py и нажми ▶ — посмотри на свой мир.")
else:
    print("В строке с ❌ написано, что должно получиться. Найди в коде, где получается по-другому.")
