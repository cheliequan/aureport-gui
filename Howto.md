# Introduction #

How to install aureport-gui,and how to add i18n support.


# Details #
**1. The step to generate rpm package**

> please run the command as follows:<br>
<blockquote>bash autogen.sh<br>
./confiure -prefix=/usr<br>
make rpm<br></blockquote>

if your system lack of PyQt,pychart,audit<br>
please run the command as follows:<br>
<blockquote>yum install PyQt<br>
yum install pychart<br>
yum install audit<br></blockquote>

<b>2. add po files</b>
<blockquote>modify the var "ALL_LINGUAS"in the configure.ac,for example.<br>
ALL_LINGUAS="zh_CN fr"<br>
add "fr.po" into po directory,run "make update-po".<br>
go to step 1<br>
~