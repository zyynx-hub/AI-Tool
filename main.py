from modules.reader import get_prepared_dataframe
from modules.qa_engine import vraag_ai

def main():
    df = get_prepared_dataframe("data/input.xlsx")

    while True:
        vraag = input("Stel je vraag aan de AI (of typ 'exit'): ")
        if vraag.lower() == "exit":
            break
        antwoord = vraag_ai(df, vraag)
        print("\nAI antwoord:")
        print(antwoord)
        print("-" * 50)

if __name__ == "__main__":
    main()
