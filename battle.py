# МИР СУЩЕСТВ · Движок боя (новички)
# Шаги — в задании на платформе. Запуск файла — кнопка ▶ вверху справа.
# Замени каждый "???" правильным значением. [САМ] — делаешь сам, AI может только подсказать.
# Застрял — возьми запрос к AI, который ты собрал в уровне «Найди сломанную функцию».

from creatures import BEATS


def element_multiplier(attacker_element, defender_element):
    """
    Множитель стихии:
      2.0 — стихия атакующего ПОБЕЖДАЕТ стихию защитника (суперэффективно);
      0.5 — стихия защитника побеждает стихию атакующего (неэффективно);
      1.0 — во всех остальных случаях.
    Пример: element_multiplier("fire", "nature") → 2.0
    """
    # [САМ] шаг 3
    if BEATS[attacker_element] == defender_element:
        return "???"
    if BEATS[defender_element] == "???":
        return 0.5
    return "???"


def calc_damage(attacker, defender, power=1.0):
    """
    Урон = int(атака × сила приёма × множитель) − защита.
    int() отбрасывает дробную часть: int(4.5) = 4.
    Пример: атака 12, сила 1.0, множитель 2.0, защита 8 → 24 − 8 = 16
    """
    mult = element_multiplier(attacker["element"], defender["element"])
    damage = int(attacker["attack"] * power * mult) - defender["defense"]
    # [САМ] шаг 4: урон не может быть меньше 1
    if damage < 1:
        damage = "???"
    return damage


# ⭐ [С AI] бонус: замени эту функцию ответом AI и прочитай его комментарии
def is_super_effective(attacker, defender):
    pass


# Бой целиком для сайта (готовая функция — читай, не меняй)
def fight(a, b, max_turns=50):
    """
    Бой целиком: возвращает (список строк лога, победитель).
    Первым ходит тот, у кого выше скорость. Существа из списка не меняются —
    бьются их копии.
    """
    a = dict(a)
    b = dict(b)
    log = []
    if b["speed"] > a["speed"]:
        attacker, defender = b, a
    else:
        attacker, defender = a, b
    turn = 1
    while a["hp"] > 0 and b["hp"] > 0 and turn <= max_turns:
        damage = calc_damage(attacker, defender)
        defender["hp"] = max(0, defender["hp"] - damage)
        line = str(turn) + ". " + attacker["name"] + " → " + defender["name"] + ": -" + str(damage)
        if is_super_effective(attacker, defender):
            line += " (суперэффективно!)"
        log.append(line)
        attacker, defender = defender, attacker
        turn += 1
    winner = a if a["hp"] > 0 else b
    return log, winner
