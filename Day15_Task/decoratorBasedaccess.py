

from functools import wraps

# User roles dictionary
users = {
    "Rahul": "admin",
    "Priya": "user",
    "Arun": "manager"
}

# Decorator factory to check required role
def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(username, *args, **kwargs):
            user_role = users.get(username)
            
            if user_role is None:
                print("User not found!")
            elif user_role == required_role:
                return func(username, *args, **kwargs)
            else:
                print("Access Denied!")
        return wrapper
    return decorator

@role_required("admin")
def delete_data(username):
    print(f"{username} can delete data")

@role_required("manager")
def view_reports(username):
    print(f"{username} can view reports")

# Test cases
delete_data("Rahul")   
delete_data("Priya")   
view_reports("Arun")   
view_reports("Rahul")  