"""
改进的时间显示模块
提供更符合阅读习惯的时间输出格式
"""

import time

# 获取当前时间戳
timestamp = time.time()
print(f"时间戳: {timestamp}")

# 默认的本地时间格式
localtime = time.localtime()
print(f"本地时间元组: {localtime}")

# 格式化时间显示 - 更符合阅读习惯
readable_time = time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime())
print(f"可读格式: {readable_time}")

# 添加中文上午/下午的时间格式
time_with_chinese_period = time.strftime("%Y年%m月%d日 %I:%M:%S %p", time.localtime()).replace('AM', '上午').replace('PM', '下午')
print(f"12小时制(中文): {time_with_chinese_period}")

# 其他常用时间格式
formats = {
    "标准格式": "%Y-%m-%d %H:%M:%S",
    "中文格式": "%Y年%m月%d日 %H时%M分%S秒",
    "日期格式": "%Y-%m-%d",
    "时间格式": "%H:%M:%S",
    "星期格式": "%Y年%m月%d日 %A",
    "12小时制": "%Y-%m-%d %I:%M:%S %p"
}

print("\n=== 不同时间格式展示 ===")
for name, fmt in formats.items():
    formatted_time = time.strftime(fmt, time.localtime())
    print(f"{name}: {formatted_time}")