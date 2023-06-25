# RUCourseSnipe
Rutgers University course sniper

Scrapes web using selenium, collects data from Rutgers Schedule of Classes and notifies user when a section has opened.
Speed of scrape depends on the amount of desired sections, can take anywhere from 1.5 seconds (1 desired section) and increases for every additional index added to the search.
Code iterates through every index requested and checks the status of the section and returns a message if the section is open as well as a direct link to register for the specific open section.
When a section opens up, a text/email notification is sent to the user.

Configured through docker (available on dockerfile in repo) and running on Microsoft Azure.
