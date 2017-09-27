from precondition.application import Application

tests_classes = [
    Application
]
def test_register_student(app):
    app.sign_up()
    app.register_student()