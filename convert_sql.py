#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import json

def translate_to_english(chinese_text):
    translations = {
        '商品管理': 'Item Management',
        '订单管理': 'Order Management', 
        '营销管理': 'Marketing Management',
        '系统设置': 'System Settings',
        '客户管理': 'Customer Management',
        '数据报表': 'Data Reports',
        '商家管理': 'Merchant Management',
        '账号管理': 'Account Management',
        '商品列表': 'Product List',
        '商品分组': 'Product Group',
        '类目管理': 'Category Management',
        '规格属性': 'Specification Attributes',
        '售后管理': 'After-sales Management',
        '查看详情': 'View Details',
        '物流详情': 'Logistics Details',
        '优惠价/折扣': 'Discount/Promotion',
        '满减/满折': 'Full Reduction/Discount',
        '优惠券': 'Coupons',
        '会员信息': 'Member Information',
        '买家分组': 'Buyer Groups',
        '会员积分': 'Member Points',
        '会员等级': 'Member Levels',
        '营销查看权限': 'Marketing View Permission',
        '编辑-提交': 'Edit-Submit',
        '发布活动': 'Launch Campaign',
        '下线': 'Offline',
        '数据字典': 'Data Dictionary',
        '元数据管理': 'Metadata Management',
        '字典新增': 'Add Dictionary',
        '字典编辑': 'Edit Dictionary',
        '字典删除': 'Delete Dictionary',
        '元数据新增': 'Add Metadata',
        '元数据删除': 'Delete Metadata',
        '元数据编辑': 'Edit Metadata',
        '租户接入': 'Tenant Access',
        '接口管理': 'API Management',
        '地址设置': 'Address Settings',
        '店铺设置': 'Store Settings',
        '数据门户': 'Data Portal',
        '子账号管理': 'Sub-account Management',
        '角色': 'Roles',
        '角色管理': 'Role Management',
        '店铺页管理': 'Store Page Management',
        '店铺页列表': 'Store Page List',
        '商家列表': 'Merchant List',
        '入驻审核': 'Entry Review',
        '开放平台管理': 'Open Platform Management',
        '商品标签': 'Product Tags',
        '运费模板': 'Shipping Template',
        '商品上下架': 'Product On/Off Shelf',
        '商品删除': 'Delete Product',
        '商品标签新增编辑': 'Add/Edit Product Tags',
        '商品标签删除': 'Delete Product Tags',
        '运费模板新增编辑': 'Add/Edit Shipping Template',
        '规格属性新增编辑': 'Add/Edit Specification Attributes',
        '类目新增编辑': 'Add/Edit Category',
        '删除类目': 'Delete Category',
        '发货': 'Ship',
        '关闭订单': 'Close Order',
        '备注': 'Remarks',
        '券码核销': 'Coupon Verification',
        '确认核销': 'Confirm Verification',
        '核销查询': 'Verification Query',
        '第2层节点': 'Level 2 Node',
        '342': '342',
        'af': 'af',
        'af2': 'af2',
        '234': '234',
    }
    return translations.get(chinese_text, chinese_text)

def convert_description_to_multilingual(description):
    if not description or description.strip() == '':
        return description
    
    english_text = translate_to_english(description)
    multilingual_format = [
        {"lang": "en", "value": english_text},
        {"lang": "zh", "value": description}
    ]
    json_str = json.dumps(multilingual_format, ensure_ascii=False)
    return json_str

def process_sql_line(line):
    # 匹配description字段的值
    pattern = r"'([^']*)'"
    matches = re.findall(pattern, line)
    
    if len(matches) >= 4:  # 确保有足够的字段
        description = matches[3]  # 第4个匹配项是description
        if description and description.strip():
            multilingual_desc = convert_description_to_multilingual(description)
            # 替换第4个单引号包围的内容
            parts = line.split("'")
            if len(parts) >= 8:  # 确保有足够的单引号分隔的部分
                parts[7] = multilingual_desc  # 第8个部分（索引7）是description的值
                return "'".join(parts)
    
    return line

def main():
    input_file = "src/main/resources/new_entry2.sql"
    output_file = "src/main/resources/new_entry2_multilingual.sql"
    
    print("开始转换SQL文件...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    converted_lines = []
    for line in lines:
        if "INSERT INTO" in line and "description" in line:
            converted_line = process_sql_line(line)
            converted_lines.append(converted_line)
        else:
            converted_lines.append(line)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(converted_lines)
    
    print(f"转换完成！输出文件: {output_file}")
    print("示例转换:")
    print("原始: '商品管理'")
    print("转换后: '[{\"lang\":\"en\",\"value\":\"Item Management\"},{\"lang\":\"zh\",\"value\":\"商品管理\"}]'")

if __name__ == "__main__":
    main()
