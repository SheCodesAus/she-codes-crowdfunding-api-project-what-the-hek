from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer
from projects.permissions import IsOwnerOrReadOnly
class CustomUserList(APIView):

	permission_classes = [permissions.IsAuthenticatedOrReadOnly,
	IsOwnerOrReadOnly]

	# if request.user.is_authenticated:

	def get(self, request):
		users = CustomUser.objects.all()
		serializer = CustomUserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = CustomUserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

class CustomUserDetail(APIView):

	def get_object(self, pk):
		try:
			return CustomUser.objects.get(pk=pk)
		except CustomUser.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		user = self.get_object(pk)
		serializer = CustomUserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk):
		user = self.get_object(pk)
		data = request.data
		serializer = CustomUserSerializer(			
			instance=user,
			data=data,
			partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)

	def delete(self, request, pk):
		user = self.get_object(pk)
		serializer = CustomUserSerializer(user)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePasswordView(generics.UpdateAPIView):
	serializer_class = ChangePasswordSerializer
	model = CustomUser
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def get_object(self, queryset=None):
		obj = self.request.user
		return obj

	def update(self, request, *args, **kwargs):
		self.object = self.get_object()
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			if not self.object.check_password(serializer.data.get("old_password")):
				return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
			self.object.set_password(serializer.data.get("new_password"))
			self.object.save()
			response = {
				'status': 'success',
				'code': status.HTTP_200_OK,
				'message': 'Password updated successfully',
				'data': []
			}
			return Response(response)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)