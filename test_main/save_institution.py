from precondition.application import Application

test_classes=[
    Application
]

#=================== Save From rusult page ===========================
#=================== Save From rusult page ===========================

def test_save_institutions_result_page(app):
    app.sign_in()
    app.save_institutions_from_result_page()
    app.logout()


#=================== Save From Product page ===========================
#=================== Save From Product page ===========================