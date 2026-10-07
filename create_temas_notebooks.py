# -*- coding: utf-8 -*-
import json, os

def make_cell(t, s):
    return {'cell_type': t, 'metadata': {}, 'source': [l + '\n' for l in s.split('\n')]}

# Tema 2: VPL e TIR Siemens
cells_t2 = [
    make_cell('markdown', """# FIAP • ENGENHARIA DA COMPUTAÇÃO (Turma 1ECR • 2022)
## Disciplina: Indústria 4.0
### Tema 2: Engenharia Econômica Industrial e Modelagem Siemens (VPL, TIR e Payback)

---

### 1. Enunciado e Contextualização do Projeto Siemens
- **Objetivo:** Avaliar a viabilidade econômica e financeira da modernização de uma célula automatizada com robôs industriais e sensores IIoT.
- **Investimento Inicial ($I_0$):** R$ 450.000,00 no instante $t=0$.
- **Economia Operacional Anual Líquida ($FC_t$):**
  - Ano 1: R$ 120.000,00
  - Ano 2: R$ 150.000,00
  - Ano 3: R$ 180.000,00
  - Ano 4: R$ 200.000,00
  - Ano 5: R$ 160.000,00
- **Taxa Mínima de Atratividade (TMA):** $i = 12\\%\\text{ ao ano}$.

---

### 2. Dedução Matemática Passo a Passo (Padrão Symbolab)

**Passo 1: Expressão Formal do Valor Presente Líquido (VPL)**
$$\\text{VPL} = -I_0 + \\sum_{t=1}^{n} \\frac{FC_t}{(1 + i)^t}$$

**Passo 2: Substituição Numérica Termo a Termo**
$$\\text{VPL} = -450.000 + \\frac{120.000}{(1{,}12)^1} + \\frac{150.000}{(1{,}12)^2} + \\frac{180.000}{(1{,}12)^3} + \\frac{200.000}{(1{,}12)^4} + \\frac{160.000}{(1{,}12)^5}$$
$$\\text{VP}_1 = \\frac{120.000}{1{,}12} = 107.142{,}86$$
$$\\text{VP}_2 = \\frac{150.000}{1{,}2544} = 119.579{,}08$$
$$\\text{VP}_3 = \\frac{180.000}{1{,}4049} = 128.120{,}44$$
$$\\text{VP}_4 = \\frac{200.000}{1{,}5735} = 127.103{,}61$$
$$\\text{VP}_5 = \\frac{160.000}{1{,}7623} = 90.788{,}30$$

**Passo 3: Soma dos Fluxos Descontados**
$$\\sum_{t=1}^5 \\text{VP}_t = 107.142{,}86 + 119.579{,}08 + 128.120{,}44 + 127.103{,}61 + 90.788{,}30 = 572.734{,}29$$
$$\\text{VPL} = 572.734{,}29 - 450.000{,}00 = +122.734{,}29$$

**Passo 4: Cálculo da Taxa Interna de Retorno (TIR)**
$$\\text{VPL}(\\text{TIR}) = 0 \\implies \\sum_{t=1}^5 \\frac{FC_t}{(1 + \\text{TIR})^t} = 450.000$$
Calculando numericamente por interpolação:
$$\\mathbf{\\text{TIR} = 22{,}76\\%\\text{ a.a.}}$$

**Passo 5: Conclusão e Decisão de Engenharia**
$$\\mathbf{\\text{VPL} = +\\text{R\\$\\ } 122.734{,}29 > 0 \\quad | \\quad \\text{TIR} = 22{,}76\\% > \\text{TMA } (12\\%)}$$
> **Decisão:** O projeto é economicamente viável, gerando retorno 10,76 pontos percentuais acima da taxa mínima de atratividade da fábrica."""),
    make_cell('code', """import numpy as np

investimento = 450000.0
fluxos = [120000.0, 150000.0, 180000.0, 200000.0, 160000.0]
tma = 0.12

vpl = -investimento + sum([fc / ((1 + tma)**(t+1)) for t, fc in enumerate(fluxos)])

# Cálculo da TIR por bisseção
def calc_npv(rate):
    return -investimento + sum([fc / ((1 + rate)**(t+1)) for t, fc in enumerate(fluxos)])

low, high = 0.0, 1.0
for _ in range(100):
    mid = (low + high) / 2.0
    val = calc_npv(mid)
    if val > 0:
        low = mid
    else:
        high = mid
tir = mid

print(f"Investimento Inicial: R$ {investimento:,.2f}")
print(f"VPL a 12% a.a.:       R$ {vpl:,.2f}")
print(f"TIR do Projeto:       {tir*100:.2f}% a.a.")
assert vpl > 0 and tir > tma, "Decisão de aprovação de investimento" """)
]

p_t2 = 'D:/fiap-industria-4-0/03_Exercicios_Tematicos/Tema_2_Engenharia_Economica/Modelagem_Financeira_Projetos_Siemens_VPL_TIR.ipynb'
with open(p_t2, 'w', encoding='utf-8') as f:
    json.dump({'cells': cells_t2, 'metadata': {'language_info': {'name': 'python'}}, 'nbformat': 4, 'nbformat_minor': 4}, f, indent=2, ensure_ascii=False)

# Tema 3: MRP e Lote Econômico
cells_t3 = [
    make_cell('markdown', """# FIAP • ENGENHARIA DA COMPUTAÇÃO (Turma 1ECR • 2022)
## Disciplina: Indústria 4.0
### Tema 3: Planejamento de Necessidades de Materiais (MRP) e Dimensionamento de Lotes

---

### 1. Enunciado e Parâmetros de Manufatura
- **Demanda Anual de Montagem:** $D = 24.000\\text{ módulos eletrônicos/ano}$
- **Custo Unitário de Emissão de Pedido (Setup):** $S = \\text{R\\$\\ } 180{,}00\\text{ por ordem}$
- **Custo Unitário de Estocagem Anual:** $H = \\text{R\\$\\ } 4{,}50\\text{ por unidade/ano}$
- **Lead Time de Fabricação:** $L = 2\\text{ semanas}$ ($10\\text{ dias úteis}$)
- **Dias Úteis por Ano:** $250\\text{ dias}$

---

### 2. Resolução Matemática Passo a Passo (Padrão Symbolab)

**Passo 1: Fórmula do Lote Econômico de Compra (EOQ / LEC - Wilson)**
$$Q^* = \\sqrt{\\frac{2 \\cdot D \\cdot S}{H}}$$

**Passo 2: Substituição Numérica**
$$Q^* = \\sqrt{\\frac{2 \\cdot 24.000 \\cdot 180}{4{,}50}} = \\sqrt{\\frac{8.640.000}{4{,}50}} = \\sqrt{1.920.000} \\approx 1.385{,}64\\text{ unidades}$$
$$\\mathbf{Q^* \\approx 1.386\\text{ unidades/lote}}$$

**Passo 3: Frequência de Pedidos e Ponto de Reposição (ROP)**
1. **Número de Ordens por Ano ($N$):**
   $$N = \\frac{D}{Q^*} = \\frac{24.000}{1.385{,}64} \\approx 17{,}32\\text{ pedidos/ano}$$
2. **Consumo Diário Médio ($d$):**
   $$d = \\frac{D}{250\\text{ dias}} = \\frac{24.000}{250} = 96\\text{ unidades/dia}$$
3. **Ponto de Reposição ($ROP$):**
   $$ROP = d \\cdot L_{\\text{dias}} = 96 \\times 10 = 960\\text{ unidades}$$

**Passo 4: Custo Total Anual de Estoque e Emissão ($CT$)**
$$CT = \\left(\\frac{D}{Q^*} \\cdot S\\right) + \\left(\\frac{Q^*}{2} \\cdot H\\right)$$
$$CT = (17{,}32 \\cdot 180) + (692{,}82 \\cdot 4{,}50) = 3.117{,}69 + 3.117{,}69 = \\text{R\\$\\ } 6.235{,}38$$

**Passo 5: Resultado Final**
$$\\mathbf{Q^* = 1.386\\text{ un} \\quad | \\quad ROP = 960\\text{ un} \\quad | \\quad CT = \\text{R\\$\\ } 6.235{,}38}$$
> **Conclusão:** Quando o estoque atingir 960 peças, uma nova ordem de 1.386 peças deve ser disparada automaticamente pelo ERP/MRP para garantir zero ruptura de estoque."""),
    make_cell('code', """import numpy as np

D = 24000.0
S = 180.0
H = 4.50
dias_uteis = 250
lead_time_dias = 10

Q_star = np.sqrt((2 * D * S) / H)
pedidos_ano = D / Q_star
consumo_diario = D / dias_uteis
rop = consumo_diario * lead_time_dias
custo_total = (D / Q_star * S) + (Q_star / 2 * H)

print(f"Lote Econômico (Q*):      {Q_star:.2f} unidades")
print(f"Pedidos por Ano:          {pedidos_ano:.2f}")
print(f"Ponto de Reposição (ROP): {rop:.0f} unidades")
print(f"Custo Total Mínimo:       R$ {custo_total:,.2f}")""")
]

p_t3 = 'D:/fiap-industria-4-0/03_Exercicios_Tematicos/Tema_3_MRP_Planejamento_Materiais/Planejamento_Necessidades_Materiais_MRP_Explosao.ipynb'
with open(p_t3, 'w', encoding='utf-8') as f:
    json.dump({'cells': cells_t3, 'metadata': {'language_info': {'name': 'python'}}, 'nbformat': 4, 'nbformat_minor': 4}, f, indent=2, ensure_ascii=False)

print("Cadernos dos Temas 2 e 3 gerados com sucesso no padrão Symbolab!")
