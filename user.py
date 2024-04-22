class UserManager:
    def __init__(self):
        self.user_list = []
        self.counter = 0

    def generate_id(self):
        self.counter += 1
        return self.counter
    
    def create_a_user(self, name, password, user_type, current_user=None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(password, str) or not password.strip():
            raise ValueError("Password must be a non-empty string.")
        if not isinstance(user_type, str) or user_type.lower() not in {"student", "teacher", "admin"}:
            raise ValueError("Invalid user type. User type must be one of 'student', 'teacher', or 'admin'.")
        if current_user and not isinstance(current_user, User):
            raise TypeError("Invalid current_user. Must be an instance of User.")
        if current_user and current_user.type != "admin":
            raise PermissionError("Only admins can create new users.")

        new_user_id = self.generate_id()
        new_user = User(new_user_id, name, password, user_type)
        self.user_list.append(new_user)


    def find_users(self, ids):
        users_found = []
        for user in self.user_list:
            if user.user_id in ids:
                users_found.append(user)
        
        return users_found

class User():
    def __init__(self, user_id: int, name: str, password: str, type: str):
        self.user_id = user_id
        self.name = name
        self.password = password
        if type not in {"student", "teacher", "admin"}:
            raise ValueError("Invalid user type")
        else:
            self.type = type # type should be either student/teacher/admin
        
    
    def __str__(self):
        return f"ID: {self.user_id}, name: {self.name}, type: {self.type}"
    