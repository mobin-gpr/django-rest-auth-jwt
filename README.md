
# django-rest-auth-jwt

Since I saw that many back-end developers have problems with the authentication system in Django REST Framework and do not have the necessary familiarity with it, I decided to separate the authentication system from one of my projects and create a project focused on this issue. so that it can be available to other developers as a document. In this project, the main authentication actions are completely written exclusively and without the use of third party packages. This system depends on email account confirmation, which after generating a dedicated jwt token is sent to the user's email and the user activates his account by clicking on the link. jwt endpoints are also used in the login section.

 ## Endpoints

- register
- confirm email
- resend confirm email
- change password
- reset password
- set password
- profile

## Run Locally

Clone the project

```bash
git clone https://github.com/mobin-gpr/fox-web-api.git
```

Go to the project directory

```bash
cd fox-web-api
```

Run

```bash
python manage.py runserver
```

## API Document

- http://localhost:8000/swagger/
- http://localhost:8000/redoc/

## License

[MIT](https://choosealicense.com/licenses/mit/)
