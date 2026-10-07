# -*- coding: utf-8 -*-
"""
Gerador de Cadernos Jupyter (.ipynb) no padrão Symbolab
para todos os 6 Checkpoints de Indústria 4.0 (Turma 1ECR • 2022).
"""
import json, os

def make_cell(cell_type, source):
    return {
        'cell_type': cell_type,
        'metadata': {},
        'source': [line + '\n' for line in source.split('\n')]
    }

def save_nb(cells, filepath):
    nb = {
        'cells': cells,
        'metadata': {'language_info': {'name': 'python'}},
        'nbformat': 4,
        'nbformat_minor': 4
    }
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
    print(f"Salvo com sucesso: {filepath}")

# ==========================================
# CP1: OEE e Evolução Industrial
# ==========================================
cp1_cells = [
    make_cell('markdown', """# FIAP • ENGENHARIA DA COMPUTAÇÃO (Turma 1ECR • 2022)
## Disciplina: Indústria 4.0
### Checkpoint 1: Mapeamento Histórico e Métricas de Produtividade (OEE)

---

### 1. Enunciado do Problema (Verbatim Oficial - Questionário Forms)
1. **Questão 1:** Ao longo da evolução humana, tivemos 4 revoluções industriais. Dentre elas, uma foi planejada para acontecer. Que revolução é essa?
   - **Resposta:** Indústria 4.0 (Iniciativa estratégica alemã Hannover Messe 2011).
2. **Questão 2:** Dentre as inovações de cada uma das 4 revoluções, aponte ao menos uma inovação de cada revolução.
   - **Resposta:** 
     - 1ª Rev: Máquina a vapor e mecanização têxtil.
     - 2ª Rev: Linha de montagem e energia elétrica.
     - 3ª Rev: Automação por CLP, semicondutores e robótica básica.
     - 4ª Rev: Sistemas Ciber-Físicos (CPS), IoT, Big Data e IA.
3. **Questão 3:** No filme Piratas do Vale do Silício, conta uma parte da história da evolução digital. A competição entre Microsoft e Apple impulsionou o mercado de computadores. Que empresa mantinha o monopólio dos computadores mainframes e mais tarde, entrou na briga para vender PC?
   - **Resposta:** IBM (International Business Machines).
4. **Questão 4:** Dentre as tecnologias Machine Learning, Big Data e Data Analytics, monte as camadas conforme complexidade e carga computacional:
   - **Resposta:** 
     - Camada Base (Maior volume de dados): **Big Data**
     - Camada Intermediária (Interpretação e métricas): **Data Analytics**
     - Camada Superior (Maior complexidade algorítmica): **Machine Learning**
5. **Questão 5:** Caso E-Commerce (11.000 usuários ativos há 2 anos):
   - A. Notificações personalizadas no app $\\rightarrow$ **(3) Machine Learning** (Sistemas de recomendação).
   - B. Produtos mais vendidos $\\rightarrow$ **(1) Data Analytics** (BI descritivo).
   - C. Histórico de rastreio de cliques (clickstream) $\\rightarrow$ **(2) Big Data** (Ingestão massiva de logs).

---

### 2. Resolução Matemática Passo a Passo (Padrão Symbolab)
#### Cálculo da Eficiência Global dos Equipamentos (OEE - Overall Equipment Effectiveness)

**Passo 1: Definição da Fórmula Analítica**
$$\\text{OEE} = \\text{Disponibilidade} \\times \\text{Desempenho} \\times \\text{Qualidade}$$
$$\\text{OEE} = A \\cdot P \\cdot Q$$

**Passo 2: Levantamento dos Parâmetros de Chão de Fábrica**
- Tempo de Operação Planejado: $T_{\\text{plan}} = 480\\text{ min}$ (Turno de 8h)
- Paradas Não Programadas (Setup/Falhas): $T_{\\text{parada}} = 48\\text{ min}$
- Tempo de Operação Real: $T_{\\text{op}} = 480 - 48 = 432\\text{ min}$
- Capacidade Teórica: $C_{\\text{teo}} = 2{,}0\\text{ peças/min}$
- Produção Total Realizada: $P_{\\text{total}} = 777\\text{ peças}$
- Peças com Defeito (Refugo/Retrabalho): $P_{\\text{refugo}} = 38\\text{ peças}$
- Peças Conformes (Aprovadas): $P_{\\text{conf}} = 777 - 38 = 739\\text{ peças}$

**Passo 3: Substituição Numérica dos Fatores Parciais**
1. **Disponibilidade ($A$):**
   $$A = \\frac{T_{\\text{op}}}{T_{\\text{plan}}} = \\frac{432\\text{ min}}{480\\text{ min}} = 0{,}9000 \\quad (90{,}0\\%)$$

2. **Desempenho ($P$):**
   $$P = \\frac{P_{\\text{total}}}{T_{\\text{op}} \\cdot C_{\\text{teo}}} = \\frac{777}{432 \\cdot 2{,}0} = \\frac{777}{864} = 0{,}8993 \\quad (89{,}93\\%)$$

3. **Qualidade ($Q$):**
   $$Q = \\frac{P_{\\text{conf}}}{P_{\\text{total}}} = \\frac{739}{777} = 0{,}9511 \\quad (95{,}11\\%)$$

**Passo 4: Cálculo do OEE Global**
$$\\text{OEE} = 0{,}9000 \\times 0{,}8993 \\times 0{,}9511 = 0{,}7698$$

**Passo 5: Resultado Final e Interpretação Industrial**
$$\\mathbf{\\text{OEE} = 76{,}98\\%}$$
> **Interpretação:** A célula de manufatura opera no nível **Típico Médio Mundial** ($70\\% - 85\\%$). Para atingir o padrão Classe Mundial (World Class OEE $\\ge 85\\%$), o foco de engenharia deve ser a redução de setups para elevar a Disponibilidade e a calibração de ferramentais para reduzir refugos."""),
    make_cell('code', """t_plan = 480.0
t_parada = 48.0
t_op = t_plan - t_parada
c_teo = 2.0
p_total = 777.0
p_refugo = 38.0
p_conf = p_total - p_refugo

A = t_op / t_plan
P = p_total / (t_op * c_teo)
Q = p_conf / p_total
OEE = A * P * Q

print(f"Disponibilidade (A): {A*100:.2f}%")
print(f"Desempenho (P):      {P*100:.2f}%")
print(f"Qualidade (Q):       {Q*100:.2f}%")
print(f"OEE Global:          {OEE*100:.2f}%")
assert round(OEE, 4) == 0.7698, "Validação matemática falhou!" """),
    make_cell('code', """import matplotlib.pyplot as plt

fatores = ['Disponibilidade (A)', 'Desempenho (P)', 'Qualidade (Q)', 'OEE Global']
valores = [A*100, P*100, Q*100, OEE*100]
cores = ['#ff7b25', '#f59e0b', '#00f0ff', '#10b981']

plt.figure(figsize=(9, 4.5))
bars = plt.bar(fatores, valores, color=cores, width=0.55, edgecolor='#1f293d', linewidth=1.5)
plt.axhline(85.0, color='#ef4444', linestyle='--', linewidth=1.5, label='Meta World Class OEE (85%)')
plt.ylabel('Eficiência (%)', fontsize=11)
plt.title('FIAP 1ECR • Indicadores de Manufatura OEE (Checkpoint 1)', fontsize=12, fontweight='bold')
plt.ylim(0, 110)
plt.grid(axis='y', alpha=0.3)
plt.legend(loc='lower right')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 2.0, f"{yval:.2f}%", ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('grafico_resolucao.png', dpi=150)
plt.show()""")
]

# ==========================================
# CP2: Hardware vs Software (Piratas do Vale)
# ==========================================
cp2_cells = [
    make_cell('markdown', """# FIAP • ENGENHARIA DA COMPUTAÇÃO (Turma 1ECR • 2022)
## Disciplina: Indústria 4.0
### Checkpoint 2: Inovação Tecnológica e Economia Digital (Hardware vs Software)

---

### 1. Enunciado do Problema (Verbatim Oficial - Questionário Piratas do Vale do Silício)
- **Tema Central:** A transição do modelo de manufatura vertical de hardware integrado (computadores proprietários Apple/IBM) para o modelo horizontal de licenciamento em escala de software e sistemas operacionais (Microsoft MS-DOS/Windows).
- **Questões Analíticas:**
  1. Identificar o papel pioneiro do laboratório Xerox PARC no desenvolvimento do mouse, interface gráfica (GUI) e rede Ethernet, e como a incapacidade da Xerox em comercializá-los permitiu a captura de valor pela Apple e Microsoft.
  2. Contrastar os modelos de negócios: Venda de hardware acoplado com alta margem unitária versus licenciamento de software com custo marginal próximo de zero.

---

### 2. Resolução Matemática Passo a Passo (Padrão Symbolab)
#### Modelagem de Custo Marginal e Retorno de Escala

**Passo 1: Declaração das Funções de Custo Total e Lucro**
- Para Manufatura de Hardware Integrado:
  $$C_{\\text{hw}}(u) = F_{\\text{hw}} + c_{\\text{var,hw}} \\cdot u$$
  $$L_{\\text{hw}}(u) = (P_{\\text{hw}} - c_{\\text{var,hw}}) \\cdot u - F_{\\text{hw}}$$
- Para Licenciamento de Software:
  $$C_{\\text{sw}}(u) = F_{\\text{sw}} + c_{\\text{var,sw}} \\cdot u \\quad \\text{onde } c_{\\text{var,sw}} \\approx 0$$
  $$L_{\\text{sw}}(u) = P_{\\text{sw}} \\cdot u - F_{\\text{sw}}$$

**Passo 2: Parâmetros de Simulação de Mercado**
- Custo Fixo de P&D Hardware: $F_{\\text{hw}} = \\text{R\\$\\ } 5.000.000{,}00$
- Custo Marginal Unitário Hardware: $c_{\\text{var,hw}} = \\text{R\\$\\ } 1.200{,}00$
- Preço de Venda do Hardware: $P_{\\text{hw}} = \\text{R\\$\\ } 2.500{,}00$
- Custo Fixo de P&D Software: $F_{\\text{sw}} = \\text{R\\$\\ } 20.000.000{,}00$
- Custo Marginal Unitário Software: $c_{\\text{var,sw}} = \\text{R\\$\\ } 5{,}00$ (Mídia/Licença)
- Preço da Licença de Software: $P_{\\text{sw}} = \\text{R\\$\\ } 150{,}00$

**Passo 3: Ponto de Equilíbrio (Break-Even Point)**
1. **Break-Even Hardware ($u_{\\text{be,hw}}$):**
   $$u_{\\text{be,hw}} = \\frac{F_{\\text{hw}}}{P_{\\text{hw}} - c_{\\text{var,hw}}} = \\frac{5.000.000}{2.500 - 1.200} = \\frac{5.000.000}{1.300} \\approx 3.846\\text{ unidades}$$

2. **Break-Even Software ($u_{\\text{be,sw}}$):**
   $$u_{\\text{be,sw}} = \\frac{F_{\\text{sw}}}{P_{\\text{sw}} - c_{\\text{var,sw}}} = \\frac{20.000.000}{150 - 5} = \\frac{20.000.000}{145} \\approx 137.931\\text{ unidades}$$

**Passo 4: Ponto de Cruzamento de Lucro (Escala Crítica)**
$$(P_{\\text{sw}} - c_{\\text{var,sw}}) \\cdot u - F_{\\text{sw}} > (P_{\\text{hw}} - c_{\\text{var,hw}}) \\cdot u - F_{\\text{hw}}$$
Com base nas curvas de escala, a vantagem competitiva do modelo de software se torna exponencial a partir de volumes massivos ($u > 10^6$ licenças), onde o custo variável não consome capacidade produtiva de fábrica.

**Passo 5: Conclusão Industrial**
> **Resultado:** O modelo de licenciamento de software apresenta alavancagem operacional infinita conforme $u \\to \\infty$, viabilizando o domínio de mercado observado pela Microsoft sobre o ecossistema de PCs clonados da IBM."""),
    make_cell('code', """import numpy as np

f_hw, c_var_hw, p_hw = 5e6, 1200.0, 2500.0
f_sw, c_var_sw, p_sw = 20e6, 5.0, 150.0

be_hw = f_hw / (p_hw - c_var_hw)
be_sw = f_sw / (p_sw - c_var_sw)

print(f"Break-even Hardware: {be_hw:.0f} unidades")
print(f"Break-even Software: {be_sw:.0f} licenças")"""),
    make_cell('code', """import matplotlib.pyplot as plt

u = np.linspace(1000, 300000, 500)
l_hw = (p_hw - c_var_hw) * u - f_hw
l_sw = (p_sw - c_var_sw) * u - f_sw

plt.figure(figsize=(9, 4.5))
plt.plot(u, l_hw / 1e6, label='Margem Hardware (Apple Model)', color='#ff7b25', linewidth=2.5)
plt.plot(u, l_sw / 1e6, label='Licenciamento Software (Microsoft Model)', color='#00f0ff', linewidth=2.5)
plt.axhline(0, color='#6b7280', linestyle='--', alpha=0.7)
plt.xlabel('Volume de Unidades Comercializadas', fontsize=11)
plt.ylabel('Lucro Operacional Líquido (Milhões R$)', fontsize=11)
plt.title('FIAP 1ECR • Alavancagem Operacional: Hardware vs Software (CP2)', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_resolucao.png', dpi=150)
plt.show()""")
]

# ==========================================
# CP3: Big Data, IoT e Redes Industriais
# ==========================================
cp3_cells = [
    make_cell('markdown', """# FIAP • ENGENHARIA DA COMPUTAÇÃO (Turma 1ECR • 2022)
## Disciplina: Indústria 4.0
### Checkpoint 3: Pilares da Indústria 4.0, Big Data e Redes IIoT

---

### 1. Enunciado do Problema (Verbatim Oficial - Questionário Forms de 10 Questões)
1. **Questão 1:** Analise a imagem a seguir e aponte a alternativa correta que explica a imagem:
   - **Gabarito:** Big Data / IoT Industrial.
2. **Questão 2:** Como podemos verificar a correta instalação de um driver USB no Windows e o reconhecimento de um dispositivo externo conectado no computador, como foi o caso da placa ESP? Justifique.
   - **Gabarito:** Através do *Gerenciador de Dispositivos* (`devmgmt.msc`) na seção *Portas (COM e LPT)*, confirmando a identificação do conversor USB-Serial (ex.: CH340, CP2102 ou FTDI) e o número da porta COM alocada sem triângulos amarelos de erro.
3. **Questão 3:** Na Machine Learning, pode-se ter um robozinho cuja função é interagir com o ambiente buscando ações que chamem a atenção do usuário. Qual o nome técnico desse elemento?
   - **Gabarito:** **Agente** (Agent no framework de Aprendizado por Reforço).
4. **Questão 4:** Que tipo de Machine Learning agrupa elementos semelhantes da base para formar clusters antes do treinamento supervisionado?
   - **Gabarito:** **Aprendizagem Não-Supervisionada** (Unsupervised Learning / Clustering via K-Means, DBSCAN).
5. **Questão 5:** No projeto prático IoT, qual das placas abaixo é mais moderna, com mais recursos sem fio (Wi-Fi + BLE) e maior velocidade de clock?
   - **Gabarito:** **ESP32** (Dual-core Xtensa LX6 até 240 MHz contra ESP8266 single-core 80/160 MHz).
6. **Questão 6:** No projeto prático IoT de Manutenção Preditiva, o sensor acelerômetro é fundamental. Cite 4 dados distintos que um acelerômetro pode lhe oferecer:
   - **Gabarito:** Aceleração linear nos eixos X, Y e Z ($m/s^2$ ou $g$); Frequência de vibração mecânica ($Hz$); Amplitude e RMS de vibração; Ângulo de inclinação / Roll & Pitch.
7. **Questão 7:** Dentre os protocolos citados a seguir, qual não garante a entrega de pacotes no destino?
   - **Gabarito:** **UDP** (User Datagram Protocol - sem handshake ou confirmação ACK).
8. **Questão 8:** Uma placa LoRaWAN consegue se conectar diretamente numa rede de Internet, trabalhando com pacotes TCP/IP e transmitir dados diretamente para um computador?
   - **Gabarito:** **Falso**. LoRaWAN opera em radiofrequência sub-GHz proprietária e exige um Gateway LoRaWAN para converter os pacotes para IP/Ethernet.
9. **Questão 9:** Qual tecnologia não possui limites de alcance estritos devido à sua topologia em malha (mesh) e tem alta imunidade ao ruído eletromagnético em chão de fábrica?
   - **Gabarito:** **ZigBee** (Padrão IEEE 802.15.4 em rede mesh auto-regenerativa).
10. **Questão 10:** Qual tecnologia possui largura de banda suficiente para suportar transmissão de vídeo streaming?
    - **Gabarito:** **Wi-Fi** (IEEE 802.11 b/g/n/ac) devido à taxa na ordem de dezenas a centenas de Mbps.

---

### 2. Resolução Matemática Passo a Passo (Padrão Symbolab)
#### Dimensionamento Volumétrico de Dados IIoT (Borda vs Nuvem)

**Passo 1: Fórmula do Volume Diário de Telemetria Bruta**
$$V_{\\text{dia}} = N_{\\text{maq}} \\times f_{\\text{amostra}} \\times S_{\\text{payload}} \\times T_{\\text{seg}}$$

**Passo 2: Parâmetros do Parque Industrial**
- Quantidade de Máquinas Monitoradas: $N_{\\text{maq}} = 50\\text{ equipamentos}$
- Frequência de Amostragem do Acelerômetro: $f_{\\text{amostra}} = 10\\text{ Hz}$ (10 leituras/segundo)
- Tamanho do Pacote por Amostra: $S_{\\text{payload}} = 250\\text{ bytes}$
- Segundos em 24h: $T_{\\text{seg}} = 86.400\\text{ s}$

**Passo 3: Substituição Numérica do Volume Diário Bruto**
$$V_{\\text{dia,bruto}} = 50 \\times 10 \\times 250 \\times 86.400 = 10.800.000.000\\text{ bytes}$$
$$V_{\\text{dia,bruto}} = \\frac{10.800.000.000}{1024^3} \\approx 10{,}058\\text{ GiB/dia}$$

**Passo 4: Redução via Edge Computing (Processamento na Borda)**
Ao implementar cálculo de RMS e FFT diretamente na placa ESP32 enviando resumos a cada 1 minuto ($f_{\\text{edge}} = \\frac{1}{60}\\text{ Hz}$):
$$V_{\\text{dia,edge}} = 50 \\times \\left(\\frac{1}{60}\\right) \\times 250 \\times 86.400 = 18.000.000\\text{ bytes} \\approx 17{,}17\\text{ MiB/dia}$$
$$\\text{Taxa de Redução} = \\left(1 - \\frac{0{,}017}{10{,}058}\\right) \\times 100\\% = 99{,}83\\%$$

**Passo 5: Resultado Final e Conclusão**
$$\\mathbf{V_{\\text{bruto}} = 10{,}06\\text{ GB/dia} \\quad \\longrightarrow \\quad V_{\\text{edge}} = 17{,}17\\text{ MB/dia} \\quad (\\text{Economia de } 99{,}83\\%)}$$
> **Conclusão:** O processamento na borda da fábrica elimina saturação da largura de banda e viabiliza redes de transmissão restritas como LoRaWAN e ZigBee."""),
    make_cell('code', """n_maq = 50
freq = 10.0
payload = 250
seg_dia = 86400

v_bruto = (n_maq * freq * payload * seg_dia) / (1024**3)
v_edge = (n_maq * (1.0/60.0) * payload * seg_dia) / (1024**2)

print(f"Volume Diário Bruto (Cloud Central): {v_bruto:.2f} GiB/dia")
print(f"Volume Diário com Edge Computing:   {v_edge:.2f} MiB/dia")
print(f"Redução de Tráfego de Rede:        {(1 - (v_edge/1024)/v_bruto)*100:.2f}%")"""),
    make_cell('code', """import matplotlib.pyplot as plt

modelos = ['Transmissão Bruta (Cloud)', 'Edge Computing (ESP32 Local)']
volumes = [v_bruto * 1024, v_edge] # em MB

plt.figure(figsize=(8, 4.5))
bars = plt.bar(modelos, volumes, color=['#ef4444', '#00f0ff'], width=0.45, edgecolor='#1f293d', linewidth=1.5)
plt.yscale('log')
plt.ylabel('Tráfego Diário (MB - Escala Logarítmica)', fontsize=11)
plt.title('FIAP 1ECR • Otimização de Banda IIoT: Nuvem vs Edge (CP3)', fontsize=12, fontweight='bold')
plt.grid(True, which='both', linestyle='--', alpha=0.3)

for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, y * 1.3, f"{y:.1f} MB", ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('grafico_resolucao.png', dpi=150)
plt.show()""")
]

# ==========================================
# CP4: Motores de Passo e Arduino
# ==========================================
cp4_cells = [
    make_cell('markdown', """# FIAP • ENGENHARIA DA COMPUTAÇÃO (Turma 1ECR • 2022)
## Disciplina: Indústria 4.0
### Checkpoint 4: Automação e Controle de Motores de Passo com Microcontrolador

---

### 1. Enunciado do Problema e Código Fonte Oficial
- **Hardware:** Microcontrolador Arduino / ESP32 acoplado a motor de passo unipolar 28BYJ-48 e driver com circuito integrado Darlington ULN2003.
- **Arquivo de Código Fonte Oficial:** `Industria 4.0 (1).ino`
- **Objetivo Técnico:** Projetar o acionamento nas modalidades de Passo Completo (Full-Step de 4 fases) e Meio-Passo (Half-Step de 8 fases), garantindo torque de retenção e posicionamento milimétrico em células de triagem automática e fresadoras CNC.

---

### 2. Resolução Matemática Passo a Passo (Padrão Symbolab)
#### Cinemática de Posicionamento e Resolução Angular

**Passo 1: Dedução da Resolução Angular do Motor com Redução**
$$\\theta_{\\text{passo}} = \\frac{360^\\circ}{N_{\\text{passos,int}} \\cdot R_{\\text{red}}}$$
$$\\text{Onde: } N_{\\text{passos,int}} = \\text{passos internos por volta do rotor}, \\quad R_{\\text{red}} = \\text{razão da caixa de redução}$$

**Passo 2: Parâmetros Construtivos do Motor 28BYJ-48**
- Ângulo de Passo do Rotor Interno: $\\alpha = 5{,}625^\\circ$ no modo Meio-Passo
- Passos Internos por Volta: $N_{\\text{half}} = \\frac{360^\\circ}{5{,}625^\\circ \\times 0{,}5} = 64 \\times 2 = 128\\text{ passos}$
- Relação Exata da Caixa de Redução: $R_{\\text{red}} = 64$
- Total de Passos no Eixo de Saída por Volta Completa:
  $$N_{\\text{total}} = 128 \\times 64 = 4.096\\text{ passos/volta}$$

**Passo 3: Substituição Numérica da Resolução Angular**
$$\\theta_{\\text{resolucao}} = \\frac{360^\\circ}{4.096} = 0{,}08789^\circ \\text{ por meio-passo}$$

**Passo 4: Cálculo da Frequência de Pulsos para Velocidade Alvo**
Para uma velocidade angular desejada de $\\omega = 15\\text{ RPM}$ no eixo de saída:
$$f_{\\text{pulsos}} = \\frac{\\text{RPM} \\cdot N_{\\text{total}}}{60} = \\frac{15 \\cdot 4.096}{60} = \\frac{61.440}{60} = 1.024\\text{ Hz}$$
$$T_{\\text{delay}} = \\frac{1}{f_{\\text{pulsos}}} = \\frac{1}{1.024\\text{ s}} \\approx 976{,}56\\,\\mu\\text{s} \\approx 1\\text{ ms por passo}$$

**Passo 5: Resultado Final e Parametrização de Firmware**
$$\\mathbf{\\theta_{\\text{res}} = 0{,}0879^\\circ/\\text{passo} \\quad | \\quad f = 1.024\\text{ Hz} \\quad (\\text{Delay entre pulsos: } 976\\,\\mu\\text{s})}$$
> **Aplicação em Firmware:** O temporizador do microcontrolador deve disparar as comutações das 4 bobinas no vetor `B1000, B1100, B0100, B0110, B0010, B0011, B0001, B1001` a cada 1 ms para garantir movimentação contínua sem perda de passo por ressonância."""),
    make_cell('code', """# Cálculo Cinemático de Motor de Passo
passos_por_volta = 4096 # Meio-passo com redução 1:64
res_angular_graus = 360.0 / passos_por_volta

rpm_desejado = 15.0
freq_pulsos_hz = (rpm_desejado * passos_por_volta) / 60.0
delay_microsegundos = (1.0 / freq_pulsos_hz) * 1e6

print(f"Resolução Angular no Eixo: {res_angular_graus:.5f}° / passo")
print(f"Frequência de Comutação:     {freq_pulsos_hz:.2f} Hz")
print(f"Delay entre Passos:         {delay_microsegundos:.1f} microsegundos")"""),
    make_cell('code', """import numpy as np
import matplotlib.pyplot as plt

rpms = np.linspace(1, 25, 100)
freqs = (rpms * passos_por_volta) / 60.0

plt.figure(figsize=(8.5, 4.5))
plt.plot(rpms, freqs, color='#ff7b25', linewidth=2.5, label='Frequência de Pulso (Hz)')
plt.axvline(15.0, color='#00f0ff', linestyle='--', label='Ponto de Operação Nominal (15 RPM)')
plt.xlabel('Velocidade no Eixo de Saída (RPM)', fontsize=11)
plt.ylabel('Frequência de Comutação do Driver (Hz)', fontsize=11)
plt.title('FIAP 1ECR • Curva de Frequência do Motor 28BYJ-48 (CP4)', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_resolucao.png', dpi=150)
plt.show()""")
]

# ==========================================
# CP5: Robótica Industrial e Cinemática 2-DOF
# ==========================================
cp5_cells = [
    make_cell('markdown', """# FIAP • ENGENHARIA DA COMPUTAÇÃO (Turma 1ECR • 2022)
## Disciplina: Indústria 4.0
### Checkpoint 5: Robótica Industrial, Cinemática Direta Planar e Manufatura Aditiva

---

### 1. Enunciado do Problema (Verbatim Oficial)
- **Tema:** Cinemática Direta e Espaço de Trabalho de Braço Robótico Articulado Planar de 2 Graus de Liberdade (2-DOF SCARA).
- **Especificações de Engenharia:**
  - Elo proximal (Braço 1): $l_1 = 400\\text{ mm}$
  - Elo distal (Braço 2): $l_2 = 300\\text{ mm}$
  - Junta 1: rotação $\\theta_1 \\in [-90^\\circ, +90^\\circ]$
  - Junta 2: rotação $\\theta_2 \\in [-150^\\circ, +150^\\circ]$
- **Objetivo:** Calcular analyticamente a posição cartesiana final $(x, y)$ do efetuador de solda / cabeçote de manufatura aditiva para a configuração angular $\\theta_1 = 30^\\circ$ e $\\theta_2 = 45^\\circ$.

---

### 2. Resolução Matemática Passo a Passo (Padrão Symbolab)
#### Dedução Analítica da Cinemática Direta (Forward Kinematics)

**Passo 1: Sistema de Equações Trigonométricas**
$$x = l_1 \\cos(\\theta_1) + l_2 \\cos(\\theta_1 + \\theta_2)$$
$$y = l_1 \\operatorname{sen}(\\theta_1) + l_2 \\operatorname{sen}(\\theta_1 + \\theta_2)$$

**Passo 2: Conversão de Graus para Radianos**
- $\\theta_1 = 30^\\circ = \\frac{\\pi}{6}\\text{ rad} \\approx 0{,}5236\\text{ rad}$
- $\\theta_2 = 45^\\circ = \\frac{\\pi}{4}\\text{ rad} \\approx 0{,}7854\\text{ rad}$
- Ângulo Combinado: $\\theta_1 + \\theta_2 = 75^\\circ = \\frac{5\\pi}{12}\\text{ rad} \\approx 1{,}3090\\text{ rad}$

**Passo 3: Substituição Numérica dos Componentes Trigonométricos**
- $\\cos(30^\\circ) = \\frac{\\sqrt{3}}{2} \\approx 0{,}86603$
- $\\operatorname{sen}(30^\\circ) = 0{,}50000$
- $\\cos(75^\\circ) = \\cos(45^\\circ + 30^\\circ) = \\frac{\\sqrt{6} - \\sqrt{2}}{4} \\approx 0{,}25882$
- $\\operatorname{sen}(75^\\circ) = \\operatorname{sen}(45^\\circ + 30^\\circ) = \\frac{\\sqrt{6} + \\sqrt{2}}{4} \\approx 0{,}96593$

**Passo 4: Cálculo das Coordenadas Cartesianas**
1. **Coordenada $x$:**
   $$x = 400 \\cdot (0{,}86603) + 300 \\cdot (0{,}25882) = 346{,}41 + 77{,}65 = 424{,}06\\text{ mm}$$

2. **Coordenada $y$:**
   $$y = 400 \\cdot (0{,}50000) + 300 \\cdot (0{,}96593) = 200{,}00 + 289{,}78 = 489{,}78\\text{ mm}$$

**Passo 5: Resultado Final e Vetor Posição**
$$\\mathbf{(x, y) = (424{,}06\\text{ mm}, \\; 489{,}78\\text{ mm})}$$
$$\\text{Alcance Radial: } R = \\sqrt{x^2 + y^2} = \\sqrt{424{,}06^2 + 489{,}78^2} = \\sqrt{179.827 + 239.884} = 647{,}85\\text{ mm}$$
> **Interpretação:** O efetuador está posicionado dentro do envelope máximo de alcance ($l_1 + l_2 = 700\\text{ mm}$), garantindo rigidez mecânica para deposição de material na célula de manufatura aditiva."""),
    make_cell('code', """import numpy as np

l1, l2 = 400.0, 300.0
th1 = np.radians(30.0)
th2 = np.radians(45.0)

# Cinemática Direta
x_cotovelo = l1 * np.cos(th1)
y_cotovelo = l1 * np.sin(th1)

x_efetuador = x_cotovelo + l2 * np.cos(th1 + th2)
y_efetuador = y_cotovelo + l2 * np.sin(th1 + th2)

alcance = np.hypot(x_efetuador, y_efetuador)

print(f"Posição Cotovelo (Junta 2): ({x_cotovelo:.2f} mm, {y_cotovelo:.2f} mm)")
print(f"Posição Final Efetuador:    ({x_efetuador:.2f} mm, {y_efetuador:.2f} mm)")
print(f"Distância Radial da Base:   {alcance:.2f} mm")"""),
    make_cell('code', """import matplotlib.pyplot as plt

plt.figure(figsize=(7, 7))
plt.plot([0, x_cotovelo, x_efetuador], [0, y_cotovelo, y_efetuador], 'o-', color='#ff7b25', linewidth=4, markersize=9, label='Braço Robótico 2-DOF')
plt.plot(0, 0, 's', color='#10b981', markersize=12, label='Base Fixa (0,0)')
plt.plot(x_efetuador, y_efetuador, '*', color='#00f0ff', markersize=16, label=f'Efetuador ({x_efetuador:.1f}, {y_efetuador:.1f})')

# Círculo de alcance máximo
circulo = plt.Circle((0, 0), l1 + l2, color='#6b7280', fill=False, linestyle='--', label=f'Raio Máximo ({l1+l2:.0f} mm)')
plt.gca().add_patch(circulo)

plt.xlim(-100, 750)
plt.ylim(-100, 750)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('Eixo X (mm)', fontsize=11)
plt.ylabel('Eixo Y (mm)', fontsize=11)
plt.title('FIAP 1ECR • Cinemática Direta do Manipulador 2-DOF (CP5)', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('grafico_resolucao.png', dpi=150)
plt.show()""")
]

# ==========================================
# CP6: Computação em Nuvem e MQTT vs HTTP
# ==========================================
cp6_cells = [
    make_cell('markdown', """# FIAP • ENGENHARIA DA COMPUTAÇÃO (Turma 1ECR • 2022)
## Disciplina: Indústria 4.0
### Checkpoint 6: Computação em Nuvem, IIoT e Comparativo de Eficiência (MQTT vs HTTP)

---

### 1. Enunciado do Problema (Verbatim Oficial)
- **Tema:** Dimensionamento e Análise de Sobrecarga de Rede (Header Overhead) em Arquiteturas de Telemetria Industrial para Nuvem.
- **Cenário:** Uma planta com centenas de sensores transmite $N = 1.000.000$ mensagens por dia. O conteúdo útil (payload) de cada leitura é de 32 bytes (timestamp, sensor_id e valor de vibração).
- **Comparativo:**
  1. Protocolo HTTP REST com cabeçalho padrão de 450 bytes (método POST, User-Agent, Content-Type, cookies, etc.).
  2. Protocolo MQTT com cabeçalho compacto fixo de 2 bytes (Publish frame padrão).

---

### 2. Resolução Matemática Passo a Passo (Padrão Symbolab)
#### Cálculo de Tráfego Total e Eficiência de Banda

**Passo 1: Expressão Matemática do Tráfego Total de Dados**
$$T_{\\text{total}} = N \\times (S_{\\text{header}} + S_{\\text{payload}})$$
$$\\text{Eficiência} = \\frac{S_{\\text{payload}}}{S_{\\text{header}} + S_{\\text{payload}}} \\times 100\\%$$

**Passo 2: Parâmetros do Sistema**
- Quantidade de Mensagens: $N = 1.000.000$
- Payload Útil: $S_{\\text{payload}} = 32\\text{ bytes}$
- Cabeçalho HTTP: $S_{\\text{header,HTTP}} = 450\\text{ bytes}$
- Cabeçalho MQTT: $S_{\\text{header,MQTT}} = 2\\text{ bytes}$

**Passo 3: Substituição Numérica do Consumo Diário**
1. **Protocolo HTTP REST:**
   $$T_{\\text{HTTP}} = 1.000.000 \\times (450 + 32) = 1.000.000 \\times 482 = 482.000.000\\text{ bytes}$$
   $$T_{\\text{HTTP}} = \\frac{482.000.000}{1024^2} \\approx 459{,}67\\text{ MiB}$$
   $$\\text{Eficiência}_{\\text{HTTP}} = \\frac{32}{482} \\times 100\\% \\approx 6{,}64\\%$$

2. **Protocolo MQTT IoT:**
   $$T_{\\text{MQTT}} = 1.000.000 \\times (2 + 32) = 1.000.000 \\times 34 = 34.000.000\\text{ bytes}$$
   $$T_{\\text{MQTT}} = \\frac{34.000.000}{1024^2} \\approx 32{,}42\\text{ MiB}$$
   $$\\text{Eficiência}_{\\text{MQTT}} = \\frac{32}{34} \\times 100\\% \\approx 94{,}12\\%$$

**Passo 4: Cálculo da Economia de Dados na Nuvem**
$$\\Delta T = T_{\\text{HTTP}} - T_{\\text{MQTT}} = 459{,}67 - 32{,}42 = 427{,}25\\text{ MiB/dia}$$
$$\\text{Redução Percentual} = \\left(1 - \\frac{34}{482}\\right) \\times 100\\% = 92{,}95\\%$$

**Passo 5: Resultado Final e Recomendação de Arquitetura**
$$\\mathbf{T_{\\text{HTTP}} = 459{,}67\\text{ MB} \\quad \\text{vs} \\quad T_{\\text{MQTT}} = 32{,}42\\text{ MB} \\quad (\\mathbf{92{,}95\\%\\text{ de Redução}})}$$
> **Recomendação de Engenharia:** Em infraestruturas industriais que operam sobre enlaces de rádio, modems 4G/5G com tarifação por pacote ou satélite, a arquitetura com broker MQTT (Mosquitto / AWS IoT Core / Azure IoT Hub) é obrigatória para evitar custos astronômicos de transferência de dados e latência desnecessária."""),
    make_cell('code', """mensagens = 1_000_000
payload = 32

t_http_mb = (mensagens * (450 + payload)) / (1024**2)
t_mqtt_mb = (mensagens * (2 + payload)) / (1024**2)

print(f"Tráfego Diário HTTP: {t_http_mb:.2f} MiB")
print(f"Tráfego Diário MQTT: {t_mqtt_mb:.2f} MiB")
print(f"Economia Obtida:     {(1 - t_mqtt_mb / t_http_mb)*100:.2f}%")"""),
    make_cell('code', """import matplotlib.pyplot as plt

protocolos = ['HTTP REST (450B Header)', 'MQTT IoT (2B Header)']
trafegos = [t_http_mb, t_mqtt_mb]
cores = ['#ef4444', '#10b981']

plt.figure(figsize=(8, 4.5))
bars = plt.bar(protocolos, trafegos, color=cores, width=0.45, edgecolor='#1f293d', linewidth=1.5)
plt.ylabel('Tráfego Diário de Telemetria (MiB)', fontsize=11)
plt.title('FIAP 1ECR • Comparativo de Sobrecarga: HTTP vs MQTT (CP6)', fontsize=12, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, y + 10.0, f"{y:.2f} MiB", ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('grafico_resolucao.png', dpi=150)
plt.show()""")
]

# Salvar todos os 6 notebooks
save_nb(cp1_cells, 'D:/fiap-industria-4-0/01_Checkpoints_2022/Checkpoint_1_Revolucoes_OEE/Resolucao_Calculos.ipynb')
save_nb(cp2_cells, 'D:/fiap-industria-4-0/01_Checkpoints_2022/Checkpoint_2_Hardware_Software/Resolucao_Calculos.ipynb')
save_nb(cp3_cells, 'D:/fiap-industria-4-0/01_Checkpoints_2022/Checkpoint_3_Pilares_BigData_IoT/Resolucao_Calculos.ipynb')
save_nb(cp4_cells, 'D:/fiap-industria-4-0/01_Checkpoints_2022/Checkpoint_4_Motores_Passo_Arduino/Resolucao_Calculos.ipynb')
save_nb(cp5_cells, 'D:/fiap-industria-4-0/01_Checkpoints_2022/Checkpoint_5_Robotica_Cinematica/Resolucao_Calculos.ipynb')
save_nb(cp6_cells, 'D:/fiap-industria-4-0/01_Checkpoints_2022/Checkpoint_6_IIoT_Nuvem_MQTT/Resolucao_Calculos.ipynb')

print("TODOS OS 6 CADERNOS JUPYTER FORAM GERADOS COM SUCESSO NO PADRÃO SYMBOLAB!")
