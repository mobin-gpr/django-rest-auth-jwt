
# django-rest-auth-jwt

Since I saw that many back-end developers have problems with the authentication system in Django REST Framework and do not have the necessary familiarity with it, I decided to separate the authentication system from one of my projects and create a project focused on this issue. so that it can be available to other developers as a document. In this project, the main authentication actions are completely written exclusively and without the use of third party packages. This system depends on email account confirmation, which after generating a dedicated jwt token is sent to the user's email and the user activates his account by clicking on the link. jwt endpoints are also used in the login section.

 ## Endpoints

- Register
- Confirm email
- Resend confirm email
- Change password
- Reset password
- Set password
- Profile

## Run Locally

Clone the project

```bash
git clone https://github.com/mobin-gpr/django-rest-auth-jwt.git
```

Go to the project directory

```bash
cd django-rest-auth-jwt
```

Run

```bash
python manage.py runserver
```

## Hints:
- The user model is custom made, the username field has been removed from it and the email field has been set in its place.
- If you do not personalize the user model according to the project, problems may arise and you will have to make changes in your code.
- django.core.mail.backends.console.EmailBackend is used for EMAIL_BACKEND so emails are printed in the terminal.
- Validation tokens that are sent to the user via email are jwt tokens that are not stored in the database, so they have high security and better efficiency.
- You can change the expiration date of access and refresh tokens in the settings.py (SIMPLE_JWT).


## API Document

- http://domain/swagger/
- http://domain/redoc/


## License

[MIT](https://choosealicense.com/licenses/mit/)
