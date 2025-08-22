[![tests](https://img.shields.io/github/actions/workflow/status/MypassionPython/Dupes/tests.yml?branch=main)](../../actions)
[![license](https://img.shields.io/github/license/MypassionPython/Dupes)](LICENSE)

# dupes
Сканує папку, рахує SHA256 і показує групи файлів з однаковим хешем.

## Вимоги
- Python 3.10+

## Використання
```bash
# Просканувати папку
python dupes.py D:\Media

# Ігнорувати дуже маленькі файли
python dupes.py D:\Media --min-size 10240
