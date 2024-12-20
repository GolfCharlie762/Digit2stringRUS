# Number to Text (Russian and English)

This Python library provides functionality to convert numbers into their textual representation in Russian, supporting grammatical cases and declensions for thousands, millions, and billions.

Эта библиотека Python предоставляет функционал для преобразования чисел в текстовое представление на русском языке, поддерживая грамматические падежи и склонения для тысяч, миллионов и миллиардов.

## Features / Особенности
- Converts numbers into Russian words. / Преобразует числа в текст на русском языке.
- Handles declensions for thousands, millions, and billions. / Обрабатывает склонения для тысяч, миллионов и миллиардов.
- Supports gender-specific forms (e.g., "одна тысяча" vs "один миллион"). / Поддерживает формы, зависящие от рода (например, "одна тысяча" и "один миллион").
- Works with any positive integer. / Работает с любыми положительными целыми числами.

## Installation / Установка

No external dependencies are required. Simply copy the `number_to_text` function into your project or include the script in your repository.

Не требует внешних зависимостей. Просто скопируйте функцию `number_to_text` в ваш проект или добавьте скрипт в репозиторий.

## Usage / Использование

### Example / Пример
```python
from number_to_text import number_to_text

# Convert a number to text
print(number_to_text(123456789))
```

### Output / Результат
```
сто двадцать три миллиона четыреста пятьдесят шесть тысяч семьсот восемьдесят девять
```

## Function Details / Подробности функции
### `number_to_text(n: int) -> str`
- **Parameters / Параметры**:
  - `n` (int): The number to convert. Must be a positive integer. / Число для преобразования. Должно быть положительным целым числом.
- **Returns / Возвращает**:
  - A string with the number in Russian words. / Строку с числом, записанным словами на русском языке.

## How It Works / Как это работает
1. Splits the number into groups of three digits (thousands, millions, billions). / Разбивает число на группы по три цифры (тысячи, миллионы, миллиарды).
2. Converts each group into text, applying proper gender rules and declensions. / Преобразует каждую группу в текст, применяя правила рода и склонения.
3. Combines the results into a full textual representation. / Объединяет результаты в полное текстовое представление.

### Example Conversions / Примеры преобразования
- `1` -> "один"
- `21` -> "двадцать один"
- `1050` -> "одна тысяча пятьдесят"
- `123456789` -> "сто двадцать три миллиона четыреста пятьдесят шесть тысяч семьсот восемьдесят девять"

## Contributing / Вклад
Contributions are welcome! Feel free to submit pull requests or open issues for improvements or bug fixes.

Принимаются любые предложения и доработки! Не стесняйтесь отправлять pull requests или открывать issues для улучшений или исправления ошибок.

## License / Лицензия
This project is licensed under the MIT License. See the `LICENSE` file for details.

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для подробностей.
