from django.shortcuts import render
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework.response import Response
from api.serializers import PasswordResetSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class PasswordResetConfirmAPIView(PasswordResetConfirmView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        path = request.path
        print("testing is working 1")
        uid = path.split('/')[-3]
        print("testing is working 2")
        user = User.objects.get(pk=uid)

        print("testing is working 3")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if request.data["new_password1"] == request.data["new_password2"]:
                user.set_password(request.data["new_password1"])
                user.save()
            else:
                return Response({'detail': _('Password confirmation is wrong.')},)
            print("testing is working 4")
            serializer.save()
        return Response(
            {'detail': _('Password has been reset with the new password.')},
        )

