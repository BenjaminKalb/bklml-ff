# BKLML File Finder

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

**BenjaminKalb Localizations Markup Language File Finder** — cross-platform CLI scanner for `.bklml` files (BKLML localizations).

## ✨ Features

- 🔍 **Recursive search for** `.bklml` files in folders
- 📊 **Metadata parsing**: `@VERSION:{1.2.0}` and `@DESCRIPTION:{text}`
- 💻 **Full cross-platform**: Linux, Windows, macOS
- ⚡ **Without dependencies** — Python standard library only
- 📦 **Easy installation**: AUR, PyPI, pipx or manual (AUR, PyPI, pipx in the next update)

## 🚀 Quick Start

### Installation

**Arch Linux (AUR):**
```bash
yay -S bklml-ff
# or
paru -S bklml-ff
```

**Any system (PyPI):**
```bash
pipx install git+https://github.com/benjaminkalb/bklml-ff.git
pip install bklml-ff
```

**Manual installation:**
```bash
git clone https://github.com/benjaminkalb/bklml-ff.git
cd bklml-ff
chmod +x bklml-ff.py
sudo cp bklml-ff.py /usr/local/bin/bklml-ff  # Linux/Mac
# Windows: rename to bklml-ff.py & add to PATH
```

### ⚡ Usage

**Help**
```bash
bklml-ff --help
```
**Search in the current folder**
```bash
bklml-ff .
```
**Recursive search with details**
```bash
bklml-ff ~/projects --details
```
**Only the upper level**
```bash
bklml-ff /path/to/folder --no-recursive -d
```

### 📊 Example of output from --details
```bash
Found 3 .bklml file(s):

File path                           | Version  | Description
----------------------------------------------------------------------
src/en.bklml                        | 1.2.0    | English 2D Game Localization
src/ru.bklml                        | 1.1.1    | Russian 2D Game Localization
plugins/auth.bklml                  | 0.9.2    | translations for lines
```

### 📋 Command Line arguments
```bash
> Argument | > Description | > Example

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

DIRECTORY	| The folder to scan (by default .)	| bklml-ff ~/src
--details, -d	| Show versions and descriptions | --details
--no-recursive | Only the upper level	| --no-recursive
--version	| Program version	| --version
--help, -h	| Reference	| --help
```

### 🤝 Contribution to the development
```bash
[1] Fork repository
[2] Create branch: git checkout -b feature/amazing-feature
[3] Commit changes: git commit -m 'Add amazing feature'
[4] Push to the branch: git push origin feature/amazing-feature
[5] Create Pull Request
```
