# قاموس لتخزين بيانات المستخدمين 
user_records = {}

# تعريف كلاس لإدارة المستخدمين
class UserManagement:
    # متغير كلاس لتتبع عدد المستخدمين المُضافين
    user_count = 0 

    # دالة المُنشئ لتخزين بيانات المستخدم عند إنشاء الكائن
    def __init__(self, first_name, last_name, email, password, status="inactive"):
        self.__first_name = first_name  # الاسم الأول للمستخدم
        self.__last_name = last_name    # اسم العائلة للمستخدم
        self.__email = email            # البريد الإلكتروني للمستخدم
        self.__password = password      # كلمة مرور المستخدم
        self.__status = status          # حالة المستخدم (نشط أو غير نشط)
        UserManagement.user_count += 1  # زيادة عدد المستخدمين مع كل عملية إضافة 

    # تمثيل نصي للكائن عند الطباعة أو التحويل إلى نص
    def __str__(self):
        return (f"First Name: {self.__first_name}\n"
                f"Last Name: {self.__last_name}\n"
                f"Email: {self.__email}\n"
                f"Password: {self.__password}\n"
                f"Status: {self.__status}\n"
                f"____________________")

    
# دالة لإضافة مستخدم جديد من خلال أخذ المدخلات من المستخدم
def add_user_input():
    first_name = input("Enter first name: ")  # إدخال الاسم الأول
    last_name = input("Enter last name: ")    # إدخال اسم العائلة
    email = input("Enter email: ")            # إدخال البريد الإلكتروني
    password = input("Enter password: ")      # إدخال كلمة المرور
    # إنشاء كائن مستخدم جديد
    user = UserManagement(first_name, last_name, email, password)
    # إضافة المستخدم إلى القاموس مع استخدام رقم المستخدم كالمفتاح
    user_records[user.user_count] = user
    return "User added successfully!"  # رسالة نجاح الإضافة


# دالة رئيسية لتشغيل البرنامج
def run_app():
    while True:  # حلقة تستمر حتى يختار المستخدم الخروج
        # عرض قائمة الخيارات للمستخدم
        print("""Welcome to User Management
        Choose an Action: 
        
          1. Add new user 
          2. Display all users 
          3. Exit """)
        user_choice = input("Enter your choice: ")  # أخذ خيار المستخدم
        if user_choice == "1":  # إذا اختار إضافة مستخدم جديد
            print(add_user_input())
        elif user_choice == "2":  # إذا اختار عرض جميع المستخدمين
            # تجميع بيانات جميع المستخدمين في نص وعرضها
            result = "\n".join(str(user) for user in user_records.values())
            # إذا لم يكن هناك مستخدمون، عرض رسالة مناسبة
            print(result if result else "No users found.")
        elif user_choice == "3":  # إذا اختار الخروج
            print("You have successfully exited the program.")
            break  # إنهاء الحلقة وبالتالي إنهاء البرنامج
        else:  # إذا أدخل خيار غير صحيح
            print("Invalid choice, please try again.")

# استدعاء الدالة الرئيسية لتشغيل البرنامج
run_app()
