from Agentic_Agent.piplimimg import entryPoint
from Tools.Rag.system_setup import createChromaDB
from fileLoder.fileLoder import file_loaders
import os

os.environ["USER_AGENT"] = "my-streamlit-app"

# Run:
# python -m Agentic_Agent.main
# streamlit run Agentic_Agent/main.py


def main():

    print("=" * 50)
    print("🤖 Agentic AI Assistant")
    print("Type 'exit' to quit")
    print("=" * 50)

    while True:

        print("\n1. Ask Question")
        print("2. Upload File")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":

            user_input = input("Ask Anything: ")

            result = entryPoint(user_input)

            print("\n" + "=" * 20)
            print("FINAL ANSWER:")
            print(result["final_answer"])
            print("=" * 20 + "\n")

        elif choice == "2":

            file_path = input("Enter PDF path: ")

            file = file_loaders(file_path)

            createChromaDB(file)

            print("Document indexed successfully.")

        elif choice == "3":
            break
