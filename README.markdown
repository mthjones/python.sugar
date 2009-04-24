Python.sugar
============
A work-in-progress Sugar for the [Espresso text-editor][espresso] for development with [Python][].

[espresso]:	http://macrabbit.com/espresso/	"The Espresso text editor"
[python]:	http://python.org/				"The Python programming language"

If you are looking for the source for the Python.sugar project, check out the [source repository][srcrepo].

[srcrepo]: http://github.com/mthjones/python.sugar-source/ "The Python.sugar source repo on GitHub"

How to Use
----------
Install any dependencies as outlined below. The instructions to install them should be available by following the links.

Once the dependencies are installed, you have a couple of easy options to install this sugar:

Download the source in .zip or .tgz format using the [download button](#download_button) **or** clone this project to your computer using git:

	git clone git://github.com/mthjones/python.sugar.git "Python.sugar"

With Espresso versions 1.0.1 and later, you should be able to just double-click the file and it will install to Espresso. If that doesn't work, then:

Move or link it to the Espresso sugars folder (note you may need to create the folder first):

	mkdir -p ~/Library/Application\ Support/Espresso/Sugars/
	
	mv Python.sugar ~/Library/Application\ Support/Espresso/Sugars/
	-- or --
	ln -s Python.sugar ~/Library/Application\ Support/Espresso/Sugars/

Dependencies
------------
- [Regex.sugar][regexsugar]

[regexsugar]: http://github.com/elliottcable/Regex.sugar "elliottcable's Regex.sugar on GitHub"

More Information
----------------
This sugar uses the naming conventions as outlined by [elliottcable][] in his [Espresso Sugar Standard][ess]. Due to the fact that this standard is not set in stone and being followed by every sugar developer yet, certain themes/foams haven't been created to work with this naming convention. Therefore they may not highlight the syntax quite as nicely as one would like.

There are a few themes/foams that do work with the [Espresso Sugar Standard][ess], however.

- [Monokaffee][] (my own)
- Most themes on [Coffee House][coffee]

[elliottcable]: http://github.com/elliottcable/ "elltiottcable on GitHub"
[ess]: http://github.com/elliottcable/espresso-sugar-standard/tree/master "elliottcable's Espresso Sugar Standard on GitHub"
[monokaffee]: http://github.com/mthjones/monokaffee/ "mthjones' Monokaffee on GitHub"
[coffee]: http://fileability.net/coffee/ "Coffee House"

Because of the unpredictable nature of Espresso sugars and themes/foams, this sugar may change often, so it is worth watching.

TODO
----
See the [Todo List][todo] (located in the source repo)

[todo]: http://github.com/mthjones/python.sugar-source/blob/master/TODO.markdown
