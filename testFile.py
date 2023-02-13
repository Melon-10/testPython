SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_check_abnormal_attendance
-- ----------------------------
CREATE TABLE `t_check_abnormal_attendance`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主键',
  `studentid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生标示',
  `student_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生标示',
  `attendance_result` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '考勤结果(出勤类别维护信息)',
  `abnormal_source` int(4) NULL DEFAULT 0 COMMENT '异常出勤数据来源（1早点名、2异常离校）',
  `type_name_logogram` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '出勤名称_简写',
  `lunch_status` int(4) NULL DEFAULT 0 COMMENT '午餐状态(1吃 0不吃)',
  `illness_dict_code` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `illness_codes` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '症状集合(逗号分开)',
  `illness_condition` int(4) NULL DEFAULT 0 COMMENT '状况(1新发起 2持续期 3隔离期)',
  `temperature` double NULL DEFAULT NULL COMMENT '体温',
  `isfollow` int(4) NULL DEFAULT 0 COMMENT '是否关注（1关注 0不关注）',
  `applicant_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '申请人标示',
  `applicant_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '申请人名称',
  `applicant_type` int(4) NULL DEFAULT 0 COMMENT '申请人类型(1教师 2家长)',
  `remarks` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  `abnormal_start_time` datetime(0) NULL DEFAULT NULL COMMENT '异常出勤开始时间',
  `abnormal_end_time` datetime(0) NULL DEFAULT NULL COMMENT '异常出勤结束时间',
  `plan_out_school_time` datetime(0) NULL DEFAULT NULL COMMENT '离校时间(计划)',
  `photograph_time` datetime(0) NULL DEFAULT NULL COMMENT '拍照时间',
  `reason` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '事由',
  `leavefile` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '假条',
  `reclassesfile` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '复课证明',
  `outphoto` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '离校拍照片',
  `leave_status` int(4) NULL DEFAULT 0 COMMENT '请假状态(1 请假中 2已复课)',
  `audit_status` int(4) NULL DEFAULT 0 COMMENT '审核状态(1已审核通过 2审核未通过  0未审核)',
  `audit_des` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '审核描述',
  `district_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区标示',
  `district_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区',
  `faculty_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部标示',
  `faculty_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部',
  `grade_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级标示',
  `grade_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级',
  `class_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级标示',
  `class_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  `type_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '出勤名称',
  `attendance_parent_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '异常上级id(用于存储家长请假后生成的子数据)',
  `out_confirm_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '异常离校确认人编号',
  `onset_date` datetime(0) NULL DEFAULT NULL COMMENT '发病日期',
  `treatment_time` datetime(0) NULL DEFAULT NULL COMMENT '就诊时间',
  `hospital_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '就诊医院',
  `other_symptom` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '其他症状备注',
  `other_illness` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '其他病情备注',
  `breakfast_status` int(4) NULL DEFAULT NULL COMMENT '早餐状态(1吃 0不吃)',
  `addmeal_status` int(4) NULL DEFAULT NULL COMMENT '加餐状态(1吃 0不吃)',
  `afternoontea_status` int(4) NULL DEFAULT NULL COMMENT '下午茶状态(1吃 0不吃)',
  `diag_result` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '诊断结果',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '请假表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_check_abnormal_attendance
-- ----------------------------

-- ----------------------------
-- Table structure for t_check_allergy_info
-- ----------------------------
CREATE TABLE `t_check_allergy_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '过敏信息编号',
  `district_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区id',
  `district_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区名称',
  `faculty_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部id',
  `faculty_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部名称',
  `grade_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级id',
  `grade_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级名称',
  `class_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级id',
  `class_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级名称',
  `student_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生id',
  `student_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生名称',
  `allergy_type` int(11) NULL DEFAULT NULL COMMENT '过敏类型：1：过敏；2：短期不吃',
  `noeat_start_time` datetime(0) NULL DEFAULT NULL COMMENT '短期不吃开始时间',
  `noeat_end_time` datetime(0) NULL DEFAULT NULL COMMENT '短期不吃结束时间',
  `food_id` int(11) NULL DEFAULT NULL COMMENT '食物id',
  `food_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '食物类别',
  `food_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '食物名称',
  `allergy_level_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '过敏程度code(字典)',
  `allergy_level_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '过敏程度名称',
  `status` int(11) NULL DEFAULT NULL COMMENT '状态：0：未知晓；1：班主任已知晓；2：医务室已知晓；3：班主任和医务室都已知晓',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人名称',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人名称',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '过敏信息管理' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_check_allergy_info
-- ----------------------------

-- ----------------------------
-- Table structure for t_check_attendance_logs
-- ----------------------------
CREATE TABLE `t_check_attendance_logs`  (
  `log_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键标示',
  `studentid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生标示',
  `attendance_time` datetime(0) NULL DEFAULT NULL COMMENT '考勤时间',
  `attendance_status` int(4) NULL DEFAULT 1 COMMENT '考勤状况(1正常 2异常)',
  `attendance_result` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '考勤结果(出勤类别维护信息)',
  `breakfast_status` int(4) NULL DEFAULT NULL COMMENT '早餐状态(1吃 0不吃)',
  `addmeal_status` int(4) NULL DEFAULT NULL COMMENT '加餐状态(1吃 0不吃)',
  `lunch_status` int(4) NULL DEFAULT 0 COMMENT '午餐状态(1吃 0不吃)',
  `afternoontea_status` int(4) NULL DEFAULT NULL COMMENT '下午茶状态(1吃 0不吃)',
  `submit_status` int(4) NULL DEFAULT 0 COMMENT '提交状态（1已提交 0未提交）',
  `abnormalid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '异常出勤标示',
  `sub_time` datetime(0) NULL DEFAULT NULL COMMENT '提交时间',
  `district_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区标示',
  `district_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区',
  `faculty_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部标示',
  `faculty_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部',
  `grade_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级标示',
  `grade_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级',
  `class_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级标示',
  `class_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级',
  `teacher_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '班主任标示',
  `teacher_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '班主任名称',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(11) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  `student_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `student_sex` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生性别',
  `lunch_holiday` int(11) NULL DEFAULT 0 COMMENT '午饭假(生成考勤时候的是否吃饭，日后吃饭状态变更了，当前午饭假不变）\r\n            数据来源于 班主任创建的是否就餐',
  `submit_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '提交人(班主任姓名、系统是admin)',
  `submit_type` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '提交类型(app、web、system)',
  `submit_source_type` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '提交数据源(字典：appwebsystem)',
  `parent_confirm_status` int(4) NULL DEFAULT 0 COMMENT '家长确认状态：0：未确认，1：已确认，2：考勤更改',
  `des` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '考勤更改备注',
  `attendance_status_new` int(4) NULL DEFAULT 1 COMMENT '新考勤状况(1正常 2异常)',
  `attendance_result_new` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '新考勤结果(出勤类别维护信息)',
  `sign` longtext COMMENT '电子签名',
  `finance_confirm_status` int(4) DEFAULT 0 COMMENT '财务确认状态：0：未确认，1：已确认，2：考勤更改',
  `finance_adopt_status` int(4) DEFAULT NULL COMMENT '财务通过状态：0：通过，1：不通过',
  PRIMARY KEY (`log_id`) USING BTREE,
  INDEX `index_studentid`(`studentid`) USING BTREE,
  INDEX `index_abnormalid`(`abnormalid`) USING BTREE,
  INDEX `index_create_date`(`create_date`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '考勤表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_attendance_type
-- ----------------------------
CREATE TABLE `t_check_attendance_type`  (
  `attendance_type_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `type_code` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '出勤编码',
  `type_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '出勤名称',
  `type_name_logogram` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '出勤名称_简写',
  `abnormal_type` int(4) NULL DEFAULT 0 COMMENT '出勤类别(1病假 2其他 )',
  `application` int(4) NULL DEFAULT 0 COMMENT '适用情况(1早进校 2异常离校 3两者都有)',
  `line_number` int(4) NULL DEFAULT 0 COMMENT '排序字段',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`attendance_type_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '出勤类别维护表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_check_attendance_type
-- ----------------------------
INSERT INTO `t_check_attendance_type` VALUES (44, '1001', '迟到', '迟', 1, 1, 1, 'c564c5e292a34c5ba39ff188d76f1d20', '2016-05-10 14:42:32', 'c564c5e292a34c5ba39ff188d76f1d20', '2016-06-30 13:41:04', 0);
INSERT INTO `t_check_attendance_type` VALUES (45, '1002', '病假', '病', 1, 3, 2, 'c564c5e292a34c5ba39ff188d76f1d20', '2016-05-10 14:43:25', 'c564c5e292a34c5ba39ff188d76f1d20', '2016-05-10 14:56:50', 1);
INSERT INTO `t_check_attendance_type` VALUES (46, '1003', '事假', '事', 1, 3, 3, 'c564c5e292a34c5ba39ff188d76f1d20', '2016-05-10 14:44:55', 'c564c5e292a34c5ba39ff188d76f1d20', '2016-06-30 14:27:08', 1);
INSERT INTO `t_check_attendance_type` VALUES (47, '1004', '休学', '休', 2, 1, 4, 'c564c5e292a34c5ba39ff188d76f1d20', '2016-05-10 14:45:14', 'ae9d2a2fa9a04aa6b2f4748023d16d12', '2017-02-20 08:39:53', 0);
INSERT INTO `t_check_attendance_type` VALUES (48, '1005', '其他', '其他', 1, 3, 5, NULL, NULL, NULL, NULL, 1);

-- ----------------------------
-- Table structure for t_check_attendance_update_meter
-- ----------------------------
CREATE TABLE `t_check_attendance_update_meter`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键标示',
  `studentid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生标示',
  `attendance_time` datetime(0) NULL DEFAULT NULL COMMENT '考勤时间',
  `attendance_result` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '考勤结果(出勤类别维护信息)',
  `lunch_status` int(4) NULL DEFAULT 0 COMMENT '午餐状态(1吃 0不吃)',
  `abnormalid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '异常出勤标示',
  `sub_time` datetime(0) NULL DEFAULT NULL COMMENT '提交时间',
  `district_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区标示',
  `district_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区',
  `faculty_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部标示',
  `faculty_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部',
  `grade_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级标示',
  `grade_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级',
  `class_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级标示',
  `class_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级',
  `teacher_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '班主任标示',
  `teacher_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '班主任名称',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  `student_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_charge
-- ----------------------------
CREATE TABLE `t_check_charge`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '收费标准设置id',
  `year` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '年',
  `month` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '月',
  `days` int(11) NULL DEFAULT NULL COMMENT '天数',
  `nursing_fee` decimal(10, 2) NULL DEFAULT NULL COMMENT '保教费',
  `food_fee` decimal(10, 2) NULL DEFAULT NULL COMMENT '餐费',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人名称',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人名称',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '收费标准设置' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_check_charge
-- ----------------------------
INSERT INTO `t_check_charge` VALUES (1, '2023', '01', 22, 480.00, 20.00, NULL, NULL, NULL, '鲁素菊', '2c91809363ecb2bb0163eccc23f9037b', '2023-01-11 17:50:11', 1);
INSERT INTO `t_check_charge` VALUES (2, '2023', '02', 23, 480.00, 20.00, NULL, NULL, NULL, '鲁素菊', '2c91809363ecb2bb0163eccc23f9037b', '2023-01-11 15:18:19', 0);

-- ----------------------------
-- Table structure for t_check_class_abnormal_temp
-- ----------------------------
CREATE TABLE `t_check_class_abnormal_temp`  (
  `temp_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '流水号',
  `class_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '班级id',
  `submit_time` datetime(0) NULL DEFAULT NULL COMMENT '提交时间',
  `student_total` int(11) NULL DEFAULT NULL COMMENT '班级学生总人数',
  `abnormal_total` int(11) NULL DEFAULT NULL COMMENT '异常总数',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` tinyint(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`temp_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '班级考勤临时表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_class_abnormal_temp_details
-- ----------------------------
CREATE TABLE `t_check_class_abnormal_temp_details`  (
  `detail_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '异常流水号',
  `temp_id` int(11) NULL DEFAULT NULL COMMENT '流水号',
  `abnorma_id` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '异常类型',
  `abnorma_quantity` int(11) NULL DEFAULT NULL COMMENT '异常数量',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(11) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`detail_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '班级临时考勤明细' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_cookbook
-- ----------------------------
CREATE TABLE `t_check_cookbook`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '带量食谱编号',
  `cookbook_start_time` datetime(0) NULL DEFAULT NULL COMMENT '食谱开始时间',
  `cookbook_end_time` datetime(0) NULL DEFAULT NULL COMMENT '食谱结束时间',
  `cookbook_url` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '食谱文件路径',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人名称',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人名称',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '带量食谱表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_cookbook_details
-- ----------------------------
CREATE TABLE `t_check_cookbook_details`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '带量食谱详情编号',
  `cookbook_id` int(11) NULL DEFAULT NULL COMMENT '食谱id',
  `week_code` int(11) NULL DEFAULT NULL COMMENT '星期编号',
  `meal_code` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '餐别编号(字典)',
  `meal_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '餐别名称',
  `cookbook_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '食谱名称',
  `food_id` int(11) NULL DEFAULT NULL COMMENT '食物id',
  `food_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '食物名称',
  `bandage` double NULL DEFAULT NULL COMMENT '带量/人(克)',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人名称',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人名称',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '带量食谱表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_food
-- ----------------------------
CREATE TABLE `t_check_food`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '食物编号',
  `food_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '食物类别',
  `food_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '食物名称',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人名称',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人名称',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '食物表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_check_food
-- ----------------------------
INSERT INTO `t_check_food` VALUES (1, '谷类及制品', '稻米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2, '谷类及制品', '低筋面粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (3, '谷类及制品', '高筋面粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (4, '谷类及制品', '高粱面面条', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (5, '谷类及制品', '挂面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (6, '谷类及制品', '挂面(富强粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (7, '谷类及制品', '黑米粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (8, '谷类及制品', '龙须面(鸡蛋)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (9, '谷类及制品', '龙须面(素)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (10, '谷类及制品', '螺丝粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (11, '谷类及制品', '馒头', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (12, '谷类及制品', '馒头(富强粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (13, '谷类及制品', '马蹄粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (14, '谷类及制品', '面条', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (15, '谷类及制品', '面条(富强粉，切面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (16, '谷类及制品', '面条(富强粉，煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (17, '谷类及制品', '米饭(蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (18, '谷类及制品', '米线', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (19, '谷类及制品', '糯米粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (20, '谷类及制品', '沙河粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (21, '谷类及制品', '籼米饭(蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (22, '谷类及制品', '小麦粉(标准粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (23, '谷类及制品', '鸭翅根', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (24, '谷类及制品', '意大利面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (25, '谷类及制品', '意粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (26, '谷类及制品', '莜麦面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (27, '谷类及制品', '玉米粒（冻）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (28, '谷类及制品', '玉米面(黄)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (29, '谷类及制品', '玉米糁(黄)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (30, '谷类及制品', '粘米浆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (31, '谷类及制品', '中筋面粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (32, '谷类及制品', '紫米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (33, '谷类及制品', '粳米(极品精米)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (34, '谷类及制品', '粳米(西域王米)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (35, '谷类及制品', '粳米(小站稻米)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (36, '谷类及制品', '籼米(标一)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (37, '谷类及制品', '籼米(标准)[机米]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (38, '谷类及制品', '早籼(标一)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (39, '谷类及制品', '早籼(标二)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (40, '谷类及制品', '晚籼(标一)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (41, '谷类及制品', '晚籼(特等)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (42, '谷类及制品', '籼稻(红)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (43, '谷类及制品', '香米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (44, '谷类及制品', '籼米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (45, '谷类及制品', '糙米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (46, '谷类及制品', '粳糯米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (47, '谷类及制品', '籼糯米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (48, '谷类及制品', '米饭(蒸，代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (49, '谷类及制品', '粳米粥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (50, '谷类及制品', '籼米粉[排米粉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (51, '谷类及制品', '籼米粉(干，细)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (52, '谷类及制品', '高蛋白豆米粉(籼米)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (53, '谷类及制品', '籼米粥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (54, '谷类及制品', '米粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (55, '谷类及制品', '玉米(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (56, '谷类及制品', '玉米(白，干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (57, '谷类及制品', '玉米(黄，干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (58, '谷类及制品', '玉米面(白)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (59, '谷类及制品', '玉米面(强化豆粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (60, '谷类及制品', '玉米粒(黄、干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (61, '谷类及制品', '玉米笋(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (62, '谷类及制品', '玉米面面条', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (63, '谷类及制品', '大麦[元麦]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (64, '谷类及制品', '黑大麦', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (65, '谷类及制品', '肚里黄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (66, '谷类及制品', '青稞', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (67, '谷类及制品', '黑米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (68, '谷类及制品', '小米面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (69, '谷类及制品', '籼米(优标)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (70, '谷类及制品', '早籼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (71, '谷类及制品', '小米(黄)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (72, '谷类及制品', '大黄米[黍子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (73, '谷类及制品', '黄米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (74, '谷类及制品', '糜子(带皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (75, '谷类及制品', '糜子米(炒米)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (76, '谷类及制品', '苦荞麦粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (77, '谷类及制品', '高粱米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (78, '谷类及制品', '荞麦', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (79, '谷类及制品', '荞麦(带皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (80, '谷类及制品', '薏米[薏仁米，苡米]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (81, '谷类及制品', '薏米面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (82, '谷类及制品', '荞麦面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (83, '谷类及制品', '燕麦', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (84, '谷类及制品', '早籼(特等)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (85, '谷类及制品', '粳米(标三)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (86, '谷类及制品', '晚籼(标二)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (87, '谷类及制品', '优糯米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (88, '谷类及制品', '早糯谷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (89, '谷类及制品', '紫红糯米[血糯米]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (90, '谷类及制品', '粳米饭(蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (91, '谷类及制品', '五谷香', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (92, '谷类及制品', '粳米(标二)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (93, '谷类及制品', '糯米[江米]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (94, '谷类及制品', '面条(标准粉，切面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (95, '谷类及制品', '油面筋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (96, '谷类及制品', '小麦胚粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (97, '谷类及制品', '河粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (98, '谷类及制品', '藜麦(散装)（河北）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (99, '谷类及制品', '藜麦(散装)（山西）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (100, '谷类及制品', '香米（泰国）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (101, '谷类及制品', '高粱面面条（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (102, '谷类及制品', '面条(富强粉，切面)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (103, '谷类及制品', '面条(富强粉，煮)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (104, '谷类及制品', '挂面(富强粉)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (105, '谷类及制品', '馒头(富强粉)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (106, '谷类及制品', '龙须面(素)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (107, '谷类及制品', '莜麦面（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (108, '谷类及制品', '玉米糁(黄)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (109, '谷类及制品', '玉米面(黄)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (110, '谷类及制品', '籼米饭(蒸)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (111, '谷类及制品', '龙须面(鸡蛋)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (112, '谷类及制品', '小米粥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (113, '谷类及制品', '小米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (114, '谷类及制品', '小麦', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (115, '谷类及制品', '小麦粉(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (116, '谷类及制品', '小麦粉(富强粉，特一粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (117, '谷类及制品', '小麦粉(特二粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (118, '谷类及制品', '麸皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (119, '谷类及制品', '小麦粉(特制)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (120, '谷类及制品', '挂面(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (121, '谷类及制品', '挂面(标准粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (122, '谷类及制品', '挂面(精制龙须面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (123, '谷类及制品', '面条(生，代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (124, '谷类及制品', '面条(特粉，切面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (125, '谷类及制品', '面条(干切面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (126, '谷类及制品', '面条(虾蓉面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (127, '谷类及制品', '小麦粉(富强粉，特一粉)（高蛋白高脂低维生素）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (128, '谷类及制品', '小麦粉(标准粉)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (129, '谷类及制品', '通心面[通心粉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (130, '谷类及制品', '花卷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (131, '谷类及制品', '空锅饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (132, '谷类及制品', '烙饼(标准粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (133, '谷类及制品', '馒头(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (134, '谷类及制品', '馒头(标准粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (135, '谷类及制品', '烧饼(加糖)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (136, '谷类及制品', '油饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (137, '谷类及制品', '油条', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (138, '谷类及制品', '花卷(加牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (139, '谷类及制品', '水面筋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (140, '谷类及制品', '面筋(肉馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (141, '谷类及制品', '稻米(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (142, '谷类及制品', '粳米(标一)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (143, '谷类及制品', '粳米(标四)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (144, '谷类及制品', '粳米(特等)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (145, '薯类、淀粉及制品', '澄粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (146, '薯类、淀粉及制品', '甘薯(红心)[山芋，红薯]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (147, '薯类、淀粉及制品', '马铃薯粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (148, '薯类、淀粉及制品', '生粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (149, '薯类、淀粉及制品', '西米', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (150, '薯类、淀粉及制品', '沾米粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (151, '薯类、淀粉及制品', '紫薯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (152, '薯类、淀粉及制品', '木薯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (153, '薯类、淀粉及制品', '蚕豆淀粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (154, '薯类、淀粉及制品', '豌豆淀粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (155, '薯类、淀粉及制品', '团粉[芡粉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (156, '薯类、淀粉及制品', '藕粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (157, '薯类、淀粉及制品', '魔芋精粉[鬼芋粉，南星粉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (158, '薯类、淀粉及制品', '淀粉(小麦)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (159, '薯类、淀粉及制品', '淀粉(大米)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (160, '薯类、淀粉及制品', '甘薯(红心)[山芋、红薯]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (161, '薯类、淀粉及制品', '淀粉(马铃薯)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (162, '薯类、淀粉及制品', '淀粉(甘薯)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (163, '薯类、淀粉及制品', '豌豆粉丝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (164, '薯类、淀粉及制品', '马铃薯丁(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (165, '薯类、淀粉及制品', '甘薯(白心)[红皮山芋]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (166, '薯类、淀粉及制品', '粉条', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (167, '薯类、淀粉及制品', '粉丝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (168, '薯类、淀粉及制品', '玉米淀粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (169, '薯类、淀粉及制品', '桂花藕粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (170, '薯类、淀粉及制品', '马铃薯[土豆，洋芋]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (171, '薯类、淀粉及制品', '甘薯粉[地瓜粉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (172, '薯类、淀粉及制品', '煎炸粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (173, '薯类、淀粉及制品', '马铃薯(烤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (174, '薯类、淀粉及制品', '马铃薯(蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (175, '薯类、淀粉及制品', '马铃薯(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (176, '薯类、淀粉及制品', '马铃薯全粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (177, '薯类、淀粉及制品', '甘薯片[白薯干]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (178, '干豆类及制品', '红豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (179, '干豆类及制品', '豆饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (180, '干豆类及制品', '豆腐', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (181, '干豆类及制品', '豆腐(北)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (182, '干豆类及制品', '豆腐干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (183, '干豆类及制品', '豆腐(南)[南豆腐]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (184, '干豆类及制品', '豆腐皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (185, '干豆类及制品', '豆浆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (186, '干豆类及制品', '豆粕(膨化)[大豆蛋白]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (187, '干豆类及制品', '豆沙', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (188, '干豆类及制品', '红豆馅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (189, '干豆类及制品', '油豆腐（大）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (190, '干豆类及制品', '豆腐脑[老豆腐]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (191, '干豆类及制品', '豆腐(北豆腐)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (192, '干豆类及制品', '豆腐(南豆腐)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (193, '干豆类及制品', '豆奶[豆乳]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (194, '干豆类及制品', '酸豆奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (195, '干豆类及制品', '豆奶(甜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (196, '干豆类及制品', '豆腐丝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (197, '干豆类及制品', '豆腐丝(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (198, '干豆类及制品', '豆腐丝(油)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (199, '干豆类及制品', '豆腐卷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (200, '干豆类及制品', '油豆腐', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (201, '干豆类及制品', '腐竹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (202, '干豆类及制品', '豆汁(生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (203, '干豆类及制品', '豆腐干(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (204, '干豆类及制品', '豆腐干(菜干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (205, '干豆类及制品', '豆腐干(酱油干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (206, '干豆类及制品', '豆腐干(卤干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (207, '干豆类及制品', '豆腐干(蒲包干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (208, '干豆类及制品', '豆腐干(香干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (209, '干豆类及制品', '豆腐干(小香干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (210, '干豆类及制品', '豆肝尖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (211, '干豆类及制品', '素大肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (212, '干豆类及制品', '素火腿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (213, '干豆类及制品', '素鸡丝卷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (214, '干豆类及制品', '素什锦', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (215, '干豆类及制品', '炸素虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (216, '干豆类及制品', '烤麸', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (217, '干豆类及制品', '绿豆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (218, '干豆类及制品', '绿豆面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (219, '干豆类及制品', '绿豆饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (220, '干豆类及制品', '枝竹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (221, '干豆类及制品', '赤小豆(干)[小豆，红小豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (222, '干豆类及制品', '小豆粥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (223, '干豆类及制品', '红豆沙(去皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (224, '干豆类及制品', '花豆(干,红)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (225, '干豆类及制品', '花豆(干,紫)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (226, '干豆类及制品', '芸豆(干,白)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (227, '干豆类及制品', '芸豆(干,红)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (228, '干豆类及制品', '芸豆(干,虎皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (229, '干豆类及制品', '芸豆(干,杂，带皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (230, '干豆类及制品', '蚕豆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (231, '干豆类及制品', '蚕豆(带皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (232, '干豆类及制品', '蚕豆(去皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (233, '干豆类及制品', '脑豆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (234, '干豆类及制品', '蚕豆(烤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (235, '干豆类及制品', '蚕豆(炸)[开花豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (236, '干豆类及制品', '扁豆(干，白)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (237, '干豆类及制品', '豇豆(干，紫)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (238, '干豆类及制品', '马牙大豆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (239, '干豆类及制品', '豇豆(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (240, '干豆类及制品', '豌豆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (241, '干豆类及制品', '豌豆(花)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (242, '干豆类及制品', '豌豆(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (243, '干豆类及制品', '鹰嘴豆[桃豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (244, '干豆类及制品', '荆豆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (245, '干豆类及制品', '木豆(干)[扭豆，豆蓉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (246, '干豆类及制品', '豇豆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (247, '干豆类及制品', '豆腐干(熏干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (248, '干豆类及制品', '豆腐干(臭干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (249, '干豆类及制品', '豆腐(内酯)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (250, '干豆类及制品', '蚕豆(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (251, '干豆类及制品', '腐竹（广西）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (252, '干豆类及制品', '素鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (253, '干豆类及制品', '豆腐皮（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (254, '干豆类及制品', '豆腐干（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (255, '干豆类及制品', '豆浆（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (256, '干豆类及制品', '红豆馅（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (257, '干豆类及制品', '千张[百页]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (258, '干豆类及制品', '眉豆(干)[饭豇豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (259, '干豆类及制品', '扁豆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (260, '干豆类及制品', '黄豆[大豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (261, '干豆类及制品', '黑豆(干)[黑大豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (262, '干豆类及制品', '青豆(干)[青大豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (263, '干豆类及制品', '黄豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (264, '干豆类及制品', '黄豆粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (265, '干豆类及制品', '豆腐花[豆腐粉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (266, '干豆类及制品', '豆浆粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (267, '干豆类及制品', '豆浆粉(维维牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (268, '干豆类及制品', '豆浆粉(多力牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (269, '干豆类及制品', '豆浆粉(大磨牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (270, '干豆类及制品', '豆腐(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (271, '蔬菜类及制品', '百合(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (272, '蔬菜类及制品', '包菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (273, '蔬菜类及制品', '贝贝南瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (274, '蔬菜类及制品', '菜花[花椰菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (275, '蔬菜类及制品', '彩椒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (276, '蔬菜类及制品', '大白菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (277, '蔬菜类及制品', '大葱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (278, '蔬菜类及制品', '蛋挞皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (279, '蔬菜类及制品', '番茄[西红柿]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (280, '蔬菜类及制品', '番杏[夏菠菜，新西兰菠菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (281, '蔬菜类及制品', '飞碟瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (282, '蔬菜类及制品', '盖菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (283, '蔬菜类及制品', '根芹[根洋芹、球根塘蒿]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (284, '蔬菜类及制品', '观达菜[根达菜，牛皮菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (285, '蔬菜类及制品', '黑豆苗', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (286, '蔬菜类及制品', '芥蓝[甘蓝菜，盖蓝菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (287, '蔬菜类及制品', '韭菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (288, '蔬菜类及制品', '辣椒(青，尖)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (289, '蔬菜类及制品', '芦笋[石刁柏，龙须菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (290, '蔬菜类及制品', '绿豆芽', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (291, '蔬菜类及制品', '梅菜（干）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (292, '蔬菜类及制品', '苜蓿[草头，金花菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (293, '蔬菜类及制品', '藕[莲藕]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (294, '蔬菜类及制品', '茄子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (295, '蔬菜类及制品', '茄子(紫皮，长)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (296, '蔬菜类及制品', '芹菜(白茎)[旱芹，药芹]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (297, '蔬菜类及制品', '青萝卜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (298, '蔬菜类及制品', '球茎茴香', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (299, '蔬菜类及制品', '秋葵[黄秋葵，羊角豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (300, '蔬菜类及制品', '去皮马蹄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (301, '蔬菜类及制品', '上海青', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (302, '蔬菜类及制品', '生菜(牛俐)[油麦菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (303, '蔬菜类及制品', '生菜(叶用莴苣)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (304, '蔬菜类及制品', '圣女果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (305, '蔬菜类及制品', '丝瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (306, '蔬菜类及制品', '丝瓜（60%）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (307, '蔬菜类及制品', '酸白菜[酸菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (308, '蔬菜类及制品', '甜椒[灯笼椒，柿子椒]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (309, '蔬菜类及制品', '豌豆苗', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (310, '蔬菜类及制品', '蕹菜[空心菜，藤藤菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (311, '蔬菜类及制品', '莴笋肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (312, '蔬菜类及制品', '莴笋叶[莴苣叶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (313, '蔬菜类及制品', '小白菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (314, '蔬菜类及制品', '西兰花[绿菜花]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (315, '蔬菜类及制品', '西生菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (316, '蔬菜类及制品', '细香葱[香葱，四季葱]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (317, '蔬菜类及制品', '洋葱(白皮）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (318, '蔬菜类及制品', '油菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (319, '蔬菜类及制品', '芋头[芋艿，毛芋]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (320, '蔬菜类及制品', '鱼腥草[蕺菜，臭菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (321, '蔬菜类及制品', '紫菜头', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (322, '蔬菜类及制品', '香瓜茄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (323, '蔬菜类及制品', '樱桃番茄[小西红柿]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (324, '蔬菜类及制品', '辣椒(小红尖辣椒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (325, '蔬菜类及制品', '辣椒(小红尖辣椒、干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (326, '蔬菜类及制品', '甜椒[灯笼椒、柿子椒]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (327, '蔬菜类及制品', '秋葵[黄秋葵、羊角豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (328, '蔬菜类及制品', '白瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (329, '蔬菜类及制品', '菜瓜[生瓜，白瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (330, '蔬菜类及制品', '方瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (331, '蔬菜类及制品', '佛手瓜[棒瓜，菜肴梨]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (332, '蔬菜类及制品', '葫芦[长瓜，蒲瓜，瓠瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (333, '蔬菜类及制品', '葫芦条(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (334, '蔬菜类及制品', '节瓜[毛瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (335, '蔬菜类及制品', '金瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (336, '蔬菜类及制品', '金丝瓜[裸瓣瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (337, '蔬菜类及制品', '南瓜(鲜)[倭瓜，番瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (338, '蔬菜类及制品', '南瓜粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (339, '蔬菜类及制品', '蛇瓜[蛇豆，大豆角]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (340, '蔬菜类及制品', '笋瓜[生瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (341, '蔬菜类及制品', '西葫芦', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (342, '蔬菜类及制品', '面西胡瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (343, '蔬菜类及制品', '小西胡瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (344, '蔬菜类及制品', '黄金西葫芦', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (345, '蔬菜类及制品', '黄茎瓜[小南瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (346, '蔬菜类及制品', '迷你黄瓜[荷兰乳黄瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (347, '蔬菜类及制品', '秋黄瓜[旱黄瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (348, '蔬菜类及制品', '南瓜(栗面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (349, '蔬菜类及制品', '大蒜(白皮，鲜)[蒜头]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (350, '蔬菜类及制品', '大蒜(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (351, '蔬菜类及制品', '青蒜(青葱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (352, '蔬菜类及制品', '蒜薹(圆)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (353, '蔬菜类及制品', '大葱(红皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (354, '蔬菜类及制品', '葱(小葱，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (355, '蔬菜类及制品', '细香葱[香葱、四季葱]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (356, '蔬菜类及制品', '洋葱(鲜)[葱头]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (357, '蔬菜类及制品', '洋葱(紫皮，脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (358, '蔬菜类及制品', '韭黄(韭芽，黄色)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (359, '蔬菜类及制品', '韭薹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (360, '蔬菜类及制品', '薤[皎头]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (361, '蔬菜类及制品', '薤白(鲜)[小根蒜，山蒜，团蒜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (362, '蔬菜类及制品', '飞碟瓜（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (363, '蔬菜类及制品', '大白菜(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (364, '蔬菜类及制品', '大白菜(白梗)[黄芽白]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (365, '蔬菜类及制品', '大白菜(青白口)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (366, '蔬菜类及制品', '大白菜(小白口)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (367, '蔬菜类及制品', '白菜(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (368, '蔬菜类及制品', '白菜薹[菜薹，菜心]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (369, '蔬菜类及制品', '红菜薹[紫菜薹]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (370, '蔬菜类及制品', '瓢儿白[瓢儿菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (371, '蔬菜类及制品', '乌菜[乌塌菜，塌棵菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (372, '蔬菜类及制品', '油菜(黑)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (373, '蔬菜类及制品', '油菜(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (374, '蔬菜类及制品', '油菜薹[菜薹]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (375, '蔬菜类及制品', '大白菜(白口)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (376, '蔬菜类及制品', '大白菜(青口)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (377, '蔬菜类及制品', '小白菜[青菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (378, '蔬菜类及制品', '鸡毛菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (379, '蔬菜类及制品', '娃娃菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (380, '蔬菜类及制品', '乌塌菜[塌菜、塌棵菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (381, '蔬菜类及制品', '油菜心', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (382, '蔬菜类及制品', '圆白菜，卷心菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (383, '蔬菜类及制品', '菜花(脱水)[脱水花椰菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (384, '蔬菜类及制品', '芥菜(鲜)[雪里红，雪菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (385, '蔬菜类及制品', '芥菜(大叶，鲜)[盖菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (386, '蔬菜类及制品', '芥菜(茎用，鲜)[青头菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (387, '蔬菜类及制品', '芥菜(小叶，鲜)[小芥菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (388, '蔬菜类及制品', '结球甘蓝(绿)[圆白菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (389, '蔬菜类及制品', '结球甘蓝(紫)[圆白菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (390, '蔬菜类及制品', '抱子甘蓝[小圆白菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (391, '蔬菜类及制品', '羽衣甘蓝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (392, '蔬菜类及制品', '芥蓝[甘蓝菜、盖蓝菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (393, '蔬菜类及制品', '菜花(白色)[花椰菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (394, '蔬菜类及制品', '西蓝花[绿菜花]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (395, '蔬菜类及制品', '菠菜(鲜)[赤根菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (396, '蔬菜类及制品', '冬寒菜(鲜)[冬苋菜，冬葵]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (397, '蔬菜类及制品', '胡萝卜缨(红，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (398, '蔬菜类及制品', '萝卜缨(青)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (399, '蔬菜类及制品', '苋菜(绿，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (400, '蔬菜类及制品', '萝卜缨(小萝卜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (401, '蔬菜类及制品', '芹菜茎', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (402, '蔬菜类及制品', '芹菜叶(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (403, '蔬菜类及制品', '甜菜叶(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (404, '蔬菜类及制品', '香菜(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (405, '蔬菜类及制品', '茼蒿(鲜)[蓬蒿菜，艾菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (406, '蔬菜类及制品', '茴香(鲜)[小茴香]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (407, '蔬菜类及制品', '荠菜(鲜)[蓟菜，菱角菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (408, '蔬菜类及制品', '番杏[新西兰菠菜、夏菠菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (409, '蔬菜类及制品', '樱桃萝卜缨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (410, '蔬菜类及制品', '白凤菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (411, '蔬菜类及制品', '紫背天葵[红风菜、血皮菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (412, '蔬菜类及制品', '芹菜(茎)[旱芹，药芹]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (413, '蔬菜类及制品', '西芹[西洋芹菜、美芹]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (414, '蔬菜类及制品', '落葵[木耳菜，软浆菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (415, '蔬菜类及制品', '苋菜(紫，鲜)[红苋]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (416, '蔬菜类及制品', '生菜[叶用莴苣]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (417, '蔬菜类及制品', '油麦菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (418, '蔬菜类及制品', '叶甜菜(白梗)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (419, '蔬菜类及制品', '莴笋叶[莴苣菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (420, '蔬菜类及制品', '达乌里胡枝子(鲜)[牛枝子，豆豆苗]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (421, '蔬菜类及制品', '蕹菜[空心菜、藤藤菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (422, '蔬菜类及制品', '观达菜[根达菜、牛皮菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (423, '蔬菜类及制品', '球茎茴香[甜茴香、意大利茴香]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (424, '蔬菜类及制品', '竹笋(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (425, '蔬菜类及制品', '白笋(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (426, '蔬菜类及制品', '鞭笋(鲜)[马鞭笋]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (427, '蔬菜类及制品', '春笋(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (428, '蔬菜类及制品', '冬笋(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (429, '蔬菜类及制品', '黑笋(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (430, '蔬菜类及制品', '毛笋(鲜)[毛竹笋]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (431, '蔬菜类及制品', '玉兰片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (432, '蔬菜类及制品', '百合(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (433, '蔬菜类及制品', '百合(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (434, '蔬菜类及制品', '菊苣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (435, '蔬菜类及制品', '芦笋(绿)[石刁柏、龙须菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (436, '蔬菜类及制品', '芦笋(紫)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (437, '蔬菜类及制品', '结球菊苣(红)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (438, '蔬菜类及制品', '软化白菊苣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (439, '蔬菜类及制品', '穿心莲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (440, '蔬菜类及制品', '红薯叶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (441, '蔬菜类及制品', '南瓜藤', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (442, '蔬菜类及制品', '三七尖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (443, '蔬菜类及制品', '棠梨花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (444, '蔬菜类及制品', '洋丝瓜苗', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (445, '蔬菜类及制品', '慈菇(鲜)[乌芋，白地果]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (446, '蔬菜类及制品', '菱角(老)[龙角]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (447, '蔬菜类及制品', '蒲菜(鲜)[香蒲，甘蒲，野茭白]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (448, '蔬菜类及制品', '水芹菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (449, '蔬菜类及制品', '茭白(鲜)[茭笋，茭粑]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (450, '蔬菜类及制品', '荸荠(鲜)[马蹄，地栗]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (451, '蔬菜类及制品', '莼菜(瓶装)[花案菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (452, '蔬菜类及制品', '红菱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (453, '蔬菜类及制品', '大薯(鲜)[参薯]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (454, '蔬菜类及制品', '葛(鲜)[葛署，粉葛]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (455, '蔬菜类及制品', '山药(鲜)[薯蓣，大薯]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (456, '蔬菜类及制品', '芋头(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (457, '蔬菜类及制品', '姜(鲜)[黄姜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (458, '蔬菜类及制品', '姜(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (459, '蔬菜类及制品', '姜(子姜，鲜)[嫩姜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (460, '蔬菜类及制品', '洋姜(鲜)[菊芋，鬼子姜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (461, '蔬菜类及制品', '艾蒿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (462, '蔬菜类及制品', '白花菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (463, '蔬菜类及制品', '白花桔梗', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (464, '蔬菜类及制品', '白沙蒿(鲜)[沙蒿]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (465, '蔬菜类及制品', '白沙蒿子(干)[沙蒿籽]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (466, '蔬菜类及制品', '白薯叶(鲜)[甘薯叶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (467, '蔬菜类及制品', '百里香(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (468, '蔬菜类及制品', '败酱(鲜)[胭脂麻]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (469, '蔬菜类及制品', '扁蓄菜(鲜)[竹节草]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (470, '蔬菜类及制品', '朝鲜蓟(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (471, '蔬菜类及制品', '刺儿菜(鲜)[小蓟，蓟蓟菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (472, '蔬菜类及制品', '达乌里胡枝子籽(鲜)[牛枝子籽，豆豆苗子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (473, '蔬菜类及制品', '大玻璃草叶(鲜)[大车前]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (474, '蔬菜类及制品', '大巢菜(鲜)[野苕子，野豌豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (475, '蔬菜类及制品', '大蓟叶(鲜)[飞廉叶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (476, '蔬菜类及制品', '地肤(鲜)[益明，扫帚苗]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (477, '蔬菜类及制品', '地笋(鲜)[地古牛，地瓜儿苗叶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (478, '蔬菜类及制品', '豆腐柴(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (479, '蔬菜类及制品', '独行菜(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (480, '蔬菜类及制品', '独行菜(宽，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (481, '蔬菜类及制品', '胡枝子(鲜)[山豆子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (482, '蔬菜类及制品', '槐花(鲜)[洋槐花，豆槐花]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (483, '蔬菜类及制品', '黄麻叶(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (484, '蔬菜类及制品', '碱蓬(鲜)[棉蓬，猪毛菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (485, '蔬菜类及制品', '轮叶党参', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (486, '蔬菜类及制品', '罗勒[兰香]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (487, '蔬菜类及制品', '马齿苋(鲜)[长寿菜，瓜子菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (488, '蔬菜类及制品', '马兰头(鲜)[马兰，鸡儿肠，路边菊]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (489, '蔬菜类及制品', '麦瓶草(鲜)[米瓦罐]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (490, '蔬菜类及制品', '牛至', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (491, '蔬菜类及制品', '牛蒡叶(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (492, '蔬菜类及制品', '爬景天(鲜)[石头菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (493, '蔬菜类及制品', '蒜苗(绿色，青蒜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (494, '蔬菜类及制品', '婆罗门参(白，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (495, '蔬菜类及制品', '婆罗门参(黑，鲜)[鸦葱]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (496, '蔬菜类及制品', '蒲公英叶(鲜)[黄花苗叶，孛孛丁叶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (497, '蔬菜类及制品', '掐不齐(鲜)[鸡眼草，牛黄草]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (498, '蔬菜类及制品', '清明菜(鲜)[鼠曲菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (499, '蔬菜类及制品', '沙参叶(鲜)[白参]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (500, '蔬菜类及制品', '沙蓬子(鲜)[沙米]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (501, '蔬菜类及制品', '山苦荬叶(鲜)[启明菜叶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (502, '蔬菜类及制品', '食用大黄(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (503, '蔬菜类及制品', '食用黄麻', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (504, '蔬菜类及制品', '酸模(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (505, '蔬菜类及制品', '汤菜(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (506, '蔬菜类及制品', '土三七(鲜)[景天三七]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (507, '蔬菜类及制品', '歪头菜(鲜)[草豆，二叶萩]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (508, '蔬菜类及制品', '梧桐子(鲜)[瓢儿果]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (509, '蔬菜类及制品', '夏枯草(鲜)[铁色草]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (510, '蔬菜类及制品', '香茅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (511, '蔬菜类及制品', '小旋花(鲜)[狗儿蔓]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (512, '蔬菜类及制品', '鸭跖草(鲜)[竹叶菜，淡竹叶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (513, '蔬菜类及制品', '野葱(鲜)[沙葱，麦葱]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (514, '蔬菜类及制品', '野韭菜(鲜)[山韭]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (515, '蔬菜类及制品', '野菊(鲜)[菊脑]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (516, '蔬菜类及制品', '野蒜(鲜)[小蒜，野葱]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (517, '蔬菜类及制品', '野苋菜(鲜)[假苋菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (518, '蔬菜类及制品', '茵陈蒿(鲜)[茵陈]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (519, '蔬菜类及制品', '榆钱(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (520, '蔬菜类及制品', '珍珠花菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (521, '蔬菜类及制品', '紫花桔梗', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (522, '蔬菜类及制品', '紫萼香茶菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (523, '蔬菜类及制品', '苣荬菜(尖叶)[取荬菜，苦麻子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (524, '蔬菜类及制品', '苜蓿籽(干)[紫苜蓿籽]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (525, '蔬菜类及制品', '茴芹(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (526, '蔬菜类及制品', '荞菜(鲜)[野荞]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (527, '蔬菜类及制品', '蒌蒿(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (528, '蔬菜类及制品', '蕨菜(鲜)[龙头菜，如意菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (529, '蔬菜类及制品', '蕨麻(干)[鹅绒委陵菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (530, '蔬菜类及制品', '枸杞菜(鲜)[枸杞头]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (531, '蔬菜类及制品', '酢浆草(鲜)[酸酸草，酸溜溜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (532, '蔬菜类及制品', '苦苣菜[苦菜、天精菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (533, '蔬菜类及制品', '苜蓿[草头、金花菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (534, '蔬菜类及制品', '鱼腥草(叶)[蕺菜、臭菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (535, '蔬菜类及制品', '鱼腥草(根)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (536, '蔬菜类及制品', '刺五加尖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (537, '蔬菜类及制品', '枸杞叶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (538, '蔬菜类及制品', '灰灰菜(干，藜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (539, '蔬菜类及制品', '荆芥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (540, '蔬菜类及制品', '金针菜(鲜)[黄花菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (541, '蔬菜类及制品', '蕨菜(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (542, '蔬菜类及制品', '苦菜[节节花，拒马菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (543, '蔬菜类及制品', '香椿(鲜)[香椿芽]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (544, '蔬菜类及制品', '黄瓜(鲜)[胡瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (545, '蔬菜类及制品', '豆薯(鲜)[凉薯，地瓜，沙葛]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (546, '蔬菜类及制品', '油菜(小)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (547, '蔬菜类及制品', '毛豆(鲜)[青豆，菜用大豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (548, '蔬菜类及制品', '分葱[四季葱，菜葱]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (549, '蔬菜类及制品', '萝卜缨(白)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (550, '蔬菜类及制品', '香菜(鲜)[芫荽]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (551, '蔬菜类及制品', '槟榔芋(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (552, '蔬菜类及制品', '刺楸(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (553, '蔬菜类及制品', '胡萝卜(红)[金笋，丁香萝卜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (554, '蔬菜类及制品', '菠菜(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (555, '蔬菜类及制品', '蒜黄(黄色)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (556, '蔬菜类及制品', '冬瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (557, '蔬菜类及制品', '黄豆芽（高矿物质）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (558, '蔬菜类及制品', '豇豆（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (559, '蔬菜类及制品', '彩椒（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (560, '蔬菜类及制品', '黑豆苗（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (561, '蔬菜类及制品', '盖菜（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (562, '蔬菜类及制品', '根芹[根洋芹、球根塘蒿]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (563, '蔬菜类及制品', '青萝卜（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (564, '蔬菜类及制品', '扁豆（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (565, '蔬菜类及制品', '紫菜头（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (566, '蔬菜类及制品', '丝瓜（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (567, '蔬菜类及制品', '辣椒(青，尖)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (568, '蔬菜类及制品', '茄子(紫皮，长)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (569, '蔬菜类及制品', '豌豆苗（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (570, '蔬菜类及制品', '绿豆芽（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (571, '蔬菜类及制品', '酸白菜[酸菜]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (572, '蔬菜类及制品', '大葱（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (573, '蔬菜类及制品', '油菜（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (574, '蔬菜类及制品', '韭菜（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (575, '蔬菜类及制品', '芋头[芋艿，毛芋]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (576, '蔬菜类及制品', '番茄[西红柿]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (577, '蔬菜类及制品', '藕[莲藕]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (578, '蔬菜类及制品', '洋葱(白皮，脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (579, '蔬菜类及制品', '奶白菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (580, '蔬菜类及制品', '苦瓜(鲜)[凉瓜，癞瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (581, '蔬菜类及制品', '豆瓣菜(鲜)[西洋菜，水田芥]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (582, '蔬菜类及制品', '大蒜(紫皮，鲜)[蒜头]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (583, '蔬菜类及制品', '莴笋(鲜)[莴苣]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (584, '蔬菜类及制品', '喷瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (585, '蔬菜类及制品', '山药(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (586, '蔬菜类及制品', '苦苦菜(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (587, '蔬菜类及制品', '白萝卜(鲜)[莱菔]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (588, '蔬菜类及制品', '卞萝卜[红皮萝卜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (589, '蔬菜类及制品', '红旦旦萝卜[樱桃萝卜，小水萝卜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (590, '蔬菜类及制品', '红萝卜[卞萝卜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (591, '蔬菜类及制品', '红心萝卜[心里美]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (592, '蔬菜类及制品', '花叶萝卜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (593, '蔬菜类及制品', '水萝卜[脆萝卜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (594, '蔬菜类及制品', '小水萝卜[算盘子，红皮萝卜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (595, '蔬菜类及制品', '红心萝卜[心里美]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (596, '蔬菜类及制品', '白萝卜(圆)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (597, '蔬菜类及制品', '樱桃萝卜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (598, '蔬菜类及制品', '胡萝卜(黄)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (599, '蔬菜类及制品', '胡萝卜(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (600, '蔬菜类及制品', '胡萝卜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (601, '蔬菜类及制品', '芥菜头[大头菜，水芥]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (602, '蔬菜类及制品', '苤蓝[玉蔓菁，球茎甘蓝，大头菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (603, '蔬菜类及制品', '甜菜根(鲜)[甜菜头，糖萝卜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (604, '蔬菜类及制品', '扁豆[月亮菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (605, '蔬菜类及制品', '蚕豆(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (606, '蔬菜类及制品', '刀豆(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (607, '蔬菜类及制品', '豆角', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (608, '蔬菜类及制品', '豆角(鲜，白)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (609, '蔬菜类及制品', '荷兰豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (610, '蔬菜类及制品', '龙豆(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (611, '蔬菜类及制品', '龙牙豆(鲜)[玉豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (612, '蔬菜类及制品', '四季豆[菜豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (613, '蔬菜类及制品', '豌豆(带荚，鲜)[回回豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (614, '蔬菜类及制品', '豌豆尖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (615, '蔬菜类及制品', '油豆角(鲜)[多花菜豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (616, '蔬菜类及制品', '垅船豆(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (617, '蔬菜类及制品', '芸豆(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (618, '蔬菜类及制品', '豇豆(长)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (619, '蔬菜类及制品', '四季豆[菜豆、芸豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (620, '蔬菜类及制品', '四棱豆[杨桃豆、翅豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (621, '蔬菜类及制品', '甜脆荷兰豆[甜豆]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (622, '蔬菜类及制品', '发芽豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (623, '蔬菜类及制品', '黄豆芽', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (624, '蔬菜类及制品', '茄子(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (625, '蔬菜类及制品', '茄子(绿皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (626, '蔬菜类及制品', '茄子(圆)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (627, '蔬菜类及制品', '番茄(整个，罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (628, '蔬菜类及制品', '奶柿子[西红柿]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (629, '蔬菜类及制品', '辣椒(红，尖，干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (630, '蔬菜类及制品', '辣椒(红，小)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (631, '蔬菜类及制品', '甜椒(脱水)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (632, '蔬菜类及制品', '葫子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (633, '蔬菜类及制品', '茄子(白皮，长)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (634, '蔬菜类及制品', '茄子(紫皮，圆)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (635, '菌藻类', '海鲜菇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (636, '菌藻类', '金钱菇(干)（大）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (637, '菌藻类', '鸡腿菇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (638, '菌藻类', '蘑菇(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (639, '菌藻类', '松茸菇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (640, '菌藻类', '玉竹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (641, '菌藻类', '金针菇(鲜)[益智菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (642, '菌藻类', '金针菇(罐装)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (643, '菌藻类', '口蘑(白蘑)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (644, '菌藻类', '木耳(干)[黑木耳，云耳]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (645, '菌藻类', '木耳(水发)[黑木耳，云耳]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (646, '菌藻类', '平菇[糙皮侧耳，青蘑]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (647, '菌藻类', '普中红蘑(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (648, '菌藻类', '双孢蘑菇[洋蘑菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (649, '菌藻类', '松蘑(干)[松口蘑，松茸]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (650, '菌藻类', '香菇(鲜)[香蕈，冬菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (651, '菌藻类', '香菇(干)[香蕈，冬菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (652, '菌藻类', '香杏丁蘑(干，大)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (653, '菌藻类', '香杏片口蘑(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (654, '菌藻类', '羊肚菌(干)[干狼肚]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (655, '菌藻类', '银耳(干)[白木耳]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (656, '菌藻类', '珍珠白蘑(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (657, '菌藻类', '榛蘑(半干)[假蜜环菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (658, '菌藻类', '榛蘑(水发)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (659, '菌藻类', '白蘑菇[双孢蘑菇、养蘑菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (660, '菌藻类', '北风菌[荷叶离褶伞、一窝羊]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (661, '菌藻类', '茶树菇(干)[柱状田头菇、茶薪菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (662, '菌藻类', '干巴菌', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (663, '菌藻类', '红奶浆菌[多汁乳菇、谷熟菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (664, '菌藻类', '黄伞菇(干)[多脂鳞伞、黄丝菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (665, '菌藻类', '鸡腿菇(干)[毛头鬼伞]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (666, '菌藻类', '鸡油菌[黄丝菌、杏菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (667, '菌藻类', '鸡枞[蚁枞、伞把菇、鸡枞菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (668, '菌藻类', '鸡枞(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (669, '菌藻类', '鸡枞(油炸)[油鸡枞]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (670, '菌藻类', '鸡枞花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (671, '菌藻类', '牛肝菌(白)[美味牛肝菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (672, '菌藻类', '牛肝菌(白、干)[美味牛肝菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (673, '菌藻类', '牛肝菌(黑)[铜色牛肝菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (674, '菌藻类', '牛肝菌(鲜)[黄皮牛肝菌，黄皮疣柄牛肝菌、黄赖头]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (675, '菌藻类', '乳牛肝菌(干)[粘盖牛肝菌、松树菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (676, '菌藻类', '牛眼镜菌(鲜)[马勃菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (677, '菌藻类', '平菇[糙皮侧耳、青蘑]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (678, '菌藻类', '青头菌[变绿红菇、绿菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (679, '菌藻类', '松蘑(干)[松茸、松口蘑]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (680, '菌藻类', '血红菇(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (681, '菌藻类', '元蘑(干)[亚侧耳、冬蘑、黄蘑]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (682, '菌藻类', '竹荪(干)[竹笙、竹参]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (683, '菌藻类', '蛹虫草(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (684, '菌藻类', '发菜(干)[仙菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (685, '菌藻类', '海带(鲜)[江白菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (686, '菌藻类', '海带[江白菜，昆布]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (687, '菌藻类', '海带(浸)[江白菜，昆布]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (688, '菌藻类', '海冻菜(干)[石花菜，冻菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (689, '菌藻类', '琼脂[紫菜胶洋粉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (690, '菌藻类', '苔菜(干)[苔条，条浒苔]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (691, '菌藻类', '紫菜(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (692, '菌藻类', '螺旋藻(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (693, '菌藻类', '裙带菜(干)[海芥菜、海木耳]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (694, '菌藻类', '海带菜(鲜，姑香牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (695, '菌藻类', '地衣(水浸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (696, '菌藻类', '草菇[大黑头细花草、稻菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (697, '菌藻类', '草菇[大黑头细花草、稻菇]（江西）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (698, '菌藻类', '蘑菇(鲜蘑)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (699, '菌藻类', '黄蘑(干)（吉林）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (700, '菌藻类', '杏鲍菇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (701, '菌藻类', '榛蘑(干)[小蜜环菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (702, '菌藻类', '大红菇(干)[草质红菇]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (703, '菌藻类', '冬菇(干)[毛柄金线菌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (704, '菌藻类', '猴头菇(罐装)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (705, '菌藻类', '黄蘑(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (706, '菌藻类', '黄蘑(水发)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (707, '水果类及制品', '柑桔', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (708, '水果类及制品', '甘美西瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (709, '水果类及制品', '蓝莓', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (710, '水果类及制品', '梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (711, '水果类及制品', '莲雾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (712, '水果类及制品', '榴莲肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (713, '水果类及制品', '米蕉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (714, '水果类及制品', '蜜桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (715, '水果类及制品', '蜜枣(无核)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (716, '水果类及制品', '啤梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (717, '水果类及制品', '苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (718, '水果类及制品', '葡萄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (719, '水果类及制品', '桑葚', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (720, '水果类及制品', '砂糖桔', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (721, '水果类及制品', '神湾小菠萝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (722, '水果类及制品', '石榴', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (723, '水果类及制品', '糖心苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (724, '水果类及制品', '桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (725, '水果类及制品', '香蕉[甘蕉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (726, '水果类及制品', '西瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (727, '水果类及制品', '印度苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (728, '水果类及制品', '祝光苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (729, '水果类及制品', '倭锦苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (730, '水果类及制品', '苹果(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (731, '水果类及制品', '梨(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (732, '水果类及制品', '梨(巴梨)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (733, '水果类及制品', '长把梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (734, '水果类及制品', '红肖梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (735, '水果类及制品', '锦丰梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (736, '水果类及制品', '京白梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (737, '水果类及制品', '库尔勒香梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (738, '水果类及制品', '莱阳梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (739, '水果类及制品', '马蹄黄梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (740, '水果类及制品', '明月梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (741, '水果类及制品', '木梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (742, '水果类及制品', '苹果梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (743, '水果类及制品', '软梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (744, '水果类及制品', '苏梅梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (745, '水果类及制品', '苏木梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (746, '水果类及制品', '酥梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (747, '水果类及制品', '酸梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (748, '水果类及制品', '香梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (749, '水果类及制品', '雪花梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (750, '水果类及制品', '鸭广梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (751, '水果类及制品', '鸭梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (752, '水果类及制品', '早酥梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (753, '水果类及制品', '冬果梨(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (754, '水果类及制品', '梨(糖水罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (755, '水果类及制品', '红果[山里红，大山楂]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (756, '水果类及制品', '红果(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (757, '水果类及制品', '海棠果[楸子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (758, '水果类及制品', '海棠(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (759, '水果类及制品', '沙果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (760, '水果类及制品', '吊蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (761, '水果类及制品', '面蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (762, '水果类及制品', '酸刺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (763, '水果类及制品', '蛇果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (764, '水果类及制品', '鳄梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (765, '水果类及制品', '桃(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (766, '水果类及制品', '白粉桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (767, '水果类及制品', '高山白桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (768, '水果类及制品', '旱久保桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (769, '水果类及制品', '桃(黄桃)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (770, '水果类及制品', '金红桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (771, '水果类及制品', '桃(久保桃)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (772, '水果类及制品', '蒲桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (773, '水果类及制品', '庆丰桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (774, '水果类及制品', '晚桃(黄)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (775, '水果类及制品', '五月鲜桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (776, '水果类及制品', '早桃(黄)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (777, '水果类及制品', '桃(糖水罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (778, '水果类及制品', '李子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (779, '水果类及制品', '李子杏', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (780, '水果类及制品', '梅[青梅]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (781, '水果类及制品', '杏', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (782, '水果类及制品', '杏(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (783, '水果类及制品', '杏干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (784, '水果类及制品', '布朗', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (785, '水果类及制品', '西梅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (786, '水果类及制品', '枣(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (787, '水果类及制品', '枣(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (788, '水果类及制品', '枣(干，大)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (789, '水果类及制品', '枣(金丝小枣)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (790, '水果类及制品', '乐陵枣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (791, '水果类及制品', '密云小枣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (792, '水果类及制品', '黑枣(无核)[乌枣]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (793, '水果类及制品', '黑枣(有核)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (794, '水果类及制品', '酒枣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (795, '水果类及制品', '冬枣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (796, '水果类及制品', '小枣(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (797, '水果类及制品', '樱桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (798, '水果类及制品', '樱桃(野，白刺)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (799, '水果类及制品', '葡萄(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (800, '水果类及制品', '红玫瑰葡萄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (801, '水果类及制品', '葡萄(巨峰)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (802, '水果类及制品', '葡萄(马奶子)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (803, '水果类及制品', '葡萄(玫瑰香)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (804, '水果类及制品', '紫葡萄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (805, '水果类及制品', '葡萄干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (806, '水果类及制品', '红提子葡萄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (807, '水果类及制品', '石榴(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (808, '水果类及制品', '石榴(红粉皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (809, '水果类及制品', '石榴(玛瑙)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (810, '水果类及制品', '石榴(青皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (811, '水果类及制品', '柿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (812, '水果类及制品', '荷柿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (813, '水果类及制品', '磨盘柿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (814, '水果类及制品', '柿饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (815, '水果类及制品', '桑葚(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (816, '水果类及制品', '桑葚(白)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (817, '水果类及制品', '桑葚(红)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (818, '水果类及制品', '桑葚(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (819, '水果类及制品', '醋栗[灯笼果]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (820, '水果类及制品', '沙棘', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (821, '水果类及制品', '无花果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (822, '水果类及制品', '中华猕猴桃[毛叶猕猴桃]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (823, '水果类及制品', '草莓[洋莓，凤阳草莓]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (824, '水果类及制品', '无花果(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (825, '水果类及制品', '橙', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (826, '水果类及制品', '福橘', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (827, '水果类及制品', '桔柑子[宽皮桂]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (828, '水果类及制品', '橘(金橘)[金枣]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (829, '水果类及制品', '芦橘', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (830, '水果类及制品', '蜜橘', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (831, '水果类及制品', '柚[文旦]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (832, '水果类及制品', '三湖红橘', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (833, '水果类及制品', '橘(四川红橘)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (834, '水果类及制品', '小叶橘', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (835, '水果类及制品', '早橘', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (836, '水果类及制品', '橘饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (837, '水果类及制品', '芭蕉[甘蕉，板蕉，牙蕉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (838, '水果类及制品', '菠萝蜜[木菠萝]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (839, '水果类及制品', '刺梨[茨梨，木梨子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (840, '水果类及制品', '番石榴[鸡矢果，番桃]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (841, '水果类及制品', '桂圆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (842, '水果类及制品', '黄皮果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (843, '水果类及制品', '荔枝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (844, '水果类及制品', '桂圆(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (845, '水果类及制品', '芒果[抹猛果，望果]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (846, '水果类及制品', '人参果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (847, '水果类及制品', '杨梅[树梅，山杨梅]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (848, '水果类及制品', '甜瓜[香瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (849, '水果类及制品', '椰子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (850, '水果类及制品', '枇杷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (851, '水果类及制品', '橄榄(白榄)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (852, '水果类及制品', '红毛丹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (853, '水果类及制品', '火龙果[仙蜜果、红龙果]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (854, '水果类及制品', '荔枝(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (855, '水果类及制品', '芒果(大头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (856, '水果类及制品', '酸木瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (857, '水果类及制品', '蒲桃[香果、水石榴]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (858, '水果类及制品', '山竹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (859, '水果类及制品', '白兰瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (860, '水果类及制品', '哈蜜瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (861, '水果类及制品', '灵蜜瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (862, '水果类及制品', '麻醉瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (863, '水果类及制品', '杨桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (864, '水果类及制品', '榴莲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (865, '水果类及制品', '西瓜(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (866, '水果类及制品', '西瓜(京欣一号)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (867, '水果类及制品', '西瓜(郑州三号)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (868, '水果类及制品', '西瓜(忠于6号，黑皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (869, '水果类及制品', '子瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (870, '水果类及制品', '余柑子[油柑子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (871, '水果类及制品', '白金瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (872, '水果类及制品', '桂圆肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (873, '水果类及制品', '桂圆(干)（广东）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (874, '水果类及制品', '黑醋栗[黑加仑]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (875, '水果类及制品', '小西瓜[地雷瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (876, '水果类及制品', '蜜枣[椰枣]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (877, '水果类及制品', '雪梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (878, '水果类及制品', '木瓜[番木瓜]（云南）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (879, '水果类及制品', '葡萄柚[西柚]（中国台湾）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (880, '水果类及制品', '葡萄柚[西柚]（以色列）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (881, '水果类及制品', '香蕉(红皮)（泰国）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (882, '水果类及制品', '香蕉(红皮)（海南）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (883, '水果类及制品', '蜜桃（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (884, '水果类及制品', '香蕉[甘蕉]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (885, '水果类及制品', '菠萝[凤梨，地菠萝]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (886, '水果类及制品', '木瓜[番木瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (887, '水果类及制品', '黄河蜜瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (888, '水果类及制品', '酸枣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (889, '水果类及制品', '柠檬', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (890, '水果类及制品', '冬果梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (891, '水果类及制品', '红玉苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (892, '水果类及制品', '金塔寺瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (893, '水果类及制品', '鹅黄梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (894, '水果类及制品', '苹果(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (895, '水果类及制品', '伏苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (896, '水果类及制品', '国光苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (897, '水果类及制品', '旱苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (898, '水果类及制品', '红富士苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (899, '水果类及制品', '红香蕉苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (900, '水果类及制品', '红星苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (901, '水果类及制品', '红元帅苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (902, '水果类及制品', '黄香蕉苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (903, '水果类及制品', '黄元帅苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (904, '水果类及制品', '金元帅苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (905, '水果类及制品', '紫酥梨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (906, '水果类及制品', '青香蕉苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (907, '水果类及制品', '秋里蒙苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (908, '水果类及制品', '香玉苹果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (909, '坚果、种子类', '巴达木', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (910, '谷类及制品', '葵花籽仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (911, '坚果、种子类', '莲蓉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (912, '坚果、种子类', '蔓越莓', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (913, '坚果、种子类', '山核桃(熟)[小核桃]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (914, '坚果、种子类', '夏威夷果（生）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (915, '坚果、种子类', '腰果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (916, '坚果、种子类', '椰蓉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (917, '坚果、种子类', '栗子(熟)[板栗]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (918, '坚果、种子类', '松子(炒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (919, '坚果、种子类', '松子仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (920, '坚果、种子类', '杏仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (921, '坚果、种子类', '杏仁(大杏仁)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (922, '坚果、种子类', '杏仁(炒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (923, '坚果、种子类', '杏仁(原味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (924, '坚果、种子类', '杏仁(漂白后)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (925, '坚果、种子类', '栗子(干)[板栗]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (926, '坚果、种子类', '杏仁(过油炸干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (927, '坚果、种子类', '杏仁(烤干，不加盐)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (928, '坚果、种子类', '杏仁(烤干，加盐)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (929, '坚果、种子类', '橡实[橡子，青冈子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (930, '坚果、种子类', '榛子(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (931, '坚果、种子类', '榛子(炒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (932, '坚果、种子类', '栗子仁(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (933, '坚果、种子类', '松子(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (934, '坚果、种子类', '杏仁(熟，带壳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (935, '坚果、种子类', '杏仁(熟，去壳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (936, '坚果、种子类', '腰果(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (937, '坚果、种子类', '榛子(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (938, '坚果、种子类', '榛子仁(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (939, '坚果、种子类', '开心果(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (940, '坚果、种子类', '香榧(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (941, '坚果、种子类', '胡麻籽', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (942, '坚果、种子类', '花生(鲜)[落花生，长生果]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (943, '坚果、种子类', '花生(炒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (944, '坚果、种子类', '花生仁(生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (945, '坚果、种子类', '花生仁(炒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (946, '坚果、种子类', '葵花子(生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (947, '坚果、种子类', '葵花子(炒，咸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (948, '坚果、种子类', '葵花子仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (949, '坚果、种子类', '莲子(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (950, '坚果、种子类', '莲子(糖水罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (951, '坚果、种子类', '南瓜子(炒)[白瓜子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (952, '坚果、种子类', '南瓜子仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (953, '坚果、种子类', '西瓜子(炒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (954, '坚果、种子类', '西瓜子仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (955, '坚果、种子类', '芝麻子(白)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (956, '坚果、种子类', '芝麻子(黑)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (957, '坚果、种子类', '芡实米(鲜)[鸡头米]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (958, '坚果、种子类', '芡实米(干)[鸡头米]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (959, '坚果、种子类', '花生(烤，勤俭牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (960, '坚果、种子类', '花生(烤，密日兴牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (961, '坚果、种子类', '花生仁(油炸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (962, '坚果、种子类', '葵花子(熟，奶油香)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (963, '坚果、种子类', '葵花子(熟，原味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (964, '坚果、种子类', '南瓜子(熟)[白瓜子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (965, '坚果、种子类', '西瓜子(熟)[黑瓜子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (966, '坚果、种子类', '栗子[板栗]（河北邢台）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (967, '坚果、种子类', '栗子[板栗]（北京密云）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (968, '坚果、种子类', '栗子[板栗]（河南）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (969, '坚果、种子类', '栗子[板栗]（山东）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (970, '坚果、种子类', '松子(生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (971, '坚果、种子类', '山核桃(熟)[小核桃]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (972, '坚果、种子类', '核桃(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (973, '坚果、种子类', '西瓜子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (974, '坚果、种子类', '栗子[板栗]（河北迁西）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (975, '坚果、种子类', '白果(干)[银杏]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (976, '坚果、种子类', '菠萝蜜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (977, '坚果、种子类', '核桃(干)[胡桃]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (978, '坚果、种子类', '毛核桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (979, '坚果、种子类', '山核桃(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (980, '坚果、种子类', '栗子(鲜)[板栗]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (981, '畜肉类及制品', '叉烧肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (982, '畜肉类及制品', '烤肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (983, '畜肉类及制品', '牛百叶(黑)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (984, '畜肉类及制品', '牛骨（腿、脊、排）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (985, '畜肉类及制品', '牛肉(肥瘦)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (986, '畜肉类及制品', '牛肉(瘦)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (987, '畜肉类及制品', '沙肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (988, '畜肉类及制品', '羊肉(肥瘦)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (989, '畜肉类及制品', '猪肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (990, '畜肉类及制品', '猪脊骨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (991, '畜肉类及制品', '猪肉(里脊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (992, '畜肉类及制品', '猪肉松', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (993, '畜肉类及制品', '猪肉(五花肉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (994, '畜肉类及制品', '猪舌[口条]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (995, '畜肉类及制品', '猪肾[猪腰子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (996, '畜肉类及制品', '猪小排', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (997, '畜肉类及制品', '猪头皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (998, '畜肉类及制品', '猪肉(前臀尖，杜长大猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (999, '畜肉类及制品', '猪肉(前臀尖，杂粮猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1000, '畜肉类及制品', '猪肉(后臀尖，杜长大猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1001, '畜肉类及制品', '猪肉(后臀尖，杂粮猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1002, '畜肉类及制品', '猪肉(硬肋，杜长大猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1003, '畜肉类及制品', '猪肉(硬肋，杂粮猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1004, '畜肉类及制品', '猪肉(通脊，杜长大猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1005, '畜肉类及制品', '猪肉(肋条肉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1006, '畜肉类及制品', '猪肉(通脊，杂粮猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1007, '畜肉类及制品', '猪小排(杜长大猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1008, '畜肉类及制品', '猪小排(杂粮猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1009, '畜肉类及制品', '猪腿肉(藏香猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1010, '畜肉类及制品', '猪肺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1011, '畜肉类及制品', '猪脑', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1012, '畜肉类及制品', '猪脾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1013, '畜肉类及制品', '猪肾(fat 8g)[猪腰子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1014, '畜肉类及制品', '猪小肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1015, '畜肉类及制品', '猪心', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1016, '畜肉类及制品', '猪血', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1017, '畜肉类及制品', '猪肾(fat 2g)[猪腰子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1018, '畜肉类及制品', '宫爆肉丁(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1019, '畜肉类及制品', '酱汁肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1020, '畜肉类及制品', '腊肉(生,fat 39g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1021, '畜肉类及制品', '卤猪杂', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1022, '畜肉类及制品', '午餐肉(北京)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1023, '畜肉类及制品', '咸肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1024, '畜肉类及制品', '猪肉罐头(珍珠里脊丝，罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1025, '畜肉类及制品', '猪肝(卤煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1026, '畜肉类及制品', '猪肉(清蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1027, '畜肉类及制品', '猪蹄(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1028, '畜肉类及制品', '猪肘棒(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1029, '畜肉类及制品', '福建式肉松', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1030, '畜肉类及制品', '老年保健肉松', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1031, '畜肉类及制品', '太仓肉松', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1032, '畜肉类及制品', '火腿心全精肉(雪舫蒋牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1033, '畜肉类及制品', '火腿心肉(生，金云牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1034, '畜肉类及制品', '腊肉(生，fat 68g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1035, '畜肉类及制品', '酱排骨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1036, '畜肉类及制品', '猪肉罐头(香糟块肉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1037, '畜肉类及制品', '猪里脊(熏烤小里脊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1038, '畜肉类及制品', '猪肉脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1039, '畜肉类及制品', '肉酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1040, '畜肉类及制品', '扒猪脸', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1041, '畜肉类及制品', '酱肘子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1042, '畜肉类及制品', '火腿肉(藏香猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1043, '畜肉类及制品', '风干肉(藏香猪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1044, '畜肉类及制品', '茶肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1045, '畜肉类及制品', '大腊肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1046, '畜肉类及制品', '大肉肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1047, '畜肉类及制品', '蛋清肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1048, '畜肉类及制品', '儿童肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1049, '畜肉类及制品', '风干肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1050, '畜肉类及制品', '广东香肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1051, '畜肉类及制品', '红果肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1052, '畜肉类及制品', '火腿肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1053, '畜肉类及制品', '腊肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1054, '畜肉类及制品', '松江肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1055, '畜肉类及制品', '蒜肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1056, '畜肉类及制品', '香肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1057, '畜肉类及制品', '香肠(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1058, '畜肉类及制品', '火腿肠(小红肠)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1059, '畜肉类及制品', '火腿肠(小泥肠)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1060, '畜肉类及制品', '午餐肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1061, '畜肉类及制品', '午餐肚', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1062, '畜肉类及制品', '火腿(fat 27g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1063, '畜肉类及制品', '金华火腿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1064, '畜肉类及制品', '火腿肠(圆腿)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1065, '畜肉类及制品', '脆皮肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1066, '畜肉类及制品', '热狗肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1067, '畜肉类及制品', '火腿肠(双汇牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1068, '畜肉类及制品', '火腿(fat 3g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1069, '畜肉类及制品', '火腿(宣威牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1070, '畜肉类及制品', '三明治火腿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1071, '畜肉类及制品', '午餐肉(上海梅林牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1072, '畜肉类及制品', '牛肉(代表值，fat 9g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1073, '畜肉类及制品', '牛肉(肋条)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1074, '畜肉类及制品', '牛肉(后腿)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1075, '畜肉类及制品', '牛肉(后腱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1076, '畜肉类及制品', '牛肉(里脊肉)[牛柳]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1077, '畜肉类及制品', '牛肉(前腿)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1078, '畜肉类及制品', '牛肉(前腱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1079, '畜肉类及制品', '牛肉(代表值，瘦，fat 3g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1080, '畜肉类及制品', '牛蹄筋(生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1081, '畜肉类及制品', '牛蹄筋(泡发)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1082, '畜肉类及制品', '牛肉(背部肉)[上脑]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1083, '畜肉类及制品', '牛肉(臀部肉)[紫盖、白板]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1084, '畜肉类及制品', '牛肉(肩部肉)[肩肉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1085, '畜肉类及制品', '牛肉(胸部肉)[牛胸]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1086, '畜肉类及制品', '牛肉(腹部肉)[牛腩]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1087, '畜肉类及制品', '牛肉(股内肉)[针扒、米龙、黄瓜条]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1088, '畜肉类及制品', '牛肉(小腿肉)[牛展、牛键子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1089, '畜肉类及制品', '牦牛肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1090, '畜肉类及制品', '牦牛牛腱肉(冻，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1091, '畜肉类及制品', '牦牛牛霖肉(冻，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1092, '畜肉类及制品', '牛鞭(泡发)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1093, '畜肉类及制品', '牛大肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1094, '畜肉类及制品', '牛肚', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1095, '畜肉类及制品', '牛肺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1096, '畜肉类及制品', '牛肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1097, '畜肉类及制品', '牛脑', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1098, '畜肉类及制品', '牛舌', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1099, '畜肉类及制品', '牛肾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1100, '畜肉类及制品', '牛心', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1101, '畜肉类及制品', '酱牛肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1102, '畜肉类及制品', '煨牛肉(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1103, '畜肉类及制品', '牛肉干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1104, '畜肉类及制品', '咖哩牛肉干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1105, '畜肉类及制品', '牛肉松', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1106, '畜肉类及制品', '牛肉(酱，五香)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1107, '畜肉类及制品', '牛肉(清香)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1108, '畜肉类及制品', '牛键子(香叶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1109, '畜肉类及制品', '牛肉干(长富牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1110, '畜肉类及制品', '牛肉干(沙爹牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1111, '畜肉类及制品', '羊肉(代表值，fat 7g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1112, '畜肉类及制品', '羊肉(冻)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1113, '畜肉类及制品', '羊肉(后腿，带骨)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1114, '畜肉类及制品', '羊肉(颈)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1115, '畜肉类及制品', '羊肉(里脊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1116, '畜肉类及制品', '羊肉(前腿，fat 3g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1117, '畜肉类及制品', '羊肉(青羊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1118, '畜肉类及制品', '羊肉(胸脯)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1119, '畜肉类及制品', '山羊肉(生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1120, '畜肉类及制品', '羊蹄筋(生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1121, '畜肉类及制品', '羊蹄筋(泡发)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1122, '畜肉类及制品', '羊肉(上脑)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1123, '畜肉类及制品', '羊肉(腰窝)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1124, '畜肉类及制品', '羊肉片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1125, '畜肉类及制品', '羊大肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1126, '畜肉类及制品', '羊肚', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1127, '畜肉类及制品', '羊肺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1128, '畜肉类及制品', '羊脑', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1129, '畜肉类及制品', '羊舌', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1130, '畜肉类及制品', '羊肾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1131, '畜肉类及制品', '羊心', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1132, '畜肉类及制品', '羊血', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1133, '畜肉类及制品', '腊羊肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1134, '畜肉类及制品', '羊肉(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1135, '畜肉类及制品', '羊肉串(电烤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1136, '畜肉类及制品', '羊肉串(烤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1137, '畜肉类及制品', '羊肉串(炸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1138, '畜肉类及制品', '羊肉干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1139, '畜肉类及制品', '羊肉(羊肉手抓)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1140, '畜肉类及制品', '山羊肉(酱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1141, '畜肉类及制品', '烧羊肉(五香)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1142, '畜肉类及制品', '羊肉串(生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1143, '畜肉类及制品', '驴肉(瘦)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1144, '畜肉类及制品', '驴鞭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1145, '畜肉类及制品', '驴肉(酱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1146, '畜肉类及制品', '驴肉(卤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1147, '畜肉类及制品', '驴肉(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1148, '畜肉类及制品', '驴肉(五香)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1149, '畜肉类及制品', '马肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1150, '畜肉类及制品', '马心', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1151, '畜肉类及制品', '马肉(卤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1152, '畜肉类及制品', '狗肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1153, '畜肉类及制品', '骆驼蹄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1154, '畜肉类及制品', '骆驼掌', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1155, '畜肉类及制品', '兔肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1156, '畜肉类及制品', '兔肉(野)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1157, '畜肉类及制品', '鹿肉(养殖梅花鹿)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1158, '畜肉类及制品', '牛肉(膝圆肉)[和尚头]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1159, '畜肉类及制品', '牛肉(里脊肉)[牛柳]（河北）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1160, '畜肉类及制品', '腊肉(培根)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1161, '畜肉类及制品', '方腿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1162, '畜肉类及制品', '羊肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1163, '畜肉类及制品', '猪肘棒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1164, '畜肉类及制品', '猪肚（河北）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1165, '畜肉类及制品', '牛蹄筋(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1166, '畜肉类及制品', '猪肉(肥瘦)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1167, '畜肉类及制品', '猪肝（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1168, '畜肉类及制品', '猪肉(里脊)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1169, '畜肉类及制品', '叉烧肉（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1170, '畜肉类及制品', '猪舌[口条]（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1171, '畜肉类及制品', '牛百叶(黑)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1172, '畜肉类及制品', '羊肉(前腿)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1173, '畜肉类及制品', '羊肉(后腿)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1174, '畜肉类及制品', '猪肉(后臀尖)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1175, '畜肉类及制品', '猪肉(腿)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1176, '畜肉类及制品', '羊肉(瘦)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1177, '畜肉类及制品', '猪肚', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1178, '畜肉类及制品', '猪大排', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1179, '畜肉类及制品', '猪皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1180, '畜肉类及制品', '猪肉(肥,fat 89g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1181, '畜肉类及制品', '猪肉(后肘)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1182, '畜肉类及制品', '猪肉(奶脯)[软五花，猪夹心]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1183, '畜肉类及制品', '猪肉(奶面)[硬五花]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1184, '畜肉类及制品', '猪肉(前肘)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1185, '畜肉类及制品', '猪肉(瘦，fat 8g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1186, '畜肉类及制品', '猪肉(瘦)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1187, '畜肉类及制品', '猪肉(fat 12g)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1188, '畜肉类及制品', '猪肉(猪脖)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1189, '畜肉类及制品', '猪大肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1190, '畜肉类及制品', '猪耳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1191, '畜肉类及制品', '猪蹄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1192, '畜肉类及制品', '猪蹄筋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1193, '禽肉类及制品', '鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1194, '禽肉类及制品', '鸡扒肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1195, '禽肉类及制品', '鸡翅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1196, '禽肉类及制品', '鸡翅根', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1197, '禽肉类及制品', '鸡翅中', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1198, '禽肉类及制品', '鸡柳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1199, '禽肉类及制品', '鸡腿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1200, '禽肉类及制品', '鸡胸脯肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1201, '禽肉类及制品', '烤鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1202, '禽肉类及制品', '乌鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1203, '禽肉类及制品', '西洋鸭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1204, '禽肉类及制品', '鸭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1205, '禽肉类及制品', '鱼头', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1206, '禽肉类及制品', '鸡血', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1207, '禽肉类及制品', '鸡肫[鸡胗]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1208, '禽肉类及制品', '扒鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1209, '禽肉类及制品', '炸鸡块[肯德基]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1210, '禽肉类及制品', '卤煮鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1211, '禽肉类及制品', '瓦罐鸡汤(肉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1212, '禽肉类及制品', '鸡肉松', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1213, '禽肉类及制品', '扒鸡(五香脱骨)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1214, '禽肉类及制品', '童子鸡(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1215, '禽肉类及制品', '鸭(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1216, '禽肉类及制品', '公麻鸭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1217, '禽肉类及制品', '母麻鸭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1218, '禽肉类及制品', '鸭皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1219, '禽肉类及制品', '鸭翅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1220, '禽肉类及制品', '鸭掌', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1221, '禽肉类及制品', '鸭肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1222, '禽肉类及制品', '鸭肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1223, '禽肉类及制品', '鸭肝(公麻鸭)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1224, '禽肉类及制品', '鸭肝(母麻鸭)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1225, '禽肉类及制品', '鸭舌[鸭条]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1226, '禽肉类及制品', '鸭心', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1227, '禽肉类及制品', '鸭血(白鸭)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1228, '禽肉类及制品', '鸭血(公麻鸭)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1229, '禽肉类及制品', '鸭血(母麻鸭)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1230, '禽肉类及制品', '鸭胰', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1231, '禽肉类及制品', '鸭肫', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1232, '禽肉类及制品', '鸭肫(公麻鸭)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1233, '禽肉类及制品', '鸭肫(母麻鸭)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1234, '禽肉类及制品', '鸭豉片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1235, '禽肉类及制品', '北京烤鸭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1236, '禽肉类及制品', '北京填鸭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1237, '禽肉类及制品', '红烧鸭(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1238, '禽肉类及制品', '酱鸭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1239, '禽肉类及制品', '酱鸭(加梅菜，罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1240, '禽肉类及制品', '盐水鸭(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1241, '禽肉类及制品', '烤鸭(老唐牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1242, '禽肉类及制品', '烤鸭(全聚德牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1243, '禽肉类及制品', '鹅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1244, '禽肉类及制品', '鸡(乌骨鸡)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1245, '禽肉类及制品', '鹅肫', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1246, '禽肉类及制品', '鹅血', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1247, '禽肉类及制品', '烧鹅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1248, '禽肉类及制品', '腊鹅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1249, '禽肉类及制品', '火鸡腿', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1250, '禽肉类及制品', '火鸡胸脯肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1251, '禽肉类及制品', '火鸡肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1252, '禽肉类及制品', '火鸡肫', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1253, '禽肉类及制品', '火鸡腿(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1254, '禽肉类及制品', '鸽', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1255, '禽肉类及制品', '鹌鹑', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1256, '禽肉类及制品', '乳鸽', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1257, '禽肉类及制品', '乳鸽(红烧)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1258, '禽肉类及制品', '鸡爪', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1259, '禽肉类及制品', '鸭胸脯肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1260, '禽肉类及制品', '烤鸡（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1261, '禽肉类及制品', '鸡翅（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1262, '禽肉类及制品', '鸡腿（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1263, '禽肉类及制品', '鸡胸脯肉（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1264, '禽肉类及制品', '鹅肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1265, '禽肉类及制品', '瓦罐鸡汤(汤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1266, '禽肉类及制品', '鸡(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1267, '禽肉类及制品', '鸡(土鸡，家养)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1268, '禽肉类及制品', '母鸡(一年内)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1269, '禽肉类及制品', '肉鸡(肥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1270, '禽肉类及制品', '华青鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1271, '禽肉类及制品', '沙鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1272, '禽肉类及制品', '鸡块(带浆粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1273, '禽肉类及制品', '野山鸡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1274, '禽肉类及制品', '鸡肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1275, '禽肉类及制品', '鸡肝(肉鸡)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1276, '禽肉类及制品', '鸡心', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1277, '乳类及制品', '卡士佐餐风味发酵乳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1278, '乳类及制品', '牛乳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1279, '乳类及制品', '牛乳(强化VA，VD)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1280, '乳类及制品', '全脂加糖奶粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1281, '乳类及制品', '学生奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1282, '乳类及制品', '芝士', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1283, '乳类及制品', '纯牛奶(全脂，乐百氏牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1284, '乳类及制品', '纯牛奶(全脂，帕玛拉特牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1285, '乳类及制品', '纯牛奶(全脂，三元牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1286, '乳类及制品', '纯牛奶(全脂，完达山牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1287, '乳类及制品', '纯牛奶(全脂，龙丹牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1288, '乳类及制品', '鲜驴奶(华麒牌，冻)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1289, '乳类及制品', '纯牛奶(全脂，蒙牛牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1290, '乳类及制品', '纯牛奶(全脂，新南洋牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1291, '乳类及制品', '纯牛奶(全脂，帕玛拉特)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1292, '乳类及制品', '纯牛奶(全脂，伊利牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1293, '乳类及制品', '纯牛奶(全脂，爱尔兰金凯利全脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1294, '乳类及制品', '纯牛奶(全脂，澳大利亚澳田纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1295, '乳类及制品', '纯牛奶(全脂，比利时纯牧牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1296, '乳类及制品', '纯牛奶(全脂，波兰美波纯全脂纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1297, '乳类及制品', '纯牛奶(全脂，丹麦爱氏晨曦有机全脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1298, '乳类及制品', '纯牛奶(全脂，德国爱氏晨曦纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1299, '乳类及制品', '纯牛奶(全脂，德国甘蒂牧场纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1300, '乳类及制品', '纯牛奶(全脂，法国得乐思全脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1301, '乳类及制品', '纯牛奶(全脂，光明纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1302, '乳类及制品', '纯牛奶(全脂，光明优+高品质纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1303, '乳类及制品', '纯牛奶(全脂，广泽澳醇纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1304, '乳类及制品', '纯牛奶(全脂，花园牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1305, '乳类及制品', '纯牛奶(全脂，辉山纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1306, '乳类及制品', '纯牛奶(全脂，龙丹松花江牧场纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1307, '乳类及制品', '纯牛奶(全脂，麦趣乐牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1308, '乳类及制品', '纯牛奶(全脂，蒙牛纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1309, '乳类及制品', '纯牛奶(全脂，蒙牛特仑苏有机纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1310, '乳类及制品', '纯牛奶(全脂，明治醇壹高温杀菌乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1311, '乳类及制品', '纯牛奶(全脂，瑞士艾美全脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1312, '乳类及制品', '纯牛奶(全脂，圣牧有机纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1313, '乳类及制品', '纯牛奶(全脂，天润牌浓缩纯奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1314, '乳类及制品', '纯牛奶(全脂，完达山纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1315, '乳类及制品', '纯牛奶(全脂，西域春牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1316, '乳类及制品', '纯牛奶(全脂，夏进纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1317, '乳类及制品', '纯牛奶(全脂，现代牧业纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1318, '乳类及制品', '纯牛奶(全脂，新希望复原乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1319, '乳类及制品', '纯牛奶(全脂，新希望千岛湖牧场纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1320, '乳类及制品', '纯牛奶(全脂，伊利纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1321, '乳类及制品', '纯牛奶(全脂，伊利金典有机纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1322, '乳类及制品', '纯牛奶(全脂，意大利培兰全脂纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1323, '乳类及制品', '纯牛奶(代表值，低脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1324, '乳类及制品', '纯牛奶(低脂，帕玛拉特)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1325, '乳类及制品', '纯牛奶(低脂，澳大利亚德运部分脱脂纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1326, '乳类及制品', '纯牛奶(低脂，德国艾德牧牌部分脱脂纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1327, '乳类及制品', '纯牛奶(低脂，蒙牛特仑苏低脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1328, '乳类及制品', '纯牛奶(低脂，明治醇壹低脂肪高温杀菌乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1329, '乳类及制品', '纯牛奶(低脂，新西兰安佳低脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1330, '乳类及制品', '纯牛奶(低脂，新西兰恒天然田园低脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1331, '乳类及制品', '纯牛奶(低脂，伊利金典低脂奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1332, '乳类及制品', '纯牛奶(低脂，意大利皮尔蒙特低脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1333, '乳类及制品', '纯牛奶(代表值，脱脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1334, '乳类及制品', '纯牛奶(脱脂，帕玛拉特)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1335, '乳类及制品', '纯牛奶(脱脂，澳大利亚澳田脱脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1336, '乳类及制品', '纯牛奶(脱脂，丹麦爱氏晨曦脱脂纯牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1337, '乳类及制品', '纯牛奶(脱脂，德国甘蒂牧场脱脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1338, '乳类及制品', '纯牛奶(脱脂，新西兰安佳轻欣脱脂牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1339, '乳类及制品', '调制乳(全脂，强化VA，VD)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1340, '乳类及制品', '调制乳(全脂，草莓味，卡夫牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1341, '乳类及制品', '调制乳(全脂，巧克力味，卡夫牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1342, '乳类及制品', '调制乳(全脂，巧克力味，三元牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1343, '乳类及制品', '调制乳(全脂，学生奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1344, '乳类及制品', '调制乳(全脂，龙丹益醇核桃牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1345, '乳类及制品', '调制乳(全脂，蒙牛特仑苏醇纤牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1346, '乳类及制品', '调制乳(全脂，蒙牛珍养型零乳糖牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1347, '乳类及制品', '调制乳(全脂，完达山臻醇牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1348, '乳类及制品', '调制乳(全脂，旺仔复原乳牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1349, '乳类及制品', '调制乳(全脂，夏进炼乳牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1350, '乳类及制品', '调制乳(全脂，新西兰安佳原味进口儿童牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1351, '乳类及制品', '调制乳(全脂，新希望特浓牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1352, '乳类及制品', '调制乳(全脂，伊利舒化奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1353, '乳类及制品', '调制乳(全脂，伊利早餐奶麦香味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1354, '乳类及制品', '调制乳(低脂，强化锌、钙，帕玛拉特)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1355, '乳类及制品', '调制乳(低脂，澳大利亚德运高钙低脂奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1356, '乳类及制品', '调制乳(低脂，伊利低脂型舒化奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1357, '乳类及制品', '调制乳(低脂，伊利高钙低脂奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1358, '乳类及制品', '调制乳(脱脂，部分复原乳，澳大利亚德运高钙脱脂奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1359, '乳类及制品', '调制乳(脱脂，伊利脱脂奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1360, '乳类及制品', '鲜牛奶(代表值，全脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1361, '乳类及制品', '鲜牛奶(全脂，光明鲜牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1362, '乳类及制品', '鲜牛奶(全脂，辉山鲜博士鲜牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1363, '乳类及制品', '鲜牛奶(全脂，完达山鲜牛乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1364, '乳类及制品', '鲜牛奶(全脂，西域春牌全脂巴氏杀菌乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1365, '乳类及制品', '鲜牛奶(全脂，现代牧场鲜牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1366, '乳类及制品', '鲜牛奶(全脂，新希望千岛湖牧场鲜牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1367, '乳类及制品', '鲜牛奶(全脂，一鸣鲜牛奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1368, '乳类及制品', '羊乳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1369, '乳类及制品', '人乳(初乳，1~7天)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1370, '乳类及制品', '人乳(过渡乳，7~14天)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1371, '乳类及制品', '人乳(成熟乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1372, '乳类及制品', '鲜驴奶(冻)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1373, '乳类及制品', '鲜驼奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1374, '乳类及制品', '鲜驼奶(冻)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1375, '乳类及制品', '驼奶(旺源牌，易拉罐)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1376, '乳类及制品', '全脂奶粉(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1377, '乳类及制品', '全脂奶粉(多维奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1378, '乳类及制品', '全脂奶粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1379, '乳类及制品', '全脂奶粉(速溶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1380, '乳类及制品', '全脂奶粉(雀巢)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1381, '乳类及制品', '全脂奶粉(伊利牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1382, '乳类及制品', '全脂奶粉(红星速溶加锌奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1383, '乳类及制品', '全脂奶粉(欧世蒙牛多维高钙高铁奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1384, '乳类及制品', '全脂奶粉(雪花钙加锌调制奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1385, '乳类及制品', '全脂奶粉(雪花高钙多维调制奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1386, '乳类及制品', '全脂甜奶粉(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1387, '乳类及制品', '全脂甜奶粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1388, '乳类及制品', '全脂甜奶粉(伊利牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1389, '乳类及制品', '全脂甜奶粉(飞鹤全脂甜乳粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1390, '乳类及制品', '全脂甜奶粉(红星速溶全脂甜奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1391, '乳类及制品', '全脂甜奶粉(三元燕山牌全脂甜奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1392, '乳类及制品', '低脂奶粉(代表值，高钙高铁)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1393, '乳类及制品', '低脂奶粉(高钙高铁，雀巢)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1394, '乳类及制品', '低脂奶粉(高钙高铁，伊利牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1395, '乳类及制品', '低脂奶粉(高钙高铁，可淇牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1396, '乳类及制品', '全脂奶粉(全脂羊乳粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1397, '乳类及制品', '驴奶粉(花麒牌，西域龙驴奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1398, '乳类及制品', '驴奶粉(金驴龙奶)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1399, '乳类及制品', '驴奶粉(源西域牌，冻干特质)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1400, '乳类及制品', '驼奶粉(花麒牌，西域龙驼奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1401, '乳类及制品', '驼奶粉(天山牧歌牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1402, '乳类及制品', '驼奶粉(旺源牌，全脂驼乳粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1403, '乳类及制品', '儿童配方奶粉(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1404, '乳类及制品', '儿童配方奶粉(安儿健A+，美赞臣)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1405, '乳类及制品', '儿童配方奶粉(适体健，美赞臣)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1406, '乳类及制品', '儿童配方奶粉(惠氏)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1407, '乳类及制品', '儿童配方奶粉(可淇牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1408, '乳类及制品', '儿童配方奶粉(完达山牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1409, '乳类及制品', '儿童配方奶粉(贝因美特选幼童配方奶粉4阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1410, '乳类及制品', '儿童配方奶粉(多美滋优阶儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1411, '乳类及制品', '儿童配方奶粉(惠氏金装学儿乐学龄前儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1412, '乳类及制品', '儿童配方奶粉(美素佳儿GOLD金装儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1413, '乳类及制品', '儿童配方奶粉(美赞臣安儿健儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1414, '乳类及制品', '儿童配方奶粉(明治珍爱童儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1415, '乳类及制品', '儿童配方奶粉(欧世蒙牛金装佳智学龄前儿童特殊配方奶粉4阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1416, '乳类及制品', '儿童配方奶粉(雀巢能恩全进口奶源儿童配方奶粉4)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1417, '乳类及制品', '儿童配方奶粉(三元爱益儿童成长配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1418, '乳类及制品', '儿童配方奶粉(完达山4段儿童奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1419, '乳类及制品', '儿童配方奶粉(完达山金装元乳4段儿童奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1420, '乳类及制品', '儿童配方奶粉(雪花学生特殊配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1421, '乳类及制品', '儿童配方奶粉(雅培金装喜康宝儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1422, '乳类及制品', '儿童配方奶粉(雅士利儿童奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1423, '乳类及制品', '儿童配方奶粉(伊利儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1424, '乳类及制品', '儿童配方奶粉(伊利金领冠儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1425, '乳类及制品', '儿童配方奶粉(伊利金装儿童配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1426, '乳类及制品', '儿童配方奶粉(伊利学生营养奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1427, '乳类及制品', '孕产妇配方奶粉(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1428, '乳类及制品', '孕产妇配方奶粉(惠氏)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1429, '乳类及制品', '孕产妇配方奶粉(美赞臣)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1430, '乳类及制品', '孕产妇配方奶粉(贝因美冠军宝贝孕妈咪配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1431, '乳类及制品', '孕产妇配方奶粉(贝因美金装爱+孕妈咪配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1432, '乳类及制品', '孕产妇配方奶粉(贝因美金装爱+准妈咪配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1433, '乳类及制品', '孕产妇配方奶粉(美乐滋优阶妈妈孕产妇配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1434, '乳类及制品', '孕产妇配方奶粉(飞帆孕产妇配方乳粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1435, '乳类及制品', '孕产妇配方奶粉(合生元金装妈妈配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1436, '乳类及制品', '孕产妇配方奶粉(亨氏超金妈妈孕产妇配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1437, '乳类及制品', '孕产妇配方奶粉(惠氏爱儿乐妈妈孕产妇配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1438, '乳类及制品', '孕产妇配方奶粉(美素佳儿GOLD金装妈妈孕产妇配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1439, '乳类及制品', '孕产妇配方奶粉(美赞臣安婴妈妈孕产妇配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1440, '乳类及制品', '孕产妇配方奶粉(雀巢妈妈孕产妇奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1441, '乳类及制品', '孕产妇配方奶粉(雀巢妈妈孕产妇营养配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1442, '乳类及制品', '孕产妇配方奶粉(三元爱力优妈妈配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1443, '乳类及制品', '孕产妇配方奶粉(圣元优博妈咪孕产妇配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1444, '乳类及制品', '孕产妇配方奶粉(完达山妈咪配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1445, '乳类及制品', '孕产妇配方奶粉(雅培妈妈喜康素金装孕产妇配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1446, '乳类及制品', '孕产妇配方奶粉(雅士利能慧金装孕产妇奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1447, '乳类及制品', '孕产妇配方奶粉(伊利金领冠妈妈配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1448, '乳类及制品', '孕产妇配方奶粉(伊利孕妇奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1449, '乳类及制品', '孕产妇配方奶粉(美可高特孕产妇配方羊奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1450, '乳类及制品', '中老年配方奶粉(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1451, '乳类及制品', '中老年配方奶粉(可淇牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1452, '乳类及制品', '中老年配方奶粉(雀巢)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1453, '乳类及制品', '中老年配方奶粉(森永牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1454, '乳类及制品', '中老年配方奶粉(三元爱益中老年配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1455, '乳类及制品', '中老年配方奶粉(雪花中老年特殊配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1456, '乳类及制品', '中老年配方奶粉(雪花中老年营养奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1457, '乳类及制品', '酸奶(代表值，全脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1458, '乳类及制品', '酸奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1459, '乳类及制品', '酸奶(脱脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1460, '乳类及制品', '酸奶(低脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1461, '乳类及制品', '酸奶(果料)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1462, '乳类及制品', '酸奶(橘味，脱脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1463, '乳类及制品', '酸奶(调味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1464, '乳类及制品', '酸奶(果粒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1465, '乳类及制品', '酸奶(全脂，美多鲜全脂果粒，草莓果粒/覆盆子果粒、桃果粒/西番莲汁/菠萝果粒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1466, '乳类及制品', '酸奶(全脂，盖瑞牌，全脂风味发酵乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1467, '乳类及制品', '酸奶(全脂，花园牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1468, '乳类及制品', '酸奶(全脂，佳丽牌，益家全脂风味发酵乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1469, '乳类及制品', '酸奶(全脂，天润牌浓缩酸奶，全脂风味发酵乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1470, '乳类及制品', '酸奶(全脂，西域春牌新疆老酸奶，凝固型)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1471, '乳类及制品', '酸奶(低脂，艾美牌，草莓、芒果、蓝莓、覆盆子、菠萝味低脂风味发酵乳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1472, '乳类及制品', '奶酪[干酪]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1473, '乳类及制品', '奶豆腐(脱脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1474, '乳类及制品', '奶豆腐(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1475, '乳类及制品', '奶疙瘩[奶酪干，干酸奶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1476, '乳类及制品', '乳酪(契达干酪，普通)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1477, '乳类及制品', '乳酪(契达干酪,脱脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1478, '乳类及制品', '曲拉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1479, '乳类及制品', '乳酪(全脂软酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1480, '乳类及制品', '酸酪蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1481, '乳类及制品', '乳酪(羊乳酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1482, '乳类及制品', '乳酪(中脂软酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1483, '乳类及制品', '奶酪(光明牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1484, '乳类及制品', '奶酪(骑士牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1485, '乳类及制品', '低脂奶酪', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1486, '乳类及制品', '硬质干酪', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1487, '乳类及制品', '奶酪(爱氏晨曦牌，儿童奶酪条)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1488, '乳类及制品', '奶酪(百嘉儿童干酪条)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1489, '乳类及制品', '奶酪(多美鲜牌，欧洲奶油奶酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1490, '乳类及制品', '奶酪(天润牌，无限欢酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1491, '乳类及制品', '酸奶疙瘩(干，农户家)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1492, '乳类及制品', '黄油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1493, '乳类及制品', '酸奶疙瘩(干，市售、加盐)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1494, '乳类及制品', '酸奶疙瘩(瑞缘牌，中脂特硬质干酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1495, '乳类及制品', '酸奶疙瘩(新鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1496, '乳类及制品', '奶油(焦克)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1497, '乳类及制品', '奶油(食品工业)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1498, '乳类及制品', '黄油渣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1499, '乳类及制品', '白脱(食品工业)[牛油、黄油]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1500, '乳类及制品', '酥油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1501, '乳类及制品', '酥油茶(原味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1502, '乳类及制品', '炼乳(甜，罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1503, '乳类及制品', '奶皮子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1504, '乳类及制品', '奶片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1505, '乳类及制品', '全脂甜炼乳(雀巢)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1506, '乳类及制品', '全脂甜炼乳(燕山牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1507, '乳类及制品', '脱脂甜炼乳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1508, '乳类及制品', '蛋白粉(益力健乳铁乳清蛋白粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1509, '乳类及制品', '牛初乳奶片(纽瑞滋牛初乳咀嚼奶片)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1510, '乳类及制品', '奶渣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1511, '乳类及制品', '人乳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1512, '乳类及制品', '奶油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1513, '乳类及制品', '酸奶(高蛋白)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1514, '乳类及制品', '奶油（上海）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1515, '乳类及制品', '酥油（西藏）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1516, '乳类及制品', '纯牛奶(全脂，德国牛)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1517, '乳类及制品', '酸奶疙瘩(干，市售)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1518, '乳类及制品', '儿童配方奶粉(雪花学生营养奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1519, '乳类及制品', '鲜驴奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1520, '乳类及制品', '纯牛奶(代表值，全脂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1521, '乳类及制品', '纯牛奶(全脂，美国牛)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1522, '乳类及制品', '纯牛奶(全脂，光明牌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1523, '蛋类及制品', '鸡蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1524, '蛋类及制品', '鸡蛋(红皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1525, '蛋类及制品', '鸡蛋(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1526, '蛋类及制品', '鸡蛋(土鸡)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1527, '蛋类及制品', '鸡蛋白', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1528, '蛋类及制品', '鸡蛋白(乌骨鸡)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1529, '蛋类及制品', '鸡蛋黄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1530, '蛋类及制品', '鸡蛋黄(乌骨鸡)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1531, '蛋类及制品', '鸡蛋(红皮）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1532, '蛋类及制品', '鸡蛋(藏鸡蛋)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1533, '蛋类及制品', '鸡蛋(乌鸡蛋,绿皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1534, '蛋类及制品', '鸡蛋粉[全蛋粉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1535, '蛋类及制品', '鸡蛋黄粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1536, '蛋类及制品', '松花蛋(鸡蛋)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1537, '蛋类及制品', '毛蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1538, '蛋类及制品', '荷包蛋(油煎)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1539, '蛋类及制品', '荷包蛋(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1540, '蛋类及制品', '鸭蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1541, '蛋类及制品', '鸭蛋白', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1542, '蛋类及制品', '鸭蛋黄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1543, '蛋类及制品', '海鸭蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1544, '蛋类及制品', '松花蛋(鸭蛋)[皮蛋]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1545, '蛋类及制品', '鸭蛋(咸鸭蛋,煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1546, '蛋类及制品', '鹅蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1547, '蛋类及制品', '鹅蛋黄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1548, '蛋类及制品', '鹅蛋(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1549, '蛋类及制品', '鹌鹑蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1550, '蛋类及制品', '鹌鹑蛋(五香罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1551, '蛋类及制品', '鸭蛋(咸鸭蛋,生)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1552, '蛋类及制品', '鸡蛋(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1553, '蛋类及制品', '鸡蛋(白皮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1554, '蛋类及制品', '鹅蛋白', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1555, '鱼虾蟹贝类', '蛤蜊', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1556, '鱼虾蟹贝类', '湟鱼(裸鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1557, '鱼虾蟹贝类', '黄鱼(小黄花鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1558, '鱼虾蟹贝类', '鲩鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1559, '鱼虾蟹贝类', '龙利鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1560, '鱼虾蟹贝类', '螺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1561, '鱼虾蟹贝类', '虾皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1562, '鱼虾蟹贝类', '鳕鱼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1563, '鱼虾蟹贝类', '瑶柱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1564, '鱼虾蟹贝类', '鱼肉滑', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1565, '鱼虾蟹贝类', '尖嘴白', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1566, '鱼虾蟹贝类', '口头鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1567, '鱼虾蟹贝类', '鲤鱼[鲤拐子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1568, '鱼虾蟹贝类', '罗非鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1569, '鱼虾蟹贝类', '泥鳅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1570, '鱼虾蟹贝类', '青鱼[青皮鱼、青鳞鱼、青混]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1571, '鱼虾蟹贝类', '乌鳢[黑鱼、乌鱼、生鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1572, '鱼虾蟹贝类', '银鱼[面条鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1573, '鱼虾蟹贝类', '湟鱼(裸鲤鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1574, '鱼虾蟹贝类', '鲇鱼[胡子鲇、鲢胡、旺虾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1575, '鱼虾蟹贝类', '鲒花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1576, '鱼虾蟹贝类', '鲢鱼[白鲢、胖子、连子鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1577, '鱼虾蟹贝类', '鲮鱼[雪鲮]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1578, '鱼虾蟹贝类', '鲮鱼(罐头)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1579, '鱼虾蟹贝类', '鳊鱼[鲂鱼、武昌鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1580, '鱼虾蟹贝类', '鳗鲡[鳗鱼、河鳗]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1581, '鱼虾蟹贝类', '鳙鱼[胖头鱼、摆佳鱼、花鲢鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1582, '鱼虾蟹贝类', '鳜鱼[桂鱼、花鲫鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1583, '鱼虾蟹贝类', '鳟鱼[红鳟鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1584, '鱼虾蟹贝类', '草鱼[白鲩、草包鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1585, '鱼虾蟹贝类', '丁桂鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1586, '鱼虾蟹贝类', '乌鳢(野生)[黑鱼、乌鱼生鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1587, '鱼虾蟹贝类', '回头鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1588, '鱼虾蟹贝类', '鮰鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1589, '鱼虾蟹贝类', '斑鳠[剑骨鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1590, '鱼虾蟹贝类', '抗浪鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1591, '鱼虾蟹贝类', '蓝鳃太阳鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1592, '鱼虾蟹贝类', '钳鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1593, '鱼虾蟹贝类', '翘嘴红鲌(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1594, '鱼虾蟹贝类', '鲥鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1595, '鱼虾蟹贝类', '鲟鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1596, '鱼虾蟹贝类', '雅鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1597, '鱼虾蟹贝类', '胭脂鱼(养殖)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1598, '鱼虾蟹贝类', '棒棒鱼(雅江冷水鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1599, '鱼虾蟹贝类', '尖嘴鱼(雅江冷水鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1600, '鱼虾蟹贝类', '胡子鱼(雅江冷水鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1601, '鱼虾蟹贝类', '白姑鱼[白米子(鱼)]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1602, '鱼虾蟹贝类', '鲹鱼[蓝圆参、边鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1603, '鱼虾蟹贝类', '带鱼[白带鱼、刀鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1604, '鱼虾蟹贝类', '堤鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1605, '鱼虾蟹贝类', '丁香鱼(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1606, '鱼虾蟹贝类', '狗母鱼[大头狗母鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1607, '鱼虾蟹贝类', '海鲫鱼[九九鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1608, '鱼虾蟹贝类', '海鳗[鲫勾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1609, '鱼虾蟹贝类', '红娘鱼[翼红娘鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1610, '鱼虾蟹贝类', '黄姑鱼[黄婆鸡]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1611, '鱼虾蟹贝类', '黄鱼(大黄花鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1612, '鱼虾蟹贝类', '黄鲂[赤虹、老板鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1613, '鱼虾蟹贝类', '金线鱼[红三鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1614, '鱼虾蟹贝类', '绿鳍马面鲀[面包鱼、橡皮鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1615, '鱼虾蟹贝类', '黄颡鱼[戈牙鱼、黄鳍鱼]（上海）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1616, '鱼虾蟹贝类', '梅童鱼[大头仔鱼、丁珠鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1617, '鱼虾蟹贝类', '沙丁鱼[沙鲻]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1618, '鱼虾蟹贝类', '沙钻鱼[多鳞鱚、沙梭鱼、麦穗鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1619, '鱼虾蟹贝类', '蛇鲻[沙梭鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1620, '鱼虾蟹贝类', '舌鳎[花纹舌头、舌头鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1621, '鱼虾蟹贝类', '油抒[香梭鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1622, '鱼虾蟹贝类', '颚针鱼[针量鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1623, '鱼虾蟹贝类', '鲅鱼[马鲛鱼、燕鲅鱼、巴鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1624, '鱼虾蟹贝类', '鲆[片口鱼、比目鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1625, '鱼虾蟹贝类', '鲈鱼[鲈花]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1626, '鱼虾蟹贝类', '鲐鱼[青鲐鱼、鲐巴鱼、青砖鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1627, '鱼虾蟹贝类', '鲑鱼[大马哈鱼、三文鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1628, '鱼虾蟹贝类', '鲑鱼籽酱[大马哈鱼籽酱、三文鱼子酱]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1629, '鱼虾蟹贝类', '鲚鱼(大)[大凤尾鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1630, '鱼虾蟹贝类', '鲚鱼(小)[小凤尾鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1631, '鱼虾蟹贝类', '鲨鱼(真鲨、白斑角鲨)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1632, '鱼虾蟹贝类', '鲳鱼(银鲳鱼)[平鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1633, '鱼虾蟹贝类', '刺泡鱼[刺鲍鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1634, '鱼虾蟹贝类', '鲷[黑鲷、铜盆鱼、大目鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1635, '鱼虾蟹贝类', '鲻鱼[白眼棱鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1636, '鱼虾蟹贝类', '鲽[比目鱼、凸眼鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1637, '鱼虾蟹贝类', '鳐鱼[夫鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1638, '鱼虾蟹贝类', '鳓鱼[快鱼、力鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1639, '鱼虾蟹贝类', '鳕鱼[鳕狭、明太鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1640, '鱼虾蟹贝类', '鲩鱼[鳘鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1641, '鱼虾蟹贝类', '带鱼(切段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1642, '鱼虾蟹贝类', '金鳇鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1643, '鱼虾蟹贝类', '双髻鲨', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1644, '鱼虾蟹贝类', '紫青低纹鮨(冰鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1645, '鱼虾蟹贝类', '鮟鱇鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1646, '鱼虾蟹贝类', '鲳鱼(鲜，刺鲳)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1647, '鱼虾蟹贝类', '大菱鲆鱼(鲜)[多宝鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1648, '鱼虾蟹贝类', '海鲈鱼(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1649, '鱼虾蟹贝类', '红鳍笛鲷[红鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1650, '鱼虾蟹贝类', '黄姑鱼(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1651, '鱼虾蟹贝类', '鲅鱼[马鲛鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1652, '鱼虾蟹贝类', '石斑鱼(老虎斑)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1653, '鱼虾蟹贝类', '石斑鱼(红石斑鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1654, '鱼虾蟹贝类', '石斑鱼(黑石斑鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1655, '鱼虾蟹贝类', '石斑鱼(花石斑鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1656, '鱼虾蟹贝类', '苏眉鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1657, '鱼虾蟹贝类', '青衣(红色)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1658, '鱼虾蟹贝类', '青衣(孔雀绿色)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1659, '鱼虾蟹贝类', '笠鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1660, '鱼虾蟹贝类', '金枪鱼肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1661, '鱼虾蟹贝类', '鲅鱼肉[马鲛鱼肉]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1662, '鱼虾蟹贝类', '鱼片干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1663, '鱼虾蟹贝类', '鱼奇油[鱼露、虾油]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1664, '鱼虾蟹贝类', '鱼排', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1665, '鱼虾蟹贝类', '鱼子酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1666, '鱼虾蟹贝类', '草鱼(熏)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1667, '鱼虾蟹贝类', '丁香鱼(香辣味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1668, '鱼虾蟹贝类', '凤尾鱼(熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1669, '鱼虾蟹贝类', '箭鱼(炸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1670, '鱼虾蟹贝类', '金枪鱼(盐水浸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1671, '鱼虾蟹贝类', '金枪鱼(油浸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1672, '鱼虾蟹贝类', '鲮鱼(豆豉，熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1673, '鱼虾蟹贝类', '鳗鱼(红烧)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1674, '鱼虾蟹贝类', '鲭鱼(烤，150℃，20分)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1675, '鱼虾蟹贝类', '鲭鱼(炸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1676, '鱼虾蟹贝类', '鲭鱼(蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1677, '鱼虾蟹贝类', '鲭鱼(煮)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1678, '鱼虾蟹贝类', '沙丁鱼(茄汁，熟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1679, '鱼虾蟹贝类', '沙丁鱼(盐水浸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1680, '鱼虾蟹贝类', '沙丁鱼(油浸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1681, '鱼虾蟹贝类', '午餐鱼(香辣味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1682, '鱼虾蟹贝类', '鳕鱼(烤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1683, '鱼虾蟹贝类', '鳕鱼(炸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1684, '鱼虾蟹贝类', '白米虾[水虾米]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1685, '鱼虾蟹贝类', '斑节对虾[草虾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1686, '鱼虾蟹贝类', '长毛对虾[大虾、白露虾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1687, '鱼虾蟹贝类', '刺蛄[刺蛄、大头虾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1688, '鱼虾蟹贝类', '东方对虾[中国对虾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1689, '鱼虾蟹贝类', '对虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1690, '鱼虾蟹贝类', '海虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1691, '鱼虾蟹贝类', '基围虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1692, '鱼虾蟹贝类', '江虾[沼虾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1693, '鱼虾蟹贝类', '龙虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1694, '鱼虾蟹贝类', '明虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1695, '鱼虾蟹贝类', '塘水虾[草虾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1696, '鱼虾蟹贝类', '虾虎', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1697, '鱼虾蟹贝类', '螯虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1698, '鱼虾蟹贝类', '北极虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1699, '鱼虾蟹贝类', '九节虾(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1700, '鱼虾蟹贝类', '口虾蛄[皮皮虾]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1701, '鱼虾蟹贝类', '罗氏沼虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1702, '鱼虾蟹贝类', '南美白对虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1703, '鱼虾蟹贝类', '青虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1704, '鱼虾蟹贝类', '琼海虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1705, '鱼虾蟹贝类', '虾米[海米、虾仁]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1706, '鱼虾蟹贝类', '虾脑酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1707, '鱼虾蟹贝类', '虾酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1708, '鱼虾蟹贝类', '虾仁(红)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1709, '鱼虾蟹贝类', '虾仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1710, '鱼虾蟹贝类', '虾仁肉丸', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1711, '鱼虾蟹贝类', '海蟹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1712, '鱼虾蟹贝类', '河蟹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1713, '鱼虾蟹贝类', '锯缘青蟹[青蟹]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1714, '鱼虾蟹贝类', '梭子蟹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1715, '鱼虾蟹贝类', '蟹肉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1716, '鱼虾蟹贝类', '海蟹(小)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1717, '鱼虾蟹贝类', '锯缘青蟹(公，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1718, '鱼虾蟹贝类', '锯缘青蟹(母，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1719, '鱼虾蟹贝类', '大闸蟹(母)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1720, '鱼虾蟹贝类', '蟹足棒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1721, '鱼虾蟹贝类', '蟹膏(大闸蟹，蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1722, '鱼虾蟹贝类', '蟹肉(大闸蟹，公，蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1723, '鱼虾蟹贝类', '蟹黄(大闸蟹，蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1724, '鱼虾蟹贝类', '蟹肉(大闸蟹，母，蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1725, '鱼虾蟹贝类', '梭子蟹(公,蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1726, '鱼虾蟹贝类', '梭子蟹(母,蒸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1727, '鱼虾蟹贝类', '鲍鱼[杂色鲍]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1728, '鱼虾蟹贝类', '鲍鱼(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1729, '鱼虾蟹贝类', '蛏子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1730, '鱼虾蟹贝类', '蛏干[蛏子缢、蛏青子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1731, '鱼虾蟹贝类', '赤贝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1732, '鱼虾蟹贝类', '河蚌', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1733, '鱼虾蟹贝类', '河蚬[蚬子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1734, '鱼虾蟹贝类', '牡蛎[海蛎子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1735, '鱼虾蟹贝类', '生蚝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1736, '鱼虾蟹贝类', '泥蚶[血蚶、珠蚶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1737, '鱼虾蟹贝类', '扇贝(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1738, '鱼虾蟹贝类', '扇贝(干)[干贝]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1739, '鱼虾蟹贝类', '鲜贝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1740, '鱼虾蟹贝类', '银蚶[蚶子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1741, '鱼虾蟹贝类', '贻贝(鲜)[淡菜、壳菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1742, '鱼虾蟹贝类', '贻贝(干)[淡菜、壳菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1743, '鱼虾蟹贝类', '海蚌[西施舌]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1744, '鱼虾蟹贝类', '鲍鱼(皱纹鲍)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1745, '鱼虾蟹贝类', '蛤蜊(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1746, '鱼虾蟹贝类', '蛤蜊(毛蛤蜊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1747, '鱼虾蟹贝类', '蛤蜊(秋蛤蜊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1748, '鱼虾蟹贝类', '蛤蜊(沙蛤蜊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1749, '鱼虾蟹贝类', '蛤蜊(杂色蛤蜊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1750, '鱼虾蟹贝类', '螺(代表值)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1751, '鱼虾蟹贝类', '红螺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1752, '鱼虾蟹贝类', '黄螺[东风螺]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1753, '鱼虾蟹贝类', '螺蛳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1754, '鱼虾蟹贝类', '石螺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1755, '鱼虾蟹贝类', '田螺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1756, '鱼虾蟹贝类', '香海螺', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1757, '鱼虾蟹贝类', '海蚌(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1758, '鱼虾蟹贝类', '海蚌(漳港海蚌，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1759, '鱼虾蟹贝类', '蛏子(焯)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1760, '鱼虾蟹贝类', '缢蛏(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1761, '鱼虾蟹贝类', '牛角江珧蛤(鲜)[长带子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1762, '鱼虾蟹贝类', '文蛤(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1763, '鱼虾蟹贝类', '血蚶(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1764, '鱼虾蟹贝类', '六角螺(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1765, '鱼虾蟹贝类', '海螺肉(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1766, '鱼虾蟹贝类', '文蛤丸', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1767, '鱼虾蟹贝类', '海参', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1768, '鱼虾蟹贝类', '海参(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1769, '鱼虾蟹贝类', '海参(水浸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1770, '鱼虾蟹贝类', '海蜇皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1771, '鱼虾蟹贝类', '海蜇头', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1772, '鱼虾蟹贝类', '墨鱼(鲜，曼氏无针乌贼）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1773, '鱼虾蟹贝类', '墨鱼(干，曼氏无针乌贼）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1774, '鱼虾蟹贝类', '乌贼(鲜，中国枪乌贼）[枪乌贼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1775, '鱼虾蟹贝类', '鱿鱼(干，中国枪乌贼）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1776, '鱼虾蟹贝类', '鱿鱼(水浸)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1777, '鱼虾蟹贝类', '乌鱼蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1778, '鱼虾蟹贝类', '章鱼(章鱼肉)[八爪鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1779, '鱼虾蟹贝类', '章鱼[八角鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1780, '鱼虾蟹贝类', '甲鱼蛋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1781, '鱼虾蟹贝类', '乌龟(龟板)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1782, '鱼虾蟹贝类', '乌龟(肉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1783, '鱼虾蟹贝类', '金鲨鱼翅(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1784, '鱼虾蟹贝类', '鱼翅(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1785, '鱼虾蟹贝类', '棘参(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1786, '鱼虾蟹贝类', '梅花参(泡发)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1787, '鱼虾蟹贝类', '墨鱼(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1788, '鱼虾蟹贝类', '墨鱼圈', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1789, '鱼虾蟹贝类', '墨鱼丸', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1790, '鱼虾蟹贝类', '鲅鱼(咸)[咸马胶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1791, '鱼虾蟹贝类', '黄鳝[鳝鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1792, '鱼虾蟹贝类', '鱼丸', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1793, '鱼虾蟹贝类', '海参(干)（高蛋白低脂高钙）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1794, '鱼虾蟹贝类', '罗非鱼(莫桑比克)[非洲黑鲫鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1795, '鱼虾蟹贝类', '河虾', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1796, '鱼虾蟹贝类', '鲭鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1797, '鱼虾蟹贝类', '鲫鱼[喜头鱼，海附鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1798, '鱼虾蟹贝类', '鲢鱼[白鲢、胖子、连子鱼]（天津）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1799, '鱼虾蟹贝类', '鲫鱼[喜头鱼，海附鱼]（天津）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1800, '鱼虾蟹贝类', '鳊鱼[鲂鱼、武昌鱼]（四川）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1801, '鱼虾蟹贝类', '黄鱼(小黄花鱼)（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1802, '鱼虾蟹贝类', '虾皮（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1803, '鱼虾蟹贝类', '海蟹(公)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1804, '鱼虾蟹贝类', '蛤蜊(花蛤蜊)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1805, '鱼虾蟹贝类', '海蟹(母)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1806, '鱼虾蟹贝类', '花骨鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1807, '鱼虾蟹贝类', '白条鱼(裸鱼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1808, '鱼虾蟹贝类', '草鱼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1809, '鱼虾蟹贝类', '赤眼鳟[金目鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1810, '鱼虾蟹贝类', '鳡鱼[猴鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1811, '鱼虾蟹贝类', '胡子鲇[塘虱(鱼)]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1812, '鱼虾蟹贝类', '黄颡鱼[戈牙鱼、黄鳍鱼]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1813, '鱼虾蟹贝类', '黄鳝丝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1814, '婴幼儿食品', '豆奶粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1815, '婴幼儿食品', '钙质糕粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1816, '婴幼儿食品', '健儿粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1817, '婴幼儿食品', '莲子健儿粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1818, '婴幼儿食品', '母乳化奶粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1819, '婴幼儿食品', '乳儿糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1820, '婴幼儿食品', '婴儿奶粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1821, '婴幼儿食品', '婴儿奶糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1822, '婴幼儿食品', '婴儿营养粉[婴宝*5410*]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1823, '婴幼儿食品', '营养乳儿糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1824, '婴幼儿食品', '婴儿配方奶粉(惠氏金装爱儿乐婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1825, '婴幼儿食品', '婴儿配方奶粉(美素佳儿GOLD金装婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1826, '婴幼儿食品', '婴儿配方奶粉(美赞臣安婴儿婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1827, '婴幼儿食品', '婴儿配方奶粉(明治珍爱儿婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1828, '婴幼儿食品', '婴儿配方奶粉(能慧金装婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1829, '婴幼儿食品', '婴儿配方奶粉(雀巢力多精婴儿配方奶粉1)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1830, '婴幼儿食品', '婴儿配方奶粉(雀巢能恩全进口奶源婴儿配方奶粉1)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1831, '婴幼儿食品', '婴儿配方奶粉(三元爱力优婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1832, '婴幼儿食品', '婴儿配方奶粉(三元爱欣宝金装婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1833, '婴幼儿食品', '婴儿配方奶粉(三元爱欣宝婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1834, '婴幼儿食品', '婴儿配方奶粉(三元金装爱力优婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1835, '婴幼儿食品', '婴儿配方奶粉(圣元优博爱系列1婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1836, '婴幼儿食品', '苹果南瓜红枣泥(亨氏苹果南瓜红枣泥2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1837, '婴幼儿食品', '婴儿配方奶粉(圣元优聪金装婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1838, '婴幼儿食品', '婴儿配方奶粉(特选初生婴儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1839, '婴幼儿食品', '婴儿配方奶粉(完达山1段配方奶粉婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1840, '婴幼儿食品', '婴儿配方奶粉(完达山金装元乳婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1841, '婴幼儿食品', '婴儿配方奶粉(完达山育儿慧金装婴儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1842, '婴幼儿食品', '婴儿配方奶粉(完达山元乳婴儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1843, '婴幼儿食品', '婴儿配方奶粉(雅培金装喜康宝婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1844, '婴幼儿食品', '婴儿配方奶粉(雅士利α-金装婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1845, '婴幼儿食品', '婴儿配方奶粉(伊利金领冠婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1846, '婴幼儿食品', '婴儿配方奶粉(伊利金装婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1847, '婴幼儿食品', '婴儿配方奶粉(伊利婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1848, '婴幼儿食品', '婴儿配方羊奶粉(美可高特小婴配方羊奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1849, '婴幼儿食品', '婴儿配方豆粉(三元爱力优豆基婴儿配方粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1850, '婴幼儿食品', '较大婴儿配方奶粉(超级飞帆较大婴儿配方奶粉Ⅳ)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1851, '婴幼儿食品', '较大婴儿配方奶粉(多美滋多领加较大婴儿配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1852, '婴幼儿食品', '较大婴儿配方奶粉(多美滋优阶贝护延续较大婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1853, '婴幼儿食品', '较大婴儿配方奶粉(飞帆较大婴儿配方奶粉Ⅱ)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1854, '婴幼儿食品', '较大婴儿配方奶粉(合生元超级呵护较大婴儿配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1855, '婴幼儿食品', '较大婴儿配方奶粉(亨氏超金智儿高较大婴儿配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1856, '婴幼儿食品', '较大婴儿配方奶粉(惠氏金装健儿乐较大婴儿和幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1857, '婴幼儿食品', '较大婴儿配方奶粉(美素佳儿GOLD金装较大婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1858, '婴幼儿食品', '较大婴儿配方奶粉(美赞臣安婴宝较大婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1859, '婴幼儿食品', '较大婴儿配方奶粉(明治珍爱宝较大婴儿和幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1860, '婴幼儿食品', '苹果泥(亨氏金香苹果泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1861, '婴幼儿食品', '较大婴儿配方奶粉(能慧金装较大婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1862, '婴幼儿食品', '较大婴儿配方奶粉(欧世蒙牛金装佳智较大婴儿配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1863, '婴幼儿食品', '较大婴儿配方奶粉(完达山2段配方奶粉较大婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1864, '婴幼儿食品', '较大婴儿配方奶粉(完达山金装元乳较大婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1865, '婴幼儿食品', '较大婴儿配方奶粉(完达山育儿慧金装较大婴儿配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1866, '婴幼儿食品', '较大婴儿配方奶粉(完达山元乳较大婴儿配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1867, '婴幼儿食品', '较大婴儿配方奶粉(雅士利α-金装较大婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1868, '婴幼儿食品', '较大婴儿配方羊奶粉(美可高特大婴配方羊奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1869, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(爱+婴幼儿配方奶粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1870, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(爱+幼儿配方奶粉4阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1871, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(贝因美较大婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1872, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(超级能恩较大婴儿及幼儿配方奶粉2段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1873, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(雀巢力多精较大幼儿及幼儿配方奶粉2)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1874, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(雀巢能恩全进口奶源较大婴儿及幼儿配方奶粉2)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1875, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(三元爱力优较大婴儿及幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1876, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(三元爱欣宝金装较大婴儿及幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1877, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(三元金装爱力优较大婴儿及幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1878, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(圣元优博爱系列2较大婴儿和幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1879, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(圣元优聪金装较大婴儿和幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1880, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(特选宝宝成长配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1881, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(雅培金装喜康宝较大婴幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1882, '婴幼儿食品', '幼儿配方奶粉(三元爱欣宝幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1883, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(雅培亲护金装较大婴儿和幼儿配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1884, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(伊利较大婴幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1885, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(伊利金领冠较大婴儿及幼儿配方奶粉）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1886, '婴幼儿食品', '较大婴儿和幼儿配方奶粉(伊利金装较大婴幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1887, '婴幼儿食品', '幼儿配方奶粉(贝因美幼儿成长配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1888, '婴幼儿食品', '幼儿配方奶粉(超级飞帆幼儿配方奶粉Ⅳ)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1889, '婴幼儿食品', '幼儿配方奶粉(超级能恩幼儿配方奶粉3段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1890, '婴幼儿食品', '幼儿配方奶粉(多美滋多学1加幼儿配方奶粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1891, '婴幼儿食品', '幼儿配方奶粉(多美滋优阶幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1892, '婴幼儿食品', '幼儿配方奶粉(多美滋幼衡多营养幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1893, '婴幼儿食品', '幼儿配方奶粉(飞帆幼儿配方奶粉Ⅱ)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1894, '婴幼儿食品', '幼儿配方奶粉(合生元超级呵护幼儿配方奶粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1895, '婴幼儿食品', '幼儿配方奶粉(亨氏超金学儿高幼儿配方奶粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1896, '婴幼儿食品', '幼儿配方奶粉(惠氏金装膳儿加幼儿全营养配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1897, '婴幼儿食品', '幼儿配方奶粉(惠氏金装幼儿乐幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1898, '婴幼儿食品', '幼儿配方奶粉(美素佳儿GOLD金装幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1899, '婴幼儿食品', '幼儿配方奶粉(美赞臣安儿宝幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1900, '婴幼儿食品', '幼儿配方奶粉(能慧金装幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1901, '婴幼儿食品', '幼儿配方奶粉(欧世蒙牛金装佳智幼儿配方奶粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1902, '婴幼儿食品', '幼儿配方奶粉(雀巢力多精幼儿配方奶粉3)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1903, '婴幼儿食品', '幼儿配方奶粉(雀巢能恩全进口奶源幼儿配方奶粉3)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1904, '婴幼儿食品', '幼儿配方奶粉(三元爱力优幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1905, '婴幼儿食品', '幼儿配方奶粉(三元爱欣宝金装幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1906, '婴幼儿食品', '苹果香蕉泥(亨氏苹果香蕉泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1907, '婴幼儿食品', '幼儿配方奶粉(三元金装爱力优幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1908, '婴幼儿食品', '幼儿配方奶粉(圣元优博爱系列3幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1909, '婴幼儿食品', '米粉(亨氏南瓜营养米粉1段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1910, '婴幼儿食品', '幼儿配方奶粉(圣元优聪金装幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1911, '婴幼儿食品', '幼儿配方奶粉(特选健儿成长配方奶粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1912, '婴幼儿食品', '幼儿配方奶粉(完达山3段配方奶粉幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1913, '婴幼儿食品', '幼儿配方奶粉(完达山金装元乳幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1914, '婴幼儿食品', '幼儿配方奶粉(完达山育儿慧金装幼儿配方奶粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1915, '婴幼儿食品', '幼儿配方奶粉(完达山元乳幼儿配方奶粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1916, '婴幼儿食品', '幼儿配方奶粉(雅培金装喜康宝幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1917, '婴幼儿食品', '幼儿配方奶粉(雅培金装小安素全营养幼儿配方粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1918, '婴幼儿食品', '幼儿配方奶粉(雅士利α-金装幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1919, '婴幼儿食品', '幼儿配方奶粉(伊利金领冠幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1920, '婴幼儿食品', '幼儿配方奶粉(伊利金装幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1921, '婴幼儿食品', '幼儿配方奶粉(伊利幼儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1922, '婴幼儿食品', '幼儿配方羊奶粉(美可高特幼儿配方羊奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1923, '婴幼儿食品', '婴儿配方奶粉(超级能恩乳蛋白部分水解婴幼儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1924, '婴幼儿食品', '婴儿配方奶粉(雅培金装亲护乳蛋白部分水解婴儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1925, '婴幼儿食品', '米粉(金装牛肉菠菜营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1926, '婴幼儿食品', '婴儿配方奶粉(惠氏S-26金装爱儿加早产儿出院后配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1927, '婴幼儿食品', '米粉(贝因美果蔬宝多维营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1928, '婴幼儿食品', '米粉(贝因美乳清蛋白营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1929, '婴幼儿食品', '米粉(多口味装)(亨氏多口味装婴儿营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1930, '婴幼儿食品', '米粉(亨氏黑米红枣营养米粉五谷系列米粉6至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1931, '婴幼儿食品', '米粉(亨氏胡萝卜营养米粉1段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1932, '婴幼儿食品', '米粉(亨氏淮山薏米营养米粉清润系列1段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1933, '婴幼儿食品', '米粉(亨氏混合蔬菜营养米粉辅食添加初期至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1934, '婴幼儿食品', '米粉(亨氏鸡肉蔬菜营养米粉肉鱼系列米粉6至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1935, '婴幼儿食品', '米粉(亨氏五谷杂粮营养米粉五谷系列米粉8至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1936, '婴幼儿食品', '米粉(亨氏鳕鱼苹果营养米粉6至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1937, '婴幼儿食品', '米粉(亨氏婴儿营养米粉辅食添加初期至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1938, '婴幼儿食品', '米粉(亨氏鱼肉蔬菜营养米粉6至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1939, '婴幼儿食品', '米粉(亨氏猪肝蔬菜营养米粉6至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1940, '婴幼儿食品', '米粉(嘉宝缤纷水果营养米粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1941, '婴幼儿食品', '米粉(嘉宝菠菜营养米粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1942, '婴幼儿食品', '米粉(嘉宝番茄牛肉营养米粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1943, '婴幼儿食品', '米粉(嘉宝胡萝卜营养米粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1944, '婴幼儿食品', '米粉(嘉宝燕麦营养米粉3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1945, '婴幼儿食品', '米粉(嘉宝营养米粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1946, '婴幼儿食品', '米粉(金装宝贝营养菠菜营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1947, '婴幼儿食品', '米粉(金装宝贝营养钙铁锌营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1948, '婴幼儿食品', '米粉(金装宝贝营养什锦水果营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1949, '婴幼儿食品', '米粉(金装宝贝营养西红柿牛肉营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1950, '婴幼儿食品', '米粉(金装宝贝营养燕麦营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1951, '婴幼儿食品', '米粉(金装核桃营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1952, '婴幼儿食品', '米粉(金装胡萝卜营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1953, '婴幼儿食品', '米粉(金装三文鱼胡萝卜营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1954, '婴幼儿食品', '米粉(金装什果套餐营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1955, '婴幼儿食品', '米粉(金装锌铁钙营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1956, '婴幼儿食品', '米粉(金装猪肝蔬菜营养米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1957, '婴幼儿食品', '米粉(圣元DHA&胡萝卜营养米粉1段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1958, '婴幼儿食品', '苹果胡萝卜泥(亨氏苹果胡萝卜泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1959, '婴幼儿食品', '米粉(圣元多维蔬菜营养米粉2段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1960, '婴幼儿食品', '米粉(圣元钙铁锌营养米粉1段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1961, '婴幼儿食品', '米粉(圣元淮山薏米营养米粉2段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1962, '婴幼儿食品', '三文鱼番茄泥(亨氏三文鱼番茄泥2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1963, '婴幼儿食品', '米粉(圣元鸡肉香菇营养米粉3段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1964, '婴幼儿食品', '米粉(圣元乳清蛋白营养米粉2段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1965, '婴幼儿食品', '米粉(圣元什锦水果营养米粉2段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1966, '婴幼儿食品', '米粉(圣元营养米粉1段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1967, '婴幼儿食品', '米粉(圣元鱼肉菠菜营养米粉2段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1968, '婴幼儿食品', '米粥(干)(方广鳕鱼胡萝卜营养雪花粥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1969, '婴幼儿食品', '奶米粉(亨氏强化铁锌钙营养奶米粉辅食添加初期至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1970, '婴幼儿食品', '奶米粉(亨氏乳清蛋白营养奶米粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1971, '婴幼儿食品', '米粉(亨氏AD钙高蛋白营养米粉加奶补钙系列米粉6至36个月适用)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1972, '婴幼儿食品', '米粉(圣元高蛋白营养米粉3段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1973, '婴幼儿食品', '面条(贝因美蛋黄营养面条)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1974, '婴幼儿食品', '面条(贝因美果蔬营养面条)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1975, '婴幼儿食品', '面条(贝因美黑芝麻营养面条)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1976, '婴幼儿食品', '面条(方广金装彩面核桃黑芝麻蔬菜营养面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1977, '婴幼儿食品', '面条(亨氏金装粒粒面黑米紫薯面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1978, '婴幼儿食品', '面条(伊威猪肝蔬菜营养面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1979, '婴幼儿食品', '饼干(贝因美营养磨牙棒饼干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1980, '婴幼儿食品', '饼干(方广科学配方宝宝机能饼干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1981, '婴幼儿食品', '饼干(格兰宝小二七种蔬菜饼干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1982, '婴幼儿食品', '饼干(嘉宝草莓苹果味星星泡芙饼干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1983, '婴幼儿食品', '饼干(嘉宝香草圈圈饼干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1984, '婴幼儿食品', '饼干(伊威全机能字母宝宝营养饼干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1985, '婴幼儿食品', '骨髓蔬菜泥(亨氏骨髓蔬菜泥3阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1986, '婴幼儿食品', '胡萝卜鱼肉泥(亨氏胡萝卜鱼肉泥2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1987, '婴幼儿食品', '混合蔬菜泥(亨氏混合蔬菜泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1988, '婴幼儿食品', '混合水果泥(亨氏混合水果泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1989, '婴幼儿食品', '甜嫩豌豆泥(亨氏甜嫩豌豆泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1990, '婴幼儿食品', '蔬菜骨泥(亨氏蔬菜骨泥2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1991, '婴幼儿食品', '香甜胡萝卜泥(亨氏香甜胡萝卜泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1992, '婴幼儿食品', '香甜南瓜泥(亨氏香甜南瓜泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1993, '婴幼儿食品', '冻干草莓脆果(果仙多维V草莓萃脆果(冻干))', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1994, '婴幼儿食品', '肝粉(伊威全机能肝粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1995, '婴幼儿食品', '肝酥(方广宝宝营养猪肝酥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1996, '婴幼儿食品', '肉松(伊威婴幼儿纯肉松)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1997, '婴幼儿食品', '肉酥(贝因美宝宝菠菜营养肉酥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1998, '婴幼儿食品', '肉酥(贝因美宝宝胡萝卜营养肉酥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (1999, '婴幼儿食品', '肉酥(原味)(贝因美宝宝原味营养肉酥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2000, '婴幼儿食品', '鳕鱼酥(方广宝宝野生鳕鱼酥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2001, '婴幼儿食品', '苹果胡萝卜汁(亨氏苹果胡萝卜汁1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2002, '婴幼儿食品', '苹果汁(亨氏苹果汁1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2003, '婴幼儿食品', '葡萄汁(亨氏葡萄汁1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2004, '婴幼儿食品', '香橙汁(亨氏香橙汁1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2005, '婴幼儿食品', '香梨汁(亨氏香梨汁1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2006, '婴幼儿食品', '甜嫩玉米泥(亨氏甜嫩玉米泥1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2007, '婴幼儿食品', '婴儿配方奶粉(爱+新生儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2008, '婴幼儿食品', '婴儿配方奶粉(爱+婴儿配方奶粉2阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2009, '婴幼儿食品', '婴儿配方奶粉(贝因美初生婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2010, '婴幼儿食品', '婴儿配方奶粉(超级飞帆婴儿配方奶粉Ⅳ)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2011, '婴幼儿食品', '婴儿配方奶粉(多美滋多乐加婴儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2012, '婴幼儿食品', '婴儿配方奶粉(多美滋优阶贝护婴儿配方奶粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2013, '婴幼儿食品', '婴儿配方奶粉(飞帆婴儿配方奶粉Ⅱ)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2014, '婴幼儿食品', '婴儿配方奶粉(合生元超级呵护婴儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2015, '婴幼儿食品', '婴儿配方奶粉(亨氏超金康儿高婴儿配方奶粉1阶段)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2016, '小吃、甜饼', '春卷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2017, '小吃、甜饼', '艾窝窝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2018, '小吃、甜饼', '白水羊头', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2019, '小吃、甜饼', '茶汤', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2020, '小吃、甜饼', '炒肝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2021, '小吃、甜饼', '豆腐脑(带卤)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2022, '小吃、甜饼', '粉皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2023, '小吃、甜饼', '灌肠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2024, '小吃、甜饼', '煎饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2025, '小吃、甜饼', '焦圈', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2026, '小吃、甜饼', '京八件', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2027, '小吃、甜饼', '栗羊羹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2028, '小吃、甜饼', '凉粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2029, '小吃、甜饼', '凉粉(带调料)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2030, '小吃、甜饼', '凉面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2031, '小吃、甜饼', '龙虾片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2032, '小吃、甜饼', '驴打滚', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2033, '小吃、甜饼', '美味香酥卷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2034, '小吃、甜饼', '蜜麻花[糖耳朵]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2035, '小吃、甜饼', '密三刀', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2036, '小吃、甜饼', '面窝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2037, '小吃、甜饼', '年糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2038, '小吃、甜饼', '青稞炒面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2039, '小吃、甜饼', '热干面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2040, '小吃、甜饼', '三刀蜜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2041, '小吃、甜饼', '汤泡', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2042, '小吃、甜饼', '甜胚子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2043, '小吃、甜饼', '甜醅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2044, '小吃、甜饼', '豌豆黄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2045, '小吃、甜饼', '香油炒面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2046, '小吃、甜饼', '油茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2047, '小吃、甜饼', '油炸豆瓣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2048, '小吃、甜饼', '炸糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2049, '小吃、甜饼', '糌粑(稞麦熟品)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2050, '小吃、甜饼', '黑芝麻汤圆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2051, '小吃、甜饼', '醪糟', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2052, '小吃、甜饼', '过桥米线', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2053, '小吃、甜饼', '蛋糕(黄蛋糕)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2054, '小吃、甜饼', '蛋清蛋糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2055, '小吃、甜饼', '宫廷蛋糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2056, '小吃、甜饼', '老年蛋糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2057, '小吃、甜饼', '奶油蛋糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2058, '小吃、甜饼', '西式蛋糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2059, '小吃、甜饼', '月饼(百寿宴点)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2060, '小吃、甜饼', '月饼(豆沙)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2061, '小吃、甜饼', '月饼(奶油果馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2062, '小吃、甜饼', '月饼(奶油松仁)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2063, '小吃、甜饼', '月饼(唐王赏月)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2064, '小吃、甜饼', '月饼(五仁)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2065, '小吃、甜饼', '月饼(香油果馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2066, '小吃、甜饼', '月饼(枣泥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2067, '小吃、甜饼', '板油酥饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2068, '小吃、甜饼', '蛋黄酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2069, '小吃、甜饼', '蛋麻脆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2070, '小吃、甜饼', '德庆酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2071, '小吃、甜饼', '鹅油卷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2072, '小吃、甜饼', '凤尾酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2073, '小吃、甜饼', '福来酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2074, '小吃、甜饼', '核桃薄脆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2075, '小吃、甜饼', '黑麻香酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2076, '小吃、甜饼', '黑洋酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2077, '小吃、甜饼', '混糖糕点', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2078, '小吃、甜饼', '鸡腿酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2079, '小吃、甜饼', '夹心酥饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2080, '小吃、甜饼', '江米条', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2081, '小吃、甜饼', '金钱酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2082, '小吃、甜饼', '京式黄酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2083, '小吃、甜饼', '开口笑', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2084, '小吃、甜饼', '廖花糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2085, '小吃、甜饼', '绿豆糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2086, '小吃、甜饼', '麻烘糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2087, '小吃、甜饼', '麻香糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2088, '小吃、甜饼', '米花糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2089, '小吃、甜饼', '起酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2090, '小吃、甜饼', '水晶饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2091, '小吃、甜饼', '酥皮糕点', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2092, '小吃、甜饼', '桃酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2093, '小吃、甜饼', '硬皮糕点', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2094, '小吃、甜饼', '芝麻桃酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2095, '小吃、甜饼', '状元饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2096, '小吃、甜饼', '茯苓夹饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2097, '小吃、甜饼', '沙琪玛蛋酥', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2098, '小吃、甜饼', '香橙水果馅饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2099, '小吃、甜饼', '鸡柳汉堡(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2100, '小吃、甜饼', '香芋甜心(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2101, '小吃、甜饼', '鸡肉汉堡(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2102, '小吃、甜饼', '鸡肉卷(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2103, '小吃、甜饼', '上校鸡块(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2104, '小吃、甜饼', '辣鸡翅(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2105, '小吃、甜饼', '劲爆鸡米花(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2106, '小吃、甜饼', '甜玉米籽粒(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2107, '小吃、甜饼', '薯条(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2108, '小吃、甜饼', '比萨饼(夹奶酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2109, '小吃、甜饼', '比萨饼(夹奶酪、肉和蔬菜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2110, '小吃、甜饼', '三明治(夹火腿、干酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2111, '小吃、甜饼', '三明治(夹鸡蛋、干酪)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2112, '小吃、甜饼', '三明治(夹鸡肉片,无调料酱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2113, '小吃、甜饼', '三明治(夹烤牛肉片)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2114, '小吃、甜饼', '三明治(夹鱼肉片)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2115, '小吃、甜饼', '干酪汉堡包(夹熏肉,夹调料酱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2116, '小吃、甜饼', '热狗(原味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2117, '小吃、甜饼', '新奥尔良鸡翅(肯德基)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2118, '小吃、甜饼', '油炸豆花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2119, '小吃、甜饼', '酿皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2120, '小吃、甜饼', '蛋糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2121, '小吃、甜饼', '三鲜豆皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2122, '小吃、甜饼', '麻花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2123, '速食食品', '面包片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2124, '速食食品', '蛋片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2125, '速食食品', '玉米片(即食粥)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2126, '速食食品', '早餐奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2127, '速食食品', '黑芝麻糊粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2128, '速食食品', '方便面', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2129, '速食食品', '鸡汁味干脆面(面饼+调味料)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2130, '速食食品', '海鲜味方便面(面饼+调味料+油料)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2131, '速食食品', '海鲜味方便面(面饼+调味料)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2132, '速食食品', '红烧牛肉方便面(面饼+调味料+蔬菜+肉酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2133, '速食食品', '红烧牛肉方便面(面饼+调味料+蔬菜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2134, '速食食品', '肉酱(红烧牛肉方便面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2135, '速食食品', '鳕鱼方便面(面饼+调味料+珍料+调味料+蔬菜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2136, '速食食品', '鳕鱼方便面(面饼+调味料+蔬菜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2137, '速食食品', '油酱料(珍料+调味油料,鳕鱼方便面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2138, '速食食品', '铁板牛肉炒面(面饼+汤料+蔬菜+调味酱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2139, '速食食品', '铁板牛肉炒面(面饼+汤料+蔬菜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2140, '速食食品', '调味酱(铁板牛肉炒面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2141, '速食食品', '玉米红烧牛肉味方便面(面饼+调味料+蔬菜+肉酱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2142, '速食食品', '燕麦片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2143, '速食食品', '玉米红烧牛肉味方便面(面饼+调味料+蔬菜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2144, '速食食品', '肉酱(玉米红烧牛肉味方便面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2145, '速食食品', '海鲜鸡汁味米线(米线+调味料+蔬菜+肉酱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2146, '速食食品', '海鲜鸡汁味米线(米线+调味料+蔬菜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2147, '速食食品', '肉酱(海鲜鸡汁味米线)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2148, '速食食品', '韭菜合子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2149, '速食食品', '糯米饭团', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2150, '速食食品', '什锦炒饭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2151, '速食食品', '虾仁炒饭', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2152, '速食食品', '面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2153, '速食食品', '多维面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2154, '速食食品', '法式牛角面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2155, '速食食品', '法式配餐面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2156, '速食食品', '黄油面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2157, '速食食品', '乐斯美面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2158, '速食食品', '麦维面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2159, '速食食品', '维生素面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2160, '速食食品', '咸面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2161, '速食食品', '椰圈面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2162, '速食食品', '桦榕面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2163, '速食食品', '饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2164, '速食食品', 'VC饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2165, '速食食品', '饼干(强化锌)[富锌饼干]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2166, '速食食品', '补血饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2167, '速食食品', '油料(海鲜味方便面)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2168, '速食食品', '儿童营养饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2169, '速食食品', '钙奶饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2170, '速食食品', '钙王饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2171, '速食食品', '高蛋白饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2172, '速食食品', '军用压缩饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2173, '速食食品', '奶油饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2174, '速食食品', '牛奶饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2175, '速食食品', '曲奇饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2176, '速食食品', '苏打饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2177, '速食食品', '维夫饼干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2178, '速食食品', '早茶饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2179, '速食食品', '饺子(三鲜馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2180, '速食食品', '饺子(猪肉白菜馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2181, '速食食品', '饺子(猪肉韭菜馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2182, '速食食品', '饺子(猪肉茴香馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2183, '速食食品', '饺子(猪肉香菇馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2184, '速食食品', '饺子(猪肉虾仁馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2185, '速食食品', '饺子(鸡肉蘑菇馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2186, '速食食品', '饺子(海鳗虾仁馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2187, '速食食品', '饺子(海鳗猪肉馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2188, '速食食品', '包子(三鲜馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2189, '速食食品', '包子(猪肉馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2190, '速食食品', '菠萝豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2191, '速食食品', '空心果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2192, '速食食品', '马铃薯片(油炸)[油炸土豆片]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2193, '速食食品', '酥香兰花豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2194, '速食食品', '米饼(鸡蛋牛奶味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2195, '速食食品', '学米饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2196, '速食食品', '蛋酥卷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2197, '速食食品', '巧克力派', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2198, '速食食品', '发式卷饼', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2199, '速食食品', '立体脆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2200, '速食食品', '饺子(素馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2201, '速食食品', '通心脆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2202, '速食食品', '洋葱圈', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2203, '速食食品', '锅巴(豆香)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2204, '速食食品', '锅巴(小米)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2205, '速食食品', '海苔', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2206, '速食食品', '香菇片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2207, '速食食品', '薯片(烧烤味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2208, '速食食品', '薯片(香辣味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2209, '速食食品', '薯圈', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2210, '速食食品', '怪味胡豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2211, '速食食品', '奶油五香豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2212, '速食食品', '夹心米果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2213, '速食食品', '乐芙球', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2214, '速食食品', '玉米花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2215, '速食食品', '果仁脆枣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2216, '速食食品', '空心脆枣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2217, '速食食品', '鱼肉粒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2218, '速食食品', '果冻(草莓水果冻)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2219, '速食食品', '果冻(蒟蒻冻)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2220, '速食食品', '果冻(蒟蒻椰果冻)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2221, '速食食品', '果冻(AD钙果冻)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2222, '速食食品', '果料面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2223, '速食食品', '麦胚面包', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2224, '速食食品', '粟米脆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2225, '速食食品', '虾片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2226, '速食食品', '饺子(猪肉芹菜馅)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2227, '速食食品', '冬菜虾仁混沌', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2228, '速食食品', '麦片', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2229, '饮料类', '可乐', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2230, '饮料类', '椰汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2231, '饮料类', '胡萝卜素王', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2232, '饮料类', '百令可乐', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2233, '饮料类', '冰川可乐', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2234, '饮料类', '橙珍(易拉罐装)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2235, '饮料类', '橙汁汽水', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2236, '饮料类', '特制柠檬汽水', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2237, '饮料类', '特制汽水', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2238, '饮料类', '维尔康运动饮料', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2239, '饮料类', '浓缩橘汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2240, '饮料类', '鲜橘汁(纸盒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2241, '饮料类', '橘子汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2242, '饮料类', '刺玫汁(纸盒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2243, '饮料类', '甘蔗汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2244, '饮料类', '红果汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2245, '饮料类', '柠檬汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2246, '饮料类', '沙棘果汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2247, '饮料类', '乌梅汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2248, '饮料类', '原汁沙棘', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2249, '饮料类', '果味奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2250, '饮料类', '喜乐(乳酸饮料)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2251, '饮料类', 'AD钙奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2252, '饮料类', '健康快车奶饮料', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2253, '饮料类', '粒粒果奶饮料', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2254, '饮料类', '巧克力豆奶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2255, '饮料类', '杏仁露', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2256, '饮料类', '核桃乳(儿童型)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2257, '饮料类', '茶砖[砖茶]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2258, '饮料类', '茶砖(小)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2259, '饮料类', '花茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2260, '饮料类', '石榴花茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2261, '饮料类', '铁观音茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2262, '饮料类', '珠茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2263, '饮料类', '大麦茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2264, '饮料类', '茶水', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2265, '饮料类', '宝宝福', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2266, '饮料类', '冰淇淋粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2267, '饮料类', '固体桔子饮料', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2268, '饮料类', '麦乳精', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2269, '饮料类', '山楂晶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2270, '饮料类', '酸梅晶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2271, '饮料类', '鲜桔晶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2272, '饮料类', '猕猴桃晶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2273, '饮料类', '绿茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2274, '饮料类', '红茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2275, '饮料类', '橘子晶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2276, '饮料类', '高乐高营养饮品', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2277, '饮料类', '菓珍', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2278, '饮料类', '桂花酸梅晶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2279, '饮料类', '柠檬茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2280, '饮料类', '巧克力麦芽营养饮品', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2281, '饮料类', '咖啡豆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2282, '饮料类', '咖啡粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2283, '饮料类', '咖啡伴侣', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2284, '饮料类', '冰棍', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2285, '饮料类', '冰砖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2286, '饮料类', '冰淇淋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2287, '饮料类', '大雪糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2288, '饮料类', '三明治冰激淋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2289, '饮料类', '双棒雪糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2290, '饮料类', '娃娃头', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2291, '饮料类', '紫雪糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2292, '饮料类', '冰激凌(草莓味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2293, '饮料类', '冰激凌(苦咖啡味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2294, '饮料类', '冰激凌(加奶油)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2295, '饮料类', '冰激凌(草莓圣代)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2296, '饮料类', '冰激凌(巧克力圣代)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2297, '饮料类', '冰激凌(脆皮甜筒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2298, '饮料类', '冰激凌(花心筒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2299, '饮料类', '冰激凌(金百合)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2300, '饮料类', '雪糕(百乐宝)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2301, '饮料类', '雪糕(红豆缘)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2302, '饮料类', '棒冰(可乐冰)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2303, '饮料类', '棒冰(奇彩旋)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2304, '饮料类', '红景天饮料', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2305, '饮料类', '可可粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2306, '饮料类', 'VC橘汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2307, '饮料类', '柿叶茶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2308, '饮料类', '甲级龙井', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2309, '饮料类', '柠檬汽水', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2310, '含酒精饮料', '酒泉酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2311, '含酒精饮料', '凉洲曲酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2312, '含酒精饮料', '宁河大曲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2313, '含酒精饮料', '宁河二曲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2314, '含酒精饮料', '曲酒(55度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2315, '含酒精饮料', '三粮小麦(55度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2316, '含酒精饮料', '丝路春酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2317, '含酒精饮料', '特制汉酒(59.9度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2318, '含酒精饮料', '特制三粮酒(56.2度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2319, '含酒精饮料', '乌林春酒(青稞酒)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2320, '含酒精饮料', '五酿春(44.4度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2321, '含酒精饮料', '小麦酒(48度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2322, '含酒精饮料', '啤酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2323, '含酒精饮料', '北京啤酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2324, '含酒精饮料', '北京特制啤酒(6度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2325, '含酒精饮料', '楚天啤酒(2.6度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2326, '含酒精饮料', '酒泉啤酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2327, '含酒精饮料', '麦饭石啤酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2328, '含酒精饮料', '美雪啤酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2329, '含酒精饮料', '秦海啤酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2330, '含酒精饮料', '清爽型啤酒(6度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2331, '含酒精饮料', '特制啤酒(5度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2332, '含酒精饮料', '维生素C啤酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2333, '含酒精饮料', '武汉啤酒(3.2度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2334, '含酒精饮料', '五星啤酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2335, '含酒精饮料', '行吟阁啤酒(3.2度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2336, '含酒精饮料', '葡萄酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2337, '含酒精饮料', '白葡萄酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2338, '含酒精饮料', '红葡萄酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2339, '含酒精饮料', '玫瑰香葡萄酒(15度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2340, '含酒精饮料', '黄酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2341, '含酒精饮料', '贡米佳酿(14度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2342, '含酒精饮料', '加饭黄酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2343, '含酒精饮料', '江米酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2344, '含酒精饮料', '糯香酒(6.4度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2345, '含酒精饮料', '善酿酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2346, '含酒精饮料', '绍兴黄酒(15度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2347, '含酒精饮料', '元红黄酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2348, '含酒精饮料', '碧绿酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2349, '含酒精饮料', '崇明老白酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2350, '含酒精饮料', '低度汉酒(37.2度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2351, '含酒精饮料', '二锅头(58度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2352, '含酒精饮料', '甘州大曲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2353, '含酒精饮料', '汉口白酒(49.6度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2354, '含酒精饮料', '汉口小麦酒(40.7度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2355, '含酒精饮料', '黄鹤楼酒(39度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2356, '含酒精饮料', '精制小麦酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2357, '含酒精饮料', '景泰大曲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2358, '含酒精饮料', '景泰二曲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2359, '含酒精饮料', '小麦酒(50度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2360, '含酒精饮料', '燕岭春(57度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2361, '含酒精饮料', '醉流霞(57度)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2362, '含酒精饮料', '蜜酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2363, '含酒精饮料', '双喜沙棘酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2364, '含酒精饮料', '香雪酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2365, '含酒精饮料', '中华沙棘酒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2366, '糖、蜜饯类', '水晶糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2367, '糖、蜜饯类', '白砂糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2368, '糖、蜜饯类', '绵白糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2369, '糖、蜜饯类', '冰糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2370, '糖、蜜饯类', '红糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2371, '糖、蜜饯类', '麦芽糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2372, '糖、蜜饯类', '蜂蜜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2373, '糖、蜜饯类', '花生牛轧糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2374, '糖、蜜饯类', '胶姆糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2375, '糖、蜜饯类', '马蹄软糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2376, '糖、蜜饯类', '奶糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2377, '糖、蜜饯类', '泡泡糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2378, '糖、蜜饯类', '棉花糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2379, '糖、蜜饯类', '巧克力(酒芯)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2380, '糖、蜜饯类', '巧克力(维夫)[朱古力威化]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2381, '糖、蜜饯类', '山楂球', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2382, '糖、蜜饯类', '什锦糖果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2383, '糖、蜜饯类', '酥糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2384, '糖、蜜饯类', '酸三色糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2385, '糖、蜜饯类', '鲜桃果汁糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2386, '糖、蜜饯类', '芝麻南糖', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2387, '糖、蜜饯类', '海棠脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2388, '糖、蜜饯类', '李广杏脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2389, '糖、蜜饯类', '南瓜果脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2390, '糖、蜜饯类', '苹果脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2391, '糖、蜜饯类', '青梅果脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2392, '糖、蜜饯类', '桃脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2393, '糖、蜜饯类', '西瓜脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2394, '糖、蜜饯类', '杏脯', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2395, '糖、蜜饯类', '金糕', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2396, '糖、蜜饯类', '金糕条[山楂条]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2397, '糖、蜜饯类', '山楂果丹皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2398, '糖、蜜饯类', '巧克力', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2399, '油脂类', '调和油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2400, '油脂类', '麻子籽', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2401, '油脂类', '胡麻油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2402, '油脂类', '豆油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2403, '油脂类', '猪油(炼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2404, '油脂类', '芝麻油[香油]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2405, '油脂类', '牛油(炼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2406, '油脂类', '鸭油(炼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2407, '油脂类', '羊油(板油)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2408, '油脂类', '羊油(炼)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2409, '油脂类', '猪油(板油)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2410, '油脂类', '菜籽油[青油]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2411, '油脂类', '茶油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2412, '油脂类', '大麻油[粟米油]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2413, '油脂类', '红花油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2414, '油脂类', '混合油(菜+棕)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2415, '油脂类', '葵花子油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2416, '油脂类', '辣椒油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2417, '油脂类', '麦胚油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2418, '油脂类', '棉籽油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2419, '油脂类', '色拉油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2420, '油脂类', '椰子油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2421, '油脂类', '玉米油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2422, '油脂类', '棕榈油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2423, '油脂类', '花生油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2424, '油脂类', '橄榄油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2425, '油脂类', '牛油(板油)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2426, '调味品类', '蚝油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2427, '调味品类', '蓝莓酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2428, '调味品类', '酱油(高级)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2429, '调味品类', '酱油(一级)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2430, '调味品类', '酱油(三级)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2431, '调味品类', '酱油(冬菇)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2432, '调味品类', '酱油(多味)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2433, '调味品类', '酱油(三鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2434, '调味品类', '酱油(晒制)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2435, '调味品类', '酱油(特母)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2436, '调味品类', '酱油(味精)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2437, '调味品类', '醋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2438, '调味品类', '白醋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2439, '调味品类', '陈醋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2440, '调味品类', '甘醋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2441, '调味品类', '黑醋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2442, '调味品类', '五香醋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2443, '调味品类', '香醋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2444, '调味品类', '熏醋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2445, '调味品类', '豆瓣酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2446, '调味品类', '豆瓣酱(辣油)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2447, '调味品类', '豆瓣辣酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2448, '调味品类', '花生酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2449, '调味品类', '黄酱[大酱]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2450, '调味品类', '酱油膏', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2451, '调味品类', '辣椒酱[辣椒糊]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2452, '调味品类', '麻辣酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2453, '调味品类', '牛肉辣瓣酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2454, '调味品类', '蒜蓉辣酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2455, '调味品类', '五香豆豉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2456, '调味品类', '香油辣酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2457, '调味品类', '芝麻酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2458, '调味品类', '郫县辣酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2459, '调味品类', '海鲜酱(阿香婆)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2460, '调味品类', '牛肉酱(阿香婆)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2461, '调味品类', '沙拉酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2462, '调味品类', '奶油攀司', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2463, '调味品类', '草莓酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2464, '调味品类', '番茄酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2465, '调味品类', '柠檬酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2466, '调味品类', '桃酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2467, '调味品类', '杏酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2468, '调味品类', '番茄沙司', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2469, '调味品类', '腐乳(白)[酱豆腐]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2470, '调味品类', '腐乳(臭)[臭豆腐]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2471, '调味品类', '腐乳(红)[酱豆腐]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2472, '调味品类', '桂林腐乳', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2473, '调味品类', '糟豆腐乳[糟乳]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2474, '调味品类', '八宝菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2475, '调味品类', '冬菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2476, '调味品类', '狗芽菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2477, '调味品类', '桂花大头菜[佛手疙瘩]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2478, '调味品类', '合锦菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2479, '调味品类', '姜(糟)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2480, '调味品类', '酱包瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2481, '调味品类', '酱大头菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2482, '调味品类', '酱甘露[地蚕，甘露子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2483, '调味品类', '酱黄瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2484, '调味品类', '酱萝卜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2485, '调味品类', '酱蘑菇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2486, '调味品类', '酱苤蓝丝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2487, '调味品类', '酱莴笋', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2488, '调味品类', '芥菜干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2489, '调味品类', '金钱萝卜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2490, '调味品类', '辣萝卜条', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2491, '调味品类', '萝卜干', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2492, '调味品类', '乳黄瓜[嫩黄瓜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2493, '调味品类', '什锦菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2494, '调味品类', '酸芥菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2495, '调味品类', '蒜头(酱)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2496, '调味品类', '蒜头(甜)[糖蒜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2497, '调味品类', '甜辣黄瓜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2498, '调味品类', '甜酸皎头', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2499, '调味品类', '咸沙葱[蒙古韭]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2500, '调味品类', '洋姜(腌)[菊芋，鬼子姜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2501, '调味品类', '榨菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2502, '调味品类', '蕨菜(腌)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2503, '调味品类', '腌芥菜头[水芥，水疙瘩]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2504, '调味品类', '腌芥菜头(煮)[煮芥，煮疙瘩]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2505, '调味品类', '腌韭菜花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2506, '调味品类', '腌龙须菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2507, '调味品类', '腌雪里红', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2508, '调味品类', '八角[大料，大茴香]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2509, '调味品类', '胡椒粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2510, '调味品类', '花椒', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2511, '调味品类', '黄毛籽', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2512, '调味品类', '芥茉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2513, '调味品类', '苦豆子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2514, '调味品类', '辣椒粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2515, '调味品类', '全料蒸肉粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2516, '调味品类', '五香粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2517, '调味品类', '茴香籽[小茴香籽]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2518, '调味品类', '咖喱粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2519, '调味品类', '湖盐[青盐]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2520, '调味品类', '精盐', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2521, '调味品类', '土盐', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2522, '调味品类', '味精', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2523, '调味品类', '鸡粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2524, '调味品类', '酵母(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2525, '调味品类', '酵母(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2526, '调味品类', '鸡精', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2527, '调味品类', '鲜味汁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2528, '调味品类', '酱油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2529, '调味品类', '五香大头菜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2530, '调味品类', '苹果酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2531, '调味品类', '甜面酱', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2532, '药食两用食物及其它', '阿胶', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2533, '药食两用食物及其它', '白术', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2534, '药食两用食物及其它', '巴戟天', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2535, '药食两用食物及其它', '霸王花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2536, '药食两用食物及其它', '北芪', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2537, '药食两用食物及其它', '贝壳粉', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2538, '药食两用食物及其它', '北杏仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2539, '药食两用食物及其它', '蚕蛹', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2540, '药食两用食物及其它', '虫草花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2541, '药食两用食物及其它', '川贝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2542, '药食两用食物及其它', '茨实', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2543, '药食两用食物及其它', '冬虫夏草[虫草]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2544, '药食两用食物及其它', '杜仲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2545, '药食两用食物及其它', '饭铲头蛇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2546, '药食两用食物及其它', '高丽参', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2547, '药食两用食物及其它', '过树榕蛇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2548, '药食两用食物及其它', '海底椰', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2549, '药食两用食物及其它', '何首乌', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2550, '药食两用食物及其它', '黄桐木（含毒性）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2551, '药食两用食物及其它', '花旗参', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2552, '药食两用食物及其它', '甲鱼[鳖]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2553, '药食两用食物及其它', '锦蛇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2554, '药食两用食物及其它', '金银花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2555, '药食两用食物及其它', '雷公根', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2556, '药食两用食物及其它', '麦冬', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2557, '药食两用食物及其它', '茅根', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2558, '药食两用食物及其它', '南杏仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2559, '药食两用食物及其它', '三索线蛇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2560, '药食两用食物及其它', '沙参', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2561, '药食两用食物及其它', '山姜子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2562, '药食两用食物及其它', '蛇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2563, '药食两用食物及其它', '石斛', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2564, '药食两用食物及其它', '水蛇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2565, '药食两用食物及其它', '太子参', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2566, '药食两用食物及其它', '田基黄', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2567, '药食两用食物及其它', '田鸡[青蛙]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2568, '药食两用食物及其它', '田鸡腿[青蛙腿]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2569, '药食两用食物及其它', '天麻', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2570, '药食两用食物及其它', '土茯苓', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2571, '药食两用食物及其它', '五指毛桃', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2572, '药食两用食物及其它', '蝎子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2573, '药食两用食物及其它', '溪黄草', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2574, '药食两用食物及其它', '益智', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2575, '药食两用食物及其它', '中国鲎[水鳖子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2576, '药食两用食物及其它', '白苏', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2577, '药食两用食物及其它', '马鹿胎(粉)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2578, '药食两用食物及其它', '蜂胶液', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2579, '药食两用食物及其它', '蛤蟆油', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2580, '药食两用食物及其它', '龟甲', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2581, '药食两用食物及其它', '刺猬皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2582, '药食两用食物及其它', '蜂王浆', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2583, '药食两用食物及其它', '裙边(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2584, '药食两用食物及其它', '鱼肚(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2585, '药食两用食物及其它', '鱼唇(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2586, '药食两用食物及其它', '阿胶（2018）', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2587, '药食两用食物及其它', '珍珠', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2588, '药食两用食物及其它', '燕窝', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2589, '药食两用食物及其它', '白芷', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2590, '药食两用食物及其它', '藿香叶(鲜)[兜娄婆香]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2591, '药食两用食物及其它', '枸杞子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2592, '药食两用食物及其它', '蜂蛹[蜂胚、蜂仔]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2593, '药食两用食物及其它', '蜂蛹(油蜂，干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2594, '药食两用食物及其它', '蜂蛹(大黄蜂)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2595, '药食两用食物及其它', '牛蛙', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2596, '药食两用食物及其它', '鸡内金', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2597, '药食两用食物及其它', '乌梢蛇', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2598, '药食两用食物及其它', '团螵蛸', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2599, '药食两用食物及其它', '薄荷(干)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2600, '药食两用食物及其它', '薄荷(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2601, '药食两用食物及其它', '北五味子叶(鲜)[五味子，秤砣子]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2602, '药食两用食物及其它', '车前(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2603, '药食两用食物及其它', '车前子(鲜)[车轮菜]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2604, '药食两用食物及其它', '陈皮', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2605, '药食两用食物及其它', '丁香', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2606, '药食两用食物及其它', '防风(根，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2607, '药食两用食物及其它', '防风(叶，鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2608, '药食两用食物及其它', '甘草', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2609, '药食两用食物及其它', '高良姜', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2610, '药食两用食物及其它', '红花', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2611, '药食两用食物及其它', '虎杖(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2612, '药食两用食物及其它', '菊花[怀菊花]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2613, '药食两用食物及其它', '决明(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2614, '药食两用食物及其它', '蛤蚧', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2615, '药食两用食物及其它', '莱菔子', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2616, '药食两用食物及其它', '罗汉果', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2617, '药食两用食物及其它', '木榧[园榧]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2618, '药食两用食物及其它', '肉豆蔻', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2619, '药食两用食物及其它', '肉桂', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2620, '药食两用食物及其它', '砂仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2621, '药食两用食物及其它', '桃仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2622, '药食两用食物及其它', '乌梅', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2623, '药食两用食物及其它', '郁李仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2624, '药食两用食物及其它', '枣仁', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2625, '药食两用食物及其它', '紫苏', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2626, '药食两用食物及其它', '紫苏(鲜)[赤苏，白苏]', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2627, '药食两用食物及其它', '茯苓', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2628, '药食两用食物及其它', '藿香', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2629, '药食两用食物及其它', '藿香(鲜)', NULL, NULL, NULL, NULL, NULL, NULL, 1);
INSERT INTO `t_check_food` VALUES (2630, '药食两用食物及其它', '牛黄', NULL, NULL, NULL, NULL, NULL, NULL, 1);

-- ----------------------------
-- Table structure for t_check_illness
-- ----------------------------
CREATE TABLE `t_check_illness`  (
  `illness_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '病情编号',
  `illness_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '病情名称',
  `illness_code` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `follow` int(4) NULL DEFAULT 0 COMMENT '是否关注(1关注 默认0不关注）',
  `parent_code` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `illness_level` int(4) NULL DEFAULT 0 COMMENT '级别(1病情 2症状 )',
  `line_number` int(4) NULL DEFAULT 0 COMMENT '顺序号',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  `parent_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '病情上级name',
  `symptom_ids` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '症状集合(id用逗号分开)',
  PRIMARY KEY (`illness_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '考勤疾病表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_illness_symptom
-- ----------------------------
CREATE TABLE `t_check_illness_symptom`  (
  `symptom_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '症状编号',
  `symptom_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '症状名称',
  `line_number` int(4) NULL DEFAULT 0 COMMENT '顺序号',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`symptom_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '疾病症状表' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_check_illness_warning
-- ----------------------------
CREATE TABLE `t_check_illness_warning`  (
  `warning_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主键',
  `warning_ranges_type` int(11) NULL DEFAULT NULL COMMENT '1：全校区 2：年级 3：班级',
  `illness_dict_code` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '病情标示',
  `illness_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '病情名称',
  `warning_num` int(11) NULL DEFAULT 1 COMMENT '预警阀值（人数）',
  `user_ids` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '编号集合，逗号分开',
  `user_names` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '姓名集合，逗号分开',
  `warning_status` int(11) NULL DEFAULT NULL COMMENT '状态(1启用。0禁用),有可能一段时间内取消预警',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` tinyint(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`warning_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '病情预警信息表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_lunch_access_record
-- ----------------------------
CREATE TABLE `t_check_lunch_access_record`  (
  `record_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '流水id',
  `lunch_student_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生登记id',
  `out_time` datetime(0) NULL DEFAULT NULL COMMENT '出校时间',
  `return_time` datetime(0) NULL DEFAULT NULL COMMENT '返校时间',
  `status` int(11) NULL DEFAULT 1 COMMENT '状态 ，默认为1：未离校，2已离校，3：已返校',
  PRIMARY KEY (`record_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '中午回家用餐学生登记' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_check_lunch_student
-- ----------------------------
CREATE TABLE `t_check_lunch_student`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '1' COMMENT '流水id',
  `term_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学年学期',
  `district_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区标示',
  `district_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区',
  `faculty_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部标示',
  `faculty_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部',
  `grade_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级标示',
  `grade_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级',
  `class_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级标示',
  `class_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级',
  `student_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生标示',
  `student_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `status` int(11) NULL DEFAULT 1 COMMENT '状态（默认1：有效，0：无效）',
  `is_transfer` int(11) NULL DEFAULT 1 COMMENT '是否家长接送（1：家长接，0：不接）',
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_user_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_user_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(11) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '中午回家用餐学生登记' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_check_student_injury
-- ----------------------------
CREATE TABLE `t_check_student_injury`  (
  `injury_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '记录id',
  `term_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学年学期',
  `district_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区标示',
  `district_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区',
  `faculty_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部标示',
  `faculty_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部',
  `grade_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级标示',
  `grade_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级',
  `class_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级标示',
  `class_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级',
  `student_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生标示',
  `student_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `Injury_time` datetime(0) NULL DEFAULT NULL COMMENT '伤病时间',
  `Injury_address` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '伤病地点',
  `subject_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '课种(学科)',
  `Injury_content` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '受伤情况',
  `Injury_treatment` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '处理情况',
  `together_student_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '陪同人员id',
  `together_student_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '陪同人员name',
  `together_teacher_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '老师到场id',
  `together_teacher_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '老师到场name',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` tinyint(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  `sex` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '性别(男、女）',
  `illness_process` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '病程',
  `chief_symptom` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '主诉症状',
  `simple_check` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '简单检查',
  `register_type` int(4) NULL DEFAULT NULL COMMENT '登记类型，1：外伤登记、2：看病登记',
  PRIMARY KEY (`injury_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '学生外伤信息表' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_check_student_lunch
-- ----------------------------
CREATE TABLE `t_check_student_lunch`  (
  `lunch_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主键编号',
  `term_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '报名学期',
  `district_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区标示',
  `district_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区',
  `faculty_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部标示',
  `faculty_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在学部',
  `grade_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级标示',
  `grade_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在年级',
  `class_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级标示',
  `class_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在班级',
  `student_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生标示',
  `student_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生姓名',
  `lunch_status` int(4) NULL DEFAULT 0 COMMENT '午餐报名状态(1吃 0不吃)',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`lunch_id`) USING BTREE,
  INDEX `index_student_id`(`student_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_check_ticket
-- ----------------------------
CREATE TABLE `t_check_ticket`  (
  `ticket_id` int(100) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `ticket_content` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '内容',
  PRIMARY KEY (`ticket_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_check_time_config
-- ----------------------------
CREATE TABLE `t_check_time_config`  (
  `config_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主键编号',
  `term_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所属学期',
  `grade_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '年级标示',
  `grade_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '年级名称',
  `weeks_num` int(4) NULL DEFAULT 0 COMMENT '周数',
  `on_shcool_time` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '上学时间',
  `out_shcool_time` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '放学时间',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`config_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '学校上放学时间配置' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_class
-- ----------------------------
CREATE TABLE `t_class`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `GRADE_GLOBAL_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '年级ID',
  `NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '班级名称',
  `GLOBAL_ID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `TEACHER_GLOBAL_ID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '班主任',
  `ROWID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CLASS_NO` int(11) NULL DEFAULT NULL COMMENT '班主任',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `t_class_index1`(`GLOBAL_ID`) USING BTREE,
  INDEX `t_class_index2`(`TEACHER_GLOBAL_ID`) USING BTREE,
  INDEX `t_class_index3`(`GRADE_GLOBAL_ID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '班级表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_district
-- ----------------------------
CREATE TABLE `t_district`  (
  `ID` bigint(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `GLOBAL_ID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '唯一标示',
  `SCHOOL_GLOBAL_ID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '' COMMENT '所属学校ID',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '校区表' ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for t_faculty
-- ----------------------------
CREATE TABLE `t_faculty`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '名称',
  `REMARK` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '描述',
  `GLOBAL_ID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'guid',
  `rowid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `SCHOOL_GLOBAL_ID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所属学校',
  `DISTRICT_GLOBAL_ID` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所属校区',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `t_fac_index1`(`GLOBAL_ID`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '学部表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for t_family_info
-- ----------------------------
CREATE TABLE `t_family_info`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `student_guid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学生id',
  `relation` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '关系',
  `parent_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '家长姓名',
  `parent_email` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '家长邮件',
  `telno` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '电话',
  `global_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '唯一标示',
  `guardian` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '监护人',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `t_fam_index1`(`global_id`) USING BTREE,
  INDEX `t_fam_index2`(`student_guid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '家长表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_grade
-- ----------------------------
CREATE TABLE `t_grade`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `LEVELS` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `SESSIONS` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `GLOBAL_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `FACUKTY_GLOBAL_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ROWID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `teacher_global_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '年级组长',
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `t_grade_index1`(`GLOBAL_ID`) USING BTREE,
  INDEX `t_grade_index2`(`FACUKTY_GLOBAL_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '年级表' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_member_unit_rel
-- ----------------------------
CREATE TABLE `t_member_unit_rel`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `MEMBER_GLOBAL_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `UNIT_GLOBAL_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  INDEX `index_MEMBER_GLOBAL_ID`(`MEMBER_GLOBAL_ID`) USING BTREE,
  INDEX `index_UNIT_GLOBAL_ID`(`UNIT_GLOBAL_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_school
-- ----------------------------
CREATE TABLE `t_school`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '主键',
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_school_year_term
-- ----------------------------
CREATE TABLE `t_school_year_term`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `morning_class_sessions` bigint(20) NULL DEFAULT NULL COMMENT '上午上课节数',
  `school_year_start_time` date NULL DEFAULT NULL COMMENT '学年开始日期',
  `school_year_end_time` date NULL DEFAULT NULL COMMENT '学年结束日期',
  `term_year_end_time` date NULL DEFAULT NULL COMMENT '学期结束日期',
  `term_year_start_time` date NULL DEFAULT NULL COMMENT '学期开始日期',
  `term_type` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学期类型',
  `school_global_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学校标识号',
  `valid_class_week` int(11) NULL DEFAULT NULL COMMENT '有效上课周数',
  `global_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '标识号',
  `class_days_per_week` int(11) NULL DEFAULT NULL COMMENT '每周上课天数',
  `daily_lessons` int(11) NULL DEFAULT NULL COMMENT '每天上课节数',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '学年学期' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_school_year_term_cur
-- ----------------------------
CREATE TABLE `t_school_year_term_cur`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `term_global_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学期标识',
  `school_global_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学校标识',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '当前学年学期' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_student
-- ----------------------------
CREATE TABLE `t_student`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CLASS_GLOBAL_ID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `STUDENT_NO` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PASSWORD` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CREATE_TIME` datetime(0) NULL DEFAULT NULL,
  `GLOBAL_ID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `PINYIN` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `rowid` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `sex` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `at_school` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `photo_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_subject
-- ----------------------------
CREATE TABLE `t_subject`  (
  `id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学科名称',
  `areaid` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所属学习领域',
  `global_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '唯一标示',
  `subjectbh` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学科编号',
  `subjectjc` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '学科简称',
  `subjectbz` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  `sourceflag` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `nullify_flag` varchar(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT '0' COMMENT '删除标志1为作废，0为正常',
  `sort` int(4) NULL DEFAULT 0,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '学科' ROW_FORMAT = Dynamic;


-- ----------------------------
-- Records of t_sync
-- ----------------------------
INSERT INTO `t_sync` VALUES (1);

-- ----------------------------
-- Table structure for t_sys_attachment
-- ----------------------------
CREATE TABLE `t_sys_attachment`  (
  `attachment_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `attachment_type` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '类型(对应application中的uploadfiledir类型)',
  `attachment_size` double NULL DEFAULT NULL COMMENT '名称',
  `file_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '文件名称(取当前时间戳,后10位)',
  `real_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '真实文件名称',
  `content_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '附件类型',
  `object_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '对象名称（业务主键编号)',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '用户编号',
  `file_path` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '路径',
  PRIMARY KEY (`attachment_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统附件表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_sys_calendar
-- ----------------------------
CREATE TABLE `t_sys_calendar`  (
  `CALENDAR_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '日期编号',
  `DISTRICT_ID` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所在校区标示',
  `DAY_CODE` date NOT NULL COMMENT '日期',
  `WEEK_CODE` int(11) NOT NULL COMMENT '星期编号',
  `CALENDAR_TYPE` int(11) NOT NULL COMMENT '假期/工作日(1：工作日。0：假期）',
  `CREATE_USER_ID` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建用户',
  `CREATE_USER_NAME` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建用户姓名',
  `CREATE_DATE` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `UPDATE_USER_ID` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '修改用户',
  `UPDATE_USER_NAME` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '修改用户姓名',
  `UPDATE_DATE` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  `IS_VALID` int(11) NULL DEFAULT 1 COMMENT '(默认1,删除后0无效)',
  PRIMARY KEY (`CALENDAR_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统日历表' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_sys_config
-- ----------------------------
CREATE TABLE `t_sys_config`  (
  `config_id` int(10) NOT NULL AUTO_INCREMENT COMMENT '配置编号',
  `config_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '配置名称',
  `config_type` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '配置类型。数据字典定义\r\n            (单选radio多选checkbox列表选择select文本text文本域textarea',
  `config_key` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '配置key(根据配置类型来存储，用逗号“，”来区分数据项',
  `config_value` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '值',
  `config_select_values` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '可选项值(用逗号分隔)',
  `config_status` int(11) NULL DEFAULT 1 COMMENT '状态(1有效<默认>，0无效）',
  `line_number` int(11) NULL DEFAULT 0 COMMENT '顺序号',
  `description` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`config_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 24 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_sys_config
-- ----------------------------
INSERT INTO `t_sys_config` VALUES (1, '班主任午饭预定状态', 'RADIOBOX', 'meal_status', '开放', '开放,关闭', 1, 1, '午饭设定，只在学期开学的时候来设置，平时做关闭');
INSERT INTO `t_sys_config` VALUES (2, '系统名称', 'TEXT', 'system_name', '校园安全管理系统', NULL, 1, 1, '系统名称可配置');
INSERT INTO `t_sys_config` VALUES (3, '系统样式', 'SELECT', 'system_style', 'blue', 'red,blue', 1, 2, '修改后，系统整个样式将改变。');
INSERT INTO `t_sys_config` VALUES (4, '临时考勤上报昨天', 'RADIOBOX', 'check_temp', '关闭', '开放,关闭', 1, 0, NULL);
INSERT INTO `t_sys_config` VALUES (5, '学生照片访问路径', 'TEXT', 'photo_url', 'http://192.168.100.238/user/images/userheads', NULL, 1, 3, '学生照片访问路径');
INSERT INTO `t_sys_config` VALUES (6, '消息推送地址', 'TEXT', 'message_push_url', 'http://127.0.0.1/messageservice/api/saveMessageAppPushmessage', NULL, 1, 4, '消息推送地址');
INSERT INTO `t_sys_config` VALUES (7, '消息应用id', 'TEXT', 'appid', 'messageservice_checkiso', NULL, 1, 5, '消息应用id');
INSERT INTO `t_sys_config` VALUES (8, '消息应用秘钥', 'TEXT', 'messageSercet', 'a118b8760bb7462b96747292c61b61f2', NULL, 1, 6, '消息应用秘钥');
INSERT INTO `t_sys_config` VALUES (9, '消息回调地址', 'TEXT', 'messageShortUrl', 'http://127.0.0.1/checkiso/messagePushInfo', NULL, 1, 7, '消息回调地址');
INSERT INTO `t_sys_config` VALUES (10, '消息推送设备类型', 'TEXT', 'deviceType', '1', NULL, 1, 8, '类型设备类别0:PC ;1:手机;2：pad');
INSERT INTO `t_sys_config` VALUES (11, '消息应用名称', 'TEXT', 'appName', '校园安全管理系统', NULL, 1, 9, '消息应用名称');
INSERT INTO `t_sys_config` VALUES (12, '文件上传路径', 'TEXT', 'uploadfiledir', '/webapp/zklcfile/checkfile', NULL, 1, 10, '件上传路径;old:/zklcfile/checkfile');
INSERT INTO `t_sys_config` VALUES (13, '企业微信id', 'TEXT', 'qywxCorpid', 'wwfed49d24c5f1da18', NULL, 1, 0, '企业微信id');
INSERT INTO `t_sys_config` VALUES (14, '企业微信密钥', 'TEXT', 'qywxSecret', '9fD0u94CwUvNVGowo2mbzsEH0aShyEWxgsD9JH5yM0M', NULL, 1, 0, '企业微信密钥');
INSERT INTO `t_sys_config` VALUES (15, '企业微信获取token路径', 'TEXT', 'qywxGettokenUrl', 'https://qyapi.weixin.qq.com/cgi-bin/gettoken', NULL, 1, 0, '企业微信获取token路径');
INSERT INTO `t_sys_config` VALUES (16, '企业微信获取jsApiTicket路径', 'TEXT', 'getJsApiTicketUrl', 'https://qyapi.weixin.qq.com/cgi-bin/get_jsapi_ticket', NULL, 1, 0, '企业微信获取jsApiTicket路径');
INSERT INTO `t_sys_config` VALUES (17, '企业微信图片素材获取路径', 'TEXT', 'getMediaUrl', 'https://qyapi.weixin.qq.com/cgi-bin/media/get', NULL, 1, 0, '企业微信图片素材获取路径');
INSERT INTO `t_sys_config` VALUES (18, '是否开启企业微信功能', 'RADIOBOX', 'is_open_qywx', '关闭', '开启,关闭', 1, 0, '是否开启企业微信功能');
INSERT INTO `t_sys_config` VALUES (19, '用餐统计时间', 'TEXT', 'eat_statistics_time', '15:00', NULL, 1, 0, '用餐统计时间');
INSERT INTO `t_sys_config` VALUES (20, '确认考勤时间设置(次月的第几天)', 'TEXT', 'confirm_check_time', '1', NULL, 1, 0, '确认考勤时间设置(次月的第几天)');
INSERT INTO `t_sys_config` VALUES (21, '家长请假时间设置', 'TEXT', 'parent_leave_time', '10:00', NULL, 1, 0, '家长请假时间设置');
INSERT INTO `t_sys_config` VALUES (22, '上课时间设置', 'TEXT', 'class_time', '8:30-17:30', NULL, 1, 0, '上课时间设置');
INSERT INTO `t_sys_config` VALUES (23, '最小请假时长设置(小时)', 'TEXT', 'min_leave_time', '2', NULL, 1, 0, '最小请假时长设置(小时)');

-- ----------------------------
-- Table structure for t_sys_dictionarys
-- ----------------------------
CREATE TABLE `t_sys_dictionarys`  (
  `DICT_ID` int(10) NOT NULL AUTO_INCREMENT,
  `DICT_TYPE` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'G-字典组,I-字典项',
  `GROUP_CODE` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CODE` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '插入业务表的值',
  `NAME` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `STATUS` int(1) NULL DEFAULT 1 COMMENT '0:禁用 1:启用',
  `LINE_NUMBER` int(1) NULL DEFAULT NULL,
  `DES` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`DICT_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_sys_dictionarys
-- ----------------------------
INSERT INTO `t_sys_dictionarys` VALUES (1, 'I', 'POST_TYPE', 'TEACHER', '教师', 1, 1, '暂无');
INSERT INTO `t_sys_dictionarys` VALUES (2, 'I', 'POST_TYPE', 'STUDENT', '学生', 1, 2, '暂无');
INSERT INTO `t_sys_dictionarys` VALUES (18, 'G', NULL, 'POST_TYPE', '角色类型', 1, 1, '暂无');
INSERT INTO `t_sys_dictionarys` VALUES (82, 'G', '', 'USER_TYPE', '用户类型', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (83, 'I', 'USER_TYPE', '100020', '教师', 1, 2, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (84, 'I', 'USER_TYPE', '100010', '学生', 1, 1, '备注');
INSERT INTO `t_sys_dictionarys` VALUES (85, 'I', 'USER_TYPE', '100040', '管理员', 1, 3, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (86, 'I', 'USER_TYPE', '100030', '其他', 1, 4, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (87, 'G', NULL, 'INFO_TYPE', '信息类型', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (88, 'I', 'INFO_TYPE', 'SYSTEMINFO', '系统信息', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (89, 'I', 'INFO_TYPE', 'MUSTREADINFO', '必读信息', 1, 2, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (90, 'I', 'INFO_TYPE', 'WARNINGINFO', '预警信息', 1, 3, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (91, 'I', 'INFO_TYPE', 'REMINDINFO', '提醒信息', 1, 4, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (95, 'I', 'sdfgd', '14321123', '分第三个电饭锅111', 1, 124323111, '宋代法规第三宋代法规11');
INSERT INTO `t_sys_dictionarys` VALUES (96, 'G', NULL, 'SYS_CONFIG_TYPE', '系统配置类型', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (97, 'I', 'SYS_CONFIG_TYPE', 'RADIOBOX', '单选', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (98, 'I', 'SYS_CONFIG_TYPE', 'CHECKBOX', '多选', 1, 2, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (99, 'I', 'SYS_CONFIG_TYPE', 'TEXT', '输入框', 1, 3, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (100, 'I', 'SYS_CONFIG_TYPE', 'TEXTAREA', '本文以', 1, 4, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (101, 'I', 'SYS_CONFIG_TYPE', 'SELECT', '下拉列表', 1, 5, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (102, 'G', NULL, 'MISSING_CLASS_TYPE', '缺课原因', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (103, 'I', 'MISSING_CLASS_TYPE', '100101', '疾病', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (104, 'I', 'MISSING_CLASS_TYPE', '100102', '伤害', 1, 2, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (105, 'I', 'MISSING_CLASS_TYPE', '100103', '其他', 1, 3, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (106, 'G', NULL, '101', '餐别', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (107, 'I', '101', '101001', '早餐', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (108, 'I', '101', '101002', '加餐', 1, 2, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (109, 'I', '101', '101003', '午餐', 1, 3, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (110, 'I', '101', '101004', '午点', 1, 4, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (111, 'G', NULL, '102', '过敏程度', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (112, 'I', '102', '102001', '低度过敏', 1, 1, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (113, 'I', '102', '102002', '中度过敏', 1, 2, NULL);
INSERT INTO `t_sys_dictionarys` VALUES (114, 'I', '102', '102003', '高度过敏', 1, 3, NULL);

-- ----------------------------
-- Table structure for t_sys_info
-- ----------------------------
CREATE TABLE `t_sys_info`  (
  `info_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '信息编号',
  `info_type` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '信息类型(数据字典)',
  `info_name` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '标题',
  `info_content` varchar(2000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '内容',
  `info_status` int(11) NULL DEFAULT 1 COMMENT '状态(默认是0未发布，1为已发布）',
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建用户编号',
  `create_user_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建用户姓名',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `is_valid` int(11) NULL DEFAULT 1 COMMENT '(默认1,删除后0无效)',
  PRIMARY KEY (`info_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统信息表' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_sys_info_publish
-- ----------------------------
CREATE TABLE `t_sys_info_publish`  (
  `user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '用户编号',
  `info_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '信息编号',
  `read_status` int(11) NULL DEFAULT 0 COMMENT '状态(默认是0 未读。1为已读）',
  `read_time` datetime(0) NULL DEFAULT NULL COMMENT '阅读时间',
  PRIMARY KEY (`user_id`, `info_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统信息发送表' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_sys_menu
-- ----------------------------
CREATE TABLE `t_sys_menu`  (
  `menu_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '按钮编号',
  `menu_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '菜单名称',
  `menu_level` int(11) NULL DEFAULT NULL COMMENT '等级(1、2)',
  `parent_id` int(11) NULL DEFAULT NULL COMMENT '父类编号',
  `menu_status` int(11) NULL DEFAULT NULL COMMENT '状态(1有效,0无效)',
  `line_number` int(11) NULL DEFAULT NULL COMMENT '顺序号',
  `location` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '跳转地址',
  `menu_type` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '菜单类型(web、app)',
  PRIMARY KEY (`menu_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 52 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统按钮表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_sys_menu
-- ----------------------------
INSERT INTO `t_sys_menu` VALUES (1, '权限管理', 1, NULL, 1, 2, 'perRoleDeploy', 'web');
INSERT INTO `t_sys_menu` VALUES (2, '数据字典', 1, NULL, 1, 1, 'dictList', 'web');
INSERT INTO `t_sys_menu` VALUES (3, '疾病维护', 1, NULL, 1, 4, 'illness', 'web');
INSERT INTO `t_sys_menu` VALUES (4, '假别维护', 1, NULL, 1, 5, 'attendanceManage', 'web');
INSERT INTO `t_sys_menu` VALUES (5, '病情预警设置', 1, NULL, 1, 6, 'illnessWarning', 'web');
INSERT INTO `t_sys_menu` VALUES (6, '校历维护', 1, NULL, 1, 7, 'calendarManage', 'web');
INSERT INTO `t_sys_menu` VALUES (7, '基础数据维护管理员', 1, NULL, 0, 7, 'basicAdministrator', 'web');
INSERT INTO `t_sys_menu` VALUES (8, '班级用餐管理', 1, NULL, 1, 13, 'basicData', 'web');
INSERT INTO `t_sys_menu` VALUES (9, '班级统计(班)', 1, NULL, 1, 10, 'attendanceLogsStatisticsByDate', 'web');
INSERT INTO `t_sys_menu` VALUES (10, '个人统计(班)', 1, NULL, 1, 11, 'attendanceLogsStatisticsByStudent', 'web');
INSERT INTO `t_sys_menu` VALUES (11, '个人统计', 1, NULL, 1, 34, 'attendanceLogsStatisticsByStudent', 'app');
INSERT INTO `t_sys_menu` VALUES (12, '班级统计', 1, NULL, 1, 33, 'attendanceLogsStatisticsByDate', 'app');
INSERT INTO `t_sys_menu` VALUES (13, '教师点名', 1, NULL, 1, 31, 'attendanceData', 'app');
INSERT INTO `t_sys_menu` VALUES (14, '学生考勤', 1, NULL, 1, 32, 'attendanceLxData', 'app');
INSERT INTO `t_sys_menu` VALUES (15, '请假单管理', 1, NULL, 1, 35, 'abnormalList', 'app');
INSERT INTO `t_sys_menu` VALUES (16, '全校考勤汇总(教)', 1, NULL, 1, 14, 'checkStatisticsByDistrict', 'web');
INSERT INTO `t_sys_menu` VALUES (17, '中途离校(教)', 1, NULL, 1, 15, 'webAbnormalLeaveSchool', 'web');
INSERT INTO `t_sys_menu` VALUES (18, '班级考勤(教)', 1, NULL, 0, 3, 'classCheck', 'web');
INSERT INTO `t_sys_menu` VALUES (19, '班级考勤统计(教)', 1, NULL, 0, 4, 'attendanceLogsOfDeanByDate', 'web');
INSERT INTO `t_sys_menu` VALUES (20, '个人考勤统计(教)', 1, NULL, 0, 5, 'attendanceLogsOfDeanByStudent', 'web');
INSERT INTO `t_sys_menu` VALUES (21, '病情汇总(医)', 1, NULL, 1, 16, 'newIllnessStatisticsByDistrict', 'web');
INSERT INTO `t_sys_menu` VALUES (22, '班级考勤(医)', 1, NULL, 0, 2, 'classCheck', 'web');
INSERT INTO `t_sys_menu` VALUES (23, '班级病假汇总(医)', 1, NULL, 0, 3, 'illnessStatisticsByClass', 'web');
INSERT INTO `t_sys_menu` VALUES (24, '个人病假汇总(医)', 1, NULL, 0, 4, 'illnessStatisticsByStudent', 'web');
INSERT INTO `t_sys_menu` VALUES (25, '用餐情况统计', 1, NULL, 1, 18, 'lunchfakemessStatistics2', 'web');
INSERT INTO `t_sys_menu` VALUES (26, '中途离校管理(保)', 1, NULL, 0, 20, 'webAbnormalAttendance', 'web');
INSERT INTO `t_sys_menu` VALUES (27, '教师点名(班)', 1, NULL, 1, 8, 'webAttendanceData', 'web');
INSERT INTO `t_sys_menu` VALUES (29, '学生考勤', 1, NULL, 1, 9, 'webAttendanceLxData', 'web');
INSERT INTO `t_sys_menu` VALUES (30, '请假单管理', 1, NULL, 1, 12, 'webAbnormalList', 'web');
INSERT INTO `t_sys_menu` VALUES (31, '班级订餐查看(食)', 1, NULL, 1, 19, 'eatStatistics', 'web');
INSERT INTO `t_sys_menu` VALUES (32, '症状维护', 1, NULL, 1, 3, 'illnessSymptomList', 'web');
INSERT INTO `t_sys_menu` VALUES (33, '症状汇总(医)', 1, NULL, 1, 17, 'symptomSummary', 'web');
INSERT INTO `t_sys_menu` VALUES (34, '系统配置', 1, NULL, 1, 5, 'systemConfig', 'web');
INSERT INTO `t_sys_menu` VALUES (35, '管理员配置', 1, NULL, 1, 36, 'adminConfig', 'web');
INSERT INTO `t_sys_menu` VALUES (36, '医务室配置', 1, NULL, 1, 37, 'infirmaryConfig', 'web');
INSERT INTO `t_sys_menu` VALUES (38, '考勤统计', 1, NULL, 1, 38, 'attendanceStatistics', 'app');
INSERT INTO `t_sys_menu` VALUES (39, '病情统计', 1, NULL, 1, 39, 'newIllnessStatisticsByDistrict', 'app');
INSERT INTO `t_sys_menu` VALUES (40, '食堂统计', 1, NULL, 1, 40, 'lunchfakemessStatistics', 'app');
INSERT INTO `t_sys_menu` VALUES (41, '离校拍照', 1, NULL, 1, 53, 'appAbnormalAttendance', 'app');
INSERT INTO `t_sys_menu` VALUES (42, '就医登记', 1, NULL, 1, 51, 'appDiseaseGrade', 'app');
INSERT INTO `t_sys_menu` VALUES (43, '就医记录', 1, NULL, 1, 52, 'appDiseaseGradeList', 'app');
INSERT INTO `t_sys_menu` VALUES (44, '就医记录', 1, NULL, 1, 44, 'webDiseaseGradeList', 'web');
INSERT INTO `t_sys_menu` VALUES (45, '就医登记', 1, NULL, 1, 43, 'webDiseaseGrade', 'web');
INSERT INTO `t_sys_menu` VALUES (46, '回家用餐登记', 1, NULL, 1, 54, 'classLunchStudentList', 'app');
INSERT INTO `t_sys_menu` VALUES (47, '回家用餐登记统计', 1, NULL, 1, 47, 'classLunchStudentStatistics', 'web');
INSERT INTO `t_sys_menu` VALUES (48, '过敏信息管理', 1, NULL, 1, 47, 'pcCheckAllergyInfo', 'web');
INSERT INTO `t_sys_menu` VALUES (49, '带量食谱管理', 1, NULL, 1, 48, 'cookbook', 'web');
INSERT INTO `t_sys_menu` VALUES (50, '收费标准管理', 1, NULL, 1, 49, 'chargeList', 'web');
INSERT INTO `t_sys_menu` VALUES (51, '过敏信息管理', 1, NULL, 1, 47, 'checkAllergyInfo', 'app');
INSERT INTO `t_sys_menu` VALUES (52, '收费统计', 1, NULL, 1, 52, 'chargeStatistics', 'web');
INSERT INTO `t_sys_menu` VALUES (53, '考勤统计', 1, NULL, 1, 53, 'attendanceStatistics', 'web');
INSERT INTO `t_sys_menu` VALUES (54, '食物管理', 1, NULL, 1, 54, 'checkFoodList', 'web');


-- ----------------------------
-- Table structure for t_sys_role
-- ----------------------------
CREATE TABLE `t_sys_role`  (
  `ROLE_ID` int(10) NOT NULL AUTO_INCREMENT COMMENT '角色编号',
  `ROLE_NAME` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '角色名称',
  `ROLE_TYPE` int(11) NULL DEFAULT NULL COMMENT '角色类型(1:系统角色，2：业务角色)',
  `ROLE_DES` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '角色描述',
  `MENU_IDS` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '拥有菜单(逗号分开)',
  `MENU_NAMES` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '拥有菜单(逗号分开)',
  `USER_IDS` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '拥有用户(逗号分开)',
  `USER_NAMES` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '拥有用户(逗号分开)',
  `CREATE_USER` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建用户',
  `CREATE_DATE` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '修改用户',
  `UPDATE_DATE` datetime(0) NULL DEFAULT NULL COMMENT '修改时间',
  `IS_VALID` int(11) NULL DEFAULT 1 COMMENT '(默认1,删除后0无效)',
  `ROLE_BUSINESS_TYPE` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '业务角色类型（数据字典获取code)',
  PRIMARY KEY (`ROLE_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_sys_role
-- ----------------------------
INSERT INTO `t_sys_role` VALUES (1, '系统管理员', 1, NULL, '1,34', '权限管理', NULL, NULL, 'admin', '2016-06-04 14:24:50', NULL, NULL, 1, NULL);
INSERT INTO `t_sys_role` VALUES (2, '业务管理员', 1, '', '32,3,6,25,49,50,52,38,54', '症状维护(web),疾病维护(web),校历维护(web),用餐情况统计(web),带量食谱管理(web),收费标准管理(web),收费统计(web),考勤统计(app),食物管理(web)', NULL, NULL, 'admin', '2016-06-04 14:24:50', NULL, NULL, 1, 'TEACHER');
INSERT INTO `t_sys_role` VALUES (3, '食堂', 1, '', '25,49,54', '用餐情况统计(web),带量食谱管理(web),食物管理(web)', NULL, NULL, 'admin', '2016-06-08 09:35:43', NULL, NULL, 1, 'TEACHER');
INSERT INTO `t_sys_role` VALUES (4, '医务室', 1, '', '30,25,48', '请假单管理(web),用餐情况统计(web),过敏信息管理(web)', NULL, NULL, 'admin', '2016-06-08 09:40:54', NULL, NULL, 1, 'TEACHER');
INSERT INTO `t_sys_role` VALUES (5, '教务处', 1, NULL, '', '', '', '', 'admin', '2016-06-08 09:54:37', NULL, NULL, 0, NULL);
INSERT INTO `t_sys_role` VALUES (6, '保卫处', 1, '', '41', '离校拍照(app)', NULL, NULL, 'admin', '2016-06-08 09:55:48', NULL, NULL, 0, 'TEACHER');
INSERT INTO `t_sys_role` VALUES (7, '班主任', 1, '', '29,30,8,25,48,53,14,15,38,51', '学生考勤(班)(web),请假单管理(web),班级用餐管理(班)(web),用餐情况统计(web),过敏信息管理(web),考勤统计(web),学生考勤(app),请假单管理(app),考勤统计(app),过敏信息管理(app)', NULL, NULL, 'admin', '2016-06-08 10:55:58', NULL, NULL, 1, 'TEACHER');
INSERT INTO `t_sys_role` VALUES (8, '校领导', 1, NULL, '', '', '', '', 'admin', '2018-01-23 10:28:27', NULL, NULL, 0, NULL);
INSERT INTO `t_sys_role` VALUES (9, '安全人员', 1, NULL, '', '', '', '', 'admin', '2018-01-23 10:50:55', NULL, NULL, 0, NULL);
INSERT INTO `t_sys_role` VALUES (10, '年级组长', 1, NULL, '16,25,53,38,40', '全校考勤汇总(教)(web),用餐情况统计(web),考勤统计(web),考勤统计(app),食堂统计(app)', '', '', 'admin', '2022-12-29 14:20:09', NULL, NULL, 1, 'TEACHER');
INSERT INTO `t_sys_role` VALUES (11, '财务', 1, NULL, '52', '收费统计(web)', NULL, NULL, 'admin', '2023-01-31 11:53:08', NULL, NULL, 1, NULL);


-- ----------------------------
-- Table structure for t_sys_schedule_config
-- ----------------------------
CREATE TABLE `t_sys_schedule_config`  (
  `config_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '配置编号',
  `schedule_name` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '配置名称',
  `schedule_group` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '配置组',
  `schedule_status` int(1) NULL DEFAULT 1 COMMENT '状态(1有效(默认)，0无效)',
  `cron_expression` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '规则表达式',
  `des` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  `schedule_function` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '任务类',
  `create_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人编号',
  `create_user_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人姓名',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人编号',
  `update_user_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人姓名',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(11) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  `schedule_type` int(11) NULL DEFAULT NULL COMMENT '类型(1：系统加载 0：不加载)',
  PRIMARY KEY (`config_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统动态定时任务配置表' ROW_FORMAT = Compact;

-- ----------------------------
-- Records of t_sys_schedule_config
-- ----------------------------
INSERT INTO `t_sys_schedule_config` VALUES (1, 'submitCheck', 'check', 1, '0 00 10 * * ?', '每天10点00分自动提交未提交的班级考勤', 'com.zklcsoftware.checkiso.job.ScheduleJobSubmitCheck', NULL, NULL, '2016-12-21 14:20:23', NULL, NULL, NULL, 1, 1);
INSERT INTO `t_sys_schedule_config` VALUES (2, 'initStudentCheck', 'studentCheck', 1, '0 20 09 * * ?', '每天6点生成学生考勤信息', 'com.zklcsoftware.checkiso.job.ScheduleJobInitStudentCheck', NULL, NULL, '2018-02-04 11:50:03', NULL, NULL, NULL, 1, 1);
INSERT INTO `t_sys_schedule_config` VALUES (3, 'sendSubmitCheck', 'sendSubmitCheck', 1, '0 00 09 * * ?', '每天9点提醒教师提交考勤信息', 'com.zklcsoftware.checkiso.job.ScheduleJobSendSubmitCheck', NULL, NULL, '2018-02-04 11:50:03', NULL, NULL, NULL, 1, 1);

-- ----------------------------
-- Table structure for t_sys_schedule_log
-- ----------------------------
CREATE TABLE `t_sys_schedule_log`  (
  `log_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '流水号',
  `schedule_type` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '类型',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '执行时间',
  `des` varchar(1000) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`log_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '系统定时器执行日志' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_sys_school_calendar
-- ----------------------------
CREATE TABLE `t_sys_school_calendar`  (
  `calendar_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键编号',
  `term_id` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所属学期',
  `weeks_num` int(4) NULL DEFAULT 0 COMMENT '周数',
  `start_time` datetime(0) NULL DEFAULT NULL COMMENT '开始日期',
  `end_time` datetime(0) NULL DEFAULT NULL COMMENT '结束日期',
  `create_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '创建人',
  `create_date` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `update_user` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '更新人',
  `update_date` datetime(0) NULL DEFAULT NULL COMMENT '更新时间',
  `is_valid` int(4) NULL DEFAULT 1 COMMENT '作废标记（1正常 0作废）',
  PRIMARY KEY (`calendar_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '校历信息表' ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for t_sys_timer_logs
-- ----------------------------
CREATE TABLE `t_sys_timer_logs`  (
  `log_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '流水号',
  `log_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '任务名称',
  `create_time` datetime(0) NULL DEFAULT NULL COMMENT '执行时间',
  PRIMARY KEY (`log_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = 't_sys_timer_logs' ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_teacher
-- ----------------------------
CREATE TABLE `t_teacher`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `TEACHER_NO` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `PASSWORD` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `CREATE_TIME` datetime(0) NULL DEFAULT NULL,
  `GLOBAL_ID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `PINYIN` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `PHONE` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `ROWID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;


-- ----------------------------
-- Table structure for t_unit
-- ----------------------------
CREATE TABLE `t_unit`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `FATHER_GLOBAL_ID` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '父ID',
  `NAME` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '名称',
  `CREATE_TIME` datetime(0) NULL DEFAULT NULL COMMENT '创建时间',
  `GLOBAL_ID` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '唯一标示',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '科室信息表' ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;

