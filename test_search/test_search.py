from precondition.application import Application

tests_classes=[
    Application
]

#=================== from autocomplete ===========================
#=================== from autocomplete ===========================
def test_search_daycare(app):
    app.login()
    app.search_daycares()
    app.logout()

def test_search_schools(app):
    app.login()
    app.search_schools()
    app.logout()

def test_search_districts(app):
    app.login()
    app.search_districts()
    app.logout()

def test_search_colleges(app):
    app.login()
    app.search_colleges()
    app.logout()
#=================== with EMPTY TEXT FIELD ===========================
#=================== with EMPTY TEXT FIELD ===========================

def test_search_daycare_empty(app):
    app.login()
    app.search_daycare_empty_field()
    app.logout()

def test_search_college_empty(app):
    app.login()
    app.search_college_empty_field()
    app.logout()

def test_search_elementary_empty(app):
    app.login()
    app.search_elementary_empty_field()
    app.logout()

def test_search_middle_empty(app):
    app.login()
    app.search_middle_empty_field()
    app.logout()

def test_search_high_empty(app):
    app.login()
    app.search_high_empty_field()
    app.logout()

def test_search_elem_middle_empty(app):
    app.login()
    app.search_elementary_middle_empty_field()
    app.logout()

def test_search_elementary_high_empty(app):
    app.login()
    app.search_elementary_high_empty_field()
    app.logout()

def test_search_middle_high_empty(app):
    app.login()
    app.search_middle_high_empty_field()
    app.logout()




