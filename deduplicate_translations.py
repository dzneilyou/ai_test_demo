#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据key去除translations中的重复数据
"""

import json
import sys
import os

def remove_duplicates_by_key(file_path, key_field='key', output_file=None):
    """
    根据key去除translations中的重复数据
    
    Args:
        file_path (str): translations文件路径
        key_field (str): 用于去重的字段名
        output_file (str): 输出文件路径
    """
    try:
        # 读取translations文件
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"原始数据条数: {len(data)}")
        
        # 使用字典去重，保留最后一个
        seen_keys = {}
        unique_data = []
        
        for item in data:
            if isinstance(item, dict) and key_field in item:
                key = item[key_field]
                seen_keys[key] = item
            else:
                unique_data.append(item)
        
        # 将去重后的数据添加到结果中
        unique_data.extend(seen_keys.values())
        
        print(f"去重后数据条数: {len(unique_data)}")
        print(f"删除了 {len(data) - len(unique_data)} 条重复数据")
        
        # 写入文件
        output_path = output_file or file_path
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(unique_data, f, ensure_ascii=False, indent=2)
        
        print(f"去重完成，结果已保存到: {output_path}")
        
        # 显示重复的key
        if len(data) > len(unique_data):
            print("\n重复的key:")
            key_count = {}
            for item in data:
                if isinstance(item, dict) and key_field in item:
                    key = item[key_field]
                    key_count[key] = key_count.get(key, 0) + 1
            
            for key, count in key_count.items():
                if count > 1:
                    print(f"  - {key}: {count} 次")
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {file_path}")
    except json.JSONDecodeError:
        print(f"错误: {file_path} 不是有效的JSON文件")
    except Exception as e:
        print(f"处理文件时出错: {e}")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python deduplicate_translations.py <translations_file> [output_file] [key_field]")
        print("示例: python deduplicate_translations.py translations.json")
        print("示例: python deduplicate_translations.py translations.json translations_unique.json")
        print("示例: python deduplicate_translations.py translations.json translations_unique.json key")
        return
    
    file_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    key_field = sys.argv[3] if len(sys.argv) > 3 else 'key'
    
    if not os.path.exists(file_path):
        print(f"错误: 文件 {file_path} 不存在")
        return
    
    remove_duplicates_by_key(file_path, key_field, output_file)

if __name__ == "__main__":
    main()
