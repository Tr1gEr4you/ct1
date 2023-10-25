import random

goodbye_count = 0
while goodbye_count < 3:
    user_input = input("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?! ").strip()

    if user_input == "ПОКА!":
        goodbye_count += 1
        if goodbye_count < 3:
            print("НЕТ, НИ РАЗУ С", random.randint(1930, 1950), "ГОДА!")
        else:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
    elif user_input.isupper():
        year = random.randint(1930, 1950)
        print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")





