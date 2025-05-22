import pandas as pd
from models import db, TouchFeature
from app import app  # 假设你的 Flask 应用入口在 app.py 中

# 初始化数据库连接
with app.app_context():
    db.create_all()  # 创建表（如果不存在）

# 读取CSV文件
df = pd.read_csv('data.csv')

# 清洗列名（确保与模型字段一致）
df.columns = [col.strip() for col in df.columns]

# 插入数据
with app.app_context():
    for _, row in df.iterrows():
        record = TouchFeature(**row.to_dict())
        db.session.add(record)
    db.session.commit()
    print("✅ 成功导入", len(df), "条记录")