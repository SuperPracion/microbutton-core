from microbutton_core.button import Button, PRESS, UNPRESS

# Default parameters
button = Button()
assert button.state == UNPRESS
assert button.press_value == PRESS
assert button.unpress_value == UNPRESS
assert button.last_press_time == -1
assert button.click_count == 0


# Specific parameters
button = Button(
    state=PRESS,
    press_value=UNPRESS,
    unpress_value=PRESS,
)
assert button.state == PRESS
assert button.press_value == UNPRESS
assert button.unpress_value == PRESS
assert button.last_press_time == -1
assert button.click_count == 0


# Bad parameters Press == Unpress
try:
    button = Button(
        press_value=PRESS,
        unpress_value=PRESS,
    )
except AttributeError as atr:
    assert atr
else:
    assert False, "No AttributeError Exception"

try:
    button = Button(
        press_value=UNPRESS,
        unpress_value=UNPRESS,
    )
except AttributeError as atr:
    assert atr
else:
    assert False, "No AttributeError Exception"
