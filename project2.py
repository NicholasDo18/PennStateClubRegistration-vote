class ClubMember:
    def __init__(self, name, email, membership_status):
        self.name = name
        self.email = email
        self.membership_status = membership_status
        self.voted_roles = set()  # Track which roles the member has voted for

class Node:
    def __init__(self, member):
        self.member = member
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, member):
        new_node = Node(member)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, email):
        removed = False
        if not self.head:
            print("List is empty.")
            return
        if self.head.member.email == email:
            self.head = self.head.next
            removed = True
        else:
            current = self.head
            prev = None
            while current:
                if current.member.email == email:
                    prev.next = current.next
                    removed = True
                    break
                prev = current
                current = current.next
        if removed:
            print(f"Member with email {email} has been removed.")
        else:
            print("Member not found.")

class ClubVoteRegistrationSystem:
    def __init__(self):
        self.members = LinkedList()  # Linked list to store members
        self.poll_results = {
            'President': {'Candidate 1': 0, 'Candidate 2': 0},
            'Vice President': {'Candidate 1': 0, 'Candidate 2': 0},
            'Secretary': {'Candidate 1': 0, 'Candidate 2': 0},
            'Treasurer': {'Candidate 1': 0, 'Candidate 2': 0}
        }

    def register_member(self, name, email, membership_status):
        # Check if the member is already registered
        current = self.members.head
        while current:
            if current.member.email == email:
                print("Member already registered.")
                return
            current = current.next
        # Create a new ClubMember object
        member = ClubMember(name, email, membership_status)
        # Add the member to the linked list
        self.members.append(member)
        print(f"{name} successfully registered.")

    def verify_eligibility(self, email):
        # Check if the member exists
        current = self.members.head
        while current:
            if current.member.email == email:
                member = current.member
                # Check membership status for eligibility
                if member.membership_status == "Active":
                    print("Member is eligible to vote.")
                    return True
                else:
                    print("Member is not eligible to vote.")
                    return False
            current = current.next
        print("Member not found.")
        return False

    def remove_member(self, email):
        self.members.remove(email)

    def vote(self, email, role, candidate):
        # Check if the member exists and is eligible to vote
        current = self.members.head
        while current:
            if current.member.email == email:
                member = current.member
                if member.membership_status != "Active":
                    print("Member is not eligible to vote.")
                    return
                # Check if the member has already voted for this role
                if role in member.voted_roles:
                    print("Member has already voted for this role.")
                    return
                # Check if the role and candidate are valid
                if role not in self.poll_results or candidate not in self.poll_results[role]:
                    print("Invalid role or candidate.")
                    return
                # Record the vote
                self.poll_results[role][candidate] += 1
                member.voted_roles.add(role)
                print("Vote recorded successfully.")
                return
            current = current.next
        print("Member not found.")

    def display_poll_results(self):
        print("Poll Results:")
        for role, candidates in self.poll_results.items():
            total_votes_role = sum(candidates.values())
            print(f"{role}:")
            for candidate, votes in candidates.items():
                percentage = (votes / total_votes_role) * 100 if total_votes_role > 0 else 0
                print(f"{candidate}: {votes} votes ({percentage:.2f}%)")
            print()

    def list_registered_members(self):
        print("Registered Members:")
        current = self.members.head
        while current:
            print(f"Name: {current.member.name}, Email: {current.member.email}")
            current = current.next

def main():
    registration_system = ClubVoteRegistrationSystem()

    while True:
        print("\nClub Vote Registration System")
        print("1. Register Member")
        print("2. Verify Eligibility")
        print("3. Vote")
        print("4. Display Poll Results")
        print("5. Remove Member")
        print("6. List Registered Members")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter member's name: ")
            email = input("Enter member's email: ")
            membership_status = input("Enter member's membership status (Active/Not Active): ")
            while membership_status not in ["Active", "Not Active"]:
                print("Invalid membership status. Please enter 'Active' or 'Not Active'.")
                membership_status = input("Enter member's membership status (Active/Not Active): ")
            registration_system.register_member(name, email, membership_status)
        elif choice == "2":
            email = input("Enter member's email to verify eligibility: ")
            registration_system.verify_eligibility(email)
        elif choice == "3":
            email = input("Enter member's email to vote: ")
            role = input("Enter the role (President/Vice President/Secretary/Treasurer): ")
            candidate = input(f"Enter the candidate (Candidate 1/Candidate 2) for {role}: ")
            registration_system.vote(email, role, candidate)
        elif choice == "4":
            registration_system.display_poll_results()
        elif choice == "5":
            email = input("Enter member's email to remove: ")
            registration_system.remove_member(email)
        elif choice == "6":
            registration_system.list_registered_members()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

