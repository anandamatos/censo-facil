/**
 * @file test-suite.js
 * @description Conjunto de testes e simulações para demonstrar a utilização
 * do módulo ES6 de validação geodésica em conformidade com as diretrizes do IBGE.
 * @version 2.1
 */

import {
  calculatePrecision,
  getStatus,
  isValid,
  getOrientationMessage,
  getMaskAngleMessage,
  isMaskAngleValid,
  hasEnoughSatellites,
  simulatePosition,
  DEFAULT_SIGMA_0,
  HDOP_THRESHOLD_OPTIMAL,
  HDOP_THRESHOLD_ACCEPTABLE,
  RECOMMENDED_MIN_SATELLITES,
  RECOMMENDED_MASK_ANGLE,
  MAX_HDOP_FOR_VALID_REGISTRATION,
  STATUS
} from './geodetic-validator.js';

console.log('═══════════════════════════════════════════════════════════════');
console.log('  🛰️  SUÍTE DE TESTES GEODÉSICOS — CENSO FÁCIL v2.1');
console.log('═══════════════════════════════════════════════════════════════');
console.log(`\n📋 Configuração:`);
console.log(`  • Desvio padrão de base (σ₀): ${DEFAULT_SIGMA_0}m`);
console.log(`  • Limite HDOP para precisão ótima: ${HDOP_THRESHOLD_OPTIMAL}`);
console.log(`  • Limite HDOP para precisão aceitável: ${HDOP_THRESHOLD_ACCEPTABLE}`);
console.log(`  • Limite para registro válido: ${MAX_HDOP_FOR_VALID_REGISTRATION}m`);
console.log(`  • Número mínimo de satélites: ${RECOMMENDED_MIN_SATELLITES}`);
console.log(`  • Ângulo de máscara recomendado: ${RECOMMENDED_MASK_ANGLE}°\n`);

// ======================================================================
// 1. CENÁRIO DE PRECISÃO ÓTIMA (HDOP <= 2.5)
// ======================================================================
console.log('───────────────────────────────────────────────────────────────');
console.log('📡 CENÁRIO 1: Sinal Ótimo (HDOP = 1.8)');
console.log('───────────────────────────────────────────────────────────────');

const hdopOptimal = 1.8;
const precisionOptimal = calculatePrecision(hdopOptimal);
const statusOptimal = getStatus(hdopOptimal);
const validOptimal = isValid(hdopOptimal);
const orientationOptimal = getOrientationMessage(hdopOptimal, 8, 10);

console.log(`  • HDOP Informado: ${hdopOptimal}`);
console.log(`  • Incerteza Horizontal (σₕ): ${precisionOptimal}m`);
console.log(`  • Status Operacional: ${statusOptimal}`);
console.log(`  • Ponto Liberado? ${validOptimal ? '✅ SIM' : '❌ NÃO'}`);
console.log(`  • 📋 Orientação: ${orientationOptimal}`);

// ======================================================================
// 2. CENÁRIO DE PRECISÃO ACEITÁVEL (2.5 < HDOP <= 5.0)
// ======================================================================
console.log('\n───────────────────────────────────────────────────────────────');
console.log('📡 CENÁRIO 2: Sinal Aceitável (HDOP = 3.8)');
console.log('───────────────────────────────────────────────────────────────');

const hdopAcceptable = 3.8;
const precisionAcceptable = calculatePrecision(hdopAcceptable);
const statusAcceptable = getStatus(hdopAcceptable);
const validAcceptable = isValid(hdopAcceptable);
const orientationAcceptable = getOrientationMessage(hdopAcceptable, 5, 15);

console.log(`  • HDOP Informado: ${hdopAcceptable}`);
console.log(`  • Incerteza Horizontal (σₕ): ${precisionAcceptable}m`);
console.log(`  • Status Operacional: ${statusAcceptable}`);
console.log(`  • Ponto Liberado? ${validAcceptable ? '✅ SIM' : '❌ NÃO'}`);
console.log(`  • 📋 Orientação: ${orientationAcceptable}`);

// ======================================================================
// 3. CENÁRIO DE PRECISÃO INSUFICIENTE (HDOP > 5.0)
// ======================================================================
console.log('\n───────────────────────────────────────────────────────────────');
console.log('📡 CENÁRIO 3: Sinal Insuficiente (HDOP = 5.5)');
console.log('───────────────────────────────────────────────────────────────');

const hdopInsufficient = 5.5;
const precisionInsufficient = calculatePrecision(hdopInsufficient);
const statusInsufficient = getStatus(hdopInsufficient);
const validInsufficient = isValid(hdopInsufficient);
const orientationInsufficient = getOrientationMessage(hdopInsufficient, 3, 25);

console.log(`  • HDOP Informado: ${hdopInsufficient}`);
console.log(`  • Incerteza Horizontal (σₕ): ${precisionInsufficient}m`);
console.log(`  • Status Operacional: ${statusInsufficient}`);
console.log(`  • Ponto Liberado? ${validInsufficient ? '✅ SIM' : '❌ NÃO'}`);
console.log(`  • 📋 Orientação: ${orientationInsufficient}`);

// ======================================================================
// 4. CENÁRIO DE PRECISÃO LIMÍTROFE (HDOP = 5.0)
// ======================================================================
console.log('\n───────────────────────────────────────────────────────────────');
console.log('📡 CENÁRIO 4: Sinal Limítrofe (HDOP = 5.0)');
console.log('───────────────────────────────────────────────────────────────');

const hdopLimit = 5.0;
const precisionLimit = calculatePrecision(hdopLimit);
const statusLimit = getStatus(hdopLimit);
const validLimit = isValid(hdopLimit);
const orientationLimit = getOrientationMessage(hdopLimit, 4, 20);

console.log(`  • HDOP Informado: ${hdopLimit}`);
console.log(`  • Incerteza Horizontal (σₕ): ${precisionLimit}m`);
console.log(`  • Status Operacional: ${statusLimit}`);
console.log(`  • Ponto Liberado? ${validLimit ? '✅ SIM' : '❌ NÃO (limite exato)'}`);
console.log(`  • 📋 Orientação: ${orientationLimit}`);

// ======================================================================
// 5. VALIDAÇÃO DE ÂNGULO DE MÁSCARA
// ======================================================================
console.log('\n───────────────────────────────────────────────────────────────');
console.log('📡 CENÁRIO 5: Validação de Ângulo de Máscara');
console.log('───────────────────────────────────────────────────────────────');

const maskAngles = [10, 20, 25, 30];
maskAngles.forEach(angle => {
  const isValidMask = isMaskAngleValid(angle);
  const message = getMaskAngleMessage(angle);
  const statusSymbol = isValidMask ? '✅' : '❌';
  console.log(`  • Ângulo: ${angle}° → ${statusSymbol} ${isValidMask ? 'Válido (≤ 20°)' : 'Inválido (> 20°)'}`);
  console.log(`      📋 ${message}`);
});

// ======================================================================
// 6. TESTE DE RESILIÊNCIA COM PARÂMETROS INVÁLIDOS
// ======================================================================
console.log('\n───────────────────────────────────────────────────────────────');
console.log('📡 CENÁRIO 6: Teste de Resiliência a Falhas');
console.log('───────────────────────────────────────────────────────────────');

const testCases = [
  { fn: () => calculatePrecision(-1.5), desc: 'HDOP negativo' },
  { fn: () => calculatePrecision('texto'), desc: 'HDOP não numérico' },
  { fn: () => calculatePrecision(2.0, -1), desc: 'sigma0 negativo' },
  { fn: () => calculatePrecision(2.0, 'a'), desc: 'sigma0 não numérico' },
  { fn: () => getStatus(-1), desc: 'HDOP negativo no getStatus' },
  { fn: () => getStatus('teste'), desc: 'HDOP não numérico no getStatus' }
];

testCases.forEach(testCase => {
  try {
    testCase.fn();
    console.log(`  ❌ ${testCase.desc}: NÃO capturou erro`);
  } catch (e) {
    console.log(`  ✅ ${testCase.desc}: capturou erro — "${e.message}"`);
  }
});

// ======================================================================
// 7. TESTE DE VALIDAÇÃO DE SATÉLITES
// ======================================================================
console.log('\n───────────────────────────────────────────────────────────────');
console.log('📡 CENÁRIO 7: Validação do Número de Satélites');
console.log('───────────────────────────────────────────────────────────────');

const satelliteCounts = [3, 4, 5, 6, 8];
satelliteCounts.forEach(count => {
  const isValidSat = hasEnoughSatellites(count);
  const statusSymbol = isValidSat ? '✅' : '⚠️';
  console.log(`  • ${count} satélites → ${statusSymbol} ${isValidSat ? 'Suficiente' : 'Insuficiente (mínimo: 5)'}`);
});

// ======================================================================
// 8. SIMULAÇÃO ASSÍNCRONA COM DIFERENTES HDOPs
// ======================================================================
console.log('\n───────────────────────────────────────────────────────────────');
console.log('📡 CENÁRIO 8: Simulação Assíncrona de Captura (500ms de atraso)');
console.log('───────────────────────────────────────────────────────────────');

const simulationCases = [
  { hdop: 1.8, label: 'Sinal Ótimo' },
  { hdop: 3.8, label: 'Sinal Aceitável' },
  { hdop: 5.5, label: 'Sinal Insuficiente' }
];

let simulationIndex = 0;

function runNextSimulation() {
  if (simulationIndex >= simulationCases.length) {
    console.log('\n✅ Todas as simulações concluídas.');
    console.log('═══════════════════════════════════════════════════════════════\n');
    return;
  }

  const sim = simulationCases[simulationIndex];
  console.log(`\n  🔄 Simulando: ${sim.label} (HDOP = ${sim.hdop})...`);

  simulatePosition(sim.hdop).then((result) => {
    console.log(`  📍 Coordenadas: ${result.coords.latitude}°, ${result.coords.longitude}°`);
    console.log(`  📊 HDOP: ${result.geodetic.hdop}`);
    console.log(`  📊 Incerteza (σₕ): ${result.geodetic.precision}m`);
    console.log(`  📊 Status: ${result.geodetic.status}`);
    console.log(`  📊 Ponto Válido: ${result.geodetic.isValid ? '✅ SIM' : '❌ NÃO'}`);
    console.log(`  📋 Orientação: ${result.geodetic.orientation}`);
    console.log('  ───────────────────────────────────────────');

    simulationIndex++;
    runNextSimulation();
  });
}

runNextSimulation();