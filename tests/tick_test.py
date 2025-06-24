from microbutton_core.button import Button

# Default parameters
button = Button()
try:
    button.tick()
except NotImplementedError as nie:
    assert nie
else:
    assert False, "No NotImplementedError Exception"


class ButtonChild(Button):
    def tick(self):
        raise Exception


btn_cld = ButtonChild()
try:
    btn_cld.tick()
except Exception as e:
    assert False, f"During test Raise Exception {e}"
else:
    assert True
