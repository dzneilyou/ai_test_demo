#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取SQL文件中的中文description值，去重，翻译为英文，并替换为多语言JSON格式
"""

import re
import json
import sys
from collections import OrderedDict

def extract_chinese_descriptions(sql_file):
    """从SQL文件中提取description字段的中文值"""
    chinese_values = []
    
    try:
        with open(sql_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 匹配description字段的中文值
        pattern = r"description\s*=\s*['\"]([^'\"]+)['\"]"
        matches = re.findall(pattern, content)
        
        for match in matches:
            # 检查是否包含中文字符
            if re.search(r'[\u4e00-\u9fff]', match):
                chinese_values.append(match)
        
        print(f"提取到 {len(chinese_values)} 个中文值")
        return chinese_values
        
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return []

def remove_duplicates(chinese_values):
    """去除重复的中文值"""
    unique_values = list(OrderedDict.fromkeys(chinese_values))
    print(f"去重后剩余 {len(unique_values)} 个唯一值")
    return unique_values

def translate_to_english(chinese_text):
    """简单的中文到英文翻译映射"""
    translations = {
        '商品管理': 'Item Management',
        '订单管理': 'Order Management',
        '营销管理': 'Marketing Management',
        '系统设置': 'System Settings',
        '商品列表': 'Product List',
        '账号管理': 'Account Management',
        '角色管理': 'Role Management',
        '数据字典': 'Data Dictionary',
        '客户管理': 'Customer Management',
        '会员信息': 'Member Information',
        '买家分组': 'Buyer Groups',
        '会员积分': 'Member Points',
        '优惠价/折扣': 'Discount/Promotion',
        '满减/满折': 'Full Reduction/Discount',
        '优惠券': 'Coupons',
        '售后管理': 'After-sales Management',
        '商品分组': 'Product Groups',
        '类目管理': 'Category Management',
        '营销查看权限': 'Marketing View Permission',
        '规格属性': 'Specification Attributes',
        '类目新增编辑': 'Add/Edit Category',
        '删除类目': 'Delete Category',
        '规格属性新增编辑': 'Add/Edit Specification Attributes',
        '编辑-提交': 'Edit-Submit',
        '下线': 'Offline',
        '发布活动': 'Launch Campaign',
        '查看详情': 'View Details',
        '数据报表': 'Data Reports',
        '字典新增': 'Add Dictionary',
        '字典编辑': 'Edit Dictionary',
        '字典删除': 'Delete Dictionary',
        '元数据管理': 'Metadata Management',
        '元数据新增': 'Add Metadata',
        '元数据删除': 'Delete Metadata',
        '元数据编辑': 'Edit Metadata',
        '物流详情': 'Logistics Details',
        '开放平台管理': 'Open Platform Management',
        '租户接入': 'Tenant Access',
        '接口管理': 'API Management',
        '会员等级': 'Member Levels',
        '商家管理': 'Merchant Management',
        '商家列表': 'Merchant List',
        '入驻审核': 'Entry Review',
        '第2层节点': 'Level 2 Node',
        '商品上下架': 'Product On/Off Shelf',
        '商品删除': 'Delete Product',
        '商品标签新增编辑': 'Add/Edit Product Tags',
        '商品标签删除': 'Delete Product Tags',
        '运费模板新增编辑': 'Add/Edit Shipping Template',
        '发货': 'Ship',
        '关闭订单': 'Close Order',
        '备注': 'Remarks',
        '地址设置': 'Address Settings',
        '券码核销': 'Coupon Verification',
        '数据门户': 'Data Portal',
        '子账号管理': 'Sub-account Management',
        '角色': 'Role',
        '店铺页管理': 'Store Page Management',
        '店铺页列表': 'Store Page List',
        '商品标签': 'Product Tags',
        '运费模板': 'Shipping Template',
        '确认核销': 'Confirm Verification',
        '核销查询': 'Verification Query',
        '店铺设置': 'Store Settings',
        '查询': 'Query',
        '修改': 'Modify',
        '交易设置': 'Transaction Settings',
        '商品新增编辑': 'Add/Edit Product',
        '同意/不同意': 'Approve/Reject',
        '确认收货/拒绝收货': 'Confirm/Reject Receipt',
        '商品查看': 'View Product',
        '商品打标去标': 'Product Tag Management',
        '商品发布': 'Publish Product',
        '运费模板删除': 'Delete Shipping Template',
        '商品编辑库存售价': 'Edit Product Inventory Price',
        '商品查询': 'Product Query',
        '商品强制下架': 'Force Offline Product',
        '商品强制删除': 'Force Delete Product',
        '菜单查看': 'View Menu',
        '菜单配置': 'Menu Configuration',
        '账号配置': 'Account Configuration',
        '账号删除': 'Delete Account',
        '角色配置': 'Role Configuration',
        '角色删除': 'Delete Role',
        '角色查看': 'View Role',
        '账号查看': 'View Account',
        '会员权益配置': 'Member Benefits Configuration',
        '数据报表查看': 'View Data Reports',
        '商品分组新增编辑': 'Add/Edit Product Groups',
        '商品分组查看': 'View Product Groups',
        '商品分组修改商品': 'Modify Products in Group',
        '商品分组配置商品': 'Configure Products in Group',
        '积分规则配置': 'Points Rules Configuration',
        '积分发放': 'Points Distribution',
        '用户积分查看': 'View User Points',
        '积分整体查看': 'View Overall Points',
        '会员信息查看': 'View Member Information',
        '会员分组新增编辑': 'Add/Edit Member Groups',
        '会员分组配置': 'Member Group Configuration',
        '会员分组查看': 'View Member Groups',
        '商家信息查看': 'View Merchant Information',
        '商家审核': 'Merchant Review',
        '商家审核编辑': 'Merchant Review Edit',
        '商家启用/清退': 'Merchant Enable/Disable',
        '地址新增编辑': 'Add/Edit Address',
        '地址删除': 'Delete Address',
        '店铺设置保存': 'Save Store Settings',
        '商城设置': 'Mall Settings',
        '商城设置保存': 'Save Mall Settings',
        '多阶段处理': 'Multi-stage Processing',
        '预售': 'Pre-sale',
        '评价管理': 'Review Management',
        '评价回复': 'Review Reply',
        '品牌管理': 'Brand Management',
        '品牌列表': 'Brand List',
        '消息管理': 'Message Management',
        '消息模板': 'Message Template',
        '账户管理': 'Account Management',
        '新增品牌': 'Add Brand',
        '编辑': 'Edit',
        '价格管理': 'Price Management',
        '协议价管理': 'Agreement Price Management',
        '协议价查看': 'View Agreement Price',
        '协议价修改': 'Modify Agreement Price',
        '协议价导入': 'Import Agreement Price',
        '秒杀': 'Flash Sale',
        '合同管理': 'Contract Management',
        '合同列表': 'Contract List',
        '合同模板': 'Contract Template',
        '营销玩法': 'Marketing Games',
        '抽奖开宝': 'Lucky Draw',
        '分享有礼': 'Share Rewards',
        '企业客户管理': 'Enterprise Customer Management',
        '客户信息查看': 'View Customer Information',
        '客户编辑': 'Edit Customer',
        '客户清退': 'Remove Customer',
        '奖品管理': 'Prize Management',
        '属性管理': 'Attribute Management',
        '数据权限': 'Data Permission',
        '满赠': 'Full Gift',
        '组合商品发布': 'Publish Bundle Products',
        '代客下单': 'Place Order for Customer',
        '代客下单确认订单': 'Confirm Customer Order',
        '代客下单创建订单': 'Create Customer Order',
        '代客下单地址': 'Customer Order Address',
        '数据权限查看': 'View Data Permission',
        '数据权限编辑': 'Edit Data Permission',
        '数据源': 'Data Source',
        '应收单列表': 'Receivable List',
        '发货单列表': 'Shipping List',
        'OMS售后列表': 'OMS After-sales List',
        'OMS商品列表': 'OMS Product List',
        '渠道商品列表': 'Channel Product List',
        '库存管理': 'Inventory Management',
        'OMS分仓库存': 'OMS Warehouse Inventory',
        '基础信息': 'Basic Information',
        '渠道店铺列表': 'Channel Store List',
        '页面管理': 'Page Management',
        '活动页面列表': 'Activity Page List',
        '源码页面列表': 'Source Code Page List',
        '素材媒体中心': 'Media Center',
        '页面模版': 'Page Template',
        '内容管理': 'Content Management',
        '内容发布': 'Content Publishing',
        '内容列表': 'Content List',
        '推广管理': 'Promotion Management',
        '推广列表': 'Promotion List',
        '渠道管理': 'Channel Management',
        '投放中心': 'Placement Center',
        '投放场景': 'Placement Scenario',
        '投放方案': 'Placement Plan',
        '资源运营': 'Resource Operations',
        '组件中心': 'Component Center',
        '组件列表': 'Component List',
        'Schema管理': 'Schema Management',
        'OMS订单列表': 'OMS Order List',
        '渠道商品库存': 'Channel Product Inventory',
        '仓库管理': 'Warehouse Management',
        '逻辑仓库列表': 'Logical Warehouse List',
        '物流快递列表': 'Logistics Express List',
        '库存同步策略': 'Inventory Sync Strategy',
        'OMS商品库存': 'OMS Product Inventory',
        '地址库维护': 'Address Library Maintenance',
        '智能拆单策略': 'Smart Split Order Strategy',
        '智能合单策略': 'Smart Merge Order Strategy',
        '智能快递策略': 'Smart Express Strategy',
        '智能审单策略': 'Smart Order Review Strategy',
        '渠道库存审批': 'Channel Inventory Approval',
        '订单标签': 'Order Tags',
        '智能打标策略': 'Smart Tagging Strategy',
        '智能阻止审单策略': 'Smart Block Review Strategy',
        '智能赠品策略': 'Smart Gift Strategy',
        '出入库管理': 'Inbound/Outbound Management',
        '任务管理': 'Task Management',
        '任务列表': 'Task List',
        '库存调拨管理': 'Inventory Transfer Management',
        '订单编辑审批': 'Order Edit Approval',
        '快递公司转换': 'Express Company Conversion',
        '加去标签': 'Add/Remove Tags',
        '批量导入': 'Batch Import',
        '批量导出': 'Batch Export',
        '启用禁用': 'Enable/Disable',
        '上下架': 'On/Off Shelf',
        '库存调整': 'Inventory Adjustment',
        '审批': 'Approval',
        '设置虚拟库存': 'Set Virtual Inventory',
        '同步到WMS': 'Sync to WMS',
        '新增': 'Add',
        '售后单审批': 'After-sales Order Approval',
        '任务code配置': 'Task Code Configuration',
        '进销存报表': 'Inventory Report',
        '售后统计报表': 'After-sales Statistics Report',
        '店铺汇总数据': 'Store Summary Data',
        '快递费用核账': 'Express Fee Reconciliation',
        '订单状态报表': 'Order Status Report',
        '订单销售报表': 'Order Sales Report',
        '日月结监控': 'Daily/Monthly Settlement Monitor',
        '商品统计报表': 'Product Statistics Report',
        '打标去标': 'Tag/Untag',
        '查看订单': 'View Order',
        '批量审单': 'Batch Order Review',
        '审单': 'Order Review',
        '合单': 'Merge Orders',
        '批量合单': 'Batch Merge Orders',
        '批量换商品': 'Batch Replace Products',
        '导入订单': 'Import Orders',
        '授权': 'Authorization',
        '查看': 'View',
        '设置与保存': 'Settings and Save',
        '详情': 'Details',
        '新增编辑复制': 'Add/Edit/Copy',
        '开启/关闭': 'Enable/Disable',
        '逻辑仓库新增编辑': 'Add/Edit Logical Warehouse',
        '导出订单': 'Export Orders',
        '批量加赠品': 'Batch Add Gifts',
        '加赠品': 'Add Gifts',
        '批量设备注': 'Batch Set Remarks',
        '批量设置仓配物流': 'Batch Set Warehouse Logistics',
        '物流仓配': 'Logistics Warehouse',
        '转异常/转正常': 'Convert to Exception/Normal',
        '拆单': 'Split Order',
        '合并回退': 'Merge Rollback',
        '仓库开启关闭': 'Warehouse Enable/Disable',
        '改状态': 'Change Status',
        '批量审批': 'Batch Approval',
        '物流快递新增编辑': 'Add/Edit Logistics Express',
        '物流快递删除': 'Delete Logistics Express',
        '物流模板编辑': 'Edit Logistics Template',
        '编辑地址库': 'Edit Address Library',
        '快递费用导入': 'Import Express Fees',
        '快递费用报表导出': 'Export Express Fee Report',
        '导入': 'Import',
        '列表查看': 'List View',
        '改收货信息': 'Change Receipt Information',
        '仓库查看': 'View Warehouse',
        '售后处理': 'After-sales Processing',
        '物流模板查看': 'View Logistics Template',
        '同步库存': 'Sync Inventory',
        '创建售后单': 'Create After-sales Order',
        '导出售后单': 'Export After-sales Orders',
        '删除': 'Delete',
        '新增编辑': 'Add/Edit'
    }
    
    return translations.get(chinese_text, chinese_text)

def create_multilingual_json(chinese_text, english_text):
    """创建多语言JSON格式"""
    multilingual_data = [
        {
            "lang": "en",
            "value": english_text
        },
        {
            "lang": "zh",
            "value": chinese_text
        }
    ]
    
    return json.dumps(multilingual_data, ensure_ascii=False)

def replace_descriptions_in_sql(sql_file, output_file, translations_dict):
    """在SQL文件中替换description字段为多语言JSON格式"""
    try:
        with open(sql_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 替换description字段
        for chinese_text, json_text in translations_dict.items():
            pattern = f"description\\s*=\\s*['\"]({re.escape(chinese_text)})['\"]"
            replacement = f"description = '{json_text}'"
            content = re.sub(pattern, replacement, content)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"替换完成，结果已保存到: {output_file}")
        
    except Exception as e:
        print(f"替换文件时出错: {e}")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python extract_and_translate.py <sql_file> [output_file]")
        return
    
    sql_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else sql_file.replace('.sql', '_multilingual.sql')
    
    print("=== 步骤1: 提取中文description值 ===")
    chinese_values = extract_chinese_descriptions(sql_file)
    
    if not chinese_values:
        print("未找到中文description值")
        return
    
    print("=== 步骤2: 去除重复值 ===")
    unique_chinese_values = remove_duplicates(chinese_values)
    
    print("=== 步骤3: 翻译为英文 ===")
    translations_dict = {}
    for chinese_text in unique_chinese_values:
        english_text = translate_to_english(chinese_text)
        json_text = create_multilingual_json(chinese_text, english_text)
        translations_dict[chinese_text] = json_text
        print(f"'{chinese_text}' -> '{english_text}'")
    
    print("=== 步骤4: 替换SQL文件中的description字段 ===")
    replace_descriptions_in_sql(sql_file, output_file, translations_dict)
    
    print(f"\n处理完成！")
    print(f"原始文件: {sql_file}")
    print(f"输出文件: {output_file}")
    print(f"处理了 {len(unique_chinese_values)} 个唯一的中文值")

if __name__ == "__main__":
    main()
