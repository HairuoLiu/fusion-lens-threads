# Reddit 发布总计划 —— 最大化覆盖 & 下载转化

目标：让**最多人看到**并**真的去用**这个 Fusion 360 镜头螺纹库。
每个 `.md` 文件是一篇**可直接复制**的 Reddit 帖子：把 `TITLE` 和 `SELF TEXT` 贴到新帖，`FIRST COMMENT` 作为第一条回复（链接受限的板块需要）。

下载直链（v1.0.0 ZIP，一键下载）：
https://github.com/HairuoLiu/fusion-lens-threads/releases/download/v1.0.0/fusion-lens-threads-v1.0.0.zip
仓库（双语 README + 截图）：https://github.com/HairuoLiu/fusion-lens-threads

---

## 一、应该发在哪些板块（按"流量 × 契合度"排序）

> 流量为 2026 年量级估算（订阅人数），仅作优先级参考。
> 契合度 = 该板块用户是否需要"镜头/滤镜螺纹"这件事。

### 🥇 第一梯队：必发（高契合 + 中高流量，转化率最高）
| 顺序 | 板块 | 约订阅 | 为什么发这里 |
|---|---|---|---|
| 1 | **r/Fusion360** | ~200k | 最精准受众——用 Fusion 的人立刻能用上，最容易出"Thanks, this is great" |
| 2 | **r/3Dprinting** | ~18M | **流量最大**的 3D 打印板块；镜头转接环/滤镜环是经典 functional print |
| 3 | **r/functionalprint** | ~2M | 适配器/功能件专属，帖子天然对口 |
| 4 | **r/AnalogCommunity** | ~1.3M | 胶片党大量打印镜头盖/转接环，M42/M39 刚需 |
| 5 | **r/vintagelenses** | ~200k | 老镜头 + 转接环，M42×1 / M39×1 直接命中 |

### 🥈 第二梯队：强推（高契合 + 大流量）
| 顺序 | 板块 | 约订阅 | 为什么发这里 |
|---|---|---|---|
| 6 | **r/AdaptedLenses** | ~150k | 转接镜头专属，100% 对口 |
| 7 | **r/mirrorless** | ~500k | 无反转接配件打印党 |
| 8 | **r/CAD** | ~1M | 通用 CAD 工具受众，顺手收藏 |
| 9 | **r/3DPrintingCommunity** | ~小 | 打印爱好者聚集，互动率高 |

### 🥉 第三梯队：谨慎发（超大流量但自推规则严）
| 顺序 | 板块 | 约订阅 | 注意事项 |
|---|---|---|---|
| 10 | **r/photography** | ~22M | **流量最大之一**，但自推审核最严；链接只放第一条评论，标 `[OC]`，预期可能被删 |
| 11 | **r/DIY** | ~22M | 同上，谨慎，先混迹再发 |
| 12 | **r/opensource** | ~1M | 开发者/FOSS 受众，易获 star |

---

## 二、怎么发才能"覆盖面积最大 + 最快拿到浏览量"

**核心战术（照做，能多拿 3–5 倍曝光）：**

1. **错峰发布，别一小时全撒。** 同一小时连发 7 个板块 = 触发 spam 过滤 + 像机器人。按上表顺序，**每天发 2–3 个**，跨 4–5 天。
2. **用"原生 crosspost"滚雪球。** Day1 在 r/Fusion360 或 r/3Dprinting 发的主帖有了几条评论后，用 Reddit 自带的 **Crosspost** 按钮转到 r/functionalprint / r/AdaptedLenses 等——复用同一条帖子的互动，不像新帖那样易被当 spam。
3. **顶帖第一条评论放下载链接。** 很多板块（尤其 r/photography、r/DIY）会自动移除正文里的裸 URL，链接放"第一条评论"最稳。
4. **发图！** 建帖时用 Reddit 的"图片"按钮挂上这 3 张截图（视觉证明 = 转化率翻倍）：
   - `thread-type-dropdown.png`（螺纹类型下拉出现本库）
   - `fusion-create-thread.png`（创建螺纹对话框）
   - `install-windows.png`（右键→用 PowerShell 运行）
   或直接贴 GitHub README 链接（里面图已渲染好）。
5. **发帖后 2 小时内秒回每条评论。** 互动率把帖子顶上 "rising" → 进入更多人的首页 → 浏览量滚雪球。
6. **最佳时段：** 周二~周四的 **美东时间 9:00–12:00** 或 **18:00–21:00**（欧美同时在线最多）。避开周五晚~周日。
7. **标 `[OC]`。** 原创内容标 `[OC]` 有 flair 曝光加成，且在自推规则下更被宽容。

---

## 三、发布节奏建议（最快覆盖版）

| 天 | 发在哪 | 用哪个文件 | 备注 |
|---|---|---|---|
| Day 1（周二/三 早） | r/Fusion360 + r/3Dprinting | r-Fusion360.md, r-3Dprinting.md | 精准 + 巨流量，打底 |
| Day 2 | r/functionalprint + r/AnalogCommunity | r-functionalprint.md, r-AnalogCommunity.md | 适配器 + 胶片党 |
| Day 3 | r/vintagelenses + r/AdaptedLenses + r/mirrorless | r-vintagelenses.md, r-mirrorless.md | 老镜头转接三连 |
| Day 4 | r/CAD + r/3DPrintingCommunity + r/opensource | r-opensource.md | 开发者/FOSS 曝光 |
| Day 5+ | r/photography、r/DIY（谨慎） | 链接放首评、标 [OC] | 超大流量，预期可能删 |

---

## 四、礼仪红线
- **9:1 法则**：每发 1 条自推，先在相关板块真诚答 9 条别人的帖——否则账号易被 ban。
- 账号需几天龄 + 少量 karma 才能在严板块发帖。
- 别用多个小号刷——会被反 spam 系统连坐。
- 链接放首评，正文用"仓库在评论区"带过，最安全。

> 注：我目前**没有 Reddit 发帖权限/凭据**（之前实测 token 返回 401、发帖返回 403），所以以上是需要你手动粘贴的内容。你只要把 Reddit "script" 应用的凭据给我（或在 WorkBuddy 连 Reddit 连接器），我就能按上面的节奏自动代发。
