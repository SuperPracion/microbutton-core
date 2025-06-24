from time import sleep
from microbutton_core.button import Button, PRESS, MIN_PRESS_TIME_OVER, LONG_PRESS

# Default parameters
button = Button()
assert button.is_click == False
# Click
button.state = PRESS
button.last_press_time = -1 #
sleep((MIN_PRESS_TIME_OVER + 1) / 1000)
button.state = PRESS
assert button.is_click == False
assert button.is_double_click == False
assert button.is_multi_click == False
assert button.is_long_press == True
assert button.click_count == 0
assert button.last_press_time == -1 #
assert button.state == LONG_PRESS
