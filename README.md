/api/menu (public access)

/api/menu/{id} (authentication required)

/api/booking (authentication required)

/api/booking/{id} (authentication required)

/auth/token/login

/auth/token/logout

/auth/users (for registering new users. NB: you should be logged in as superuser)

{
user: testuser, password: "test12345"

superuser: superuser, password: "pass123"
}
