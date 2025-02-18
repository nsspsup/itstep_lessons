class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, value):
        if not self.head:
            print("List is empty, nothing to delete.")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not found in the list.")
        else:
            temp.next = temp.next.next

    def contains(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def replace(self, old_value, new_value):
        temp = self.head
        while temp:
            if temp.data == old_value:
                temp.data = new_value
                return
            temp = temp.next
        print("Value not found in the list.")

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Function to handle user input and menu
def main():
    ll = LinkedList()

    # Initial user input
    numbers = input("Enter numbers separated by spaces: ").split()
    for num in numbers:
        ll.append(int(num))

    while True:
        print("\nMenu:")
        print("1. Add an item to the list")
        print("2. Delete an item from the list")
        print("3. Show the list contents")
        print("4. Check if the list contains a value")
        print("5. Replace a value in the list")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num = int(input("Enter the number to add: "))
            ll.append(num)

        elif choice == '2':
            num = int(input("Enter the number to delete: "))
            ll.delete(num)

        elif choice == '3':
            ll.display()

        elif choice == '4':
            num = int(input("Enter the number to check: "))
            if ll.contains(num):
                print(f"{num} is in the list.")
            else:
                print(f"{num} is not in the list.")

        elif choice == '5':
            old_val = int(input("Enter the value to replace: "))
            new_val = int(input("Enter the new value: "))
            ll.replace(old_val, new_val)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")


# Run the program
if __name__ == "__main__":
    main()
