#!/usr/bin/env python3
"""
大模型开发综合演示运行器
Comprehensive LLM Development Demo Runner

整合所有演示模块：
1. llm_patterns_demo.py - 核心模式演示
2. technical_analysis.py - 技术原理分析
3. business_challenges.py - 业务挑战方案
4. extended_challenges.py - 扩展技术难点

作者：SuperClaude
日期：2025-08-10
使用：python run_all_demos.py
"""

import asyncio
import sys
import time
import logging
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

def print_banner():
    """打印标题横幅"""
    banner = """
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║                   🤖 大模型开发核心技术综合演示平台 🤖                        ║
    ║                                                                              ║
    ║    Zero-Shot | Few-Shot | CoT | ReAct | Multi-Agent | LangGraph             ║
    ║                                                                              ║
    ║          技术原理 | 实现挑战 | 业务难点 | 前沿技术                          ║
    ║                                                                              ║
    ║                        Powered by SuperClaude v2.0.1                        ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_section_divider(title: str):
    """打印章节分隔符"""
    width = 80
    padding = (width - len(title) - 4) // 2
    divider = "=" * padding + f"  {title}  " + "=" * padding
    if len(divider) < width:
        divider += "="
    
    print(f"\n{divider}")

def print_subsection(title: str):
    """打印子章节标题"""
    print(f"\n📍 {title}")
    print("-" * (len(title) + 4))

async def run_demo_with_timing(demo_func, demo_name: str):
    """运行演示并计时"""
    print_subsection(f"开始 {demo_name}")
    
    start_time = time.time()
    try:
        await demo_func()
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\n✅ {demo_name} 完成 (耗时: {duration:.2f}秒)")
        return True, duration
        
    except Exception as e:
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"\n❌ {demo_name} 失败: {str(e)} (耗时: {duration:.2f}秒)")
        logger.error(f"{demo_name} 执行失败", exc_info=True)
        return False, duration

def print_summary(results: dict):
    """打印执行总结"""
    print_section_divider("执行总结")
    
    total_time = sum(result[1] for result in results.values())
    success_count = sum(1 for result in results.values() if result[0])
    total_count = len(results)
    
    print(f"\n📊 总体统计:")
    print(f"   • 总演示数量: {total_count}")
    print(f"   • 成功演示: {success_count}")
    print(f"   • 失败演示: {total_count - success_count}")
    print(f"   • 总执行时间: {total_time:.2f}秒")
    print(f"   • 成功率: {success_count/total_count*100:.1f}%")
    
    print(f"\n📈 各模块执行情况:")
    for demo_name, (success, duration) in results.items():
        status = "✅" if success else "❌"
        print(f"   {status} {demo_name:<35} {duration:>8.2f}s")
    
    if success_count == total_count:
        print(f"\n🎉 所有演示均执行成功！")
    else:
        print(f"\n⚠️  有 {total_count - success_count} 个演示执行失败，请查看日志了解详情。")

async def main():
    """主函数"""
    
    print_banner()
    
    # 检查演示文件是否存在
    demo_files = [
        "llm_patterns_demo.py",
        "technical_analysis.py", 
        "business_challenges.py",
        "extended_challenges.py"
    ]
    
    print_section_divider("环境检查")
    
    missing_files = []
    for file in demo_files:
        if not Path(file).exists():
            missing_files.append(file)
            print(f"❌ 缺少文件: {file}")
        else:
            print(f"✅ 找到文件: {file}")
    
    if missing_files:
        print(f"\n❌ 缺少 {len(missing_files)} 个必要文件，无法运行完整演示。")
        print("请确保所有演示文件都在当前目录下。")
        return
    
    print("\n✅ 所有演示文件检查完毕，准备开始演示...")
    
    # 导入演示模块
    try:
        print_subsection("导入演示模块")
        
        print("导入核心模式演示模块...")
        from llm_patterns_demo import main as patterns_main
        
        print("导入技术分析模块...")
        from technical_analysis import run_technical_analysis_demo
        
        print("导入业务挑战模块...")
        from business_challenges import run_business_challenges_demo
        
        print("导入扩展技术挑战模块...")
        from extended_challenges import run_extended_challenges_demo
        
        print("✅ 所有模块导入成功")
        
    except ImportError as e:
        print(f"❌ 模块导入失败: {e}")
        print("请确保所有依赖包已正确安装。")
        return
    
    # 执行所有演示
    print_section_divider("开始综合演示")
    
    results = {}
    
    # 1. 核心模式演示
    success, duration = await run_demo_with_timing(
        patterns_main, 
        "Zero-Shot/Few-Shot/CoT/ReAct/Multi-Agent/LangGraph 核心模式"
    )
    results["核心模式演示"] = (success, duration)
    
    # 2. 技术原理分析
    success, duration = await run_demo_with_timing(
        run_technical_analysis_demo,
        "提示工程/上下文管理/幻觉检测/性能优化 技术分析"
    )
    results["技术原理分析"] = (success, duration)
    
    # 3. 业务挑战解决方案
    success, duration = await run_demo_with_timing(
        run_business_challenges_demo,
        "成本控制/质量保证/用户体验/运营监控 业务方案"
    )
    results["业务挑战方案"] = (success, duration)
    
    # 4. 扩展技术难点
    success, duration = await run_demo_with_timing(
        run_extended_challenges_demo,
        "高级推理/多模态融合/知识更新 前沿技术"
    )
    results["扩展技术挑战"] = (success, duration)
    
    # 打印总结
    print_summary(results)
    
    # 技术要点总结
    print_section_divider("技术要点总结")
    
    technical_points = [
        {
            "分类": "核心模式",
            "要点": [
                "Zero-Shot: 依赖预训练知识，指令工程是关键",
                "Few-Shot: 示例选择和顺序影响效果",
                "CoT: 逐步推理提升复杂任务准确性",
                "ReAct: 推理与行动循环，需要工具集成",
                "Multi-Agent: 专业化分工，协作机制设计",
                "LangGraph: 图结构工作流，支持复杂依赖"
            ]
        },
        {
            "分类": "技术挑战",
            "要点": [
                "提示工程: 敏感性高，需要系统化测试框架",
                "上下文管理: 长度限制，需要智能压缩策略",
                "幻觉控制: 事实验证，多源交叉检查",
                "性能优化: 缓存策略，批处理，负载均衡",
                "安全防护: 输入验证，输出过滤，权限控制",
                "可观测性: 全链路监控，性能分析"
            ]
        },
        {
            "分类": "业务难点",  
            "要点": [
                "成本控制: 实时监控，智能优化建议",
                "质量保证: 多维评估，持续改进机制",
                "用户体验: 响应时间，个性化，易用性",
                "运营维护: SLA管理，故障预警，容量规划",
                "合规管理: 数据隐私，内容审核，法规遵循",
                "商业价值: ROI评估，价值量化，场景适配"
            ]
        },
        {
            "分类": "前沿技术",
            "要点": [
                "高级推理: 多类型推理融合，逻辑一致性检查",
                "多模态融合: 语义对齐，层次化融合架构", 
                "知识更新: 动态维护，冲突检测，增量学习",
                "联邦学习: 隐私保护，分布式训练",
                "对抗防护: 攻击检测，鲁棒性增强",
                "可解释AI: 决策透明，用户信任建立"
            ]
        }
    ]
    
    for category in technical_points:
        print(f"\n🔬 {category['分类']}:")
        for i, point in enumerate(category['要点'], 1):
            print(f"   {i}. {point}")
    
    # 最终总结
    print_section_divider("最终总结")
    
    conclusion = """
    🎯 核心收获:
    
    1. **技术架构**: 从基础模式到高级架构的演进路径
       • 掌握六大核心模式的原理和应用场景
       • 理解技术实现的关键难点和解决方案
       
    2. **工程实践**: 从原型到生产的工程化考量  
       • 成本控制和性能优化的平衡策略
       • 质量保证和用户体验的提升方法
       
    3. **前沿趋势**: 从当前能力到未来发展方向
       • 多模态融合和高级推理的技术突破
       • 知识更新和持续学习的系统设计
       
    4. **最佳实践**: 从理论学习到实际应用的转化
       • 选择合适的技术模式解决具体问题
       • 建立完整的开发、测试、部署流程
    
    💡 下一步行动建议:
    
    • 深入学习感兴趣的特定技术领域
    • 结合实际业务场景进行技术选型
    • 建立完整的评估和监控体系
    • 关注前沿技术发展和最佳实践
    
    📚 扩展学习资源:
    
    • 学术论文: 关注顶级会议(ACL, NeurIPS, ICML)最新研究
    • 开源项目: LangChain, LlamaIndex, Haystack等框架
    • 行业报告: McKinsey, Gartner等机构的AI应用报告
    • 技术社区: Hugging Face, OpenAI, Anthropic技术博客
    """
    
    print(conclusion)
    
    print("\n" + "="*80)
    print("🎉 感谢使用大模型开发核心技术综合演示平台！")
    print("💬 如有问题或建议，欢迎反馈交流。")
    print("🚀 祝您在大模型开发的道路上越走越远！")
    print("="*80)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n❌ 用户中断执行")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n💥 程序执行出现未预期错误: {e}")
        logger.error("程序执行失败", exc_info=True)
        sys.exit(1)