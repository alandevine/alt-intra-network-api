class HandSanitizer:

    """Interface between Network and hand sanitizer unit

        :param unit_id: unique id assigned by server
        :type unit_id: int

        :param config_file_path: path to json config file
        :type config_file_path: string

        :param unit_capacity_ml: capacity of the unit in ml
        :type unit_capacity_ml: int

        :param dispense_amount_ml: amount of liquid dispensed in ml
        :type dispense_amount_ml: int

        :param minimum_amount_ml: minimum amount of liquid for the unit to be operational
        :type minimum_amount_ml: int

        :param sanitizer_threshold: percentage of liquid in the unit in which a notification is sent to the user
        :type sanitizer_threshold: float

        TODO:
            - Add all methods pertaining to the spec
        """

    def __init__(self,
                 unit_id,
                 config_file_path,
                 unit_capacity_ml,
                 dispense_amount_ml,
                 minimum_amount_ml,
                 sanitizer_threshold):

        """Constructor Method"""

        self.unit_id = unit_id
        self.config_file_path = config_file_path
        self.unit_capacity_ml = unit_capacity_ml
        self.dispense_amount_ml = dispense_amount_ml
        self.minimum_amount_ml = minimum_amount_ml
        self.sanitizer_threshold = sanitizer_threshold

    def set_dispense_amount(self, quantity):
        """Method for setting the dispense amount

        :param quantity: amount of liquid dispensed in ml
        :type quantity: int
        :raises AssertionError: if a negative number or a number that is greater than the total capacity of the unit
                                is provided an AssertionError will be thrown.
        :rtype: void

        TODO:
            - Replace Assert with try/ except block
        """
        assert 0 < quantity < self.unit_capacity_ml
        self.dispense_amount_ml = quantity

    def set_sanitizer_threshold(self, thresh):
        """Method for setting the quantity threshold
        :param thresh: amount of liquid dispensed in ml
        :type thresh: float
        :raises AssertionError: If a negative float or a float greater than 1 is provided, an AssertionError will be
                                thrown.
        :rtype: void

        TODO:
            - Replace Assert with try/ except block
        """
        assert 0 < thresh < 1.0
        self.sanitizer_threshold = thresh

    def _calc_minimum_amount(self):
        """Generates a somewhat arbitrary number
        this is subject to change
        """

        self.minimum_amount_ml = self.dispense_amount_ml * 2

    def update_config_file(self):
        pass
