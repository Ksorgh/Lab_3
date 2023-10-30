def find_common_participants(str1, str2, deli=','):
    part1 = set(str1.split(deli))
    part2 = set(str2.split(deli))
    common_participants = sorted(list(part1.intersection(part2)))
    return common_participants


fg = "Фролов,Сидоров,Пещачкин"
second = "Сидоров,Фролов,Овечкин"

print(find_common_participants(fg, second))


