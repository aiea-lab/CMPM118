# Tasks
- [ ]  Read and agree to the [group expectations](https://docs.google.com/document/d/1RdUDc-3IlxvtmzgO67xgRhiaI-1ztCdxiZT3Brb-LLo/edit?usp=sharing).
    - [ ]  Ask any questions to @lgilpin on discord
    - [ ]  Feel free to add suggestions in comments
- [ ]  Join the auditor teamspace on Notion
- [ ]  Add yourself to the members database: [Members](https://www.notion.so/16e0927aad754d5b996ca393d231ac08?pvs=21)
    - [ ]  Choose the template that corresponds to your level (undergrad, MS or PhD) and fill out the information in the template to the best of your ability with what you are comfortable sharing.  (This is used internally in the lab and will not be shared outside of our Notion namespace).
    - [ ]  Add your start date
    - [ ]  Add the status as auditor
    - [ ]  Add your end date (if known).  This is the intended graduation date.
    - [ ]  Add your name
    - [ ]  Add your project if known
    - [ ]  Optional: Add a photo
    - [ ]  Optional: Give yourself an informative emoji.
- [ ]  Join the Lab Discord - [https://discord.gg/eEmWTFCh](https://discord.gg/eEmWTFCh)
    - [ ]  Change your nickname to your name
    - [ ]  Introduce yourself and ask for the auditor role on discord
- [ ]  Sign up for 5 units (this is *not* required for summer students or interns):
    - [ ]  If you are an **undergraduate,** sign up for CMPM 118 by claiming one of the [permission codes](https://www.notion.so/aiea/Credits-and-Courses-2e0c03a14c2c80629160d35afe13adce?source=copy_link#317c03a14c2c80d489a1c376faa56d21) for your quarter
    - [ ]  If you are a graduate student, sign up for a 5 unit independent study, and be sure to fill out the independent study syllabus:
    [Independent Study Guidelines](https://www.notion.so/Independent-Study-Guidelines-2ae3eb5c200242ca8c25292aad2b8082?pvs=21)
- [ ]  Add yourself to the AIEA Lab website (you can use the information you added from the internal members page):
    - [ ]  Request to join the AIEA github on dicord.
    - [ ]  Download hugo.
    - [ ]  Checkout or fork the group website: https://github.com/aiea-lab/aiea-lab.github.io
    - [ ]  Follow the steps on the README to ensure that that you can run the website locally using `hugo server` (and go to [localhost](http://localhost) to check)
    - [ ]  Create a new branch (which will be turned into a PR and then merged): `git checkout -b [your_name]_auditor` (or whatever you would like to make it).
    - [ ]  Create your group member profile.  Copy one of the existing member profiles, or you can copy the template: `cp archetypes/person.md content/auditor/[your_name].md`
    - [ ]  Edit `[your_name].md`
        - [ ]  Replace `[your_name]` with your name
        - [ ]  Change the `date` to the date you joined the group.
        - [ ]  Make the id your first name (if unique in the group, otherwise add a last initial as well).
        - [ ]  Change `name=""` to `name=[your_full_name]`
        - [ ]  Add your picture
            1. Copy a square photo of yourself into `static/img/portraits` as `[your_name].jpg`
            2. Replace `[your_name]` in `portraits/[your_name].jpg`
        - [ ]  Add a short bio for yourself in the `short_bio`
        - [ ]  Add a short name for yourself
        - [ ]  Add a title, e.g., Undergraduate, Masters, PhD, PhD candidate, Collaborator, etc.
        - [ ]  Add socials:
            - [ ]  Add email in `[your_name]@ucsc.edu`
            - [ ]  Add twitter if you have one (otherwise remove it).
            - [ ]  Add google scholar if you have one (otherwise remove it).
            - [ ]  Add your github name
        - [ ]  Add your education (course is the degree you received: PhD, MS, BS).
        - [ ]  Add your role at UCSC (PhD, MS, BS, collaborator).
        - [ ]  Add education with `[[education]] course = "" institution = "" year = 2023`
        - [ ]  Add bio and any other information.
    - [ ]  Test your changes, by running `hugo server` and checking the changes on `localhost`
        - [ ]  Only commit your `[name].md` and image file (which should be located in `static/img/portraits/`
    - [ ]  add your changes to your branch
        - [ ]  `git add ...`
        - [ ]  `git commit -m "Adding [your_name] user profile"`
        - [ ]  `git push`
    - [ ]  If you get a permission denied error while doing `git push`
        - [ ]  Create a new `fork` in aiea-lab.github.io repo
        - [ ]  Clone your fork
        - [ ]  Continue from [step 3] onwards
    - [ ]  Create a pull request to merge into master.  See more here:
    
    [Creating a pull request - GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
    
    - [ ]  (For `forked` repo) Create a pull request to merge into master. See more here:
- [ ]  Add yourself to the group google calendar: [google calendar](https://calendar.google.com/calendar/u/0?cid=Y19iMzYxYWYyZGVjZDA4ZmE4MWFlZTkyMjMxNjNlMGU5NWMxNDU2MmRkOGZmZDMxYWZhNWRjYzY5MmZiOTgzOTVkQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20)
    
    [ ](https://calendar.google.com/calendar/u/0/r?cid=c_b361af2decd08fa81aee9223163e0e95c14562dd8ffd31afa5dcc692fb98395d@group.calendar.google.com)
    
- [ ]  Add yourself to the auditors group mailing list if you haven’t been added already https://groups.google.com/a/ucsc.edu/g/aiea-auditors-group/members
- [ ]  Make sure you can access the [group google drive:](https://drive.google.com/drive/folders/14KZ_JnDH_bNm5lx2XlGXVn42W1TMObro?usp=drive_link)
    - [ ]  Make an introductory slide for yourself under the **Auditors** section: https://docs.google.com/presentation/d/1EST82USQJk2sLFw-x4eJzWFZGu1I4jWnHw8Dd5pCXZI/edit?usp=sharing

# Deliverable

- Write one page about getting onboarded to github and any issues or feedback you have.
- Upload your deliverable to Canvas under deliverable 1.

# Don't Forget
- Don't forget to fill out the [weekly status form](https://www.notion.so/aiea/16cc03a14c2c8069881de3f814456c59?pvs=106) on Fridays at 5pm. 
