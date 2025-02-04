def find_word(f, word):
    g_idx = 0
    for line in f:
        line = line.lower()
        idx = 0
        while idx != -1:
            idx = line.find(word, idx)
            if idx > -1:
                yield g_idx + idx
                idx += 1

        g_idx += len(line)


try:
    with open("soft_rolls.md", encoding="utf-8") as file:
        a = find_word(file, "мягкие булки")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден!")
except:
    print("Ошибка обработки файла!")
