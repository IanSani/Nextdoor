![MAISHA MTAANI](/static/img/logo.png)


## Built By [Ian sani](https://github.com/iansani/)

## Description
This is a web application that allows users to join neighborhoods, create new neighborhoods, delete hoods, update and create profiles.
Users can communicate to other members in the hoods they join.

**Users must log in with credible emails**

## User Stories
These are the behaviors/features that the application implements for use by a user.

Users would like to:
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Add, Edit and Delete hoods,posts,businesses
* Delete hoods,posts,businesses
* Manage the application.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Admin Authentication | **On demand, verify emails before proceeding** | Access Admin dashboard |
| Display all hoods,posts,businesses | **Home page** | Clickable links to open live hoods,posts,businesses in different sites |
| To add an hoods,posts,businesses  | **Admin/Users** | Click on add and upload respectively|
| To edit hoods,posts,businesses  | **Admin/Users** | Redirected to the  hoods,posts,businesses form details and editing happens|
| To delete an hoods,posts,businesses  | **Admin/Users** | click on hoods,posts,businesses object and confirm by delete button|
| To search hoods by id | **Enter text in search bar** | Users can search by Hoods by ID|
| View posts by neighbours | **Add posts** | Users can add posts to hoods they join|

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/iansani/Nextdoor
        $ cd Nextdoor

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test mtaa

## Technologies Used
* Python3.6
* Django  framework and postgresql database

## Known Bugs

* Occupants/resident count

## License

Copyright (c) 2018 IanSani
