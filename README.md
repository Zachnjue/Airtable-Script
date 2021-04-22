# Airtable-Script

Based on a Script given for interviewees as shown below:

Scripting Assignment
Part 1: Scripting
**HIGH LEVEL OBJECTIVE**
Write a script to gather the list of installed applications on your macOS computer and create a basic report of unapproved
applications in Airtable. We expect the assignment to take a few hours to complete.

**DETAILS**
The script should perform three steps:
1. Gather a list of bundle identifiers of the applications that are installed on a macOS computer.
2. Retrieve a list of approved bundle identifiers from a specific Airtable base.
3. Create a "report" (i.e. an Airtable record) that contains computer's hostname and the list of unapproved bundle
identifiers.

To retrieve the list of approved bundle identifiers: you'll need an Airtable account (https://airtable.com/signup). Then, visit this
shared base https://airtable.com/shr2ELsDUq9FTMoS0 and click "Copy base". This approved bundle identifiers are in the
Approved applications table. You should use the Airtable API to retrieve the list.
To create the "report": Using the Airtable API, create a new record in the Reports table of the base that you copied; the
computer's host name should be stored in the Host field and the list of unapproved bundle identifiers should be stored in
the Unapproved bundle identifiers field.
For details about how to use the Airtable API, please see https://airtable.com/api.
You may use whichever language you feel most comfortable with, but we recommend Node, Ruby, or Python since there are
Airtable SDKs available for them.

Also, please include a README that covers:
● How long you spent on the assignment.
● What you like about your implementation.
● What you would change if you were going to do it again.
● Instructions for how to run the application (e.g. any steps for installing third party libraries or specific a version of the
scripting language).

WHAT WE'RE LOOKING FOR:
● Clean, readable, maintainable code.
● Adequate error handling.
