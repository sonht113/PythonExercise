
# Author: Ho Trong Son
# Date: 06/07/2021
# Program: project_page_33
# PROBLEM:
#     1. Open a Python shell, enter the following expressions, and observe the results:
#     a. 8
#     b. 8 * 2
#     c. 8 ** 2
#     d. 8/12
#     e. 8 // 12
#     f. 8/0

#     2. Write a Python program that prints (displays) your name, address, and telephone number.

#     3. Evaluate the following code at a shell prompt: print ("Your name is", name).Then assign name an appropriate value, and evaluate the statement again.

#     4. Open an IDLE window, and enter the program from Figure 1-7 that computes the area of a rectangle. Load the program into the shell by pressing the F5 key,
#     and correct any errors that occur. Test the program with different inputs by
#     running it at least three times.

#     5. Modify the program of Project 4 to compute the area of a triangle. Issue the appropriate prompts for the triangle’s base and height, and change the names of
#     the variables appropriately. Then, use the formula .5 * base * height to compute the area. Test the program from an IDLE window.

#     6. Write and test a program that computes the area of a circle. This program should request a number representing a radius as input from the user. It should use the formula
#     3.14 * radius ** 2 to compute the area and then output this result suitably labeled.

#     7. Write and test a program that accepts the user’s name (as text) and age (as a number)
#     as input. The program should output a sentence containing the user’s name and age.

#     8. Enter an input statement using the input function at the shell prompt. When the
#     prompt asks you for input, enter a number. Then, attempt to add 1 to that number, observe the results, and explain what happened.

#     9. Enter an input statement using the input function at the shell prompt. When the prompt asks you for input, enter your first name, observe the results, and explain
#     what happened.

#     10. Enter the expression help() at the shell prompt. Follow the instructions to browse the topics and modules.


#     SOLUTION:

#  1) Open a Python shell, enter the following expressions, and observe the results:

#   a)
from typing import NamedTuple
print(8)
#   b)
print(8*2)
#   c)
print(8**2)
#   d)
print(8/12)
#   e)
print(8//12)
#   f)
#   print(8/0)
try:
    print(8/0)
except ZeroDivisionError:
    print ("Error!!!")

#   2) Write a Python program that prints (displays) your name, address, and telephone number.

print("Name: Hồ Trọng Sơn")
print("Address: My Chau - Phu My - Binh Dinh")
print("Phone: 0399187817")

#   3) Evaluate the following ode at a shell prompt: print ("Your name is", name).Then assign name an appropriate value, and evaluate the statement again.
name = input("Enter your name: ")
print("Your name is: " + name) # nếu chỉ dòng code này thif sẽ lỗi biến name undefine... Nên ta sẽ định nghĩa cho biến name bằng cách nhập giá trị name tùy ý từ console

#   4) Open an IDLE window, and enter the program from Figure 1-7 that computes the area of a rectangle. Load the program into the shell by pressing the F5 key,and correct any errors that occur. Test the program with different inputs byrunning it at least three times.
width = int(input("Enter with width: "))
height = int(input("Enter with height: "))
area = width * height
print("The area is", area, "square units.")
#   test 1:
#   Enter with width: 10
#   Enter with height: 5
#   The area is 50 square units.

#   test 2:
#   Enter with width: 8
#   Enter with height: 2
#   The area is 16 square units.

#   test 3:
#   Enter with width: 10
#   Enter with height: 7
#   The area is 70 square units.

#   5) Modify the program of Project 4 to compute the area of a triangle. Issue the appropriate prompts for the triangle’s base and height, and change the names ofthe variables appropriately. Then, use the formula .5 * base * height to compute the area. Test the program from an IDLE window.
base = float(input("Enter with base: "))
height = float(input("Enter with height: "))
area =  0.5 * base * height
print("The area is", area, "square units.")

#   Enter with base: 3
#   Enter with height: 4
#   The area is 6 square units.

#   6) Write and test a program that computes the area of a circle. This program should request a number representing a radius as input from the user. It should use the formula 3.14 * radius ** 2 to compute the area and then output this result suitably labeled.
from math import pi
r = float(input ("Input the radius of the circle : "))
area = pi * r**2
print("The area of the circle with radius " + str(r) + " is: " + str(area))
#   Input the radius of the circle : 8
#   The area of the circle with radius 5.0 is: 201.06192982974676

#   7) Write and test a program that accepts the user’s name (as text) and age (as a number) as input. The program should output a sentence containing the user’s name and age.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name, "is", age, "years old.")
#   Enter your name: Son
#   Enter your age: 22
#   Son is 22 years old.

#   8) Enter an input statement using the input function at the shell prompt. When theprompt asks you for input, enter a number. Then, attempt to add 1 to that number, observe the results, and explain what happened.
number = input('Number: ')
number = number + 1
print(number)
#    num = num + 1
#   TypeError: can only concatenate str (not "int") to str (The error “typeerror: can only concatenate str (not “int”) to str” is raised when you try to concatenate a string and an integer)
#   Correct code:
#   number = int(input('Please enter number: '))
#   number = number + 1
#   print("Number after: " + number)
#   Number: 5
#   Number after: 6

#   9) Enter an input statement using the input function at the shell prompt. When the prompt asks you for input, enter your first name, observe the results, and explain what happened
first_name = input("Enter your first name:")
print(first_name)
#   Enter your first name :Son
#   => Son
#   No error behind run program

#   10) Enter the expression help() at the shell prompt. Follow the instructions to browse the topics and modules.
help()
# trongson@MyComputer7250:~/Documents/HoTrongSon_50150$ python3
# Python 3.9.5 (default, May 11 2021, 08:20:37)
# [GCC 10.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> help
# Type help() for interactive help, or help(object) for help about object.
# >>> help()
#
# Welcome to Python 3.9's help utility!
#
# If this is your first time using Python, you should definitely check out
# the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.
#
# Enter the name of any module, keyword, or topic to get help on writing
# Python programs and using Python modules.  To quit this help utility and
# return to the interpreter, just type "quit".
#
# To get a list of available modules, keywords, symbols, or topics, type
# "modules", "keywords", "symbols", or "topics".  Each module also comes
# with a one-line summary of what it does; to list the modules whose name
# or summary contain a given string such as "spam", type "modules spam".
#
# help> topics
#
# Here is a list of available topics.  Enter any topic name to get more help.
#
# ASSERTION           DELETION            LOOPING             SHIFTING
# ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
# ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
# ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
# AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
# BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
# BINARY              EXECUTION           NONE                STRINGS
# BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
# BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
# CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
# CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
# CLASSES             FRAMES              PACKAGES            TUPLES
# CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
# COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
# COMPLEX             IMPORTING           PRIVATENAMES        UNARY
# CONDITIONAL         INTEGER             RETURNING           UNICODE
# CONTEXTMANAGERS     LISTLITERALS        SCOPING
# CONVERSIONS         LISTS               SEQUENCEMETHODS
# DEBUGGING           LITERALS            SEQUENCES
#
# help> modules
#
# Please wait a moment while I gather a list of all available modules...
#
# /usr/lib/python3/dist-packages/UpdateManager/backend/__init__.py:11: PyGIWarning: Gtk was imported without specifying a version first. Use gi.require_version('Gtk', '3.0') before import to ensure that the right version gets loaded.
#   from gi.repository import GLib, Gtk, Snapd
# AptUrl              _yaml               gtweak              re
# CommandNotFound     _zoneinfo           gzip                readline
# DistUpgrade         abc                 hashlib             reportlab
# HweSupportStatus    aifc                heapq               reprlib
# LanguageSelector    antigravity         hmac                requests
# NvidiaDetector      apport              hpmudext            resource
# PIL                 apport_python_hook  html                rlcompleter
# Quirks              apt                 http                runpy
# UbuntuDrivers       apt_inst            httplib2            scanext
# UpdateManager       apt_pkg             icecream            sched
# Xlib                aptdaemon           idna                secrets
# __future__          aptsources          imaplib             secretstorage
# _abc                argparse            imghdr              select
# _aix_support        array               imp                 selectors
# _ast                ast                 importlib           setuptools
# _asyncio            asttokens           inspect             shelve
# _bisect             asynchat            io                  shlex
# _blake2             asyncio             ipaddress           shutil
# _bootlocale         asyncore            itertools           signal
# _bootsubprocess     atexit              janitor             simplejson
# _bz2                audioop             jeepney             site
# _cffi_backend       base64              json                sitecustomize
# _codecs             bcrypt              jwt                 six
# _codecs_cn          bdb                 kazam               smtpd
# _codecs_hk          binascii            keyring             smtplib
# _codecs_iso2022     binhex              keyword             sndhdr
# _codecs_jp          bisect              language_support_pkgs socket
# _codecs_kr          blinker             launchpadlib        socketserver
# _codecs_tw          brlapi              ldb                 softwareproperties
# _collections        builtins            lib2to3             speechd
# _collections_abc    bz2                 libfuturize         speechd_config
# _compat_pickle      cProfile            libpasteurize       spwd
# _compression        cairo               linecache           sqlite3
# _contextvars        calendar            locale              sre_compile
# _crypt              certifi             lockfile            sre_constants
# _csv                cgi                 logging             sre_parse
# _ctypes             cgitb               louis               ssl
# _ctypes_test        chardet             lsb_release         stat
# _curses             chunk               lzma                statistics
# _curses_panel       click               macaroonbakery      string
# _datetime           cmath               mailbox             stringprep
# _dbm                cmd                 mailcap             struct
# _dbus_bindings      code                mako                subprocess
# _dbus_glib_bindings codecs              markupsafe          sunau
# _decimal            codeop              marshal             symbol
# _distutils_hack     collections         math                symtable
# _elementtree        colorama            mimetypes           sys
# _functools          colorsys            mmap                sysconfig
# _gdbm               compileall          modulefinder        syslog
# _hashlib            concurrent          monotonic           systemd
# _heapq              configparser        multiprocessing     tabnanny
# _imp                contextlib          nacl                talloc
# _io                 contextvars         netifaces           tarfile
# _json               copy                netrc               telnetlib
# _ldb_text           copyreg             nis                 tempfile
# _locale             crypt               nntplib             termios
# _lsprof             cryptography        ntpath              test
# _lzma               csv                 nturl2path          textwrap
# _markupbase         ctypes              numbers             this
# _md5                cups                oauthlib            threading
# _multibytecodec     cupsext             olefile             time
# _multiprocessing    cupshelpers         opcode              timeit
# _opcode             curses              operator            token
# _operator           dataclasses         optparse            tokenize
# _osx_support        datetime            orca                trace
# _peg_parser         dateutil            os                  traceback
# _pickle             dbm                 ossaudiodev         tracemalloc
# _posixshmem         dbus                paramiko            tty
# _posixsubprocess    deb822              parser              turtle
# _py_abc             debconf             past                types
# _pydecimal          debian              pathlib             typing
# _pyio               debian_bundle       pcardext            uaclient
# _queue              decimal             pdb                 ufw
# _random             defer               pexpect             unicodedata
# _sha1               difflib             pickle              unittest
# _sha256             dis                 pickletools         uno
# _sha3               distro              pip                 unohelper
# _sha512             distro_info         pipes               urllib
# _signal             distutils           pkg_resources       urllib3
# _sitebuiltins       doctest             pkgutil             usbcreator
# _socket             duplicity           platform            uu
# _sqlite3            email               plistlib            uuid
# _sre                encodings           poplib              venv
# _ssl                enum                posix               wadllib
# _stat               errno               posixpath           warnings
# _statistics         executing           pprint              wave
# _string             fasteners           problem_report      weakref
# _strptime           faulthandler        profile             webbrowser
# _struct             fcntl               pstats              wheel
# _symtable           filecmp             pty                 wsgiref
# _sysconfigdata__linux_x86_64-linux-gnu fileinput           ptyprocess          xdg
# _sysconfigdata__x86_64-linux-gnu fnmatch             pwd                 xdrlib
# _testbuffer         formatter           py_compile          xkit
# _testcapi           fractions           pyatspi             xml
# _testimportmultiple ftplib              pyclbr              xmlrpc
# _testinternalcapi   functools           pydoc               xxlimited
# _testmultiphase     future              pydoc_data          xxsubtype
# _thread             gc                  pyexpat             yaml
# _threading_local    genericpath         pygments            zipapp
# _tracemalloc        getopt              pygtkcompat         zipfile
# _uuid               getpass             pymacaroons         zipimport
# _warnings           gettext             pyrfc3339           zlib
# _weakref            gi                  pytz                zoneinfo
# _weakrefset         glob                queue
# _xxsubinterpreters  graphlib            quopri
# _xxtestfuzz         grp                 random
#
# Enter any module name to get more help.  Or, type "modules spam" to search
# for modules whose name or summary contain the string "spam".
