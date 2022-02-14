.. Game theory documentation master file, created by
   sphinx-quickstart on Tue May 23 16:18:26 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Preparation
===========

Update hackmd link if necessary.

Group Preparation
=================

Data collection
***************

Create a Google form with the following **required** information for all
students:

- Student first name
- Student last name
- Student number

Also, optional:

- Group name
- Point of contact email address.

In week 1 of Second semester send the following to all students::

    Dear all,

    For the group assessment you should now form a group of 4 students.

    Once you have a group, before the <DEADLINE AGREED IN CLASS> please fill in
    the following form with the require information.

    After <DEADLINE AGREED IN CLASS> I will create groups for all students not
    yet in groups.

    Vince

Group formation
***************

Once :code:`<DEADLINE AGREED IN CLASS>` has passed, download the google form
spreadsheet and create :code:`assets/assessment/<year>/group/main.numbers` with the
following format::

    Last name || First name || Student number || Group name || Presentation schedule

Use :code:`2022-05-03-0930` as the format for the presentation schedule.

Export the :code:`main.numbers` file to :code:`assets/assessment/<year>/group/main.csv`

Download the class list from the VLE. In learning central this is under "Grade
Centre" save the file in: :code:`assets/assessment/<YEAR>/gc_....csv`.

Create :code:`assets/assessment/<year>/main.ipynb`. The following will create
:code:`df` which is a list of all students in the class::

    import pandas as pd
    import numpy as np
    df = pd.read_csv("gc_2122....csv")[["Last Name", "First Name", "Username"]]

This will read in the assigned students::

    assigned_student_df = pd.read_csv("./group/main.csv")
    assigned_student_numbers = assigned_student_df["Username"]
    df["assigned"] = df["Username"].isin(assigned_student_numbers)

The following will create a list of unassigned students::

    np.random.seed(0)
    print(df[~df["Username"].isin(assigned_student_numbers)].sample(frac = 1).reset_index(drop=True))

**Manually** add these students to the
:code:`assets/assessment/<year>/group/main.numbers` and assign groups.

Once all students are assigned (keep exporting the numbers file to csv) the
following code will write a draft of all emails::

    with open("emails.txt", "w") as text_file:
        for _, f in assigned_student_df.groupby("Group_name"):
            email_text = "===============\n\n\n"
            last_names = list(f["Last Name"])
            first_names = list(f["First Name"])
            emails = [f"{username}@cardiff.ac.uk" for username in f["Username"]]
            presentation_date = list(f["Presentation Date"])[0]
            group_name = list(f["Group_name"])[0]
            text_file.write("\n\n\n")
            text_file.write("TO:\n")
            for email in emails:
                text_file.write(f"{email}, ")
            text_file.write("\n\n")
            text_file.write("Important Information Game Theory")
            text_file.write("\n\n")
            for first_name, last_name in zip(first_names, last_names):
                text_file.write(f"{first_name} {last_name}, ")
            text_file.write(f"\n\nYour group name is '{group_name}' and your presentation date is {presentation_date}")
            text_file.write("\n\nThanks,\nVince")


Send all those emails.
