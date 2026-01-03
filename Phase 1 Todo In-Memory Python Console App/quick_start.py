#!/usr/bin/env python3
"""
Quick start script for the Menu-Driven Todo CLI Application
"""

def main():
    print("Menu-Driven Todo CLI Application")
    print("=" * 40)
    print("This application provides a menu-driven interface for managing tasks.")
    print("\nFeatures:")
    print("- Zero-padded numeric IDs (001, 002, 003, etc.)")
    print("- Clear menu interface with numbered options (1-6)")
    print("- Add, View, Update, Delete, Mark Complete/Incomplete, Exit")
    print("- In-memory storage (tasks lost on restart)")
    print("- Clean console output with visual separators")
    print("\nTo run the application, use: python src/todo_app.py")
    print("\nThe application will display a menu with these options:")
    print("  1. Add Task")
    print("  2. View Tasks")
    print("  3. Update Task")
    print("  4. Delete Task")
    print("  5. Mark Complete / Incomplete")
    print("  6. Exit")

if __name__ == "__main__":
    main()