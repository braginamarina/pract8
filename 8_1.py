
capitals = {"Россия": "Москва","Франция": "Париж","Германия": "Берлин","Италия": "Рим","Япония": "Токио"}

print("Все пары страна-столица:")
for country, capital in capitals.items():
    print(f"{country} -> {capital}")

country_name = input("\nВведите название страны: ")
if country_name in capitals:
    print(f"Столица {country_name}: {capitals[country_name]}")
else:
    print("Страна не найдена")

sorted_capitals = dict(sorted(capitals.items()))
print("\nСловарь в алфавитном порядке стран:")
for country, capital in sorted_capitals.items():
    print(f"{country} -> {capital}")