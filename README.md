# alpha2phon
A terminal utility written in Python that converts Latin letters and numbers to their NATO phonetic versions.
## Why?
I made this program primarily because I am interested in ham radio, and I wanted to ease my experience by creating this program so I don't have to manually memorize every phonetic character, but also for my grandpa who is also interested in ham radio.
## How to set up
You need to have the Python programming language installed on your computer. The alpha2phon.py file be in your home directory.
In Windows create the file <code>alpha2phon.bat</code> inside of your home directory (C:\Users\{YOURNAMEHERE}) and let it contain this text:
<pre>
@py.exe %USERPROFILE%\alpha2phon.py %*
</pre>
For Linux, the Python programming language is alredy preinstalled on most distributions. Make the file <code>alpha2phon</code> in your home directory, and make it contain this code:
<pre>
#!/usr/bin/env bash
python3 $HOME/alpha2phon.py "$@"
</pre>
Then, move the file to <code>/usr/bin</code>.
