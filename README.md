
## Sublime Text Plugin - Swap Boolean Polarity

This is a Sublime Text plugin which swaps the polarity of boolean values of any
text which the current selection or selections are on.

The values TRUE/True/true are translated to FALSE/False/false and visa-versa.
The letter case (UPPER/Title/lower) used by each boolean value is preserved. Any
selections which are not on a boolean value are left in place and unaltered.

The command is designed to be run using the keyboard so that any boolean value
can have its polarity quickly swapped. Although it does not take long to type
*true* or *false* it is something that coders do on a regular basis and a
keypress does it faster. I was surprised that nobody had written a Sublime Text
plugin to do this, since writing it I've found myself using it a lot. It is
especially useful when you want to swap several boolean values, for instance
while testing, just create multiple selections on the boolean values and hit the
command's keys.

#### Requirements / Tested:

- Sublime Text v.2 or v.3
- ST v.2 (Build 2221) - tested and working.
- ST v.3 (Build 3065) - tested and working.

#### Installation:

In the near future I will set up a package and release this plugin using
[PackageControl](https://sublime.wbond.net) the Sublime Text Package Manager,
this will allow for easy installation from within Sublime Text.

For the time being please install manually.

- Create a directory called `SwapBooleanPolarity` in your Sublime Text packages
directory.
- Put the files from this repository into that directory.

#### Setup:

Add the keys line below to your user Key Bindings file, altering the actual keys
specified below to whatever key combination you want to use. `ctrl+shift+b` are
the keys which I use but my build keys have been changed to keys that suit me
better.

``` json
{"keys": ["ctrl+shift+b"], "command": "swap_boolean_polarity" },
```

