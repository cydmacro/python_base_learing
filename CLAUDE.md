# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **test_code** repository for the **Python基础教学 (Python Fundamentals Teaching)** 10-day AI trainer bootcamp curriculum. It contains 70+ executable Python files organized by day (days.day01-days.day10), with classroom demos, practice exercises, assessment answers, and three major projects.

### Repository Context
- **Location**: `/Users/cyd/dash/python备课/python基础教学/test_code/`
- **Parent Project**: Obsidian Dash - Personal Knowledge Management System
- **Purpose**: Executable code examples and teaching materials for Python fundamentals with AI/ML focus
- **Content Type**: Python code files (70+ .py files, ~10,280 lines), Markdown documentation, project examples
- **Target Audience**: Complete Python beginners preparing for AI trainer roles

## Repository Structure

### Directory Organization (By Day)
```
test_code/
├── days.day01-days.day10/          # 10 days of organized code (课堂演示, 下午练习, 测评答案)
├── docs/                 # Documentation and teaching materials
├── 项目案例/              # 3 major projects with v1/v2/v3 versions
├── backup/               # Original file backups
├── app/                  # Sample app code (products.py, users.py, ai_writer.py)
└── data/                 # Sample data files for exercises
```

### Daily Code Structure (days.day01-days.day10)
Each day contains:
- **课堂演示/** - Classroom demonstration code (3-4 files)
- **下午练习/** - Afternoon practice exercises (2-3 files)
- **测评答案/** - Assessment answer files with multiple solution versions
- **Day{N}.md** - Daily lesson plan and objectives
- **README.md** - Daily quick reference guide

### Three Major Projects (项目案例/)
1. **project1_文本清洗/** - Text cleaning tool (v1: 80 lines, v2: 150 lines, v3: 250 lines)
2. **project2_图片分类/** - Image classification dataset preparation (v1: 100 lines, v2: 180 lines, v3: 280 lines)
3. **project3_csv工具/** - CSV data processing tool (v1: 120 lines, v2: 220 lines, v3: 350 lines)

## Common Development Tasks

### Running Code Examples
```bash
# Run a specific day's classroom demo
cd days.day01/课堂演示/
python 1_1_hello_world.py

# Run afternoon practice exercises
cd days.day02/下午练习/
python 2_4.py

# Run project examples
cd 项目案例/project1_文本清洗/
python v1_basic.py      # Basic version
python v2_enhanced.py   # Enhanced version with functions
python v3_complete.py   # Complete OOP version
```

### Testing Code
```bash
# Run all demo code (if available)
python run_all_demos.py

# Test specific concepts
python typing_test.py
python cot.py
```

### Working with Dependencies
```bash
# Install dependencies for advanced examples
pip install -r requirements.txt

# Note: Basic examples (days.day01-days.day06) use only standard library
# Advanced examples (days.day07-days.day10) require pandas, numpy, etc.
```

### Navigating Documentation
```bash
# View daily lesson plans
cat days.day01/Day1课件.md

# View daily README for quick reference
cat days.day01/README.md

# View comprehensive documentation
cat docs/README.md

# View assessment questions
cat docs/测评/Day1_测评.md
```

## 10-Day Curriculum Overview

### Day 1-2: Python Basics (days.day01/)
- **Topics**: Variables, data types, input/output, basic operators
- **Key Files**: `1_1_hello_world.py`, `1_2_calculator.py`, `1_3_bmi_calculator.py`
- **Dependencies**: None (standard library only)
- **AI Context**: Variable naming for annotation tool field design

### Day 2: Core Data Types (days.day02/)
- **Topics**: Strings, lists, dictionaries, tuples, sets
- **Key Files**: `2_1.py` through `2_6.py`
- **Dependencies**: None (standard library only)
- **AI Context**: Dictionary structures match Label Studio JSON exports

### Day 3: Logic and Loops (days.day03/)
- **Topics**: if/elif/else, while/for loops, list comprehensions
- **Key Files**: `3_1.py` through `3_6.py`
- **Dependencies**: None (standard library only)
- **AI Context**: Multi-condition logic for annotation quality checks

### Day 4: Advanced Loops (days.day04/)
- **Topics**: enumerate(), zip(), iterators, generators
- **Key Files**: `4_1.py` through `4_4.py`
- **Dependencies**: None (standard library only)
- **AI Context**: Batch file processing for annotation datasets

### Day 5: Functions and Exceptions (days.day05/)
- **Topics**: Functions, lambda, map/filter/reduce, exception handling
- **Key Files**: `5_1.py` through `5_3.py`
- **Dependencies**: None (standard library only)
- **AI Context**: Lambda expressions for quick annotation rule definitions

### Day 6: File Processing (days.day06/)
- **Topics**: File I/O, JSON processing, os module, regex
- **Key Files**: `6_1.py`, `6_2_json_processing.py`, `6_3.py`
- **Dependencies**: None (standard library only)
- **AI Context**: JSON files correspond to Label Studio export format

### Day 7: Pandas Data Processing (days.day07/)
- **Topics**: DataFrame/Series, data cleaning, filtering
- **Key Files**: `7_1_pandas_basic.py`, `7_2_pandas_clean.py`, `7_3_pandas_filter.py`
- **Dependencies**: pandas, numpy
- **AI Context**: DataFrame for structured annotation data storage

### Day 8: AI Annotation Tools (days.day08/)
- **Topics**: Label Studio data parsing, quality checks, batch file renaming
- **Key Files**: `8_1_label_export.py`, `8_2_quality_check.py`, `8_3_batch_rename.py`
- **Dependencies**: pandas, json
- **AI Context**: Label Studio is mainstream open-source annotation tool

### Day 9-10: Comprehensive Projects (days.day09/, days.day10/)
- **Topics**: Three major projects with progressive complexity
- **Key Projects**: Text cleaning, image classification, CSV processing
- **Dependencies**: pandas, numpy, opencv-python (optional)
- **AI Context**: Real-world data processing for model training

## Code Architecture

### Progressive Version System
All major projects follow a three-version progression:
- **v1_basic.py**: Direct implementation, procedural programming (80-120 lines)
- **v2_enhanced.py**: Function encapsulation, enhanced features (150-220 lines)
- **v3_complete.py**: OOP design, production-ready code (250-350 lines)

### Code Comment Style (4 Dimensions)
All code files use a 4-dimensional commenting approach:
```python
# 【知识点】Knowledge point explanation
# 【实战技巧】Practical tip for real-world usage
# 【易错点】Common mistake warning
# 【扩展思考】Extended thinking question
```

### Assessment Answer Structure
Assessment answers provide multiple solution approaches:
- **v1基础版**: Basic implementation for beginners
- **v2改进版/字典版**: Improved version with better data structures
- **v3完整版**: Complete version with full validation and error handling

## Important Notes

### File Encoding
- All files use UTF-8 encoding with Chinese comments
- Code examples use Python 3.x syntax (Python 3.6+ recommended)
- f-string formatting is the preferred method for string interpolation

### Dependency Management
- **Day 1-6**: Standard library only (no external dependencies)
- **Day 7-8**: Requires pandas, numpy
- **Day 9-10**: May require additional packages (opencv-python, pillow)
- Full dependency list in `requirements.txt` (includes parent project dependencies)

### Teaching Philosophy
- **Gradual difficulty increase**: 10-15% complexity increase per day
- **Scenario-based learning**: All examples tied to AI annotation work
- **Hands-on practice**: 3 hours theory + 3 hours practice per day
- **Real-world applications**: Label Studio integration, data processing workflows

## Working with Code

### When Adding New Examples
1. Place code in appropriate day directory (`day{N}/课堂演示/` or `day{N}/下午练习/`)
2. Follow naming convention: `{chapter}_{section}.py` (e.g., `1_1_hello_world.py`)
3. Include 4-dimensional comments for key concepts
4. Test code execution before committing
5. Update corresponding README.md

### When Creating Project Files
1. Create three versions (v1_basic, v2_enhanced, v3_complete)
2. Ensure progressive complexity (v1 → v2: +70-100 lines, v2 → v3: +100-130 lines)
3. Include comprehensive comments explaining design decisions
4. Provide sample data files in `data/` directory if needed

### When Writing Assessment Answers
1. Place in `day{N}/测评答案/` directory
2. Use naming pattern: `Day{N}_测评_实操题{M}_{description}_v{X}.py`
3. Provide at least 2 solution versions (basic + enhanced)
4. Include detailed comments explaining the approach

## Integration Context

### Parent Project Relationship
- Part of Obsidian Dash knowledge management system
- Independent from parent project's RAG/FastAPI systems
- Focuses on Python teaching rather than production systems
- Can be used as standalone teaching material

### AI/ML Career Context
All examples are designed for AI trainer role preparation:
- Data annotation workflows (Label Studio)
- Dataset preparation (image classification, text cleaning)
- Quality control automation
- Batch data processing
- Statistical analysis of annotation work