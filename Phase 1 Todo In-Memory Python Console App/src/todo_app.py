import sys
import os
# Add the project root to the path so imports work when running from command line
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from src.services.task_manager import TaskManager
from src.cli.menu_interface import MenuInterface


def main():
    """
    Main application entry point for the menu-driven todo application.
    Initializes the task manager and menu interface, then runs the main loop.
    """
    print("Starting Todo Application...")

    # Initialize the task manager and menu interface
    task_manager = TaskManager()
    menu_interface = MenuInterface(task_manager)

    # Main application loop
    while True:
        try:
            # Display the menu
            menu_interface.display_menu()

            # Get user choice
            choice = menu_interface.get_user_choice()

            # Process the user's choice
            if choice == "1":
                menu_interface.handle_add_task()
            elif choice == "2":
                menu_interface.handle_view_tasks()
            elif choice == "3":
                menu_interface.handle_update_task()
            elif choice == "4":
                menu_interface.handle_delete_task()
            elif choice == "5":
                menu_interface.handle_toggle_completion()
            elif choice == "6":
                if menu_interface.handle_exit():
                    break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

    print("Application closed.")


if __name__ == "__main__":
    main()