# Simple Notepad Application

class Notepad:
    def __init__(self):
        self.notes = []

    def show_menu(self):
        print("\n=== Notepad Menu ===")
        print("1. View Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Exit")

    def view_notes(self):
        print("\n=== Your Notes ===")
        if not self.notes:
            print("No notes available.")
        else:
            for idx, note in enumerate(self.notes, start=1):
                print(f"{idx}. {note}")

    def add_note(self):
        note = input("Enter your note: ")
        self.notes.append(note)
        print("Note added successfully!")

    def delete_note(self):
        self.view_notes()
        if not self.notes:
            return

        try:
            note_index = int(input("Enter the number of the note to delete: "))
            if 1 <= note_index <= len(self.notes):
                deleted_note = self.notes.pop(note_index - 1)
                print(f"Note '{deleted_note}' deleted successfully!")
            else:
                print("Invalid note number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.view_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                self.delete_note()
            elif choice == "4":
                print("Exiting Notepad. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    notepad = Notepad()
    notepad.run()
