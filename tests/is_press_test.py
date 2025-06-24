from microbutton_core.button import Button, PRESS

# Default parameters
button = Button()
assert button.is_click == False
# Press
button.state = PRESS
assert button.is_click == False
assert button.is_double_click == False
assert button.is_multi_click == False
assert button.is_long_press == False
assert button.click_count == 0
assert button.last_press_time != -1
assert button.state == PRESS
