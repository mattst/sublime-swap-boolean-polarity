#
# Name:             Swap Boolean Polarity
#
# File:             SwapBooleanPolarity.py
#
# Requirements:     Plugin for Sublime Text v.2 and v.3
#
# Tested:           ST v.3 build 3065 - tested and working.
#                   ST v.2 build 2221 - tested and working.
#
# Written by:       mattst - https://github.com/mattst
#
# Url:              https://github.com/mattst/sublime-swap-boolean-polarity
#
# Version:          0.1
#
# ST Command:       swap_boolean_polarity
#
# Description:      See class description below.
#

import sublime, sublime_plugin

class SwapBooleanPolarityCommand(sublime_plugin.TextCommand):
    """
    The SwapBooleanPolarityCommand class is a Sublime Text plugin which swaps
    the polarity of boolean values of any text which the current selection or
    selections are on. TRUE/True/true are translated to FALSE/False/false and
    visa-versa. The letter case (UPPER/Title/lower) used by each boolean value
    is preserved. All selections which are not on a boolean value are left in
    place and unaltered.
    """

    def run(self, edit, **kwargs):
        """
        run() is called when the command is run. Duhhh. :)
        """

        # The list of boolean values which are handled by this class.
        bool_list = [ "true", "false", "True", "False", "TRUE", "FALSE" ]

        # Loop through all the active selections.
        for sel in self.view.sel():

            # Get the region of the word which the selection is on.
            word_region = self.view.word(sel)

            # Get the text of word_region.
            word_text = self.view.substr(word_region)

            # If word_text is a boolean value.
            if word_text in bool_list:

                # Get the boolean's mirror value: true = false, false = true.
                swap_text = self.swap_boolean_polarity(word_text)

                # Replace word_text with swap_text.
                self.view.replace(edit, word_region, swap_text)

    # End of def run()

    def swap_boolean_polarity(self, bool_val):
        """
        swap_boolean_polarity() returns the opposite boolean value to bool_val
        while maintaining the letter case (UPPER/Title/lower) used by it.
        """

        if bool_val == "true":
            return "false"

        elif bool_val == "false":
            return "true"

        elif bool_val == "True":
            return "False"

        elif bool_val == "False":
            return "True"

        elif bool_val == "TRUE":
            return "FALSE"

        elif bool_val == "FALSE":
            return "TRUE"

        # Fail safe, should never happen.
        else:
            return bool_val

    # End of def swap_boolean_polarity()

# End of class SwapBooleanPolarityCommand()
