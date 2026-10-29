Citizen Complaint System (Digital Public Goods Solution)

Overview
The Citizen Complaint System is an open-source, digital public service tool developed as part of the Object-Oriented Programming (PROG211) curriculum at Limkokwing University of Creative Technology, Sierra Leone. It enables citizens to report civic issues (such as road damage, water supply failures, and waste management problems) directly to local government authorities, ensuring transparent tracking and community-driven accountability.

This project has been designed and implemented to adhere strictly to Digital Public Goods (DPG) standards, promoting open-source collaboration, inclusivity, and data privacy.

Alignment with Digital Public Goods (DPG) Standards

Digital Public Goods are open-source software, open data, open AI models, open standards, or open content collections that adhere to privacy and other applicable laws, do no harm, and help attain the Sustainable Development Goals (SDGs). This project aligns with DPG principles in the following ways:

Open-Source Software & Transparency
GitHub Repository: The complete source code is hosted publicly on GitHub, allowing friends review, community contributions, and public auditing.

Modularity: Built using modular Object-Oriented Programming (OOP) principles in Python, making it easy for other developers or municipal bodies to fork, extend, and adapt the code for other public administrative services.

Inclusive and Accessible Design
The platform provides a straightforward, text-based interface for citizens regardless of high-end infrastructure constraints.
It addresses fundamental urban issues (e.g., water supply failures, municipal waste) affecting local communities, ensuring the tool serves vulnerable and underserved populations directly.

Privacy-Respecting Architecture
The system is designed to minimize the collection of sensitive personal data, utilizing lightweight record structures that prioritize functional reporting over invasive profiling.

Technical Implementation & OOP Architecture
The solution fulfills all criteria outlined in the PROG211 assignment brief using Python:

Task 1: OOP Basics (Classes, Attributes & Objects)
Implemented two primary classes: Citizen and Complaint (inheriting from Citizen).
Encapsulates attributes such as name, National_i, Age, Description, and Location.

Task 2: Python Data Structures
Utilizes lists and dictionary data structures (within complaint_registry) to store, append, and display multiple user and complaint records dynamically.

Task 3: Methods
Instance Methods: E.g., see_complaint_info() for rendering individual complaint details.
Class Methods@classmethod): E.g., display_info() to access shared registry data across class instances.

Static Methods (@staticmethod): E.g., register() for helper utility actions without tightly bound instance states.

Example Usage & Code Execution

Below is a sample of how the program executes and manages citizen complaints:

# Initialization of citizen and complaint objects
citizen = Citizen("alfred", "we123", 786)
complaint = Complaint("angella", "N3425", 14, "I am Having water issues", "new England ville")
complaint2 = Complaint("kabia", "fg45", 12, "i want to eat", "sierra leone")
citizen.register("vandi", "wer34", 12)

# Displaying registry and formatted outputs
print(complaint.display_info())
complaint.see_complaint_info()


Sample Output:

User name: vandi
Id: wer34
Age:12
[{'Name': 'angella', 'National_id': 'N3425', 'Age': 14, 'Description': 'I am Having water issues', 'Location': 'new England ville'}, {'Name': 'kabia', 'National_id': 'fg45', 'Age': 12, 'Description': 'i want to eat', 'Location': 'sierra leone'}]
************************************************==
Problem Affecting people
User: angella
Problem: I am Having water issues
Location: new England ville
************************************************==
************************************************==
Problem Affecting people
User: kabia
Problem: Bad Road
Location: sierra leone
************************************************==
