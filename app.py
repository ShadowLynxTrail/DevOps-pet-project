import daterime
import random

morning_mottos = [
    "Системное мышление — ключ к успеху.",
    "CI/CD — это не боль, а автоматизация.",
    "Работает? Не трогай!",
    "Лучше сделать и переделать, чем не сделать вообще."
]

def main():
 print("===DevOps Pet Project ===")
 print(f"Время запуска:{datetime.datetime.now()}")
 print(f"Девиз дня:{random.choise(morning_mottos)}")

if __name__ == "__main__":
  main()
