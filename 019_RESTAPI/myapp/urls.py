
from django.urls import path
from myapp.views import *

urlpatterns = [
   path("adddata",add_data,name="addData"),
   path("viewdata",view_data,name="viewdata"),
   path("updatedata/<id>",update_data,name="updatedata"),
   path("deletedata/<id>",delete_data,name="deletedata"),


    path("students",get_students,name="students"),
    path("setstudent",set_student,name="setstudent"),
    path("updatestudent/<id>",update_student,name="updatestudent"),
    path("deletestudent/<id>",delete_student,name="deletestudent")

]
