# Sublime text 3 configuration
I followed this guide https://medium.com/sabuj-jana/my-sublime-text-setup-for-competitive-coding-in-c-e439bd361f23  
I will resume it a lot

### Disadvantage over some online IDEs
When program throws an error during execution, you wont get proper error code, nor any usefull info.

### Install Sublime text 3
https://www.sublimetext.com/

### Install MinGW
http://www.mingw.org/  
(install all components from the basic setup)

### Path
add "C:\MinGW\bin to" system path (windows enviromental variables)  
*after this step, command "gcc" should be recogniced in windows cmd

## sublime text config
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
* create the files "source.cpp", "input.txt", "output.txt" and open them  
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
* set up a nice layout for your files: "View > layout > column:3" and then "View > groups > max columns:2"
* Now Click Build or Ctrl+B, and you should get the output into output.txt file

## code templates
to create a new code template, go to "tools > developer > new snippet"
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