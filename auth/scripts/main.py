from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from users.models import Student
from django.contrib.auth import authenticate


user = authenticate(username="john", password="johnpassword")
print(user)
content_type = ContentType.objects.get_for_model(Student, for_concrete_model=False)
print(content_type)
print([p.codename for p in Permission.objects.filter()])
student_permissions = Permission.objects.filter(content_type=content_type)
print([s.codename for s in student_permissions])
for permission in student_permissions:
    print(permission.codename)
    user.user_permissions.add(permission)
    print(user.user_permissions)
print(user.save())
print([p.codename for p in user.user_permissions.all()])

print(user.has_perm("users.add_user"))
print(user.has_perm("users.add_person"))
print(user.has_perm("users.can_eat_pizzas"))
print(user.has_perms(("users.add_student", "users.can_deliver_pizzas")))
