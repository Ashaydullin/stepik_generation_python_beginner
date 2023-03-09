genom = str(input().lower())
print(
      f"Аденин: {genom.count('а')}",
      f"Гуанин: {genom.count('г')}",
      f"Цитозин: {genom.count('ц')}",
      f"Тимин: {genom.count('т')}",
      sep = "\n"
      )