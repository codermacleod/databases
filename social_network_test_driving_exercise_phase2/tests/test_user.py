from lib.user import User

"""
Constructs with a username, account and email_address:
"""

def test_constructs_with_username_account_email_address():
    user = User("Danny Boy", 123, "danny@highlands.com")
    assert user.username == "Danny Boy"
    assert user.account == 123
    assert user.email_address == "danny@highlands.com"
