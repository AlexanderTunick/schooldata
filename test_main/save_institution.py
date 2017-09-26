from precondition.application import Application

test_classes=[
    Application
]

#=================== Save From rusult page ===========================
#=================== Save From rusult page ===========================

def test_open_close_watchlist(app):
    app.sign_in()
    app.open_close_watchlist()
    app.logout()

def test_save_school(app):
    app.sign_in()
    app.save_school()
    app.delete_saved()
    app.logout()

def test_save_from_product_page(app):
    app.sign_in()
    app.save_from_product_page()


#=================== Save From Product page ===========================
#=================== Save From Product page ===========================