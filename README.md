# Преобразование чисел в текст (русский)

Эта библиотека Python предоставляет функциональность для преобразования чисел в их текстовое представление на русском языке, поддерживая грамматические падежи и склонения для тысяч, миллионов и миллиардов.

## Особенности
- Преобразует числа в русские слова.
- Обрабатывает склонения для тысяч, миллионов и миллиардов.
- Поддерживает формы, зависящие от пола (например, "одна тысяча" против "один миллион").
- Работает с любым положительным целым числом.

## Установка

Никаких внешних зависимостей не требуется. Просто скопируйте функцию `number_to_text` в свой проект или добавьте скрипт в свой репозиторий.

## Использование

### Пример
``python
из number_to_text импортирует number_to_text

# Преобразовать число в текст
для печати(number_to_text(123456789))
```

### Вывод
```
сто двадцать три миллиона четыреста пятьдесят шесть тысяч семьсот восемьдесят девять
```

## Подробные сведения о функции
### `number_to_text(n: int) -> str`
- **Параметры**:
  - `n` (int): число для преобразования. Должно быть положительным целым числом.
- **Возвращает**:
  - Строка с номером, написанным русскими словами.

## Как это работает
1. Разбивает число на группы из трех цифр (тысячи, миллионы, миллиарды).
2. Преобразует каждую группу в текст, применяя соответствующие правила рода и склонения.
3. Объединяет результаты в полное текстовое представление.

### Примеры преобразований
- `1` -> "один"
- `21` -> "двадцать один"
- `1050` -> "одна тысяча пятьдесят"
- `123456789` -> "сто двадцать три миллиона четыреста пятьдесят шесть тысяч семьсот восемьдесят девять"

## Внесение вклада
Приветствуется вклад! Не стесняйтесь отправлять запросы на доработку или открывать вопросы для улучшения или исправления ошибок.

## Лицензия
Этот проект лицензирован по лицензии MIT. Подробности смотрите в файле `ЛИЦЕНЗИЯ`.
# Number to Text (Russian)

This Python library provides functionality to convert numbers into their textual representation in Russian, supporting grammatical cases and declensions for thousands, millions, and billions.

## Features
- Converts numbers into Russian words.
- Handles declensions for thousands, millions, and billions.
- Supports gender-specific forms (e.g., "одна тысяча" vs "один миллион").
- Works with any positive integer.

## Installation

No external dependencies are required. Simply copy the `number_to_text` function into your project or include the script in your repository.

## Usage

### Example
```python
from number_to_text import number_to_text

# Convert a number to text
print(number_to_text(123456789))
```

### Output
```
сто двадцать три миллиона четыреста пятьдесят шесть тысяч семьсот восемьдесят девять
```

## Function Details
### `number_to_text(n: int) -> str`
- **Parameters**:
  - `n` (int): The number to convert. Must be a positive integer.
- **Returns**:
  - A string with the number in Russian words.

## How It Works
1. Splits the number into groups of three digits (thousands, millions, billions).
2. Converts each group into text, applying proper gender rules and declensions.
3. Combines the results into a full textual representation.

### Example Conversions
- `1` -> "один"
- `21` -> "двадцать один"
- `1050` -> "одна тысяча пятьдесят"
- `123456789` -> "сто двадцать три миллиона четыреста пятьдесят шесть тысяч семьсот восемьдесят девять"

## Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for improvements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
