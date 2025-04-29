#!/usr/bin/env python3
from application import init_app
from application.database import db, User

# 1. Spin up your app context
app = init_app()
with app.app_context():
    # 2. Create a new User instance (password will be hashed automatically)
    test_email = 'test@example.com'
    test_password = 'P@ssw0rd'
    user = User.create(test_email, test_password)
    
    # 3. Persist to the database
    db.session.add(user)
    db.session.commit()
    
    print(f'Created user id={user.id} email={user.email}')
