# Sublime text 3 configuration
I followed this guide https://medium.com/sabuj-jana/my-sublime-text-setup-for-competitive-coding-in-c-e439bd361f23  
I will resume it a lot

### Disadvantage over some online IDEs
When program throws an error during execution, you wont get proper error code, nor any usefull info.

### Install Sublime text 3
https://www.sublimetext.com/
##### * You can skip sublime text instalation and config if u just copy the installed program folder in this repo

### Install MinGW
http://www.mingw.org/  
(install all components from the basic setup)

### Path
add "C:\MinGW\bin to" system path (windows enviromental variables)  
*after this step, command "gcc" should be recogniced in windows cmd

## sublime text config
#### Building
* Go to Tools>Build System>New build system...
* paste this on the file that will open, and save it (name of file is the name of build system)  
```
{
  "cmd": ["g++.exe","-std=c++17", "${file}", "-o", "${file_base_name}.exe", "&&" , "${file_base_name}.exe<input.txt>output.txt"],
  "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
  "working_dir": "${file_path}",
  "selector": "source.cpp",
  "shell": true  
}
```

* Go to Tools>Build System>YourSystemName
* create the files "source.cpp", "input.txt", "output.txt" on the same folder, and open them  

content of source.cpp
```
#include <iostream>
using namespace std;
int main() {	
    int x;
    cin>>x;
    int y=25;
    cout<<"Sum of x+y = " << x+y;
    return 0;
}
```
content of input.txt
```
15
```
* Now Click Build (Ctrl+B by default), and you should get the output into output.txt file

#### Layout
* set up a nice layout for your files: "View > layout > column:3" and then "View > groups > max columns:2"

#### Changing keybindings
Go to Preferences->key bindings
will open two files, the default keybindings and the user keybindings.

for example u can change "build" and "cancel_build" keybinds to f1 and f2 pasting this code into the user keybindings file
```
[
	{ "keys": ["f1"], "command": "build" },
	{ "keys": ["f2"], "command": "cancel_build" },
]
```

## Code templates
To create a new code template, go to "tools > developer > new snippet"
and paste this in the snippet file
```
<snippet>
	<content><![CDATA[
//#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main() {	
	int x;
	cin>>x;
	while(x>0){
		printf("%d\n",x);
		x--;
	}
}
]]></content>
	<tabTrigger>nkbasic</tabTrigger>
</snippet>
```
now, when u type nkbasic, tab will autocomplete with the content of the snippet