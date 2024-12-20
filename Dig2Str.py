def number_to_text(n):
    ones = [
        "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"
    ]
    ones_female = [
        "ноль", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"
    ]
    tens = [
        "", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
        "девяносто"
    ]
    teens = [
        "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
        "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"
    ]
    hundreds = [
        "", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"
    ]
    thousands = ["тысяча", "тысячи", "тысяч"]
    millions = ["миллион", "миллиона", "миллионов"]
    billions = ["миллиард", "миллиарда", "миллиардов"]

    def get_gendered_ones(num, gender):
        return ones_female[num] if gender == "female" else ones[num]

    def declension(count, forms):
        if 10 <= count % 100 <= 20:
            return forms[2]
        if count % 10 == 1:
            return forms[0]
        if 2 <= count % 10 <= 4:
            return forms[1]
        return forms[2]

    def triplet_to_text(triplet, gender="male"):
        result = []
        if triplet[0] != 0:
            result.append(hundreds[triplet[0]])
        if triplet[1] == 1:
            result.append(teens[triplet[2]])
        else:
            if triplet[1] != 0:
                result.append(tens[triplet[1]])
            if triplet[2] != 0:
                result.append(get_gendered_ones(triplet[2], gender))
        return " ".join(result)

    def split_number(n):
        num_str = f"{n:,}".replace(",", "")
        num_str = num_str.zfill((len(num_str) + 2) // 3 * 3)
        return [list(map(int, num_str[i:i + 3])) for i in range(0, len(num_str), 3)]

    if n == 0:
        return ones[0]

    parts = split_number(n)
    result = []
    unit_forms = [None, thousands, millions, billions]

    for i, triplet in enumerate(parts):
        gender = "male" if i != 1 else "female"
        if triplet != [0, 0, 0]:
            triplet_text = triplet_to_text(triplet, gender)
            if i > 0:
                triplet_text += f" {declension(int(''.join(map(str, triplet))), unit_forms[i])}"
            result.append(triplet_text)

    return " ".join(result[::-1])
