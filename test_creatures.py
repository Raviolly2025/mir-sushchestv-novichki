# ПРОВЕРКА ЭТАПА 3 · ДАННЫЕ (трек «Новички»)
# Запуск: открой этот файл и нажми ▶ вверху справа.
# Этот файл менять не нужно. Но его полезно прочитать: здесь видно,
# какие правила проверяет программа.

passed = 0
failed = 0


def check(condition, what):
    """Печатает результат одной проверки."""
    global passed, failed
    if condition:
        passed += 1
        print("  ✅", what)
    else:
        failed += 1
        print("  ❌", what)


print("Проверяю файл creatures.py...\n")

try:
    from creatures import creatures, ELEMENTS, BEATS
except Exception as error:
    print("❌ Файл creatures.py не запускается. Ошибка:")
    print("  ", type(error).__name__, "-", error)
    print("Подсказка: проверь запятые, кавычки и скобки рядом со строкой из ошибки.")
    raise SystemExit

FIELDS = ["name", "element", "hp", "attack", "defense", "speed"]

check(len(creatures) >= 3, "В списке минимум 3 существа")

names = []
for number, c in enumerate(creatures, start=1):
    print("\nСущество №" + str(number) + ":")
    has_all = all(field in c for field in FIELDS)
    check(has_all, "есть все поля: " + ", ".join(FIELDS))
    if not has_all:
        continue

    name = c["name"]
    check(isinstance(name, str) and name.strip() not in ("", "???"),
          "имя — это текст в кавычках, не пустое и не «???» (сейчас: " + repr(name) + ")")
    if isinstance(name, str):
        check(len(name) <= 20, "имя не длиннее 20 символов")
        names.append(name)

    check(c["element"] in ELEMENTS,
          "стихия из списка ELEMENTS (сейчас: " + repr(c["element"]) + ")")

    stats_are_numbers = all(isinstance(c[f], int) for f in ["hp", "attack", "defense", "speed"])
    check(stats_are_numbers, "характеристики — целые числа без кавычек")
    if not stats_are_numbers:
        continue

    check(20 <= c["hp"] <= 60, "здоровье от 20 до 60 (сейчас: " + str(c["hp"]) + ")")
    check(5 <= c["attack"] <= 20, "атака от 5 до 20 (сейчас: " + str(c["attack"]) + ")")
    check(0 <= c["defense"] <= 10, "защита от 0 до 10 (сейчас: " + str(c["defense"]) + ")")
    check(1 <= c["speed"] <= 10, "скорость от 1 до 10 (сейчас: " + str(c["speed"]) + ")")
    total = c["attack"] + c["defense"] + c["speed"]
    check(total <= 30, "атака + защита + скорость не больше 30 (сейчас: " + str(total) + ")")

print("\nВесь мир:")
check(len(names) == len(set(names)), "у всех существ разные имена")
elements_used = set(c.get("element") for c in creatures)
check(len(elements_used) >= 2, "в мире хотя бы 2 разные стихии")

print("\n⭐ Бонус:")
try:
    text = open("creatures.py", encoding="utf-8").read()
    after = text.split("# Мои слова:", 1)[1] if "# Мои слова:" in text else ""
    words = [line for line in after.splitlines() if line.strip().startswith("#") and len(line.strip()) > 10]
    if words:
        print("  ⭐ Есть объяснение словаря своими словами")
    else:
        print("  · Объяснение словаря своими словами пока не написано (это не обязательно)")
except Exception:
    pass

print("\nИтог:", passed, "проверок пройдено,", failed, "не пройдено.")
if failed == 0:
    print("🎉 Отлично! Отметь задание выполненным на платформе.")
else:
    print("Исправь проверки с ❌ и запусти ещё раз.")
