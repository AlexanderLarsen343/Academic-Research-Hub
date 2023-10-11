# Software Requirements Specification

## 
--------
Prepared by:

* `<Alexander Larsen>`,`<Voiland College>`
* `<Erick Pairault>`,`<Voiland College>`
* `<Gabriel Muccillo Hartz>`,`<Voiland College>`
* `<author1>`,`<Voiland College>`

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [Your Project Title](#your-project-title)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. User Interface](#3-user-interface)
- [4. Product Backlog](#4-product-backlog)
- [4. References](#4-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2023-10-05 |Initial draft | 1.0        |
|Revision 2|      |         |         |
|      |      |         |         |

----
# 1. Introduction

This is an application where students can find job positionings demanding a certain set of skills that are posted by professors. To create such application, we will used Flask as our base functionality, SQL alchemy for our database, HTML for templates, CSS for styling, and maybe Bootstrap for more styling. 

## 1.1 Document Purpose

The purpose of this document is to create a foundation of ideas of our project to make sure all group members are on the same page.

## 1.2 Product Scope

The purpose of our application is to create a convient and easy connection between professors creating research opportunities and students for looking those oppotunities. Both parties should be able to have a secured account with login. Professors will be able to post opportunities and view student applications. Students will be able to browse posted opportunities and apply. 

## 1.3 Document Overview

The rest of the document will go indepth on both functional and nonfunctional requirements. Going over what the end goal is for each user, we will create a list of use cases that will then shape the functionality of our system.

----
# 2. Requirements Specification
This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

## 2.1 Customer, Users, and Stakeholders

The main users of this application will be students and professors. The customer and stakeholer in this scenario will be the instituion that makes use of this software.

----
## 2.2 Use Cases

This section will go over all use case for all iterations of the project. Each use case will be either from the perspective of the professor or student.

For each use case you should have the following:

* Name,
* Actors,
* Triggers (what initiates the use case),
* Preconditions (in what system state is this use case applicable),
* Actions (what actions will the code take to implement the use case),
* Alternative paths
* Postconditions (what is the system state after the use case is done),
* Acceptance tests (list one or more acceptance tests with concrete values for the parameters, and concrete assertions that you will make to verify the postconditions).

Each use case should also have a field called "Iteration" where you specify in which iteration you plan to implement this feature.

You may use the following table template for your use cases. Copy-paste this table for each use case you will include in your document.

| Use case # 1      |As a student, I want to be able to register an account|
| ------------------ |--|
| Name              | Add registration  |
| Users             | Student  |
| Rationale         | A student needs to be able to create an account  |
| Triggers          | A student navigates to registration  |
| Preconditions     | Account cannot already exist when registering.   |
| Actions           | 1. A student clicks on the "Sign in" page <br>2. They click 'register' for account <br>3. They input they information like username, password, and email. <br>4. System will check validation of submission (character limitations and required fields) <br>5. If passed validation, a new user account will be created for the student and their information stored in the system |
|Alternative Path | If the account already exists, then the user will just be redirected to the same page upon submission.
| Postconditions    |Student account is now in the database  |
| Acceptance tests  |Add a student either in python or through the app and query the database manually  |
| Iteration         |Iteration 2  |

| Use case # 2      |  As a user, I want to be able to log into my account |
| ------------------ |--|
| Name              | Add Login  |
| Users             | Student  |
| Rationale         | Accounts have all your information and are how studnets apply. They must be able to login |
| Triggers          |  Student navigates to login page |
| Preconditions     | Page is already loaded and student is not already signed in |
| Actions           |  1. Student enters into the signin page <br> 2. Student enters their username and password <br> 3. System will check validation of fields and query the database for a match <br> 4. If succesfull, Student is navigated to the home page with their account |
| Alternative paths | Submission is invalid and student is navigated to the same login page with errors  |
| Postconditions    | Student user is now in their account  |
| Acceptance tests  | Test via creating a user and logging in  |
| Iteration         | Iteration 2  |

| Use case # 2      ||
| ------------------ |--|
| Name              | |
| Users             | |
| Rationale         | |
| Triggers          | |
| Preconditions     | |
| Actions           | |
| Postconditions    | |
| Acceptance tests  | |
| Iteration         | |

| Use case # 2      ||
| ------------------ |--|
| Name              | |
| Users             | |
| Rationale         | |
| Triggers          | |
| Preconditions     | |
| Actions           | |
| Postconditions    | |
| Acceptance tests  | |
| Iteration         | |

| Use case # 2      ||
| ------------------ |--|
| Name              | |
| Users             | |
| Rationale         | |
| Triggers          | |
| Preconditions     | |
| Actions           | |
| Postconditions    | |
| Acceptance tests  | |
| Iteration         | |

| Use case # 2      ||
| ------------------ |--|
| Name              | |
| Users             | |
| Rationale         | |
| Triggers          | |
| Preconditions     | |
| Actions           | |
| Postconditions    | |
| Acceptance tests  | |
| Iteration         | |

| Use case # 2      ||
| ------------------ |--|
| Name              | |
| Users             | |
| Rationale         | |
| Triggers          | |
| Preconditions     | |
| Actions           | |
| Postconditions    | |
| Acceptance tests  | |
| Iteration         | |

| Use case # 13      |   |
| ------------------ |--|
| Name              | View Student Qualifications  |
| Users             | Faculty Users  |
| Rationale         | A faculty user should be able to view the qualifications of a student to make an informed decision as to whether or not they should proceed with approving them for an interview.  |
| Triggers          | The faculty selects “View Student Qualifications”.  |
| Preconditions     | Student(s) have applied for the research position, and the student(s) have all the appropriate criteria filled out.  |
| Actions           | 1. The user selects “View Student Qualifications”.<br>2. The software displays the student’s GPA, technical elective courses they have taken, research topics they are interested in, programming languages they have experience with, and prior research experience.  |
| Alternative paths | 1. After step 2, the user may choose to close the page that displays the student’s qualifications.  |
| Postconditions    | The student’s information is displayed to the faulty user.  |
| Acceptance tests  | Make sure that the student’s information that is displayed correctly contains their GPA, technical elective courses, research topics, programming language, and prior research experience.  |
| Iteration         | Iteration 2  |

| Use case # 14      |   |
| ------------------ |--|
| Name              | Approve for Interview  |
| Users             | Faculty Users  |
| Rationale         | A faculty user after having reviewed a student’s profile, should be able to have the ability to approve or decline the student for an interview. This is also relevant for the student who should be able to check their application later to see if they were accepted or not for an interview.  |
| Triggers          | The faculty selects the “Approve/Decline for interview” option.  |
| Preconditions     | There are student applications for the research position the faculty has posted/ is looking at.  |
| Actions           | 1. The user selects a research position they have posted.<br>2. The software displays the list of students who have applied for the position.<br>3. The faculty selects “Approve/Decline for interview” for the application(s) they desire.<br>4. The software asks for confirmation from the user.<br>5. The user selects their choice.<br>6. The software updates the application(s) according to the choice.  |
| Alternative paths | 1. In step 3, the user can select multiple applications to Approve or Decline for interview at a time. In the case they choose multiple, the software will specify all the applications that have been selected for Approval/Rejection for confirmation.<br>2. In step 5, the user can select to not confirm their selection the software will return to the list of students that have applied for the position.  |
| Postconditions    | Student Applications for the research position will have “Approved/Rejected for interview” updated on their application.  |
| Acceptance tests  | Make sure that all applications the user accepted or rejected have been appropriately displayed on their profile.  |
| Iteration         | Iteration 3  |


| Use case # 15      |   |
| ------------------ |--|
| Name              | Update Status of Application  |
| Users             | Faculty Users  |
| Rationale         | A faculty user after having interviewed a student, should be able to have the ability to hire or reject a student for the position. This is also relevant for the student who should be able to check their application later to see if they were accepted or not for the research position.  |
| Triggers          | The faculty selects the “Hire/Decline” option. |
| Preconditions     | There are student applications for the research position the faculty has posted, and the application the user is looking at has already been “Approved for Interview”. |
| Actions           | 1. The user selects a research position they have posted.<br>2. The software displays the list of students who have applied for the position.<br>3. The user selects a student application that has already been “Approved for Interview”.<br>4. The software displays the student application.<br>5. The user selects “Update Status of Application”.<br>6. The software asks “Hire/Decline”.<br>7. The user selects their choice.<br>8. The software asks for confirmation from the user.<br>9. The user selects their choice.<br>10. The software updates the application according to the choice.  |
| Alternative paths | 1. In step 3, the user may select an application that has not been “Approved for Interview” and in this case when the user selects “Update Status of Application” the software will not display the options to “Hire/Decline”.<br>2. In step 9, if the user chooses to not confirm their choice the software will return to the student application.  |
| Postconditions    | Student Applications for the research position will have “Hired/Declined” updated on their application.  |
| Acceptance tests  | Make sure that all applications the user hired or declined have been appropriately displayed on their profile.  |
| Iteration         | Iteration 3  |


| Use case # 16      |   |
| ------------------ |--|
| Name              | Delete Research Position  |
| Users             | Faculty Users  |
| Rationale         | A faculty user may need to delete a research position because all the slots are filled, there wasn’t enough funding, or because an error that requires the position to be removed.  |
| Triggers          | The faculty selects “Delete Research Position”.  |
| Preconditions     | The research position already exists.  |
| Actions           | 1. The user selects “Delete Research Position”.<br>2. The software asks for confirmation from the user.<br>3. The user selects “yes”.<br>4. The software removes the research position and updates all the applications for the position. |
| Alternative paths | 1. In step 3, the user may select no, and the software returns to the research position page.  |
| Postconditions    | The research position doesn’t exist and application for the position show “Position is not available”.  |
| Acceptance tests  | Make sure that the research position no longer appears and that on the status of all applications it is stated “Position is not available”.  |
| Iteration         | Iteration 3  |
----
## 2.3 Non-Functional Requirements

List the non-functional requirements in this section.

You may use the following template for non-functional requirements.

1. [Enter a Concise Requirement Name]:  [provide a concise description, in clear and easily understandable language to specify the requirement]

----
# 3. User Interface

Here you should include the sketches or mockups for the main parts of the interface.

----
# 4. Product Backlog

Here you should include a link to your GitHub repo issues page, i.e., your product backlog. Make sure to create an issue for each use case. You should also create issues for the initial development tasks that you plan to work on during iteration1. 

----
# 4. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.

----
----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 

| Max Points  | **Content** |
| ----------- | ------- |
| 10          | Do the requirements clearly state the customers’ needs? |
| 5           | Do the requirements avoid specifying a design (note: customer-specified design elements are allowed; non-functional requirements may specify some major design requirements)? |
| | |  
|    | **Completeness** |
| 25 | Are use cases written in sufficient detail to allow for design and planning? |
| 4 | Do use cases have acceptance tests? | 
| 25 | Is your use case model complete? Are all major use cases included in the document? |
| 10 |  Are the User Interface Requirements given with some detail? Are there some sketches, mockups?  |
| | |  
|   | **Clarity** |
| 5 | Is the document carefully written, without typos and grammatical errors? |
| 4 | Is each part of the document in agreement with all other parts? |
|   | Are all items clear and not ambiguous? (Minor document readability issues should be handled off-line, not in the review, e.g. spelling, grammar, and organization). |
|   |   |
|    | **GitHub Issues** |
| 12 | Has the team setup their GitHub Issues page? Have they  generated the list of user stories, use-cases, created milestones, assigned use-cases (issues) to milestones?   Example GitHub repo (check the issues): https://github.com/WSU-CptS322-Fall2022/TermProjectSampleRepo/issues  |

