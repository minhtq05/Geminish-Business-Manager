class User():
    def __init__(self, id, email, password, created_on, is_admin):
        self.id = id
        self.email = email
        self.password = password
        self.created_on = created_on
        self.is_admin = is_admin

    def __repr__(self):
        return f"User(\
                    id={self.id}, \
                    email:{self.email} \
                )"