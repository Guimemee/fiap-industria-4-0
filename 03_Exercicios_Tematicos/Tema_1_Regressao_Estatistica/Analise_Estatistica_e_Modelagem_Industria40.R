# ==============================================================================
# FIAP • ENGENHARIA DA COMPUTAÇÃO - INDÚSTRIA 4.0 & SISTEMAS DE INFORMAÇÃO
# Análise Estatística, Regressão Linear Simples/Múltipla, ANOVA e Otimização
# Prof. Dr. Sandro Ferraz
# ==============================================================================

# 1. REGRESSÃO LINEAR SIMPLES: PREÇO DE VEÍCULOS (FORD KA) VS IDADE (WEBMOTORS)
# Dados de Amostragem do Mercado Automotivo
idade_anos <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
preco_mil_reais <- c(42.5, 38.0, 35.2, 31.0, 27.5, 24.8, 21.0, 18.5, 15.2, 12.0)
dados_carros <- data.frame(Idade = idade_anos, Preco = preco_mil_reais)

# Ajuste do Modelo Linear por Mínimos Quadrados Ordinários (OLS)
modelo_simples <- lm(Preco ~ Idade, data = dados_carros)
cat("=== RESUMO DO MODELO DE REGRESSÃO LINEAR SIMPLES ===\n")
print(summary(modelo_simples))
cat("\n=== TABELA DE ANÁLISE DE VARIÂNCIA (ANOVA) ===\n")
print(anova(modelo_simples))

# Gráfico de Dispersão com Reta de Tendência e Intervalo de Confiança 95%
plot(dados_carros$Idade, dados_carros$Preco, pch = 19, col = "#0969da", cex = 1.5,
     xlab = "Idade do Veículo (Anos)", ylab = "Preço Médio (R$ Mil)",
     main = "Depreciação de Mercado - Ford Ka (Webmotors / FIPE)")
abline(modelo_simples, col = "#cf222e", lwd = 2.5)
grid()

# 2. REGRESSÃO LINEAR MÚLTIPLA: CUSTOS INDIRETOS DE FABRICAÇÃO
# Variáveis: Custo Indireto (Y), Horas-Máquina (X1), Horas de Mão-de-Obra Direta (X2)
horas_maq <- c(120, 150, 180, 210, 240, 270, 300, 330, 360, 390)
horas_mo <- c(450, 500, 560, 610, 680, 720, 790, 830, 890, 950)
custo_indireto <- c(28.5, 33.2, 38.0, 43.1, 48.7, 53.0, 59.2, 64.0, 70.1, 75.8)
dados_fabrica <- data.frame(Custo = custo_indireto, H_Maq = horas_maq, H_MO = horas_mo)

modelo_multiplo <- lm(Custo ~ H_Maq + H_MO, data = dados_fabrica)
cat("\n=== RESUMO DO MODELO DE REGRESSÃO LINEAR MÚLTIPLA ===\n")
print(summary(modelo_multiplo))

# 3. PLANEJAMENTO DE NECESSIDADES DE MATERIAIS (MRP) E LOTE ECONÔMICO (LEC / EOQ)
# Demanda Anual (D), Custo de Pedido (S), Custo de Armazenagem Unitário (H)
D <- 12000 # unidades/ano
S <- 250.0 # R$/pedido
H <- 15.0  # R$/unidade/ano

Q_otimo_LEC <- sqrt((2 * D * S) / H)
N_pedidos_ano <- D / Q_otimo_LEC
Custo_Total_Estoque <- (D / Q_otimo_LEC) * S + (Q_otimo_LEC / 2) * H

cat("\n=== DIMENSIONAMENTO DE LOTE ECONÔMICO DE COMPRA (LEC/EOQ) ===\n")
cat(sprintf("Lote Econômico Ótimo (Q*):    %.2f unidades\n", Q_otimo_LEC))
cat(sprintf("Número de Pedidos por Ano:   %.2f pedidos\n", N_pedidos_ano))
cat(sprintf("Custo Total Anual Otimizado: R$ %.2f\n", Custo_Total_Estoque))
