# from django.contrib.auth.mixins import UserPassesTestMixin
#
# class IsAdminTest(UserPassesTestMixin):
#     def test_func(self):
#         if self.request.user.is_admin:
#             return True
#         else:
#             return False
#
# class IsWaiterTest(UserPassesTestMixin):
#     def test_func(self):
#         if self.request.user.role == 2:
#             return True
#         else:
#             return False
#
# class IsCoockerTest(UserPassesTestMixin):
#     def test_func(self):
#         if self.request.user.role == 3:
#             return True
#         else:
#             return False
#
