# Python多版本管理 - macOS M1

## 概述

在 macOS M1 芯片上管理多个Python版本，推荐使用 pyenv 工具，它能够轻松切换不同的Python版本并管理项目依赖。

## 安装 pyenv

### 使用 Homebrew 安装
```bash
# 安装 pyenv
brew install pyenv

# 安装 pyenv-virtualenv (可选，用于虚拟环境管理)
brew install pyenv-virtualenv
```

### 配置 Shell 环境
```bash
# 对于 zsh (macOS 默认)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

# 重新加载配置
source ~/.zshrc

# 对于 bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

source ~/.bash_profile
```

## Python版本管理

### 查看可安装的Python版本
```bash
# 列出所有可安装的版本
pyenv install --list

# 查看最新的稳定版本
pyenv install --list | grep -E "^\s*3\.[0-9]+\.[0-9]+$" | tail -10
```

### 安装Python版本
```bash
# 安装特定版本
pyenv install 3.11.7
pyenv install 3.10.13
pyenv install 3.9.18

# 安装最新版本
pyenv install 3.12.1
```

### 设置Python版本
```bash
# 设置全局默认版本
pyenv global 3.11.7

# 设置当前目录使用特定版本
pyenv local 3.10.13

# 临时切换版本（当前shell会话）
pyenv shell 3.9.18

# 查看当前使用的版本
pyenv version

# 查看所有已安装的版本
pyenv versions
```

## 虚拟环境管理

### 创建虚拟环境
```bash
# 使用特定Python版本创建虚拟环境
pyenv virtualenv 3.11.7 myproject-env

# 使用当前Python版本创建虚拟环境
pyenv virtualenv myproject-env
```

### 激活和停用虚拟环境
```bash
# 激活虚拟环境
pyenv activate myproject-env

# 停用虚拟环境
pyenv deactivate

# 删除虚拟环境
pyenv uninstall myproject-env
```

### 项目级虚拟环境
```bash
# 在项目目录中设置虚拟环境
cd /path/to/your/project
pyenv local myproject-env

# 检查当前环境
pyenv which python
pyenv which pip
```

## M1芯片特殊注意事项

### 编译优化
```bash
# 设置编译环境变量（安装Python前）
export LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix bzip2)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib"
export CPPFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include -I$(brew --prefix zlib)/include"

# 安装依赖
brew install openssl readline sqlite3 xz zlib bzip2
```

### Rosetta兼容性
```bash
# 如果需要x86_64兼容性
arch -x86_64 pyenv install 3.10.13

# 检查架构
python -c "import platform; print(platform.machine())"
```

## 常用项目配置

### 创建新项目环境
```bash
# 1. 创建项目目录
mkdir my-python-project
cd my-python-project

# 2. 创建并设置虚拟环境
pyenv virtualenv 3.11.7 my-python-project
pyenv local my-python-project

# 3. 安装依赖
pip install --upgrade pip
pip install -r requirements.txt

# 4. 确认环境
python --version
pip --version
```

### requirements.txt管理
```bash
# 生成依赖文件
pip freeze > requirements.txt

# 安装依赖
pip install -r requirements.txt

# 更新依赖
pip install --upgrade package_name
pip freeze > requirements.txt
```

## 故障排除

### 常见问题

#### 1. pyenv命令未找到
```bash
# 检查PATH设置
echo $PATH | grep pyenv

# 重新添加到PATH
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

#### 2. Python编译失败
```bash
# 安装编译依赖
brew install openssl readline sqlite3 xz zlib bzip2

# 重新安装Python
pyenv install 3.11.7
```

#### 3. 虚拟环境激活问题
```bash
# 检查pyenv-virtualenv是否正确安装
brew list | grep pyenv

# 重新初始化
eval "$(pyenv virtualenv-init -)"
```

### 环境验证
```bash
# 检查pyenv状态
pyenv --version
pyenv versions
pyenv which python
pyenv which pip

# 检查Python环境
python --version
python -c "import sys; print(sys.executable)"
python -c "import platform; print(platform.machine())"
```

## 最佳实践

### 1. 项目隔离
- 每个项目使用独立的虚拟环境
- 使用 `.python-version` 文件记录项目Python版本
- 维护清晰的 `requirements.txt`

### 2. 版本选择
- 生产环境使用稳定版本（如3.11.x）
- 学习新特性时使用最新版本
- 维护旧项目时保留对应版本

### 3. 定期维护
```bash
# 清理不用的版本
pyenv uninstall 3.8.10

# 更新pyenv
brew upgrade pyenv

# 检查过期的虚拟环境
pyenv versions
```

### 4. 开发工作流
```bash
# 新项目标准流程
mkdir project_name
cd project_name
pyenv virtualenv 3.11.7 project_name
pyenv local project_name
pip install --upgrade pip
touch requirements.txt
```

## 与其他工具集成

### Poetry 集成
```bash
# 安装Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Poetry会自动检测pyenv设置的Python版本
poetry init
poetry install
```

### VS Code 配置
```json
// .vscode/settings.json
{
    "python.pythonPath": "~/.pyenv/versions/myproject-env/bin/python"
}
```

这样配置后，你可以在macOS M1上轻松管理多个Python版本，为不同项目创建隔离的开发环境。