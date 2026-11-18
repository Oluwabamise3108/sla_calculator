## 1. Ticket ID with surrounding space and different cases are accepted

**Context:** The rule says the ticket ID must start with TCK-. A user
may paste an ID with space before or after it, or enter in a lowercase.

**Alternative considered:** Make user reenter the ID in an acceptable form (TCK-) in uppercase.

**Reason:** This is used by the organization itself to check the status of a ticket.
Accepting all case and spaces allows the status check to be faster for the user.
The advantage is that the user that cannot see the space or time conscious to meet a quota does not have to worry about letter cases or extra spaces


## 2. y and n are accepted 

**Context:** The rule says the user must enter yes or no if a response was already given
User can use y in place of yes or n in place of no.

**Alternative considered:** Make user spell out the yes or no on each run

**Reason:** Again user need to move fast through the program to get the status of a ticket.
The program is all set to make that as fast as possible. The cost is that user might enter 'y' or 'n' as a mistake and it will still go through and accepted as a valid answer


## 3. When user enter an empty ticket ID

**Context:** The rule says the user must enter a ticket ID.
User might mistakenly skip the ticket ID input

**Alternative considered:** Advise user the ticket ID input cannot be empty

**Reason:** Decided to stick with the same response "Ticket is invalid. Must start with TCK-"
Chose that because member might initially not understand which is the ticket ID, the response also provided a direction to what is needed.