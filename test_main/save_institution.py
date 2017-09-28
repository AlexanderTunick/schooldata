from precondition.application import Application

test_classes=[
    Application
]

#=================== Save From rusult page ===========================
#=================== Save From rusult page ===========================

def test_open_close_watchlist(app):
    app.sign_in()
    app.open_close_watchlist()
    app.log_out()

def test_save_school(app):
    app.sign_in()
    app.save_school()
    app.delete_saved()
    app.log_out()

def test_save_from_product_page(app):
    app.sign_in()
    app.save_from_product_page()
    app.log_out()

def test_activate_link_in_watchlist(app):
    app.sign_in()
    app.activate_link_in_watchlist()
    app.log_out()

def test_all_schools_link(app):
    app.login()
    app.all_schools_link()
    app.log_out()



#=================== Save From Product page ===========================
#=================== Save From Product page ===========================