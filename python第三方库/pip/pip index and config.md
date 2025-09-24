[pip documentation v25.2](https://pip.pypa.io/en/stable/)

[腾讯云pip源配置](https://cloud.tencent.com/developer/article/1601851)
[使用腾讯云镜像源加速pip](https://mirrors.cloud.tencent.com/help/pypi.html)

常见的 PyPI（Python Package Index）软件包镜像源：

- Official: https://pypi.org/
- 腾讯云: https://mirrors.cloud.tencent.com/pypi/simple/
- 阿里云: https://mirrors.aliyun.com/pypi/simple/
- 百度: https://mirror.baidu.com/pypi/simple
- 清华大学: https://pypi.tuna.tsinghua.edu.cn/simple/
- 中国科技大学: https://pypi.mirrors.ustc.edu.cn/simple/

## pip install from specific index

```bash
$ pip3 help install

Package Index Options:

  -i, --index-url <url>       Base URL of the Python Package Index (default https://pypi.org/simple). This
                              should point to a repository compliant with PEP 503 (the simple repository API)
                              or a local directory laid out in the same format.

General Options:

  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.

  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid
                              or any HTTPS.

```

用 pip 安装软件包时，可通过 `-i` 选项临时指定 Index 镜像源（One-time use）。例如，指定从腾讯云pypi软件源下载安装 tccli：

```bash
pip install tccli -i http://mirrors.tencentyun.com/pypi/simple
```

> WARNING: The repository located at mirrors.tencentyun.com is not a trusted or secure host and is being ignored.

通过 `--trusted-host` 选项可以指定可信主机，即使它没有有效的 HTTPS 证书也可以被信任。

```bash
pip install tccli -i http://mirrors.tencentyun.com/pypi/simple --trusted-host mirrors.tencentyun.com
```

以上 HTTP 域名已经停止服务，建议改用 HTTPS 新域名：

```bash
pip install tccli -i https://mirrors.cloud.tencent.com/pypi/simple --trusted-host mirrors.cloud.tencent.com
```

## pip config set global.index-url

如果 pip3 -V >= 10.0.0，也可考虑使用 `pip config set` 命令配置全局 index-url 和 trusted-host。

pip3 config 配置命令的完整格式：`pip3 config [<file-option>] subcommand [command.option] [value]`。

> [Configuration - pip documentation v25.2](https://pip.pypa.io/en/stable/topics/configuration/)

关于 `file-option`，可选 `--user`、`--global` 和 `--site` 三个级别：

- `--global`: Use the system-wide configuration file only
- `--user`: Use the user configuration file only
- `--site`: Use the current environment configuration file only

> If none of `--user`, `--global` and `--site` are passed, a virtual environment configuration file is used if one is *active* and the file *exists*, e.g., site: `$HOME/.venv/pip.conf`. Otherwise, all modifications happen to the user file by *default*, i.e., `$HOME/.config/pip/pip.conf`.

执行 `pip3 config debug` 将列举 global、user、current 三个级别的配置文件，以及配置文件中的具体配置（如果有的话）。

```bash
$ pip3 config debug
env_var:
env:
global:
  /opt/homebrew/share/pip/pip.conf, exists: False
  /Library/Application Support/pip/pip.conf, exists: False
site:
  /opt/homebrew/opt/python@3.13/Frameworks/Python.framework/Versions/3.13/pip.conf, exists: False
user:
  /Users/faner/.pip/pip.conf, exists: False
  /Users/faner/.config/pip/pip.conf, exists: False
```

`pip3 config` 子命令（Subcommands）如下：

- **list**: List the active configuration (or from the file specified)
- **edit**: Edit the configuration file in an editor
- **get**: Get the value associated with command.option
- **set**: Set the command.option=value
- **unset**: Unset the value associated with command.option
- **debug**: List the configuration files and values defined under them

执行 `pip3 config set global.option value` 全局配置将会写入当前用户的配置文件 `$HOME/.config/pip/pip.conf`。

```bash
pip3 config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
pip3 config get global.index-url
pip3 config set global.trusted-host mirrors.cloud.tencent.com
pip3 config get global.trusted-host
```

执行 `pip3 config list` 可以查看所有的配置项；执行 `pip3 config debug` 可检查写入到哪个配置文件。

如果想取消配置，则可以执行 `pip3 config unset global.option`。

```bash
pip3 config unset global.index-url
pip3 config unset global.trusted-host
```

## pip config set global.proxy

此外，pip install 支持通过选项 `--proxy` 指定通过代理服务器访问 PyPI 软件源，例如通过 Web Proxy 192.168.6.140:8080 下载安装 requests 包：

```bash
pip3 install requests --proxy http://192.168.6.140:8080
```

也可以将 proxy 选项参数配置到全局配置文件中，这样就不需要每次都指定 `--proxy` 选项了。

```bash
# set proxy
pip3 config set global.proxy http://192.168.6.140:8080
# read proxy
pip3 config get global.proxy
# unset proxy
pip3 config unset global.proxy
```

也可在终端设置 `HTTP_PROXY` 和 `HTTPS_PROXY` 环境变量来指定命令行代理：

```bash
HTTP_PROXY=http://192.168.6.140:8080
HTTPS_PROXY=https://192.168.6.140:8080
echo $HTTP_PROXY
echo $HTTPS_PROXY

# for Windows Command Prompt
set HTTP_PROXY=http://192.168.6.140:8080
set HTTPS_PROXY=https://192.168.6.140:8080
echo %HTTP_PROXY%
echo %HTTPS_PROXY%
```

在 Unix-Like OS 中，可通过 export 将代理环境变量导出到所有 subshells 中：

```bash
export HTTP_PROXY=http://192.168.6.140:8080
export HTTPS_PROXY=https://192.168.6.140:8080
```

在 macOS 中，通过 System Settings | Network | Wi-Fi | Details | Proxies 设置 HTTP、HTTPS、SOCKS 代理。
在 Windows 中，通过 Settings | Network & Internet | Proxy | Manual proxy setup | Use a proxy server 设置代理服务器。

- 对于老版 Windows 系统，Win+R 输入 `inetcpl.cpl` 可快速调起 IE 的 **Internet 选项**，通过 Connections | LAN settings 设置 Proxy Server。
