
## 一、发行版标签（Labels）

### 常用标签类型

| 标签 | 含义 | 适用场景 |
|------|------|----------|
| `🚀 Release` | 正式发布 | 主要版本更新 |
| `✨ Feature` | 功能新增 | 添加新功能 |
| `🐛 Bug Fix` | 问题修复 | 修复 bug |
| `🔧 Maintenance` | 维护更新 | 代码优化、重构 |
| `⚡ Performance` | 性能优化 | 提升运行速度 |
| `📝 Documentation` | 文档更新 | 仅文档变更 |
| `🧪 Beta` | 测试版本 | 公开测试版 |
| `🚨 Critical` | 紧急修复 | 重要安全补丁 |

### 标签使用建议
>选择最能反映版本内容的标签，避免过多标签混淆用户。
### 🏷️ 标签
- 🚀 Release
- ✨ Feature
- 📦 Python Package

---

## 二、发行版标题



### 版本号命名规范（Semantic Versioning）
推荐使用 语义化版本控制（Semantic Versioning）：
```
vX.Y.Z 🏷️ 标签 - 版本主题
```
- X (Major): 重大更新，不兼容的 API 变更
- Y (Minor): 新功能，向后兼容
- Z (Patch): 修复 bug，向后兼容

### 示例

```
v1.0.0 🚀 Release - 首次正式发布
v1.1.0 ✨ Feature - 添加数据导出功能
v1.1.1 🐛 Bug Fix - 修复登录验证问题
v2.0.0-beta 🧪 Beta - 测试版本
```

---

## 三、发行版说明模板

### 📋 v1.0.0 🚀 Release

简要描述本次版本的核心内容。

### 🏷️ 标签
- 🚀 Release
- ✨ Feature
- 📦 Python Package

### ✨ 新增功能
- 功能描述 1
- 功能描述 2

### 🔧 改进优化
- 优化项 1
- 优化项 2

### 🐛 Bug 修复
- 修复项 1
- 修复项 2

### ⚠️ 注意事项
- 兼容性说明
- 迁移指南

### 📦 技术栈
- Python 3.8+
- GitHub Actions

### 🛠️ 安装使用
```bash
示例代码
pip install your-package
```
### 📝 更新日志
[CHANGELOG.md](https://github.com/your-username/your-repo/blob/main/CHANGELOG.md)

---

## 四、发布步骤

1. 打开 GitHub 仓库 → 点击 **Releases**
2. 点击 **Draft a new release**
3. **Tag version**: 输入 `v1.0.0`
4. **Release title**: 粘贴标题
5. **Description**: 粘贴说明
6. 点击 **Publish release**
