def lucky_numbers(num, luckyset):
    if num > 1000:
        return

    if num != 0:
        luckyset.add(num)

    lucky_numbers(num * 10 + 4, luckyset)
    lucky_numbers(num * 10 + 7, luckyset)


def check(n, luckyset):
    for x in luckyset:
        if x != 0 and n % x == 0:
            return "YES"
    return "NO"


n = int(input())
luckyset = set()

lucky_numbers(0, luckyset)

print(check(n, luckyset))