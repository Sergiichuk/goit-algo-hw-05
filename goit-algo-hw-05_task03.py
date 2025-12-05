import timeit

# Алгоритм КМП
def kmp_search(text, pattern):
    if pattern == "":
        return 0
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    if pattern == "":
        return 0
    m, n = len(pattern), len(text)
    p, t, h = 0, 0, 1
    q = 101
    for i in range(m - 1):
        h = (h * 256) % q
    for i in range(m):
        p = (256 * p + ord(pattern[i])) % q
        t = (256 * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (256 * (t - ord(text[i]) * h) + ord(text[i + m])) % q
    return -1


# Алгоритм Боєра–Мура
def boyer_moore(text, pattern):
    if pattern == "":
        return 0
    m = len(pattern)
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    i = m - 1
    while i < len(text):
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1
        if j == -1:
            return k + 1
        i += skip.get(text[i], m)
    return -1


# Функції для завантаження текстів 
def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# Замір часу 
def measure_time(func, text, substring):
    return timeit.timeit(lambda: func(text, substring), number=10)



def main():
    print("= Порівняння алгоритмів пошуку підрядка =")
    text1 = load_text("texts/text1.txt")
    text2 = load_text("texts/text2.txt")

    existing = "алгоритм"          # реальний підрядок
    nonexistent = "abrakadabra"    # вигаданий

    algorithms = {
        "Boyer-Moore": boyer_moore,
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp
    }

    for name, text in [("Текст 1", text1), ("Текст 2", text2)]:
        print(f"\n--- {name} ---")
        for alg_name, func in algorithms.items():
            t_exist = measure_time(func, text, existing)
            t_fake = measure_time(func, text, nonexistent)
            print(f"{alg_name}: знайдений = {t_exist:.6f} c, не знайдений = {t_fake:.6f} c")


if __name__ == "__main__":
    main()

