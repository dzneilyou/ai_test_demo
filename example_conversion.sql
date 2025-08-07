-- 原始格式
INSERT INTO gmall_customer.new_entry (id, parent_entry_code, code, description, entry_type_code, entry_scene_code, url, icon, `order`, remark, ref_1, ref_2, create_id, gmt_create, update_id, gmt_modified, deleted, can_auth, has_classified, real_scene_code) VALUES (1, null, 'item-manager', '商品管理', 'menu', 'console', '', 'el-icon-goods', 0, '', null, null, null, null, 'admin(2)', '2022-09-21 11:15:24', 0, 1, 0, 'console');

-- 转换后的多语言格式
INSERT INTO gmall_customer.new_entry (id, parent_entry_code, code, description, entry_type_code, entry_scene_code, url, icon, `order`, remark, ref_1, ref_2, create_id, gmt_create, update_id, gmt_modified, deleted, can_auth, has_classified, real_scene_code) VALUES (1, null, 'item-manager', '[{"lang":"en","value":"Item Management"},{"lang":"zh","value":"商品管理"}]', 'menu', 'console', '', 'el-icon-goods', 0, '', null, null, null, null, 'admin(2)', '2022-09-21 11:15:24', 0, 1, 0, 'console');

-- 更多示例
-- 原始: '订单管理'
-- 转换后: '[{"lang":"en","value":"Order Management"},{"lang":"zh","value":"订单管理"}]'

-- 原始: '营销管理'
-- 转换后: '[{"lang":"en","value":"Marketing Management"},{"lang":"zh","value":"营销管理"}]'

-- 原始: '系统设置'
-- 转换后: '[{"lang":"en","value":"System Settings"},{"lang":"zh","value":"系统设置"}]'

-- 原始: '客户管理'
-- 转换后: '[{"lang":"en","value":"Customer Management"},{"lang":"zh","value":"客户管理"}]'
