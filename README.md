# auto-xjtu-proxy

## 介绍
该脚本可用于西安交通大学的VPN代理，将开启一个本地端口（默认127.0.0.1:12380），通过该端口访问的网站将返回重定向信息，重定向网址为相应网址的WEBVPN网址。需要的脚本分为两类，一类是Java Script，配合Tampermonkey使用，用于实现WEBVPN的自动登录，是非核心脚本；另一类是Python Script，配合Proxy SwitchyOmega使用，用于开启代理端口，并重定向网址。

## 使用说明

### 1.  浏览器插件安装

需要的浏览器插件为Tampermonkey(非核心脚本)和Proxy SwitchyOmega。

### 2. JavaScript-Tampermonkey (非核心脚本)

在Tampermonkey中，安装JavaScript文件夹下的两个脚本。

#### 2.1 Auto Click Login for XJTU WebVPN

Auto Click Login for XJTU WebVPN 用于自动点击网页的登录按钮，以便进行后续登录操作。
适用网址：[https://webvpn.xjtu.edu.cn/login](https://webvpn.xjtu.edu.cn/login)
该脚本不需要修改，直接使用

#### 2.2 Auto Login for XJTU WebVPN

Auto Login for XJTU WebVPN 用于自动填写账号和密码，并自动点击登录按钮，实现登录操作。
适用网址：https://webvpn.xjtu.edu.cn/http*/*/openplatform/login.html; https://org.xjtu.edu.cn/*/login.html
该脚本需要需改后使用，var username = "你的学号"; var password = "你的密码";

### 3.PythonScript-VBScript

#### 3.1 下载
下载PythonScript和VBScript置于同一文件夹下。

文件说明如下：

PythonScript/direct_port.py开启端口127.0.0.1:12380（端口可在脚本中修改），该端口不对流量进行任何修改。
PythonScript/proxy_port.py开启端口127.0.0.1:12380（端口可在脚本中修改），端口对浏览器返回重定向网页信息，返回的网页是原网页对应的WEBVPN网址。
PythonScript/run.py调用direct_port.py和proxy_port.py，并实现了脚本的托盘运行，对应的托盘图标为direct.png/proxy.png
PythonScript/requirements.txt为运行Python脚本需要的库。
VBScript/WebVPN.vbs可以在Windows环境下无窗口运行run.py，实现静默运行（不显示CMD窗口）。

#### 3.2 安装库

借助requirements.txt，安装对应的库。
可使用命令`pip3 install -r requirements.txt`或是`conda install --yes --file requirements.txt`进行安装。

#### 3.3 运行脚本

把PythonScript和VBScript置于同一文件夹下，双击WebVPN.vbs即可运行，运行后在托盘处显示图标。
可通过创建WebVPN.vbs快捷方式把程序放在开始菜单和开机启动，开机启动文件夹可在运行窗口中输入`shell:Common Startup`打开。
通过右击托盘图标，可以实现直连/代理模式切换。默认为直连模式。

### 4.  浏览器配置

运行脚本后，在Proxy SwitchyOmega中，设置127.0.0.1:12380端口，并添加需要连接代理端口的网页。

## 其他说明

在配置完成后，该程序可以一直运行，不必关闭。当使用校园网时，把模式切换为直连，而非校园网则切换为代理。
如果退出脚本时，则需要把Proxy SwitchyOmega中设置的代理网页清除，不然这些网页在浏览时，仍然通过设置的端口访问，但此时端口关闭，则无法连接。
所以，不建议退出该脚本。

同时，该脚本可以与其他VPN同时使用，通过Proxy SwitchyOmega来控制网页需要访问的端口。

#### 感谢

1. [lcandy2/webvpn-converter](https://github.com/lcandy2/webvpn-converter)
2. [spencerwooo/bit-webvpn-converter](https://github.com/spencerwooo/bit-webvpn-converter)
3. [ESWZY/webvpn-dlut](https://github.com/ESWZY/webvpn-dlut)


