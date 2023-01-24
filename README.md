![](assets/logo.svg)

[**简体中文**](README.md) | [English](README.en.md)

---

## 简介

[PDFuck](https://github.com/mmdjiji/pdfuck) 是一个去除 PDF 编辑密码的工具，以命令行方式使用。

## 安装

在安装前，请确保你安装了 Python (>=3.0) 及与之版本相匹配的 pip，然后在命令提示符中输入下面的命令：

```bash
pip install pdfuck
```

## 使用

### 去除 PDF 密码

例如，想要去除密码的 PDF 文件位于 `example.pdf`，只需输入下面的命令：

```bash
pdfuck example.pdf
```

输出文件的默认路径为 `example.fucked.pdf`。

### 手动指定输出文件路径

如果想要手动指定输出文件的路径，可以使用 `-o` 参数，例如：

```bash
pdfuck example.pdf -o target.pdf
```

### PDF 文件含有打开密码

使用 `-p` 参数手动指定打开密码，例如：

```bash
pdfuck example.pdf -p password
```

## 致谢

感谢以下开源项目，本项目的完成离不开这些作者贡献的代码。

* [pikepdf](https://github.com/pikepdf/pikepdf)

## 工作流

### 配置开发环境

```bash
pip install -r requirements.txt
```

### 构建与测试

```bash
python -m build
pip install --editable .
```

## 开源协议

[GPL-3.0](LICENSE)
