from microbutton_core.button import Button, PRESS, UNPRESS

# Default parameters
button = Button()
assert button.is_click == False
assert button.is_double_click == False
assert button.is_multi_click == False
assert button.is_long_press == False
assert button.click_count == 0
assert button.state == UNPRESS
assert button.last_press_time == -1
# Press
button.state = PRESS
# Unpress
button.state = UNPRESS
assert button.click_count == 1
assert button.state == UNPRESS
assert button.last_press_time != -1