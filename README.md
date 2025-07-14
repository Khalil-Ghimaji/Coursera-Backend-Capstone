The project folder is little_lemon, The app contain the index.html and its related view is restaurant, and the api related files (models,views,serializers,...) are in the littleLemonAPI. Thanks !

Sorry if you found the work duplicated in both applications. it wasn't first like this but after submitting the work one learner failed me saying he didn't find any of the requested files (models, serializers, etc...) that's why i duplicated the work before submitting again. it may seem weird but it was the only way to make sure the files are there and the work is done.

/api/menu (public access)

/api/menu/{id} (authentication required)

/api/bookings (authentication required)

/api/bookings/{id} (authentication required)

/auth/token/login

/auth/token/logout

/auth/users (for registering new users. NB: you should be logged in as superuser)

{
user: testuser, password: "test12345"

superuser: superuser, password: "pass123"
}
