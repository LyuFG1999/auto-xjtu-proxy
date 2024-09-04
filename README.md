# auto-xjtu-proxy

#### 介绍
该脚本可用于西安交通大学的VPN代理，将开启一个本地端口（默认127.0.0.1:12380），通过该端口访问的网站将返回重定向信息，重定向网址为相应网址的WEBVPN网址。需要的脚本分为两类，一类是Java Script，配合Tampermonkey使用，用于实现WEBVPN的自动登录，是非核心脚本；另一类是Python Script，配合Proxy SwitchyOmega使用，用于开启代理端口，并重定向网址。

#### 使用说明

1.  浏览器插件安装

需要的浏览器插件为Tampermonkey(非核心脚本)和Proxy SwitchyOmega。

2. JavaScript-Tampermonkey (非核心脚本)

在Tampermonkey中，安装JavaScript文件夹下的两个脚本。

2.1 Auto Click Login for XJTU WebVPN
Auto Click Login for XJTU WebVPN 用于自动点击网页的登录按钮，以便进行后续登录操作。
适用网址：https://webvpn.xjtu.edu.cn/login
该脚本不需要修改，直接使用

2.2 Auto Login for XJTU WebVPN
Auto Login for XJTU WebVPN 用于自动填写账号和密码，并自动点击登录按钮，实现登录操作。
适用网址：https://webvpn.xjtu.edu.cn/http*/*/openplatform/login.html; https://org.xjtu.edu.cn/*/login.html
该脚本需要需改后使用，var username = "你的学号"; var password = "你的密码";

3.





2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
