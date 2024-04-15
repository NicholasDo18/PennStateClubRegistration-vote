class ClubMember:
  def __init__(self, name, email, membership_status):
      self.name = name
      self.email = email
      self.membership_status = membership_status
      self.voted_roles = set()  # Track which roles the member has voted for

class ClubVoteRegistrationSystem:
  def __init__(self):
      self.members = {}  # Dictionary to store members
      self.poll_results = {
          'President': {'Candidate 1': 0, 'Candidate 2': 0},
          'Vice President': {'Candidate 1': 0, 'Candidate 2': 0},
          'Secretary': {'Candidate 1': 0, 'Candidate 2': 0},
          'Treasurer': {'Candidate 1': 0, 'Candidate 2': 0}
      }

  def register_member(self, name, email, membership_status):
      # Check if the member is already registered
      if email in self.members:
          print("Member already registered.")
          return
      # Create a new ClubMember object
      member = ClubMember(name, email, membership_status)
      # Add the member to the dictionary
      self.members[email] = member
      print(f"{name} successfully registered.")

  def verify_eligibility(self, email):
      # Check if the member exists
      if email not in self.members:
          print("Member not found.")
          return False
      member = self.members[email]
      # Check membership status for eligibility
      if member.membership_status == "Active":
          print("Member is eligible to vote.")
          return True
      else:
          print("Member is not eligible to vote.")
          return False

  def vote(self, email, role, candidate):
      # Check if the member exists and is eligible to vote
      if email not in self.members:
          print("Member not found.")
          return
      member = self.members[email]
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

  def display_poll_results(self):
      print("Poll Results:")
      total_votes = sum(sum(role.values()) for role in self.poll_results.values())
      for role, candidates in self.poll_results.items():
          print(f"{role}:")
          for candidate, votes in candidates.items():
              percentage = (votes / total_votes) * 100 if total_votes > 0 else 0
              print(f"{candidate}: {votes} votes ({percentage:.2f}%)")
          print()


def main():
  registration_system = ClubVoteRegistrationSystem()

  while True:
      print("\nClub Vote Registration System")
      print("1. Register Member")
      print("2. Verify Eligibility")
      print("3. Vote")
      print("4. Display Poll Results")
      print("5. Exit")

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
          print("Exiting program.")
          break
      else:
          print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
