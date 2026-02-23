from app import app

def test_001_header_presence(dash_duo):

    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)

def test_002_visualisation_presence(dash_duo):

    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-graph", timeout=10)

def test_003_radio_buttons_presence(dash_duo):

    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-radio", timeout=10)