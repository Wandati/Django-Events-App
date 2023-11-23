## Django Events App

The Django Events App is a web application built using the Django framework, designed to manage and showcase events seamlessly. Whether you are organizing conferences, workshops, or social gatherings, this app provides a robust platform to handle event creation, registration, and attendee management.

## Features

Event Creation: Easily create and manage events with details such as title, date, location, and description.
User Registration: Allow users to register for events and keep track of attendees.
Authentication: Secure user authentication system to protect event data and manage user access.
Event Dashboard: A dashboard for event organizers to view and manage registered attendees.
Responsive Design: A user-friendly interface that adapts to various devices, ensuring a smooth experience for both organizers and attendees.
Downloads: Ability to download events as pdf,csv
Venue Creation: Easily create and manage venues to host the events

## Getting Started

## Prerequisites

Python 3.x
Django (install using pip install Django)

## Installation

Clone the repository:

bash
git clone https://github.com/Wandati/django-events-app.git
Navigate to the project directory:

bash

cd django-events-app
Install dependencies:

bash

pip install -r requirements.txt
Apply migrations:

bash

python manage.py migrate
Create a superuser account:

bash
python manage.py createsuperuser
Start the development server:

bash

python manage.py runserver
Access the application at http://127.0.0.1:8000/ in your web browser.

## Usage

Log in to the Django admin interface using the superuser credentials.

Create new events using the "Events" section.
Create new venues using the "Vnues" section.

Users can register for events through the public-facing interface.

Organizers can manage event details and view the list of registered attendees in the dashboard.

## Contributing

Feel free to contribute and make changes to the project

## License

Copyright (c) Marvin Wandati
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgments

The Django team for creating a powerful and versatile web framework.
Contributors and the open-source community for valuable insights and support
