from precondition.application import Application

test_classes = [
    Application
]

def test_login_pop_write_review_page(app):
    app.login()
    app.login_pop_write_review_page()
    app.log_out()

def test_login_pop_search_result(app):
    app.login()
    app.login_pop_search_result()
    app.delete_1_saved()
    app.log_out()

def test_login_pop_product(app):
    app.login()
    app.login_pop_product()
    app.delete_1_saved()
    app.log_out()