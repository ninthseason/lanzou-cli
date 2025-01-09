> ### lanzou/ 来自于 https://github.com/zaxtyson/LanZouCloud-API
> 
> ### 但由于存在致命BUG [#110](https://github.com/zaxtyson/LanZouCloud-API/issues/110),[#109](https://github.com/zaxtyson/LanZouCloud-API/issues/109) 且仍未修复，故暂且将修复版置于仓库内，待修复后再添加至 requirements.txt

---

一个简要的上传文件至蓝奏云的命令行工具。

仅支持上传文件：`python lanzou-cli.py <filename>`

上传成功将返回`0`，并于标准输出打印`<文件分享url> <文件密码> <下载直链>`

遇到任何错误将返回错误码：

- -3: 参数错误
- -2: 无法读取 cookie.json
- 其余错误码与 LanZouCloud-API 一致: https://github.com/zaxtyson/LanZouCloud-API/wiki/0x01-%E9%94%99%E8%AF%AF%E7%A0%81%E8%AF%B4%E6%98%8E

所有错误提示均打印于标准错误输出。

---

需要准备`cookie.json`于根目录下，以供程序读取。其格式为：

```json
{
  "phpdisk_info": "...",
  "ylogin": "..."
}
```

详情请见此处：https://github.com/zaxtyson/LanZouCloud-API/wiki/0x02-%E7%99%BB%E5%BD%95%E5%92%8C%E6%B3%A8%E9%94%80#login_by_cookiecookie
