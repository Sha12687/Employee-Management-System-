from App.services.auth_service import AuthService

user =AuthService.authenticate_user(
    "admin","SHA1234"
)
print(user)


user1 =AuthService.authenticate_user(
    "employee","worng"
)

print(user1)

