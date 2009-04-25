#!/usr/bin/env python
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
		print("hello!")
		print  ("hello")
		print "hello"
		globals()
		file
		file('some random path')
		self.__init__
		self.  do_something
	

lambda abc=5, a, e: print(x)

# keywords
from blah import *
import a

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