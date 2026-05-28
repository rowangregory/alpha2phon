# alpha2phon
A terminal utility written in Python that converts letters and numbers to their NATO phonetic versions.
## Why?
I made this program primarily because I am interested in ham radio, and I wanted to ease my experience by creating this program so I don't have to manually memorize every phonetic character, but also for my grandpa who is also interested in ham radio.
## How to set up
You need to have the Python programming language installed on your computer. The alpha2phon.py file be in your home directory.
In Windows create the file <code>alpha2phon.bat</code> inside of your home directory (C:\Users\{YOURNAMEHERE}) and let it contain this text:
<pre>
@py.exe %USERPROFILE%\alpha2phon.py %*
</pre>
For Linux, the Python programming language is already preinstalled on most distributions. Make sure the file is at least somewhere in your PATH (https://unix.stackexchange.com/questions/36871/where-should-a-local-user-executable-be-placed-under-home/36874#36874), such as <code>/home/{YOURNAMEHERE}/.local/bin/</code> or <code>/home/{YOURNAMEHERE}/bin/</code>, and make it contain this code:
<pre>
#!/usr/bin/env bash
python3 $HOME/alpha2phon.py "$@"
</pre>
Then run <code>chmod +x alpha2phon</code> in the directory alpha2phon is in to make it actually runnable.
