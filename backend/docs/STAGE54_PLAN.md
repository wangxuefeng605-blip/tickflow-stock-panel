# Stage54 Plan

## Goal

完善 TickFlow Stock Panel 的智能反馈闭环能力，建立从策略生成、扫描结果、用户反馈到模型优化的基础链路。

---

## Phase 1: Feedback Loop Foundation

### Backend

- 增加反馈事件数据结构
- 增加反馈记录接口
- 增加策略结果评价能力
- 统一 feedback / strategy / scanner 数据模型

### Frontend

- Scanner 页面增加反馈入口
- 展示策略结果反馈状态
- 增加反馈状态管理

---

## Phase 2: Strategy Intelligence Enhancement

### Backend

- 优化策略执行结果追踪
- 增加策略评分计算
- 支持历史反馈查询

### Frontend

- 增加策略评分展示
- 增加历史反馈列表
- 优化 Scanner 交互体验

---

## Phase 3: Data Integration

### API

- 整合 scanner API
- 整合 strategy API
- 统一 frontend api client 类型定义

### Testing

- 增加 feedback 单元测试
- 增加 API 测试
- 保持 pytest 全量通过

---

## Phase 4: Performance

### Frontend

- 优化大 chunk 加载
- 优化动态 import
- 优化 Scanner 页面性能

### Backend

- 优化查询性能
- 增加缓存策略

---

## Acceptance Criteria

- pytest 全量通过
- npm run build 成功
- feedback 数据链路可用
- scanner 支持反馈闭环
- API 类型保持一致