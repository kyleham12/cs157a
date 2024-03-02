import time

class HashMap:
    def __init__(self):
        self.map = {}

    def insert(self, session_id, data):
        self.map[session_id] = data

    def delete(self, session_id):
        if session_id in self.map:
            del self.map[session_id]

    def search(self, session_id):
        return self.map.get(session_id, None)

    def update(self, session_id, new_data):
        if session_id in self.map:
            self.map[session_id] = new_data

class Node:
    def __init__(self, session_id, timestamp):
        self.session_id = session_id
        self.timestamp = timestamp
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, session_id):
        new_node = Node(session_id, time.time())
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, session_id):
        current = self.head
        while current:
            if current.session_id == session_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                break
            current = current.next

    def search(self, session_id):
        current = self.head
        while current:
            if current.session_id == session_id:
                return current.timestamp
            current = current.next
        return None

    def update(self, session_id):
        current = self.head
        prev = None
        while current:
            if current.session_id == session_id:
                current.timestamp = time.time()
                if current == self.head:
                    break
                else:
                    prev.next = current.next
                    current.next = self.head
                    self.head = current
                break
            prev = current
            current = current.next

def main():
    print("Enter the following commands to perform their respective actions:")
    print("'Insert': Add a new user session with its corresponding data.")
    print("'Deletion': Remove a user session when it expires or the user logs out.")
    print("'Search': Retrieve session data using the session ID.")
    print("'Update': Update the timestamp of the last activity for a given session ID.")
    print("'q': Quits application.")

    map = HashMap()
    list = DoublyLinkedList()

    while True:
        command = input("Command: ")
        command = command.strip().lower()
        if command == 'q':
            print("Quiting application...")
            return None
        elif command == 'insert':
            userid = 0
            while True:
                try:
                    userid_input = input("Enter the user id: ")
                    userid = int(userid_input)
                except ValueError:
                    print("Invalid input. Please enter an integer user id: ")
                if userid in map:
                    print("Insertion failed because session has already been inserted. Try a different user id.")
                else: break
            data = input("Enter data for user: ")
            map.insert(userid, data)
            list.insert(userid)
        elif command == 'deletion':
            print()
        elif command == 'search':
            print()
        elif command == 'update':
            print()
        else:
            print("Invalid command. Try again\n\n")
            

if __name__ == "__main__":
    main()