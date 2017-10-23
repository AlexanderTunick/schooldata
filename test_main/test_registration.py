from precondition.application import Application

tests_classes = [
    Application
]
def test_register_student(app):
    app.sign_up()
    app.register_student()
    app.log_out()

def test_register_parent(app):
    app.sign_up()
    app.register_parent()
    app.log_out()

def test_register_other(app):
    app.sign_up()
    app.register_other()
    app.log_out()

def test_register_member(app):
    app.sign_up()
    app.register_member()
    app.log_out()

def test_register_teacher_em1_em2ver(app):
    app.sign_up()
    app.register_teacher_em1_em2ver()
    app.log_out()

def test_register_teacher_em1_em2unver(app):
    app.sign_up()
    app.register_teacher_em1_em2unver()
    app.log_out()

def test_register_student_verified_email(app):
    app.sign_up_student()
    app.register_student_verified_email()
    app.delete_profile()
    app.log_out()

def test_register_parent_verified_email(app):
    app.sign_up_student()
    app.register_parent_verified_email()
    app.delete_profile()
    app.log_out()

def test_register_other_verified_email(app):
    app.sign_up_student()
    app.register_other_verified_email()
    app.delete_profile()
    app.log_out()