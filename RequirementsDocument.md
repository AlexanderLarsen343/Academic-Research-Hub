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
| Triggers          | A student clicks on the sign in page or create account  |
| Preconditions     | Account cannot already exist when registering.   |
| Actions           | 1. A student clicks on the "Sign in" page <br>2. They click 'register' for account <br>3. They input they information like username, password, and email. <br>4. System will check validation of submission (character limitations and required fields) <br>5. If passed validation, a new user account will be created for the student and their information stored in the system |
| Postconditions    |Student account is now in the database  |
| Acceptance tests  |Add a student either in python or through the app and query the database manually  |
| Iteration         |Iteration 2  |

| Use case # 1      |   |
| ------------------ |--|
| Name              | "enter your reponse here"  |
| Users             | "enter your reponse here"  |
| Rationale         | "enter your reponse here"  |
| Triggers          | "enter your reponse here"  |
| Preconditions     | "enter your reponse here"  |
| Actions           | "enter your reponse here"  |
| Alternative paths | "enter your reponse here"  |
| Postconditions    | "enter your reponse here"  |
| Acceptance tests  | "enter your reponse here"  |
| Iteration         | "enter your reponse here"  |

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

