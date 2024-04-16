from django.db import models

# Create your models here.



class TeacherData(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=200, default="-")
    phoneno = models.CharField(max_length=200, default="-")
    emailid = models.CharField(max_length=200, default="-")
    address = models.CharField(max_length=1000, default="-")
     
    # branch = models.CharField(max_length=1000, default="-") # comps, extc, aids
    # div      = models.CharField(max_length=200,  default="A") # comps, extc, aids
    # year     = models.IntegerField(default=2024)

    def __str__(self):
        return f"{self.id}-{self.name} - Phoneno : {self.phoneno} Address : {self.address}"


class Studattendence(models.Model):
    id = models.AutoField(primary_key=True)

    day         = models.CharField(max_length=200, default="-")
    starttime   = models.CharField(max_length=200, default="-")
    year         = models.CharField(max_length=200, default="-")
    div         = models.CharField(max_length=200, default="-")

    rollno      = models.IntegerField(default=0)
    leacture    = models.CharField(max_length=200, default="-") #subject
    lectProf    = models.CharField(max_length=200, default="-")
    timestamp   = models.CharField(max_length=200, default="-")
    status      = models.CharField(max_length=200, default="present")

    def __str__(self):
        return f"{self.id}-{self.rollno} - leacture {self.leacture} lectProf : {self.lectProf} - {self.timestamp}"
   


class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)


    branch         = models.CharField(max_length=200, default="-")
    year         = models.CharField(max_length=200, default="-")
    div         = models.CharField(max_length=200, default="-")
    day         = models.CharField(max_length=200, default="-")
    starttime   = models.CharField(max_length=200, default="-")
    endtime     = models.CharField(max_length=200, default="-")
    leacture    = models.CharField(max_length=200, default="-") #subject
    lectProf    = models.CharField(max_length=200, default="-")
    status      = models.CharField(max_length=200, default="present")

    def __str__(self):
        return f"{self.id}-{self.branch} - {self.year} - {self.div} - {self.day} - {self.starttime} : {self.endtime} --- {self.leacture} - {self.lectProf} - {self.status}"

   



class Studentprofile(models.Model):
    id = models.AutoField(primary_key=True)

    # profile image
    imgpath= models.CharField(max_length=200, default="attendapp/setup/studentprofileimg/boy avatar.png")  
    # attendapp\setup\studentprofileimg\boy avatar.png
    
    year   = models.IntegerField(default=2024)
    rollno = models.IntegerField(default=0)
    name   = models.CharField(max_length=200, default="-")

    div    = models.CharField(max_length=200, default="-")
    branch = models.CharField(max_length=200, default="-")
    
    y1cgpa = models.FloatField(verbose_name='Y1CGPA', default=0.0)
    y1sgpa = models.FloatField(verbose_name='Y1SGPA', default=0.0)
    
    y2cgpa = models.FloatField(verbose_name='Y2CGPA', default=0.0)
    y2sgpa = models.FloatField(verbose_name='Y2SGPA', default=0.0)
    
    y3cgpa = models.FloatField(verbose_name='Y3CGPA', default=0.0)
    y3sgpa = models.FloatField(verbose_name='Y3SGPA', default=0.0)
    
    y4cgpa = models.FloatField(verbose_name='Y4CGPA', default=0.0)
    y4sgpa = models.FloatField(verbose_name='Y4SGPA', default=0.0)
    
    address = models.CharField(max_length=1000, default="-")
    phoneno = models.CharField(max_length=200, default="-")
    
    parentphoneno = models.CharField(max_length=200, default="-")

    teachername = models.CharField(max_length=200, default="Sahil")
    

    def __str__(self):
        return f"{self.id}-{self.name} - Role : {self.rollno} Branch : {self.branch} Phoneno : {self.phoneno}"

    
    


# sgpa = models.DateField()
# leave_type = models.CharField(max_length=50, default="Sick")
# days = models.CharField(max_length=50, default="")
# reason = models.TextField()
# llmsuggest = models.CharField(max_length=50, default="Maybe") # Yes, No, Maybe
# status = models.CharField(max_length=50, default="")

# class Employaccdata(models.Model):
#     eacc_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=255, default="")
#     fullname = models.CharField(max_length=255, default="")
#     password = models.CharField(max_length=255, default="")
#     email = models.CharField(max_length=255, default="")
#     phoneno = models.CharField(max_length=255, default="")
#     address = models.CharField(max_length=500, default="")
#     gender = models.CharField(max_length=500, default="")
#     dateofbirth = models.CharField(max_length=50, default="")
#     MaritalStatus = models.CharField(max_length=50, default="")
#     EmployeePhotoPath = models.CharField(max_length=1000, default="")


#     role = models.CharField(max_length=255, default="") #HR, Manager, Employeeeeeee
#     department = models.CharField(max_length=255, default="")
#     jobtitle = models.CharField(max_length=255, default="")
#     manager = models.CharField(max_length=255, default="")
#     dateofjoin = models.CharField(max_length=255, default="")
#     status = models.CharField(max_length=50, default="") # Working, NotWorking, OnLeave 


#     EmpStatus = models.CharField(max_length=255, default="") # (Full-time, Part-time, Contract)
#     EmpType = models.CharField(max_length=255, default="") # (Permanent, Temporary, Internship)
#     WorkLoc = models.CharField(max_length=1000, default="") # (2-3 sample offices)

#     Checkin = models.CharField(max_length= 50, default="12:00") # (2-3 sample offices)
#     Checkout = models.CharField(max_length=50, default="19:00") # (2-3 sample offices)

#     # Annully
#     SickLeavecount = models.CharField(max_length=255, default="0")
#     PrivilegeLeavecount = models.CharField(max_length=255, default="0")
#     CasualLeavecount = models.CharField(max_length=255, default="0")
#     MaternityLeavecount = models.CharField(max_length=255, default="0")

#     Productivityvalue   = models.CharField(max_length=10, default="0")
#     Satisfactionvalue   = models.CharField(max_length=10, default="0")
#     FeedbackScorevalue  = models.CharField(max_length=10, default="0")
#     Skillsvalue         = models.CharField(max_length=10, default="0")
#     Communicationvalue  = models.CharField(max_length=10, default="0")


#     # clust_data = models.CharField(max_length=500, default="")

#     def __str__(self):
#         return f"{self.user_name} - Role : {self.role} Dep : {self.department} Mage : {self.manager}"





# class Leave(models.Model):
#     leave_id = models.AutoField(primary_key=True)

#     department = models.CharField(max_length=100, default="")
#     user_name = models.CharField(max_length=255, default="")
#     date = models.DateField()
#     leave_type = models.CharField(max_length=50, default="Sick")
#     days = models.CharField(max_length=50, default="")
#     reason = models.TextField()
#     llmsuggest = models.CharField(max_length=50, default="Maybe") # Yes, No, Maybe
#     status = models.CharField(max_length=50, default="")


#     def __str__(self):
#         return f"{self.leave_id} - {self.user_name} - Type : {self.leave_type} Dep : {self.department} Status : {self.status}"

# class Reimbusement(models.Model):
#     reimbus_id = models.AutoField(primary_key=True)

#     department = models.CharField(max_length=100, default="")
#     user_name = models.CharField(max_length=255, default="")
#     date = models.DateField()
#     expense_type = models.CharField(max_length=50, default="")
#     amount = models.CharField(max_length=100, default="")
#     shortdesc = models.TextField()
#     pdfpath = models.CharField(max_length=50, default="")
#     status = models.CharField(max_length=50, default="")
#     paymenttype = models.CharField(max_length=50, default="") #check/deposit

#     days = models.CharField(max_length=50, default="")

#     def __str__(self):
#         return f"{self.reimbus_id} - {self.user_name} - Type : {self.expense_type} Dep : {self.department} Status : {self.status}"



# class Msgdata(models.Model):
#     msg_id = models.AutoField(primary_key=True)

#     user_name = models.CharField(max_length=255, default="")
#     shortdesc = models.TextField()

#     def __str__(self):
#         return f"{self.msg_id} - {self.user_name}"


# class Chatdata(models.Model):
#     chat_id = models.AutoField(primary_key=True)


#     user_name = models.CharField(max_length=255, default="")
#     query = models.TextField()
#     shortdesc = models.TextField()

#     def __str__(self):
#         return f"{self.chat_id} - {self.user_name}"





# class SensorData(models.Model):
#     # api_key = models.CharField(max_length=300)
#     nodename = models.CharField(max_length=255)
#     depth_1 = models.FloatField(default=0.0)
#     depth_2 = models.FloatField(default=0.0)
#     depth_3 = models.FloatField(default=0.0)
#     temperature = models.FloatField(default=0.0)
#     humidity = models.FloatField(default=0.0)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     # mode = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.nodename} - {self.timestamp}"


# class Nodedata(models.Model):
#     user_name = models.CharField(max_length=255, default="")
#     node_name = models.CharField(max_length=255, default="")
#     Loc_lat = models.CharField(max_length=20, default="")
#     Loc_long = models.CharField(max_length=20, default="")
#     api_key = models.CharField(max_length=300, default="")

#     def __str__(self):
#         return f"{self.user_name} - {self.node_name}"


# class Clusterdata(models.Model):
#     user_name = models.CharField(max_length=255, default="")
#     cluster_name = models.CharField(max_length=255, default="")
#     clust_data = models.CharField(max_length=500, default="")

#     def __str__(self):
#         return f"{self.user_name} - {self.cluster_name}"


# ------------------------------------
# Sample Code Below
# ------------------------------------

# class Product(models.Model):
#     Product_id = models.AutoField(primary_key=True)
#     product_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     slug = models.CharField(max_length=100, default="")
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     image = models.ImageField(upload_to="tze/images", default="")
#     testimoniallink = models.CharField(max_length=300, default="")
#     ytlink = models.CharField(max_length=300, default="")
#     benifits = models.CharField(max_length=300, default="")
#     how_to_use = models.CharField(max_length=400, default="")
#     doc_link = models.CharField(max_length=300, default="")
#     net_Qty = models.CharField(max_length=100, default="")
#     pack_of = models.CharField(max_length=50, default="")
#     # pub_date = models.DateField()
#     # subcategory = models.CharField(max_length=30, default="")

#     def __str__(self):
#         return self.product_name

# # mem: member
# class Contact(models.Model):
#     mem_id = models.AutoField(primary_key=True)

#     mem_name = models.CharField(max_length=60, default="")
#     mem_image = models.ImageField(upload_to="tze/contactImages", default="")
#     mem_desc = models.CharField(max_length=300, default="")
#     mem_email = models.CharField(max_length=100, default="")
#     mem_phone = models.IntegerField(default=0)
#     mem_fb_link = models.CharField(max_length=100, default="")
#     mem_IG_link = models.CharField(max_length=100, default="")
#     mem_status = models.CharField(max_length=100, default="")
#     mem_tag = models.CharField(max_length=20, default="")

#     def __str__(self):
#         return self.mem_name

# class Contact(models.Model):
#     msg_id = models.AutoField(primary_key=True)

#     name = models.CharField(max_length=50, default="")
#     email = models.CharField(max_length=70, default="")
#     phone = models.IntegerField(default=0)
#     msg = models.CharField(max_length=500, default="")

#     def __str__(self):
#         return self.name
