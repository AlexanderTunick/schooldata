from precondition.application import Application

tests_classes=[
    Application
]

#=================== from autocomplete ===========================
#=================== from autocomplete ===========================
def test_search_daycare(app):
    app.login()
    app.search_daycares()
    app.log_out()

def test_search_schools(app):
    app.login()
    app.search_schools()
    app.log_out()

def test_search_districts(app):
    app.login()
    app.search_districts()
    app.log_out()

def test_search_colleges(app):
    app.login()
    app.search_colleges()
    app.log_out()

#=================== with EMPTY TEXT FIELD ===========================
#=================== with EMPTY TEXT FIELD ===========================
def test_search_daycare_empty(app):
    app.login()
    app.search_daycare_empty_field()
    app.log_out()

def test_search_college_empty(app):
    app.login()
    app.search_college_empty_field()
    app.log_out()

def test_search_elementary_empty(app):
    app.login()
    app.search_elementary_empty_field()
    app.log_out()

def test_search_middle_empty(app):
    app.login()
    app.search_middle_empty_field()
    app.log_out()

def test_search_high_empty(app):
    app.login()
    app.search_high_empty_field()
    app.log_out()

def test_search_elem_middle_empty(app):
    app.login()
    app.search_elementary_middle_empty_field()
    app.log_out()

def test_search_elementary_high_empty(app):
    app.login()
    app.search_elementary_high_empty_field()
    app.log_out()

def test_search_middle_high_empty(app):
    app.login()
    app.search_middle_high_empty_field()
    app.log_out()

#=================== SEARCH WITH ONE LETTER AND STATE ===========================
#=================== SEARCH WITH ONE LETTER AND STATE ===========================
def test_search_d_letter_all_states(app):
    app.login()
    app.search_d_letter_allstates()
    app.log_out()

def test_search_s_letter_daycare_state(app):
    app.login()
    app.search_daycare_s_letter_state()
    app.log_out()

def test_search_a_letter_elem_state(app):
    app.login()
    app.search_elementary_a_letter_state()
    app.log_out()

def test_search_j_letter_middle_state(app):
    app.login()
    app.search_middle_b_letter_state()
    app.log_out()

def test_search_s_letter_high_state(app):
    app.login()
    app.search_high_s_letter_state()
    app.log_out()

def test_search_s_letter_college_state(app):
    app.login()
    app.search_college_s_letter_state()
    app.log_out()

def test_search_s_letter_elem_middle_state(app):
    app.login()
    app.search_elem_middle_s_letter_state()
    app.log_out()

def test_search_d_letter_elem_high_state(app):
    app.login()
    app.search_elem_high_s_letter_d_letter_state()
    app.log_out()

def test_search_s_letter_mid_high_state(app):
    app.login()
    app.search_midl_high_s_letter_state()
    app.log_out()

def test_search_zipcode_with_state(app):
    app.login()
    app.search_zip_code_with_state()
    app.log_out()

def test_zipcode_no_criterion(app):
    app.login()
    app.search_zip_code_no_criteria()
    app.log_out()

def test_search_city_no_state(app):
    app.login()
    app.search_city_no_state()
    app.assort5()
    app.log_out()

def test_search_with_magnifying_glass(app):
    app.login()
    app.search_with_magnifying_glass()
    app.assort5()
    app.log_out()