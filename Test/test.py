#!/usr/bin/env python
# encoding: utf-8
"""
@description Python Sugar tests
@author 	 Matt Jones <m.t.h.jones@gmail.com>
@copyright 	 The MIT License

Copyright (c) 2009

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
# single-line comment

# string
"hello there"
r"hello there"
u"hello there"

# regex
r"[123]*"

# triple-quoted string/docstring
"""
long string is looooooo
ooooooooooooooooooooooo
ooooooooooooooooooooong
"""

# string escaping
"\a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\u\v\w\x\y\z \\\"\'"
"\u1111"
"\uGGGG" # should fail: can only take hex values (G not in hex)
"\U11111111"
"\UGGGGGGGG" # should fail: can only take hex values (G not in hex)
"\x12"
"\xGG" # should fail: can only take hex values (G not in hex)
"\x111" # should only match first two numbers after \x

# numbers
1
-1

1.1
-1.1

.1
-.1

1.
-1.

0.1
-0.1
0.1e10
0.1e-10
-0.1e10
-0.1e-10

1e10
-1e10
1e-10
-1e-10

0j
1+0j
1-15j
0 ++++++ 1j
1.5 ++++ 1j
1.5e10 ++ 1.0j
0b11001 +-+ 20j

0b010111
0b000002 # should fail: 2 not binary
0x123456
0xAAAAAG # should fail: G not hex
0o123456
0o111118 # should fail: 8 not oct
01234567
01111118 # should fail: 8 not oct

1L
0b0L
0x0L
0o0L
0L

# collection literals
# list:
[1, 2, 3, 4, 5, 6]

# dict:
{1: 2, 3: 4, 5: 6}
{
 "a": 2,
 "b": 3,
 "c": 4
}
{1:2}

# set:
{1, 2, 3, 4, 5, 6} # should not be dictionary!
{'abc:'} # should not be dictionary!

# tuple:
(1, 2, 3, 4, 5, 6)

# storage types
@classwrapper
class ABC(object, metaclass=Blah):
	__metaclass__ = ABCMeta
	
	@not_builtin_decorator
	@classmethod
	def a(self, b, c, d):
		if a:
			do_something
		else:
			do_something_else
		
		print("hello!")
		print  ("hello")
		print "hello"
		globals()
		file
		file('some random path')
		self.__init__
		self.  do_something
	

lambda abc=5, a, e, a=(1,2,3): print(x)

# keywords
from blah import *
from abc import abc
import a

from Calendar import something as name

from

try
except
finally
raise

for
while
if
elif
else
with

break
continue
pass
return
yield

global
nonlocal

as
assert
del
exec
print

class
def
lambda 			:

# operators
>
<
>=
<=
==
!=
<>

+=
-=
*=
/=
//=
**=
%=
<<=
>>=
&=
|=
^=
=

+
-
*
/
//
**
>>
<<
%

&
|
^
~
is
and
or
not
in

# delimiters
;
{  }
(  )
[  ]
,
:
.
"  "
'  '
`  `

if a:
	print("a")
elif b:
	print("b")
else:
	print("dunno")


