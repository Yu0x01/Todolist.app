# by ivan
# ver 1.0 - 改善版本

import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """從檔案載入任務"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_tasks(self):
        """儲存任務到檔案"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
    
    def add_task(self, description, priority="中"):
        """新增任務"""
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_at": None
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ 已新增任務：{description}")
    
    def list_tasks(self):
        """顯示所有任務"""
        if not self.tasks:
            print("📝 目前沒有任務")
            return
        
        print("\n📋 你的任務清單：")
        print("-" * 50)
        for task in self.tasks:
            status = "✅" if task["completed"] else "⏳"
            priority_emoji = {"高": "🔴", "中": "🟡", "低": "🟢"}
            print(f"{task['id']}. {status} {task['description']} "
                  f"{priority_emoji.get(task['priority'], '⚪')} {task['priority']}")
            if task["completed"] and task["completed_at"]:
                print(f"   完成時間：{task['completed_at']}")
        print("-" * 50)
    
    def complete_task(self, task_id):
        """標記任務為完成"""
        for task in self.tasks:
            if task["id"] == task_id:
                if not task["completed"]:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.save_tasks()
                    print(f"🎉 任務 '{task['description']}' 已完成！")
                else:
                    print("⚠️  這個任務已經完成了")
                return
        print("❌ 找不到這個任務編號")
    
    def delete_task(self, task_id):
        """刪除任務"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted_task = self.tasks.pop(i)
                # 重新編號
                for j, task in enumerate(self.tasks):
                    task["id"] = j + 1
                self.save_tasks()
                print(f"🗑️  已刪除任務：{deleted_task['description']}")
                return
        print("❌ 找不到這個任務編號")

def get_valid_input(prompt, valid_options=None):
    """取得有效的用戶輸入"""
    while True:
        user_input = input(prompt).strip()
        if valid_options is None or user_input in valid_options:
            return user_input
        print(f"❌ 請輸入有效的選項：{', '.join(valid_options)}")

def main():
    print("🎯 歡迎使用待辦事項清單！")
    print("=" * 50)
    
    # 取得用戶姓名
    name = input("請輸入您的姓名：").strip()
    if not name:
        print("❌ 請輸入姓名才能開始使用")
        return
    
    print(f"👋 你好，{name}！歡迎使用待辦事項清單！")
    
    # 初始化待辦事項清單
    todo = TodoList()
    
    while True:
        print("\n📋 請選擇操作：")
        print("1. 📝 新增任務")
        print("2. 📋 查看任務")
        print("3. ✅ 標記完成")
        print("4. 🗑️  刪除任務")
        print("5. 🚪 退出")
        
        choice = get_valid_input("請輸入選項 (1-5)：", ["1", "2", "3", "4", "5"])
        
        if choice == "1":
            description = input("請輸入任務描述：").strip()
            if description:
                priority = get_valid_input("請選擇優先級 (高/中/低)：", ["高", "中", "低"])
                todo.add_task(description, priority)
            else:
                print("❌ 任務描述不能為空")
        
        elif choice == "2":
            todo.list_tasks()
        
        elif choice == "3":
            todo.list_tasks()
            if todo.tasks:
                try:
                    task_id = int(input("請輸入要完成的任務編號："))
                    todo.complete_task(task_id)
                except ValueError:
                    print("❌ 請輸入有效的數字")
        
        elif choice == "4":
            todo.list_tasks()
            if todo.tasks:
                try:
                    task_id = int(input("請輸入要刪除的任務編號："))
                    todo.delete_task(task_id)
                except ValueError:
                    print("❌ 請輸入有效的數字")
        
        elif choice == "5":
            print(f"👋 謝謝使用，{name}！再見！")
            break

if __name__ == "__main__":
    main()
