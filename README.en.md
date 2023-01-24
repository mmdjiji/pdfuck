![](assets/logo.svg)

[简体中文](README.md) | [**English**](README.en.md)

---

## Introduction

[PDFuck](https://github.com/mmdjiji/pdfuck) is a tool to remove PDF editing password, which is used in CLI (command line) mode.

## Installation

Before installing, please ensure that you have installed Python (>=3.0) and its matching version of pip, and then enter the following command at the command prompt:

```bash
pip install pdfuck
```

## Usage

### Remove PDF password

For example, if you want to remove the password from the PDF file which is located in `example.pdf`, just enter the following command:

```bash
pdfuck example.pdf
```

The default path of the output file is `example.fucked.pdf`.

### Manually specify the output file path

If you want to specify the path of the output file manually, you can use the `-o` parameter, for example:

```bash
pdfuck example.pdf -o target.pdf
```

### PDF file requires opening password

Use the `-p` parameter to manually specify the opening password, for example:

```bash
pdfuck example.pdf -p password
```

## Credit

Thanks for the following open source projects. The completion of this project is inseparable from the code contributed by these authors.

* [pikepdf](https://github.com/pikepdf/pikepdf)

## Workflow

### Configure development environment

```bash
pip install -r requirements.txt
```

### Build and test

```bash
python -m build
pip install --editable .
```

## License

[GPL-3.0](LICENSE)
