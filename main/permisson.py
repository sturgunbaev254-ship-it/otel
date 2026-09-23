from rest_framework.permissions import BasePermission

class isownerOrReadOnly(BasePermission):
    def has_object_permisssion(self, request,view,obj):
        if request.method in ['GET',"HEAD","OPTIONS"]:
            return True
        return obj.user==request.user