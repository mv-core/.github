<!-- mv-core Organization Profile README -->
<div align="center">

<svg width="100%" height="200" viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%">
        <animate attributeName="stop-color" values="#667eea;#764ba2;#f093fb;#667eea" dur="4s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%">
        <animate attributeName="stop-color" values="#764ba2;#f093fb;#667eea;#764ba2" dur="4s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%">
        <animate attributeName="stop-color" values="#f093fb;#667eea;#764ba2;#f093fb" dur="4s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <rect width="800" height="200" rx="20" fill="url(#grad1)" />
  
  <!-- Floating particles -->
  <circle cx="150" cy="50" r="40" fill="rgba(255,255,255,0.05)">
    <animate attributeName="cy" values="50;40;50" dur="3s" repeatCount="indefinite" />
  </circle>
  <circle cx="650" cy="150" r="60" fill="rgba(255,255,255,0.03)">
    <animate attributeName="cy" values="150;160;150" dur="4s" repeatCount="indefinite" />
  </circle>
  
  <!-- DNA strand decorative -->
  <path d="M 50 100 Q 100 50, 150 100 T 250 100" stroke="rgba(255,255,255,0.1)" stroke-width="2" fill="none">
    <animate attributeName="d" values="M 50 100 Q 100 50, 150 100 T 250 100;M 50 100 Q 100 150, 150 100 T 250 100;M 50 100 Q 100 50, 150 100 T 250 100" dur="3s" repeatCount="indefinite" />
  </path>
  
  <!-- Main Title -->
  <text x="400" y="70" text-anchor="middle" dominant-baseline="middle" 
        fill="white" font-family="monospace" font-size="56" font-weight="900" filter="url(#glow)">
    🤖 mv-core
  </text>
  
  <!-- Subtitle -->
  <text x="400" y="115" text-anchor="middle" dominant-baseline="middle" 
        fill="rgba(255,255,255,0.9)" font-family="monospace" font-size="15" letter-spacing="3">
    RESEARCH &amp; DEVELOPMENT LIBRARY
  </text>
  
  <!-- Animated nucleotides -->
  <text x="400" y="160" text-anchor="middle" dominant-baseline="middle" font-family="monospace" font-size="18" letter-spacing="6">
    <tspan fill="#FF6B6B">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" repeatCount="indefinite" />A
    </tspan>
    <tspan fill="#4ECDC4">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" begin="0.3s" repeatCount="indefinite" />T
    </tspan>
    <tspan fill="#95E1D3">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" begin="0.6s" repeatCount="indefinite" />C
    </tspan>
    <tspan fill="#F7DC6F">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="1.5s" begin="0.9s" repeatCount="indefinite" />G
    </tspan>
    <tspan fill="rgba(255,255,255,0.3)"> • </tspan>
    <tspan fill="#FFFFFF" font-size="14">FORK</tspan>
    <tspan fill="rgba(255,255,255,0.3)"> • </tspan>
    <tspan fill="#FFFFFF" font-size="14">PATTERN</tspan>
    <tspan fill="rgba(255,255,255,0.3)"> • </tspan>
    <tspan fill="#FFFFFF" font-size="14">EXECUTE</tspan>
  </text>
</svg>

<br>

[![ИИ / Машинное обучение](https://img.shields.io/badge/🤖_ИИ___Машiнное_обученiе-16-5865F2?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Aai-ml)<br>
[![Агенты и инструменты](https://img.shields.io/badge/🧠_Агенты_i_iнструменты-18-57F287?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Aai-agent)<br>
[![Экосистема MCP](https://img.shields.io/badge/🔌_Экосiстема_MCP-6-FEE75C?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Amcp)<br>
[![Инфраструктура и DevOps](https://img.shields.io/badge/🏗️_Инфраструктура_i_DevOps-11-ED4245?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Ainfra)<br>
[![Блокчейн](https://img.shields.io/badge/⛓️_Блокчейн-4-EB459E?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Ablockchain)<br>
[![Рантаймы](https://img.shields.io/badge/⚙️_Рантаймы-4-5865F2?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Aruntime)<br>
[![Инструменты и утилиты](https://img.shields.io/badge/🧰_Инструменты_i_утiлiты-9-95A5A6?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Autils)<br>
[![Безопасность](https://img.shields.io/badge/🔒_Безопасность-2-E74C3C?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Asecurity)<br>
[![Железо](https://img.shields.io/badge/🔧_Железо-1-8E44AD?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Ahardware)<br>
[![Справочники и знания](https://img.shields.io/badge/📚_Справочнiкi_i_знанiя-6-F1C40F?style=for-the-badge&logo=github)](https://github.com/orgs/mv-core/repositories?q=topic%3Areference)

<br><br>

<i>⚡ Каждый форк — паттерн, который Mimic может мимикрировать</i>

</div>

---

## 🧬 Геном

<div align="center">

> *«Организация акумулирует в себе ядро для автономной и полезной работы совокупностью всех инструментов и сил — на сколько это будет в силах этой организации.»*

<br>

<i>Каждый форк — аллель. Каждый topic — хромосома. Каждый паттерн — инструкция в ДНК <a href="https://github.com/Mayveskii/Mimic">Mimic</a>.</i>

</div>

---

## 📂 Домены

<details open>
<summary><b>🤖 ИИ / Машинное обучение</b> — <i>Инференс, модели, токенизация</i> (16 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [gonka](https://github.com/mv-core/gonka) | Jupyter Notebook | Gonka AI Compute |
| [liteparse](https://github.com/mv-core/liteparse) | Rust | A fast, helpful, and open-source document parser |
| [termubit](https://github.com/mv-core/termubit) | C++ | Termubit-Core Sovereign Tree |
| [vllm](https://github.com/mv-core/vllm) | Python | A high-throughput and memory-efficient inference and serving |
| [claude-cookbooks](https://github.com/mv-core/claude-cookbooks) | Jupyter Notebook | A collection of notebooks/recipes showcasing some fun and ef |
| [llama.cpp](https://github.com/mv-core/llama.cpp) | C++ | LLM inference in C/C++ |
| [transformers](https://github.com/mv-core/transformers) | Python | 🤗 Transformers: the model-definition framework for state-of- |
| [Awesome-AI-Benchmarking](https://github.com/mv-core/Awesome-AI-Benchmarking) | N/A | AI Benchmarking Tools |
| [tokenizers](https://github.com/mv-core/tokenizers) | Rust | 💥 Fast State-of-the-Art Tokenizers optimized for Research an |
| [openai-cookbook](https://github.com/mv-core/openai-cookbook) | Jupyter Notebook | Examples and guides for using the OpenAI API |
| [deepmind-research](https://github.com/mv-core/deepmind-research) | Jupyter Notebook | This repository contains implementations and illustrative co |
| [mimic-code](https://github.com/mv-core/mimic-code) | Jupyter Notebook | MIMIC Code Repository: Code shared by the research community |
| [Quantum-Machine-Learning](https://github.com/mv-core/Quantum-Machine-Learning) | Python | Reproducible QML benchmark: VQC vs QSVM on binary tasks. Mod |
| [Kimi-K2](https://github.com/mv-core/Kimi-K2) | N/A | Kimi K2 is the large language model series developed by Moon |
| [minbpe](https://github.com/mv-core/minbpe) | Python | Minimal, clean code for the Byte Pair Encoding (BPE) algorit |
| [DeepPavlov](https://github.com/mv-core/DeepPavlov) | Python | An open source library for deep learning end-to-end dialog s |

[→ Все ии / машинное обучение](https://github.com/orgs/mv-core/repositories?q=topic%3Aai-ml)
</details>

<details open>
<summary><b>🧠 Агенты и инструменты</b> — <i>AI-агенты, ассистенты кодинга, CLI</i> (18 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [herdr](https://github.com/mv-core/herdr) | Rust | agent multiplexer that lives in your terminal. |
| [ECC](https://github.com/mv-core/ECC) | JavaScript | The agent harness performance optimization system. Skills, i |
| [synth-personas](https://github.com/mv-core/synth-personas) | TypeScript | Codex CLI + Claude Code skills (and a TypeScript CLI) that f |
| [openbrief](https://github.com/mv-core/openbrief) | TypeScript |  |
| [kimi-cli](https://github.com/mv-core/kimi-cli) | Python | Kimi Code CLI is your next CLI agent. |
| [opencode-anomalyco-](https://github.com/mv-core/opencode-anomalyco-) | TypeScript | The open source coding agent. |
| [hermes-agent](https://github.com/mv-core/hermes-agent) | Python | The agent that grows with you |
| [graphify](https://github.com/mv-core/graphify) | Python | AI coding assistant skill (Claude Code, Codex, OpenCode, Cur |
| [limenex](https://github.com/mv-core/limenex) | Python | Deterministic stateful governance for AI agents and agentic  |
| [contextplus](https://github.com/mv-core/contextplus) | TypeScript | Semantic Intelligence for Large-Scale Engineering. Context+  |
| [qwen-code](https://github.com/mv-core/qwen-code) | TypeScript |  |
| [gh-aw-mcpg](https://github.com/mv-core/gh-aw-mcpg) | Go | Github Agentic Workflows MCP Gateway |
| [openmythos](https://github.com/mv-core/openmythos) | Python | A theoretical reconstruction of the Claude Mythos architectu |
| [caveman](https://github.com/mv-core/caveman) | Python | 🪨 why use many token when few token do trick — Claude Code s |
| [agency-agents](https://github.com/mv-core/agency-agents) | Shell | A complete AI agency at your fingertips - From frontend wiza |
| [ai-reviewer](https://github.com/mv-core/ai-reviewer) | Go |  |
| [code-mode](https://github.com/mv-core/code-mode) | TypeScript | Claude Code is an agentic coding tool that lives in your ter |
| [OpenAgentsControl](https://github.com/mv-core/OpenAgentsControl) | TypeScript | AI agent framework for plan-first development workflows with |

[→ Все агенты и инструменты](https://github.com/orgs/mv-core/repositories?q=topic%3Aai-agent)
</details>

<details open>
<summary><b>🔌 Экосистема MCP</b> — <i>Model Context Protocol серверы и инструменты</i> (6 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [skillsees](https://github.com/mv-core/skillsees) | TypeScript | Skills, MCP servers, Custom Agents, Agents.md for SDKs to gr |
| [skills](https://github.com/mv-core/skills) | Python | Public repository for Agent Skills |
| [exa-mcp-server](https://github.com/mv-core/exa-mcp-server) | TypeScript | Exa MCP for web search and web crawling! |
| [mcp-chat](https://github.com/mv-core/mcp-chat) | TypeScript | Examples of using Pipedream's MCP server in your app or AI a |
| [awesome-mcp-servers](https://github.com/mv-core/awesome-mcp-servers) | N/A | A collection of MCP servers. |
| [workflows-mcp-server](https://github.com/mv-core/workflows-mcp-server) | TypeScript | Model Context Protocol server that enables AI agents to disc |

[→ Все экосистема mcp](https://github.com/orgs/mv-core/repositories?q=topic%3Amcp)
</details>

<details open>
<summary><b>🏗️ Инфраструктура и DevOps</b> — <i>Kubernetes, Terraform, облако</i> (11 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [openobserve](https://github.com/mv-core/openobserve) | TypeScript | Open source observability platform for logs, metrics, traces |
| [terraform-provider-aws](https://github.com/mv-core/terraform-provider-aws) | Go | The AWS Provider enables Terraform to manage AWS resources. |
| [seaweedfs](https://github.com/mv-core/seaweedfs) | Go | SeaweedFS is a distributed storage system for object storage |
| [pulumi](https://github.com/mv-core/pulumi) | Go | Pulumi - Infrastructure as Code in any programming language  |
| [terraform](https://github.com/mv-core/terraform) | Go | Terraform enables you to safely and predictably create, chan |
| [kubernetes](https://github.com/mv-core/kubernetes) | Go | Production-Grade Container Scheduling and Management |
| [etcd](https://github.com/mv-core/etcd) | Go | Distributed reliable key-value store for the most critical d |
| [netboot.xyz](https://github.com/mv-core/netboot.xyz) | Jinja | Your favorite operating systems in one place.  A network-bas |
| [go-service-template-rest](https://github.com/mv-core/go-service-template-rest) | HTML | AI-native Go REST template for solo developers: orchestrator |
| [git](https://github.com/mv-core/git) | C | Git Source Code Mirror - This is a publish-only repository b |
| [polymerase](https://github.com/mv-core/polymerase) | Go | A tool for populating templates with environment variables a |

[→ Все инфраструктура и devops](https://github.com/orgs/mv-core/repositories?q=topic%3Ainfra)
</details>

<details open>
<summary><b>⛓️ Блокчейн</b> — <i>Web3, ноды, смарт-контракты</i> (4 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [bsc](https://github.com/mv-core/bsc) | Go | A BNB Smart Chain client based on the go-ethereum fork |
| [go-ethereum](https://github.com/mv-core/go-ethereum) | Go | Go implementation of the Ethereum protocol |
| [opengnk](https://github.com/mv-core/opengnk) | Go | Drop-in OpenAI API proxy for Gonka decentralized inference.  |
| [metamask-docs](https://github.com/mv-core/metamask-docs) | MDX | Developer documentation for MetaMask |

[→ Все блокчейн](https://github.com/orgs/mv-core/repositories?q=topic%3Ablockchain)
</details>

<details open>
<summary><b>⚙️ Рантаймы</b> — <i>Языки, компиляторы, базы данных</i> (4 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [gcc](https://github.com/mv-core/gcc) | C++ |  |
| [bun](https://github.com/mv-core/bun) | Rust | Incredibly fast JavaScript runtime, bundler, test runner, an |
| [rustnet](https://github.com/mv-core/rustnet) | Rust | Per-process network monitoring for your terminal with deep p |
| [sled](https://github.com/mv-core/sled) | Rust | the champagne of beta embedded databases |

[→ Все рантаймы](https://github.com/orgs/mv-core/repositories?q=topic%3Aruntime)
</details>

<details open>
<summary><b>🧰 Инструменты и утилиты</b> — <i>Терминал, загрузчики, тулзы</i> (9 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [warp](https://github.com/mv-core/warp) | Rust | Warp is an agentic development environment, born out of the  |
| [yt-dlp](https://github.com/mv-core/yt-dlp) | Python | A feature-rich command-line audio/video downloader |
| [airflow](https://github.com/mv-core/airflow) | Python | Apache Airflow - A platform to programmatically author, sche |
| [goreleaser](https://github.com/mv-core/goreleaser) | Go | Release engineering, simplified |
| [langchain](https://github.com/mv-core/langchain) | Python | The agent engineering platform. |
| [semantic-kernel](https://github.com/mv-core/semantic-kernel) | C# | Integrate cutting-edge LLM technology quickly and easily int |
| [rtk](https://github.com/mv-core/rtk) | Rust | CLI proxy that reduces LLM token consumption by 60-90% on co |
| [gastown](https://github.com/mv-core/gastown) | Go | Gas Town - multi-agent workspace manager |
| [gitingest](https://github.com/mv-core/gitingest) | Python | Replace 'hub' with 'ingest' in any GitHub URL to get a promp |

[→ Все инструменты и утилиты](https://github.com/orgs/mv-core/repositories?q=topic%3Autils)
</details>

<details open>
<summary><b>🔒 Безопасность</b> — <i>Пентест, Active Directory, хакинг</i> (2 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [Awesome-Hacking](https://github.com/mv-core/Awesome-Hacking) | N/A | A collection of various awesome lists for hackers, pentester |
| [GOAD](https://github.com/mv-core/GOAD) | PowerShell | game of active directory |

[→ Все безопасность](https://github.com/orgs/mv-core/repositories?q=topic%3Asecurity)
</details>

<details open>
<summary><b>🔧 Железо</b> — <i>Embedded, схемы, bare metal</i> (1 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [GuitarPedal](https://github.com/mv-core/GuitarPedal) | C | Linus learns analog circuits |

[→ Все железо](https://github.com/orgs/mv-core/repositories?q=topic%3Ahardware)
</details>

<details open>
<summary><b>📚 Справочники и знания</b> — <i>Awesome-листы, статьи, кукбуки</i> (6 репо)</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [awesome-selfhosted](https://github.com/mv-core/awesome-selfhosted) | N/A | A list of Free Software network services and web application |
| [awesome-go](https://github.com/mv-core/awesome-go) | Go | A curated list of awesome Go frameworks, libraries and softw |
| [HelloGitHub](https://github.com/mv-core/HelloGitHub) | Python | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-le |
| [papers-we-love](https://github.com/mv-core/papers-we-love) | Shell | Papers from the computer science community to read and discu |
| [awesome](https://github.com/mv-core/awesome) | N/A | 😎 Awesome lists about all kinds of interesting topics |
| [the-book-of-secret-knowledge](https://github.com/mv-core/the-book-of-secret-knowledge) | N/A | A collection of inspiring lists, manuals, cheatsheets, blogs |

[→ Все справочники и знания](https://github.com/orgs/mv-core/repositories?q=topic%3Areference)
</details>


<details>
<summary><b>📦 Прочее</b> — без категории</summary>

| Репо | Язык | Описание |
|------|------|----------|
| [freellmapi](https://github.com/mv-core/freellmapi) | TypeScript | OpenAI-compatible proxy that stacks the free tiers of 16 LLM |
| [opencode-setup](https://github.com/mv-core/opencode-setup) | TypeScript | CLI setup for configuring opencode to use GonkaGate as a cus |
| [void](https://github.com/mv-core/void) | TypeScript |  |
| [mimiclaw](https://github.com/mv-core/mimiclaw) | C | MimiClaw: Run OpenClaw on a $5 chip. No OS(Linux). No Node.j |
</details>

---

<div align="center">

<b>🔧 Автор</b> <a href="https://github.com/Mayveskii">Mayveskii</a> · 
<b>🧠 Питает</b> <a href="https://github.com/Mayveskii/Mimic">Mimic</a>

</div>
