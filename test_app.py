import app

def test_index():
    assert app.index() == "<h1>This is my Final Assignment</h1>"
def test_thank():
    assert app.thanks() == "<h2>Thank you <i >WincTeam,</i> for all the things you have done for me.</h2>"