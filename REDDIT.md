# Sharing this project on Reddit / 在 Reddit 上发布本项目

A practical playbook for launching **fusion-lens-threads** on Reddit without
getting your post removed for "self-promotion." Read a target sub's rules before
posting — some require a flair, some ban links in the post body, some have a
weekly "show off" thread instead of standalone posts.

一份把 **fusion-lens-threads** 发到 Reddit 的实操指南，帮你避免被当成"自我推广"删帖。
发帖前务必先看目标版块的规则——有的要求加 flair、有的禁止正文放链接、有的只允许在
每周固定的"作品展示"帖里发。

---

## 1. Where to post (recommended subreddits) / 发哪些板块

Ordered by fit. Sizes are rough and change over time — check the sidebar.
按契合度排序，人数为大致量级，以侧边栏为准。

### 🥇 Tier 1 — best fit / 最契合

| Subreddit | Why it fits / 为什么合适 | Watch out / 注意 |
|-----------|--------------------------|------------------|
| **r/Fusion360** | Exactly your tool's audience — Fusion users who need custom threads. | Show a screenshot of the Thread dropdown; they'll instantly get it. |
| **r/functionalprint** | Loves *useful* printed parts. Lens adapters/filter rings are textbook functional prints. | Must show a **real printed part** (Image #9) — pure software posts do worse here. |
| **r/3Dprinting** | Huge, loves free tools that make printing easier. | Big sub = strict rules; lead with a photo, put the GitHub link in a comment if links are restricted. |
| **r/vintagelenses** | M39 / M42 shooters constantly build adapters. Perfect keyword match. | Frame it as "I made adapters for my vintage glass — sharing the tool." |
| **r/AnalogCommunity** | Film shooters adapting M42 mounts, DIY culture. | Keep it lens-focused, not just "look at my code." |

### 🥈 Tier 2 — good, post later / 次选，隔几天再发

| Subreddit | Why / 为什么 | Watch out / 注意 |
|-----------|-------------|------------------|
| **r/mirrorless** | Adapting vintage/lens threads to mirrorless bodies is a constant topic. | Tie it to a concrete use (e.g. custom lens hood / adapter). |
| **r/opensource** | Rewards the free/MIT angle. | Lead with the open-source story, not the photography. |
| **r/AdaptedLenses** | Niche but 100% on-topic if active. | Smaller reach; still worth a targeted post. |
| **r/CAD** / **r/cad** | Broader CAD crowd; thread libraries are relatable. | Less lens-specific; emphasize the "custom thread family" workflow. |
| **r/DIY** | General maker crowd. | Needs a strong visual result to stand out. |
| **r/photography** | Massive reach. | ⚠️ Strict self-promo rules — often only allowed in specific threads. Read rules first or you'll be removed/banned. |

**Suggested schedule / 建议节奏:** post to **one Tier-1 sub per day** over ~5 days
(not all at once — mass cross-posting the same hour looks like spam). Engage with
comments before moving to the next. Reuse the same images.
每天只发**一个** Tier-1 版块，分散到约 5 天，别同一小时全撒出去；先回完评论再发下一个。

---

## 2. How to write the post / 帖子怎么写

### Title templates / 标题模板 (English)

Pick one and tweak — concrete + benefit-driven beats clever:

- `I made a free tool that adds every common lens/filter thread (M39–M42–M52…) to Fusion 360 — 0.75 & 1.0 mm pitch, one-click install [MIT, open source]`
- `Tired of hand-modeling M42 threads in Fusion 360? I generated all 73 lens/filter sizes as a custom thread library (free/MIT)`
- `[OC] Open-source Fusion 360 thread library for camera lens & filter mounts — Mac + Windows installer`

标题模板（中文版块，如有）：

- `我做了个免费工具：把所有常见镜头/滤镜螺纹（M39–M42–M52…）加进 Fusion 360，0.75 和 1.0 螺距，一键安装（MIT 开源）`

### Body template / 正文模板 (English)

```
I 3D-print / machine lens adapters and got tired of hand-modeling threads,
so I built a small open-source tool that drops a custom thread family into
Fusion 360.

What it does:
- Adds 73 common lens/filter diameters (24–127 mm), incl. M39/M40/M42/M43
- Each in BOTH 0.75 mm and 1.0 mm pitch
- External + internal with a 0.10 mm fit clearance, so parts actually screw together
- One-click installer for macOS (bash) and Windows (PowerShell), no dependencies
- Auto-detects your Fusion ThreadData folder

After running the installer + restarting Fusion, "镜头尺寸螺纹规格 (Lens Size
Thread Specs)" shows up right in the Thread Type dropdown.

Free and MIT-licensed. Feedback / more sizes welcome:
👉 https://github.com/HairuoLiu/fusion-lens-threads

(Screenshots + printed part below.)
```

> If a sub **bans links in the body**, remove the URL from the post and put it in
> your **first comment** instead — a very common and accepted workaround.
> 若版块**禁止正文放链接**，就把链接删掉，发在你自己的**第一条评论**里——这是普遍接受的做法。

### Images to attach / 配图

Use the images from the README (see `docs/images/README.md`). For Reddit, the
**best-performing first image** is either the printed part (Image #9) or the
Thread dropdown screenshot (Image #3). Reddit favors image/gallery posts over
link posts — upload images directly and put the repo link in the text/comment.
Reddit 更偏爱图片/相册帖而非纯链接帖——直接上传图片，链接放正文或评论。

A short **screen-recording GIF** of picking the thread performs especially well.

---

## 3. Etiquette that keeps you from getting banned / 避免被封的礼仪

- **Read the rules + follow the "9:1" spirit** — don't only ever post your own
  stuff; comment and participate genuinely. 别只发自己的东西，平时也真实参与讨论。
- **Disclose it's yours** — mark `[OC]` / say "I made this." Reddit hates stealth
  marketing. 明确说明是自己做的，Reddit 反感偷偷营销。
- **Don't spam-crosspost** the same minute to 8 subs. Space them out. 别同一时间狂发。
- **Reply to every early comment** in the first hour or two — engagement drives
  the algorithm. 头一两小时内尽量回复每条评论。
- **Add flair** if the sub requires it (e.g. "Tool", "Project", "OC"). 按要求加 flair。
- **Take feedback well** — "can you add size X?" → add it, reply, and you get a
  free second post ("added the sizes you asked for"). 把反馈变成下一篇更新帖的素材。
- **Best times (rough):** weekday mornings US Eastern tend to get more reach for
  hobby subs; avoid late Friday/weekend nights. Check when your target sub is
  active. 一般美东工作日上午流量较好，避开周五深夜和周末夜里。

---

## 4. Pre-launch checklist / 发布前检查清单

- [ ] Repo is **public** and the README renders correctly on GitHub.
- [ ] Screenshots added to `docs/images/` (at least Image #3 and #9).
- [ ] `LICENSE` present and README states **MIT** clearly. ✅ (done)
- [ ] Repo has a short **description** + **topics/tags** (e.g. `fusion-360`,
      `3d-printing`, `threads`, `photography`, `lens`, `camera`) on GitHub — this
      helps discovery. Set via the ⚙️ next to "About".
- [ ] A couple of GitHub **Releases**/tags so people can download a ZIP. (optional)
- [ ] You've drafted the title + body + which sub goes first.

Good luck with the launch! 🚀
