# Secure Login System (Decorators) 

def login_required(func):
    def wrapper(logged_in):
        if logged_in:
            func()
        else:
            print("Please Login First")
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard(True)
dashboard(False)