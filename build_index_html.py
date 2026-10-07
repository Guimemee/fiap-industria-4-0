# -*- coding: utf-8 -*-
"""
Gerador do Portal Standalone do GitHub Pages para Indústria 4.0
FIAP • Engenharia da Computação • Turma 1ECR 2022
"""

html_content = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FIAP • Indústria 4.0 | Turma 1ECR • 2022</title>
  
  <!-- Favicon & Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <!-- KaTeX for Symbolab-level Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>

  <style>
    :root {
      --bg-dark: #0a0e17;
      --bg-card: #111827;
      --bg-surface: #1a2333;
      --border: #1f293d;
      --text-main: #f3f4f6;
      --text-muted: #94a3b8;
      --amber: #ff7b25;
      --amber-light: #f59e0b;
      --cyan: #00f0ff;
      --cyan-muted: #38bdf8;
      --green: #10b981;
      --red: #ef4444;
      --radius: 12px;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'Fira Code', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      padding-top: 80px;
    }

    /* Target anchors with scroll offset */
    [id] {
      scroll-margin-top: 95px;
    }

    /* Fixed Header conforming strictly to user requirements */
    header {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      background: rgba(10, 14, 23, 0.94);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      z-index: 1000;
      padding: 10px 24px;
    }

    .header-container {
      max-width: 1240px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 3px;
    }

    .header-row-1 {
      font-size: 1.05rem;
      font-weight: 800;
      letter-spacing: -0.2px;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .header-row-1 .brand-fiap {
      color: var(--amber);
      font-weight: 900;
      letter-spacing: 0.5px;
    }

    .header-row-2 {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }

    .header-tagline {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--cyan);
      letter-spacing: 0.6px;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .header-repo-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-surface);
      border: 1px solid var(--amber);
      color: #ffffff;
      padding: 4px 12px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.82rem;
      font-weight: 700;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .header-repo-btn:hover {
      background: var(--amber);
      color: #000;
      box-shadow: 0 0 12px rgba(255, 123, 37, 0.4);
    }

    /* Container */
    .container {
      max-width: 1240px;
      margin: 0 auto;
      padding: 24px 20px;
    }

    /* Hero SVG Banner */
    .hero-banner {
      width: 100%;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      overflow: hidden;
      margin-bottom: 24px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
    }

    .hero-banner img {
      width: 100%;
      height: auto;
      display: block;
    }

    /* Quick Navigation Pills */
    .nav-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-bottom: 32px;
      background: var(--bg-card);
      padding: 12px;
      border-radius: var(--radius);
      border: 1px solid var(--border);
    }

    .nav-pill {
      background: var(--bg-surface);
      color: var(--text-muted);
      border: 1px solid transparent;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
    }

    .nav-pill:hover, .nav-pill.active {
      color: #ffffff;
      background: #242f44;
      border-color: var(--amber);
    }

    /* Metrics Grid */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-bottom: 36px;
    }

    .metric-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-top: 3px solid var(--amber);
      padding: 20px;
      border-radius: var(--radius);
      position: relative;
    }

    .metric-card.cyan {
      border-top-color: var(--cyan);
    }

    .metric-card.green {
      border-top-color: var(--green);
    }

    .metric-label {
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }

    .metric-value {
      font-size: 2.2rem;
      font-weight: 900;
      color: #ffffff;
      line-height: 1.1;
      margin-bottom: 6px;
    }

    .metric-card.amber .metric-value { color: var(--amber); }
    .metric-card.cyan .metric-value { color: var(--cyan); }
    .metric-card.green .metric-value { color: var(--green); }

    .metric-sub {
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    /* Section Header */
    .section-title {
      font-size: 1.7rem;
      font-weight: 800;
      color: #ffffff;
      margin: 40px 0 16px 0;
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 2px solid var(--border);
      padding-bottom: 10px;
    }

    .section-title span.badge-num {
      background: var(--amber);
      color: #000;
      font-size: 0.8rem;
      font-weight: 900;
      padding: 4px 10px;
      border-radius: 20px;
    }

    /* Card Item */
    .item-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 24px;
      transition: border-color 0.2s;
    }

    .item-card:hover {
      border-color: rgba(255, 123, 37, 0.4);
    }

    .item-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 14px;
      gap: 12px;
      flex-wrap: wrap;
    }

    .item-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: #ffffff;
    }

    .item-badges {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .badge {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
    }

    .badge.amber { border-color: var(--amber); color: var(--amber); }
    .badge.cyan { border-color: var(--cyan); color: var(--cyan); }
    .badge.green { border-color: var(--green); color: var(--green); }

    /* Statement Box (Verbatim) */
    .statement-box {
      background: #0f1523;
      border-left: 4px solid var(--amber);
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin: 16px 0;
      font-size: 0.93rem;
      color: #cbd5e1;
    }

    .statement-box strong {
      color: #ffffff;
    }

    .statement-label {
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--amber);
      letter-spacing: 0.8px;
      margin-bottom: 6px;
    }

    /* Symbolab Math Box */
    .math-step-box {
      background: #131a29;
      border: 1px solid #243048;
      border-radius: 8px;
      padding: 18px;
      margin: 16px 0;
    }

    .math-step-title {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .math-highlight {
      background: rgba(0, 240, 255, 0.08);
      border: 1px solid rgba(0, 240, 255, 0.3);
      padding: 12px;
      border-radius: 6px;
      font-weight: 600;
      color: #ffffff;
      margin-top: 10px;
    }

    /* Code Block Container */
    .code-container {
      position: relative;
      background: #0b0f19;
      border: 1px solid var(--border);
      border-radius: 8px;
      margin: 16px 0;
      overflow: hidden;
    }

    .code-header {
      background: #161f30;
      padding: 8px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.78rem;
      color: var(--text-muted);
      font-family: var(--font-mono);
      border-bottom: 1px solid var(--border);
    }

    .copy-btn {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .copy-btn:hover {
      background: var(--amber);
      color: #000;
    }

    .copy-btn.copied {
      background: var(--green);
      color: #000;
    }

    pre code {
      display: block;
      padding: 14px;
      overflow-x: auto;
      font-family: var(--font-mono);
      font-size: 0.88rem;
      color: #e2e8f0;
      line-height: 1.5;
    }

    /* Image Resolution */
    .res-plot {
      width: 100%;
      max-width: 720px;
      border-radius: 8px;
      border: 1px solid var(--border);
      margin: 14px 0;
      display: block;
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border);
      padding: 40px 20px;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-top: 60px;
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
      body {
        padding-top: 85px;
      }

      .header-row-1 {
        font-size: 0.95rem;
      }

      .header-tagline, .header-repo-btn {
        font-size: 0.78rem;
      }

      .section-title {
        font-size: 1.35rem;
      }

      .item-card {
        padding: 16px;
      }
    }
  </style>
</head>
<body>

  <!-- FIXED HEADER: Line 1 = FIAP Eng Computação | Line 2 = TURMA 1ECR 2022 + Ver Repositório -->
  <header>
    <div class="header-container">
      <div class="header-row-1">
        <span class="brand-fiap">FIAP</span> • Engenharia da Computação
      </div>
      <div class="header-row-2">
        <span class="header-tagline">TURMA 1ECR • 2022</span>
        <a href="https://github.com/Guimemee/fiap-industria-4-0" target="_blank" rel="noopener" class="header-repo-btn" id="header-repo-link">
          Ver Repositório ↗
        </a>
      </div>
    </div>
  </header>

  <main class="container">
    
    <!-- Hero SVG Banner -->
    <div class="hero-banner">
      <img src="card_technologies.svg" alt="FIAP Indústria 4.0 - Smart Factory Dashboard" width="1200" height="520">
    </div>

    <!-- Quick Navigation Pills -->
    <nav class="nav-pills">
      <a href="#checkpoints" class="nav-pill active">📌 6 Checkpoints Oficiais</a>
      <a href="#provas-parte1" class="nav-pill">📝 Provas (Parte 1)</a>
      <a href="#exercicios-tematicos" class="nav-pill">📚 Exercícios por Tema</a>
      <a href="#global-solution" class="nav-pill">🚀 Global Solution & Sprints</a>
      <a href="#cadernos-jupyter" class="nav-pill">📐 Cadernos Symbolab (.ipynb)</a>
    </nav>

    <!-- Metrics Cards -->
    <section class="metrics-grid">
      <div class="metric-card amber">
        <div class="metric-label">EFICIÊNCIA GLOBAL (OEE)</div>
        <div class="metric-value">85.0%</div>
        <div class="metric-sub">Padrão World Class Manufacturing</div>
      </div>
      <div class="metric-card cyan">
        <div class="metric-label">ECONOMIA DE BANDA (MQTT)</div>
        <div class="metric-value">-92.9%</div>
        <div class="metric-sub">Redução de Header Overhead (450B → 2B)</div>
      </div>
      <div class="metric-card amber">
        <div class="metric-label">RESOLUÇÃO ANGULAR CNC</div>
        <div class="metric-value">0.088°</div>
        <div class="metric-sub">Motor 28BYJ-48 Half-Step (4096 passos/v)</div>
      </div>
      <div class="metric-card green">
        <div class="metric-label">LATÊNCIA EDGE COMPUTING</div>
        <div class="metric-value">&lt; 1.0 ms</div>
        <div class="metric-sub">Processamento na Borda (ESP32 Dual-Core)</div>
      </div>
    </section>

    <!-- ======================================================== -->
    <!-- SECTION 1: 6 CHECKPOINTS OFICIAIS 2022 -->
    <!-- ======================================================== -->
    <section id="checkpoints">
      <h2 class="section-title">
        <span class="badge-num">01</span> Suíte Oficial de Avaliações: 6 Checkpoints
      </h2>

      <!-- CP 1 -->
      <article class="item-card" id="cp1">
        <div class="item-header">
          <div>
            <h3 class="item-title">Checkpoint 1: Mapeamento Histórico, Revoluções Industriais & OEE</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Questionário Forms Oficial + Cálculo de Eficiência Geral de Equipamentos</div>
          </div>
          <div class="item-badges">
            <span class="badge amber">2022 • Oficial</span>
            <span class="badge cyan">Forms Verbatim</span>
            <span class="badge green">Symbolab Math</span>
          </div>
        </div>

        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original (Forms)</div>
          <p><strong>Questão 1:</strong> Ao longo da evolução humana, tivemos 4 revoluções industriais. Dentre elas, uma foi planejada para acontecer. Que revolução é essa?<br>
          <em>Gabarito:</em> Indústria 4.0 (Hannover Messe 2011, projeto estratégico de alta tecnologia do governo alemão).</p>
          <br>
          <p><strong>Questão 2:</strong> Dentre as inovações de cada uma das 4 revoluções, aponte ao menos uma inovação de cada revolução.<br>
          <em>Gabarito:</em> 1ª: Máquina a vapor e teares mecânicos; 2ª: Linha de montagem e energia elétrica; 3ª: CLP, semicondutores e robótica básica; 4ª: Sistemas Ciber-Físicos (CPS), IoT e IA.</p>
          <br>
          <p><strong>Questão 3:</strong> No filme Piratas do Vale do Silício, conta uma parte da história da evolução digital. A competição entre Microsoft e Apple impulsionou o mercado de computadores. Que empresa mantinha o monopólio dos computadores mainframes e mais tarde, entrou na briga para vender PC?<br>
          <em>Gabarito:</em> IBM (International Business Machines).</p>
          <br>
          <p><strong>Questão 4:</strong> Dentre as tecnologias Machine Learning, Big Data e Data Analytics, monte as camadas conforme complexidade e carga computacional:<br>
          <em>Gabarito:</em> Base: Big Data (Carga de dados) → Meio: Data Analytics → Topo: Machine Learning (Complexidade algorítmica).</p>
          <br>
          <p><strong>Questão 5:</strong> Caso E-Commerce (11.000 usuários ativos há 2 anos): Faça a correspondência das perguntas com as técnicas:<br>
          - Notificações personalizadas no app → <strong>(3) Machine Learning</strong><br>
          - Produtos mais vendidos → <strong>(1) Data Analytics</strong><br>
          - Histórico do rastreio dos clicks feitos pelos usuários → <strong>(2) Big Data</strong></p>
        </div>

        <div class="math-step-box">
          <div class="math-step-title">📐 Memória de Cálculo Passo a Passo (Padrão Symbolab)</div>
          <p><strong>Definição:</strong> $\\text{OEE} = A \\times P \\times Q$</p>
          <p><strong>1. Disponibilidade:</strong> $A = \\frac{432\\text{ min}}{480\\text{ min}} = 0{,}9000 \\quad (90{,}0\\%)$</p>
          <p><strong>2. Desempenho:</strong> $P = \\frac{777\\text{ peças}}{432\\text{ min} \\times 2{,}0\\text{ un/min}} = \\frac{777}{864} = 0{,}8993 \\quad (89{,}93\\%)$</p>
          <p><strong>3. Qualidade:</strong> $Q = \\frac{739\\text{ peças aprovadas}}{777\\text{ peças produzidas}} = 0{,}9511 \\quad (95{,}11\\%)$</p>
          <div class="math-highlight">
            $$\\mathbf{\\text{OEE Global} = 0{,}9000 \\times 0{,}8993 \\times 0{,}9511 = 76{,}98\\%}$$
          </div>
        </div>

        <img src="01_Checkpoints_2022/Checkpoint_1_Revolucoes_OEE/grafico_resolucao.png" alt="Gráfico OEE Checkpoint 1" class="res-plot">

        <div class="code-container">
          <div class="code-header">
            <span>Python • Execução Computacional OEE</span>
            <button class="copy-btn" onclick="copyCode(this)">Copiar Código</button>
          </div>
          <pre><code># Cálculo OEE no Checkpoint 1
t_plan, t_parada, c_teo = 480.0, 48.0, 2.0
p_total, p_refugo = 777.0, 38.0

A = (t_plan - t_parada) / t_plan
P = p_total / ((t_plan - t_parada) * c_teo)
Q = (p_total - p_refugo) / p_total
OEE = A * P * Q

print(f"OEE Final: {OEE*100:.2f}%")</code></pre>
        </div>
      </article>

      <!-- CP 2 -->
      <article class="item-card" id="cp2">
        <div class="item-header">
          <div>
            <h3 class="item-title">Checkpoint 2: Inovação Tecnológica e Economia Digital</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Hardware Integrado vs Licenciamento de Software (Piratas do Vale do Silício)</div>
          </div>
          <div class="item-badges">
            <span class="badge amber">2022 • Oficial</span>
            <span class="badge cyan">Engenharia Econômica</span>
          </div>
        </div>

        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original</div>
          <p>Analisar a transição tecnológica retratada na criação dos microcomputadores: a captura de valor sobre inovações do Xerox PARC (mouse e GUI), e o contraste de modelos de negócio entre a verticalização de hardware (Apple/IBM) e o modelo de licenciamento de software com custo marginal nulo (Microsoft).</p>
        </div>

        <div class="math-step-box">
          <div class="math-step-title">📐 Memória de Cálculo Passo a Passo (Padrão Symbolab)</div>
          <p><strong>Break-Even Hardware:</strong> $u_{\\text{be,hw}} = \\frac{5.000.000}{2.500 - 1.200} = 3.846\\text{ unidades}$</p>
          <p><strong>Break-Even Software:</strong> $u_{\\text{be,sw}} = \\frac{20.000.000}{150 - 5} = 137.931\\text{ licenças}$</p>
          <div class="math-highlight">
            $$\\mathbf{\\text{Alavancagem Operacional: Para } u > 150.000, \\text{ Software supera Hardware em Lucratividade e Escalabilidade}}$$
          </div>
        </div>

        <img src="01_Checkpoints_2022/Checkpoint_2_Hardware_Software/grafico_resolucao.png" alt="Gráfico Hardware vs Software CP2" class="res-plot">
      </article>

      <!-- CP 3 -->
      <article class="item-card" id="cp3">
        <div class="item-header">
          <div>
            <h3 class="item-title">Checkpoint 3: Pilares da Indústria 4.0, Big Data & Redes IIoT</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Avaliação de 10 Questões + Dimensionamento de Tráfego de Borda (Edge Computing)</div>
          </div>
          <div class="item-badges">
            <span class="badge amber">2022 • Oficial</span>
            <span class="badge cyan">10 Questões Forms</span>
            <span class="badge green">Edge Computing</span>
          </div>
        </div>

        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original (10 Questões do Questionário Forms)</div>
          <p>1. Identificação dos pilares de Indústria 4.0.<br>
          2. Verificação de portas no Windows (`devmgmt.msc`) para drivers USB dos módulos ESP.<br>
          3. Machine Learning: O elemento interativo no ambiente é chamado de <strong>Agente</strong>.<br>
          4. Agrupamento de elementos semelhantes: <strong>Aprendizagem Não-Supervisionada (Clustering)</strong>.<br>
          5. Comparativo ESP8266 vs ESP32: <strong>ESP32</strong> (Dual-Core 240MHz, BLE e Wi-Fi).<br>
          6. Sensor acelerômetro para preditiva: Aceleração triaxial ($g$), Frequência ($Hz$), RMS e Inclinação.<br>
          7. Protocolo sem garantia de entrega: <strong>UDP</strong>.<br>
          8. Conexão direta LoRaWAN à Internet IP: <strong>Falso</strong> (exige Gateway LoRaWAN).<br>
          9. Rede em malha com alta imunidade a ruído eletromagnético fabril: <strong>ZigBee</strong>.<br>
          10. Tecnologia para streaming de vídeo: <strong>Wi-Fi</strong>.</p>
        </div>

        <div class="math-step-box">
          <div class="math-step-title">📐 Memória de Cálculo Passo a Passo (Padrão Symbolab)</div>
          <p><strong>Telemetria Bruta na Nuvem (50 máquinas, 10Hz, 250B):</strong></p>
          <p>$$V_{\\text{bruto}} = 50 \\times 10 \\times 250 \\times 86.400 = 10.800.000.000\\text{ bytes} = 10{,}06\\text{ GiB/dia}$$</p>
          <p><strong>Com Edge Computing Local (Amostragem RMS a cada 60s):</strong></p>
          <p>$$V_{\\text{edge}} = 50 \\times (1/60) \\times 250 \\times 86.400 = 18.000.000\\text{ bytes} = 17{,}17\\text{ MiB/dia}$$</p>
          <div class="math-highlight">
            $$\\mathbf{\\text{Redução no Enlace de Comunicação} = 99{,}83\\% \\quad (\\text{Economia Massiva de Banda})}$$
          </div>
        </div>

        <img src="01_Checkpoints_2022/Checkpoint_3_Pilares_BigData_IoT/grafico_resolucao.png" alt="Gráfico Edge Computing CP3" class="res-plot">
      </article>

      <!-- CP 4 -->
      <article class="item-card" id="cp4">
        <div class="item-header">
          <div>
            <h3 class="item-title">Checkpoint 4: Automação e Controle de Motores de Passo (Arduino)</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Motor 28BYJ-48 + Driver Darlington ULN2003 + Código C++ Oficial</div>
          </div>
          <div class="item-badges">
            <span class="badge amber">2022 • Oficial</span>
            <span class="badge cyan">Arduino C++</span>
            <span class="badge green">Half-Step</span>
          </div>
        </div>

        <div class="statement-box">
          <div class="statement-label">Especificação Técnica de Engenharia</div>
          <p>Controle de motor unipolar 28BYJ-48 em modo Meio-Passo (8 fases de comutação). Relação de redução $R = 64$. Eixo de saída com $4.096\\text{ passos por volta}$. Rotação contínua e posicionamento micrométrico para robôs de triagem.</p>
        </div>

        <div class="math-step-box">
          <div class="math-step-title">📐 Memória de Cálculo Passo a Passo (Padrão Symbolab)</div>
          <p><strong>Resolução Angular:</strong> $\\Delta \\theta = \\frac{360^\\circ}{4.096} = 0{,}08789^\\circ\\text{ por passo}$</p>
          <p><strong>Frequência de Pulso para 15 RPM:</strong></p>
          <p>$$f = \\frac{15 \\times 4.096}{60} = 1.024\\text{ Hz} \\implies T_{\\text{delay}} = \\frac{1}{1.024} = 976{,}6\\,\\mu\\text{s}$$</p>
          <div class="math-highlight">
            $$\\mathbf{\\theta_{\\text{resolução}} = 0{,}0879^\\circ \\quad | \\quad f_{\\text{comutação}} = 1.024\\text{ Hz} \\quad (\\text{Delay } \\approx 1\\text{ ms})}$$
          </div>
        </div>

        <img src="01_Checkpoints_2022/Checkpoint_4_Motores_Passo_Arduino/grafico_resolucao.png" alt="Curva de Frequência Motor CP4" class="res-plot">

        <div class="code-container">
          <div class="code-header">
            <span>Arduino C++ • Acionamento Half-Step (Industria 4.0.ino)</span>
            <button class="copy-btn" onclick="copyCode(this)">Copiar Código</button>
          </div>
          <pre><code>// Controle de Motor de Passo 28BYJ-48 com Driver ULN2003
const int pinoBobina1 = 8;
const int pinoBobina2 = 9;
const int pinoBobina3 = 10;
const int pinoBobina4 = 11;

// Matriz de Meio-Passo (Half-Step)
const int passos[8][4] = {
  {1, 0, 0, 0}, {1, 1, 0, 0}, {0, 1, 0, 0}, {0, 1, 1, 0},
  {0, 0, 1, 0}, {0, 0, 1, 1}, {0, 0, 0, 1}, {1, 0, 0, 1}
};

void setup() {
  pinMode(pinoBobina1, OUTPUT);
  pinMode(pinoBobina2, OUTPUT);
  pinMode(pinoBobina3, OUTPUT);
  pinMode(pinoBobina4, OUTPUT);
}

void loop() {
  for (int fase = 0; fase < 8; fase++) {
    digitalWrite(pinoBobina1, passos[fase][0]);
    digitalWrite(pinoBobina2, passos[fase][1]);
    digitalWrite(pinoBobina3, passos[fase][2]);
    digitalWrite(pinoBobina4, passos[fase][3]);
    delayMicroseconds(976); // Velocidade de 15 RPM
  }
}</code></pre>
        </div>
      </article>

      <!-- CP 5 -->
      <article class="item-card" id="cp5">
        <div class="item-header">
          <div>
            <h3 class="item-title">Checkpoint 5: Robótica Industrial e Cinemática Direta 2-DOF</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Manipulador Robótico Planar SCARA + Envelope de Manufatura Aditiva</div>
          </div>
          <div class="item-badges">
            <span class="badge amber">2022 • Oficial</span>
            <span class="badge cyan">Robótica SCARA</span>
            <span class="badge green">Trigonometria Analítica</span>
          </div>
        </div>

        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original</div>
          <p>Deduzir as coordenadas cartesianas do efetuador de um manipulador robótico planar de 2 elos ($l_1 = 400\\text{ mm}$, $l_2 = 300\\text{ mm}$), operando nas juntas $\\theta_1 = 30^\\circ$ e $\\theta_2 = 45^\\circ$.</p>
        </div>

        <div class="math-step-box">
          <div class="math-step-title">📐 Memória de Cálculo Passo a Passo (Padrão Symbolab)</div>
          <p>$$x = l_1 \\cos(\\theta_1) + l_2 \\cos(\\theta_1 + \\theta_2) = 400 \\cdot \\cos(30^\\circ) + 300 \\cdot \\cos(75^\\circ)$$</p>
          <p>$$x = 400 \\cdot (0{,}86603) + 300 \\cdot (0{,}25882) = 346{,}41 + 77{,}65 = 424{,}06\\text{ mm}$$</p>
          <p>$$y = l_1 \\operatorname{sen}(\\theta_1) + l_2 \\operatorname{sen}(\\theta_1 + \\theta_2) = 400 \\cdot \\operatorname{sen}(30^\\circ) + 300 \\cdot \\operatorname{sen}(75^\\circ)$$</p>
          <p>$$y = 400 \\cdot (0{,}50000) + 300 \\cdot (0{,}96593) = 200{,}00 + 289{,}78 = 489{,}78\\text{ mm}$$</p>
          <div class="math-highlight">
            $$\\mathbf{(x, y) = (424{,}06\\text{ mm}, \\; 489{,}78\\text{ mm}) \\quad | \\quad \\text{Alcance Radial: } R = 647{,}85\\text{ mm}}$$
          </div>
        </div>

        <img src="01_Checkpoints_2022/Checkpoint_5_Robotica_Cinematica/grafico_resolucao.png" alt="Cinemática Robótica CP5" class="res-plot">
      </article>

      <!-- CP 6 -->
      <article class="item-card" id="cp6">
        <div class="item-header">
          <div>
            <h3 class="item-title">Checkpoint 6: Computação em Nuvem e Eficiência de Protocolos IIoT</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Análise Comparativa de Overhead de Cabeçalho: HTTP REST vs MQTT</div>
          </div>
          <div class="item-badges">
            <span class="badge amber">2022 • Oficial</span>
            <span class="badge cyan">Broker MQTT</span>
            <span class="badge green">Sobrecarga de Rede</span>
          </div>
        </div>

        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original</div>
          <p>Dimensionar a largura de banda necessária para uma infraestrutura com $1.000.000\\text{ mensagens/dia}$ com payload de 32 bytes, comparando o overhead de 450 bytes do protocolo HTTP com o pacote compacto de 2 bytes do protocolo MQTT.</p>
        </div>

        <div class="math-step-box">
          <div class="math-step-title">📐 Memória de Cálculo Passo a Passo (Padrão Symbolab)</div>
          <p>$$T_{\\text{HTTP}} = 10^6 \\times (450 + 32) = 482.000.000\\text{ bytes} = 459{,}67\\text{ MiB/dia} \\quad (\\text{Eficiência: } 6{,}64\\%)$$</p>
          <p>$$T_{\\text{MQTT}} = 10^6 \\times (2 + 32) = 34.000.000\\text{ bytes} = 32{,}42\\text{ MiB/dia} \\quad (\\text{Eficiência: } 94{,}12\\%)$$</p>
          <div class="math-highlight">
            $$\\mathbf{\\text{Economia Direta de Banda: } 427{,}25\\text{ MB/dia} \\quad (\\mathbf{92{,}95\\%\\text{ de Redução}})}$$
          </div>
        </div>

        <img src="01_Checkpoints_2022/Checkpoint_6_IIoT_Nuvem_MQTT/grafico_resolucao.png" alt="Comparativo HTTP vs MQTT CP6" class="res-plot">
      </article>
    </section>

    <!-- ======================================================== -->
    <!-- SECTION 2: PROVAS PARTE 1 -->
    <!-- ======================================================== -->
    <section id="provas-parte1">
      <h2 class="section-title">
        <span class="badge-num">02</span> Provas de Engenharia & Avaliações Complementares (Parte 1)
      </h2>

      <!-- NAC 01 -->
      <article class="item-card" id="prova-nac1">
        <div class="item-header">
          <div>
            <h3 class="item-title">Prova NAC 01: Linhas Inteligentes, Tempo e Redução de Estoques</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Estudo de Caso Droll Mecanics • Balanceamento de Capacidade Produtiva</div>
          </div>
          <div class="item-badges">
            <span class="badge cyan">Parte 1</span>
            <span class="badge amber">Modelos 1 & 2</span>
          </div>
        </div>
        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original</div>
          <p>A empresa Droll Mecanics está integrando suas linhas, tornando-as mais inteligentes e integrando-as do ponto de vista de calendário (tempo), o que reduz a necessidade de estoques para toda a cadeia de negócios. Para tal fim, todas as atividades foram convertidas em tempo (minutos), dessa forma a logística da empresa opera sob demanda puxada (Just-in-Time).</p>
        </div>
      </article>

      <!-- NAC 02 -->
      <article class="item-card" id="prova-nac2">
        <div class="item-header">
          <div>
            <h3 class="item-title">Prova NAC 02: Modelagem Financeira de Automação (Modelo Siemens)</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Valor Presente Líquido (VPL), Taxa Interna de Retorno (TIR) e Taxa de Atratividade</div>
          </div>
          <div class="item-badges">
            <span class="badge cyan">Parte 1</span>
            <span class="badge green">VPL / TIR</span>
          </div>
        </div>
        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original</div>
          <p>A aplicação de valor presente é feita no instante zero e é recomendada para a decisão fundamental se o projeto é viável ou não. A solução passa pelo equilíbrio entre a empresa contratante e a prestadora de serviços, assegurando retorno com base no fluxo de caixa descontado e amortização de ativos de automação.</p>
        </div>
      </article>

      <!-- PS 01 -->
      <article class="item-card" id="prova-ps1">
        <div class="item-header">
          <div>
            <h3 class="item-title">Prova Semestral PS 01: Modelagem Estatística e Custos Fabris</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Regressão Linear $Y = aX + b$ • Separação de Custos Fixos e Variáveis de Produção</div>
          </div>
          <div class="item-badges">
            <span class="badge cyan">Parte 1</span>
            <span class="badge amber">Regressão Linear</span>
          </div>
        </div>
        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original</div>
          <p>Critérios de modelagem: A variável independente $X$ determina os direcionadores operacionais de custo, permitindo projetar a reta orçamentária dos custos indiretos de fabricação e margem de contribuição com rigor estatístico.</p>
        </div>
      </article>

      <!-- PS 02 -->
      <article class="item-card" id="prova-ps2">
        <div class="item-header">
          <div>
            <h3 class="item-title">Prova Semestral PS 02 & Sub: Sistemas de Informação e Decisão (SIRE)</h3>
            <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 4px;">Planejamento de Necessidades Materiais (MRP) e Governança Corporativa de TI</div>
          </div>
          <div class="item-badges">
            <span class="badge cyan">Parte 1</span>
            <span class="badge green">MRP & SIRE</span>
          </div>
        </div>
        <div class="statement-box">
          <div class="statement-label">Enunciado Integral Original</div>
          <p>Integração de dados corporativos e sistemas de chão de fábrica para tomada de decisão em tempo real, dimensionamento de estoques de segurança e lead times de suprimentos.</p>
        </div>
      </article>
    </section>

    <!-- ======================================================== -->
    <!-- SECTION 3: EXERCÍCIOS TEMÁTICOS -->
    <!-- ======================================================== -->
    <section id="exercicios-tematicos">
      <h2 class="section-title">
        <span class="badge-num">03</span> Exercícios das Apostilas por Núcleo Temático
      </h2>

      <div class="item-card" id="tema1">
        <h3 class="item-title" style="color: var(--amber);">Tema 1: Modelagem Estatística e Regressões em Custos</h3>
        <p style="color: var(--text-muted); margin-top: 6px;">Análise exploratória, regressão linear simples e múltipla com decomposição de custos fabris.</p>
        <div class="math-highlight" style="margin: 12px 0;">
          <strong>Equação Ajustada (Ford Ka / Depreciação):</strong> $\\text{Preço} = 44{,}91 - 3{,}34 \\cdot \\text{Idade} \\quad (R^2 = 99{,}72\\%, \\; p < 0{,}001)$
        </div>
      </div>

      <div class="item-card" id="tema2">
        <h3 class="item-title" style="color: var(--cyan);">Tema 2: Engenharia Econômica e Rentabilização Siemens</h3>
        <p style="color: var(--text-muted); margin-top: 6px;">Valor Futuro (VF), Valor Presente (VP), VPL, TIR e tomada de decisão sobre novos investimentos.</p>
        <div class="math-highlight" style="margin: 12px 0;">
          <strong>Projeto Automatizado Siemens:</strong> $\\text{Investimento} = -450\\text{k} \\implies \\text{VPL} = +\\text{R\\$\\ } 122.734{,}29 \\quad | \\quad \\text{TIR} = 22{,}76\\% > 12\\%$
        </div>
      </div>

      <div class="item-card" id="tema3">
        <h3 class="item-title" style="color: var(--green);">Tema 3: MRP e Planejamento de Necessidades Materiais</h3>
        <p style="color: var(--text-muted); margin-top: 6px;">Dimensionamento do Lote Econômico de Compra (EOQ/Wilson) e Ponto de Reposição de Estoque.</p>
        <div class="math-highlight" style="margin: 12px 0;">
          <strong>Lote Econômico:</strong> $Q^* = \\sqrt{\\frac{2 \\cdot 24000 \\cdot 180}{4{,}50}} = 1.386\\text{ un} \\quad | \\quad ROP = 960\\text{ un}$
        </div>
      </div>

      <div class="item-card" id="tema4">
        <h3 class="item-title" style="color: #ec4899;">Tema 4: Automação e Redes Industriais IIoT</h3>
        <p style="color: var(--text-muted); margin-top: 6px;">Programação C++ de microcontroladores para motores de passo, protocolos LoRaWAN, ZigBee e segurança.</p>
      </div>

      <div class="item-card" id="tema5">
        <h3 class="item-title" style="color: #a855f7;">Tema 5: Estudos de Caso de Mercado e E-Commerce</h3>
        <p style="color: var(--text-muted); margin-top: 6px;">Inteligência de mercado automotivo (Webmotors), elasticidade de preços e governança corporativa de startups.</p>
      </div>
    </section>

    <!-- ======================================================== -->
    <!-- SECTION 4: GLOBAL SOLUTION & CHALLENGE SPRINTS -->
    <!-- ======================================================== -->
    <section id="global-solution">
      <h2 class="section-title">
        <span class="badge-num">04</span> Grandes Desafios Integradores: Global Solution & Sprints
      </h2>

      <article class="item-card" id="gs-card">
        <h3 class="item-title">Global Solution (GS 2º Semestre): Manutenção Preditiva & Smart Grid</h3>
        <div class="statement-box" style="margin-top: 12px;">
          <div class="statement-label">Enunciado Oficial Integrado</div>
          <p>Desenvolvimento de sistema inteligente com sensoriamento de vibração e temperatura em tempo real acoplado a broker MQTT e detecção de anomalias por machine learning.</p>
        </div>
      </article>

      <article class="item-card" id="sprints-card">
        <h3 class="item-title">Challenge Sprints (Sprints 1 a 4)</h3>
        <div class="statement-box" style="margin-top: 12px;">
          <div class="statement-label">Resolução das 4 Etapas Interdisciplinares</div>
          <p>- <strong>Sprint 1:</strong> Mapeamento do ecossistema e ideação da célula ciber-física.<br>
          - <strong>Sprint 2:</strong> Prototipação com sensores e firmware C++ para ESP32.<br>
          - <strong>Sprint 3:</strong> Integração de telemetria na nuvem e banco de dados temporais.<br>
          - <strong>Sprint 4:</strong> Modelo preditivo de falhas e apresentação executiva para banca examinadora.</p>
        </div>
      </article>
    </section>

    <!-- ======================================================== -->
    <!-- SECTION 5: CADERNOS JUPYTER SYMBOLAB -->
    <!-- ======================================================== -->
    <section id="cadernos-jupyter">
      <h2 class="section-title">
        <span class="badge-num">05</span> Cadernos Jupyter Interativos (.ipynb) no Repositório
      </h2>

      <div class="item-card">
        <p style="margin-bottom: 16px; color: var(--text-muted);">
          Todos os cadernos estão estruturados com memória de cálculo passo a passo, fórmulas em $\\LaTeX$, gráficos renderizados e assertivas de validação:
        </p>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 10px;">
          <li>📓 <code>01_Checkpoints_2022/Checkpoint_1_Revolucoes_OEE/Resolucao_Calculos.ipynb</code></li>
          <li>📓 <code>01_Checkpoints_2022/Checkpoint_2_Hardware_Software/Resolucao_Calculos.ipynb</code></li>
          <li>📓 <code>01_Checkpoints_2022/Checkpoint_3_Pilares_BigData_IoT/Resolucao_Calculos.ipynb</code></li>
          <li>📓 <code>01_Checkpoints_2022/Checkpoint_4_Motores_Passo_Arduino/Resolucao_Calculos.ipynb</code></li>
          <li>📓 <code>01_Checkpoints_2022/Checkpoint_5_Robotica_Cinematica/Resolucao_Calculos.ipynb</code></li>
          <li>📓 <code>01_Checkpoints_2022/Checkpoint_6_IIoT_Nuvem_MQTT/Resolucao_Calculos.ipynb</code></li>
          <li>📓 <code>03_Exercicios_Tematicos/Tema_1_Regressao_Estatistica/Analise_Estatistica_e_Modelagem_Industria40.ipynb</code></li>
          <li>📓 <code>03_Exercicios_Tematicos/Tema_2_Engenharia_Economica/Modelagem_Financeira_Projetos_Siemens_VPL_TIR.ipynb</code></li>
          <li>📓 <code>03_Exercicios_Tematicos/Tema_3_MRP_Planejamento_Materiais/Planejamento_Necessidades_Materiais_MRP_Explosao.ipynb</code></li>
        </ul>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer>
    <div style="font-weight: 800; color: #ffffff; font-size: 1.1rem; margin-bottom: 8px;">
      FIAP • ENGENHARIA DA COMPUTAÇÃO • TURMA 1ECR • 2022
    </div>
    <p>Acervo Acadêmico e Repositório Digital de Indústria 4.0</p>
    <p style="margin-top: 12px; font-size: 0.8rem; color: #64748b;">
      Construído com padrão Symbolab para cálculos e arquitetura responsiva para web e dispositivos móveis.
    </p>
  </footer>

  <!-- Script for 1-click code copying -->
  <script>
    function copyCode(button) {
      const pre = button.closest('.code-container').querySelector('pre code');
      if (!pre) return;
      navigator.clipboard.writeText(pre.innerText).then(() => {
        const originalText = button.innerText;
        button.innerText = '✓ Copiado!';
        button.classList.add('copied');
        setTimeout(() => {
          button.innerText = originalText;
          button.classList.remove('copied');
        }, 2000);
      });
    }
  </script>
</body>
</html>
'''

with open('D:/fiap-industria-4-0/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html gerado com sucesso!")
