__all__ = ["Button"]
__version__ = "1.0.0"
__author__ = "Akhmetov Timur Elmirovich"

from time import time

# PRESS - 0
# UNPRESS - 1
# LONG_PRESS = 2
# Click - Click count == 1
# Double Click - Click count == 2
# Multi Click - Click count > 2

PRESS = 0
UNPRESS = 1
LONG_PRESS = 2
MIN_PRESS_TIME_OVER = 400  # ms


class Button:

    def __init__(
        self,
        state: int = UNPRESS,
        press_value: int = PRESS,
        unpress_value: int = UNPRESS,
    ):
        if press_value == unpress_value:
            raise AttributeError(
                f"press_value: {press_value} and unpress_value {unpress_value} are equal!"
            )
        self._state = state
        self.press_value = press_value
        self.unpress_value = unpress_value
        self.last_press_time = -1
        self.click_count = 0

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: int):
        now = time()
        if value == self.press_value:
            if (
                self._state == PRESS
                and (now - self.last_press_time) > MIN_PRESS_TIME_OVER
            ):
                # Long press
                self._state = LONG_PRESS
                self.click_count = 0
            elif self._state == UNPRESS:
                # Press
                self._state = PRESS
                self.last_press_time = now
        elif value == self.unpress_value:
            # Unpress
            if (now - self.last_press_time) > MIN_PRESS_TIME_OVER:
                self.click_count = 0
                # Reset Press
            if self._state in [PRESS, LONG_PRESS]:
                # Click
                self.click_count += 1
            self._state = UNPRESS

    @property
    def is_press(self) -> bool:
        """Return True if current button state is PRESS"""
        return self._state == PRESS

    @property
    def is_unpress(self) -> bool:
        """Return True if current button state is UNPRESS"""
        return self._state == UNPRESS

    @property
    def is_long_press(self) -> bool:
        """Return True if button long press or False other"""
        return self._state == LONG_PRESS

    @property
    def is_click(self) -> bool:
        """Return True if button click of False other"""
        return self.click_count == 1

    @property
    def is_double_click(self) -> bool:
        """Return True if button double click or False other"""
        return self.click_count == 2

    @property
    def is_multi_click(self) -> bool:
        """Return True if button multi click or False other"""
        return self.click_count > 2

    def tick(self):
        raise NotImplementedError(
            "Function tick() is necessary! In tick function assign self.value = new value from data source."
        )
