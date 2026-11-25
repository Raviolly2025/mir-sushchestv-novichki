# МИР СУЩЕСТВ · Хранение истории боёв в файле history.json
# Работает, только когда запущен сервер (app.py). На GitHub-версии истории нет.

import json
import os

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "history.json")
MAX_BATTLES = 20          # храним только последние бои
MAX_NAME_LENGTH = 20


def load_history():
    """Читает историю. Файл мог сломаться или быть изменён — проверяем каждую запись."""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, encoding="utf-8") as f:
            data = json.load(f)
    except (ValueError, OSError):
        return []
    if not isinstance(data, list):
        return []
    good = []
    for item in data:
        if (isinstance(item, dict)
                and all(isinstance(item.get(k), str) and len(item[k]) <= MAX_NAME_LENGTH
                        for k in ("first", "second", "winner"))):
            good.append(item)
    return good[-MAX_BATTLES:]


def add_battle(first, second, winner):
    """Добавляет бой в историю и сохраняет файл."""
    history = load_history()
    history.append({"first": first, "second": second, "winner": winner})
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(history[-MAX_BATTLES:], f, ensure_ascii=False, indent=2)
