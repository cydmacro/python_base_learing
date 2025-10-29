# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Python基础教学 (Python Fundamentals Teaching)** curriculum, part of the Obsidian Dash personal knowledge management system. It contains a comprehensive 6-chapter Python teaching curriculum with AI/ML focus, designed for beginners and professionals preparing for AI trainer roles.

### Repository Context
- **Location**: `/Users/cyd/dash/python备课/python基础教学/`
- **Parent Project**: Obsidian Dash - Personal Knowledge Management System
- **Purpose**: Educational curriculum for Python fundamentals with AI model training extensions
- **Content Type**: Pure documentation (Markdown format), no executable code

## Curriculum Structure

### Core Chapters (3,926 lines total)
1. **第一章.md** - Python零基础极速上手实战 (612 lines)
   - Environment setup, syntax basics, data types
2. **第二章.md** - 核心数据类型讲解 (760 lines)
   - Strings, lists, dictionaries, tuples, sets
3. **第三章.md** - 逻辑判断和高级循环 (630 lines)
   - Logic operators, loops, comprehensions, iterators
4. **第四章.md** - 高级函数 (577 lines)
   - Functions, lambda, higher-order functions
5. **第五章.md** - 异常处理和OOP编程 (601 lines)
   - Exception handling, OOP concepts, inheritance
6. **第六章.md** - 文件处理和常用模块 (405 lines)
   - File I/O, pip, common modules

### Supplementary Content
- **大模型扩展.md** - AI trainer interview preparation (341 lines)
- **第一章.assets/** - 4 installation/setup screenshots
- **第五章.assets/** - 1 diagram image
- **gemini_ppt/1.md** - Marp presentation format (parent directory)

## Common Tasks

### Viewing Content
```bash
# Read any chapter
cat 第一章.md

# View with line numbers
cat -n 第二章.md

# Search across all chapters
grep -n "lambda" *.md

# Count total lines
wc -l *.md
```

### Content Navigation
```bash
# Quick overview of all chapters
head -20 第*.md

# Find specific topics
grep -i "exception" *.md
grep -i "class" 第五章.md

# List all sections (headers)
grep "^#" *.md
```

### Working with Assets
```bash
# List all image assets
ls -la *.assets/

# Check image sizes
du -sh *.assets/*
```

## Content Characteristics

### Teaching Approach
- **AI大模型版** - AI-integrated teaching methodology
- Progressive difficulty from basics to advanced OOP
- Practical code examples throughout
- Industry-relevant case studies for AI/ML roles
- Interview preparation focus

### Key Topics Covered
- Python 3.x syntax and best practices
- Data structures and algorithms
- Functional programming with lambda
- Object-oriented programming
- Exception handling patterns
- File I/O operations
- AI/ML preparation (data annotation, model training)

### Target Audience
- Complete Python beginners
- Professionals transitioning to AI/ML roles
- Interview preparation for AI trainer positions
- Data scientists and ML engineers

## File Specifications

### Format Details
- All files use UTF-8 encoding with Chinese content
- Markdown formatted with code blocks
- Executable file permissions (unusual for .md files)
- No actual Python code files - documentation only
- Images in PNG format within .assets directories

### Content Guidelines
- Chapters follow numbered sequence (第一章 through 第六章)
- Each chapter divided into numbered sections
- Code examples use Python 3.x syntax
- Tables for method/function comparisons
- Visual aids for installation steps

## Integration with Parent Project

This curriculum is part of the larger Obsidian Dash system:
- Follows the Input → Processing → Output knowledge flow
- Located in specialized teaching preparation area
- Integrates with broader AI/ML learning resources
- No dependencies on RAG systems or vector databases from parent project

## Notes for Development

### When Editing Content
- Maintain consistent chapter numbering scheme
- Preserve UTF-8 encoding for Chinese text
- Keep code examples Python 3.x compatible
- Update .assets directories when adding images
- Follow existing Markdown formatting patterns

### When Adding New Content
- Place new chapters in root directory with pattern `第N章.md`
- Create corresponding `.assets` directory for images
- Maintain progressive difficulty curve
- Include practical examples and exercises
- Consider AI/ML application context

### Important Considerations
- This is documentation-only, no Python environment needed
- No build, test, or deployment processes
- No dependencies or package management
- Parent project's RAG/FastAPI systems are separate
- Content is version-controlled via parent Git repository