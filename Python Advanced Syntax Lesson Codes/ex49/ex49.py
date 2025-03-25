from docxtpl import DocxTemplate

# 基本变量替换
doc = DocxTemplate("template1.docx")

context = {
    "name": "小红",
    "course": "Python全栈开发",
    "date": "2025年4月1日"
}

doc.render(context)
doc.save("output.docx")
print("Word文档已生成!")

# 批量生成Word文件
students = [
    {"name": "小红", "course": "Excel自动化", "date": "2025-04-01"},
    {"name": "小明", "course": "Python入门", "date": "2025-04-05"},
    {"name": "小强", "course": "数据分析", "date": "2025-04-08"},
    {"name": "小刚", "course": "前端开发", "date": "2025-04-09"},
    {"name": "小芳", "course": "Java基础", "date": "2025-04-10"},
    {"name": "小军", "course": "Linux运维", "date": "2025-04-11"},
    {"name": "小兰", "course": "C语言入门", "date": "2025-04-12"},
    {"name": "小东", "course": "Vue框架", "date": "2025-04-13"},
    {"name": "小梅", "course": "JavaScript进阶", "date": "2025-04-14"},
    {"name": "小云", "course": "Python数据处理", "date": "2025-04-15"},
    {"name": "小林", "course": "Excel VBA", "date": "2025-04-16"},
    {"name": "小慧", "course": "MySQL数据库", "date": "2025-04-17"},
    {"name": "小斌", "course": "网络安全", "date": "2025-04-18"},
    {"name": "小玉", "course": "Web全栈", "date": "2025-04-19"},
    {"name": "小雷", "course": "Node.js入门", "date": "2025-04-20"},
    {"name": "小倩", "course": "PPT美化", "date": "2025-04-21"},
    {"name": "小雪", "course": "Python可视化", "date": "2025-04-22"},
    {"name": "小涛", "course": "爬虫开发", "date": "2025-04-23"},
    {"name": "小丽", "course": "Java高级", "date": "2025-04-24"},
    {"name": "小波", "course": "React开发", "date": "2025-04-25"},
    {"name": "小倩倩", "course": "AI入门", "date": "2025-04-26"},
    {"name": "小萌", "course": "PowerPoint进阶", "date": "2025-04-27"},
    {"name": "小洋", "course": "Python Web", "date": "2025-04-28"},
    {"name": "小楠", "course": "Numpy应用", "date": "2025-04-29"},
    {"name": "小轩", "course": "Pandas分析", "date": "2025-04-30"},
    {"name": "小志", "course": "Docker实战", "date": "2025-05-01"},
    {"name": "小薇", "course": "Git使用", "date": "2025-05-02"},
    {"name": "小宁", "course": "机器学习基础", "date": "2025-05-03"},
    {"name": "小乐", "course": "深度学习入门", "date": "2025-05-04"},
    {"name": "小浩", "course": "办公自动化", "date": "2025-05-05"},
    {"name": "小琪", "course": "Jupyter使用", "date": "2025-05-06"},
    {"name": "小童", "course": "Markdown语法", "date": "2025-05-07"},
    {"name": "小迪", "course": "图表设计", "date": "2025-05-08"},
    {"name": "小阳", "course": "ChatGPT辅助办公", "date": "2025-05-09"},
    {"name": "小虎", "course": "Python GUI", "date": "2025-05-10"},
    {"name": "小曼", "course": "Pycharm使用", "date": "2025-05-11"},
    {"name": "小冉", "course": "办公效率提升", "date": "2025-05-12"},
    {"name": "小紫", "course": "语音识别", "date": "2025-05-13"},
    {"name": "小峰", "course": "自动化测试", "date": "2025-05-14"},
    {"name": "小晨", "course": "接口测试", "date": "2025-05-15"},
    {"name": "小远", "course": "Power BI", "date": "2025-05-16"},
    {"name": "小杰", "course": "Scrapy爬虫", "date": "2025-05-17"},
    {"name": "小涵", "course": "数据可视化", "date": "2025-05-18"},
    {"name": "小乐乐", "course": "算法基础", "date": "2025-05-19"},
    {"name": "小文", "course": "编程逻辑", "date": "2025-05-20"},
    {"name": "小喆", "course": "JSON处理", "date": "2025-05-21"},
    {"name": "小舟", "course": "表单设计", "date": "2025-05-22"},
    {"name": "小岚", "course": "网页排版", "date": "2025-05-23"},
    {"name": "小薰", "course": "自动化办公技巧", "date": "2025-05-24"},
    {"name": "小诚", "course": "Python爬虫", "date": "2025-05-25"},
    {"name": "小影", "course": "批量处理工具", "date": "2025-05-26"}
]

for student in students:
    doc = DocxTemplate("template1.docx")
    doc.render(student)
    doc.save(f"{student['name']}_通知.docx")

print("批量生成完毕!")

# 条件判断 (if-else)
doc = DocxTemplate("template2.docx")
context = {
    "name": "小红",
    "score": 95
}
doc.render(context)
doc.save("output.docx")
print("Word文档已生成!")

# for循环 (生成动态列表或表格)
data = {
    "students": [
        {"name": "小红", "math": 90, "chinese": 88, "english": 92},
        {"name": "小明", "math": 85, "chinese": 81, "english": 89},
        {"name": "小强", "math": 78, "chinese": 85, "english": 90},
        {"name": "李雷", "math": 92, "chinese": 90, "english": 85},
        {"name": "韩梅", "math": 88, "chinese": 92, "english": 90},
        {"name": "张三", "math": 70, "chinese": 75, "english": 78},
        {"name": "李四", "math": 83, "chinese": 86, "english": 80},
        {"name": "王五", "math": 95, "chinese": 91, "english": 93},
        {"name": "赵六", "math": 60, "chinese": 65, "english": 70},
        {"name": "小花", "math": 89, "chinese": 87, "english": 90},
    ]
}

doc = DocxTemplate("template3.docx")
doc.render(data)
doc.save("output.docx")
print("Word文档已生成!")
