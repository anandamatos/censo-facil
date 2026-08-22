/**
 * @file geodetic-validator.js
 * @description Módulo ES6 para validação geodésica e integração com a API de Geolocalização do navegador,
 * em conformidade com as diretrizes do Censo Agropecuário do IBGE 2026.
 * @module geodetic-validator
 * @version 2.1
 * @author IBGE - Censo Fácil Team
 * @license MIT
 */

// === CONSTANTES DE CONFIGURAÇÃO ===

/**
 * Limiares de Precisão (HDOP) conforme o Manual do Recenseador
 * e estudos de relação entre HDOP e erro de posicionamento
 */
export const HDOP_THRESHOLD_OPTIMAL = 2.5;
export const HDOP_THRESHOLD_ACCEPTABLE = 5.0;
export const HDOP_THRESHOLD_RECOMMENDED = 2.0;

/**
 * Desvio padrão de base padrão do receptor (sigma0) para o receptor integrado do DMC
 */
export const DEFAULT_SIGMA_0 = 1.2;

/**
 * Constantes para orientação em campo
 */
export const RECOMMENDED_MIN_SATELLITES = 5;
export const RECOMMENDED_MASK_ANGLE = 20;
export const MAX_HDOP_FOR_VALID_REGISTRATION = 5.0;

/**
 * Estados operacionais do componente
 */
export const STATUS = {
  LOADING: 'loading',
  OPTIMAL: 'optimal',
  ACCEPTABLE: 'acceptable',
  INSUFFICIENT: 'insufficient',
  ERROR: 'error'
};

// === FUNÇÕES DE CÁLCULO GEODÉSICO ===

/**
 * Calcula a incerteza horizontal (sigma_h) em metros com base no HDOP e sigma_0.
 * Equação fundamental: σₕ = HDOP × σ₀
 *
 * @param {number} hdop - Índice de diluição de precisão horizontal.
 * @param {number} [sigma0=DEFAULT_SIGMA_0] - Desvio padrão de base do receptor do dispositivo.
 * @returns {number} Incerteza horizontal estimada (σₕ) em metros.
 * @throws {TypeError} Se os parâmetros forem inválidos.
 * @example
 * calculatePrecision(1.8) // retorna 2.16
 */
export function calculatePrecision(hdop, sigma0 = DEFAULT_SIGMA_0) {
  if (typeof hdop !== 'number' || isNaN(hdop) || hdop < 0) {
    throw new TypeError('O valor de HDOP deve ser um número positivo.');
  }
  if (typeof sigma0 !== 'number' || isNaN(sigma0) || sigma0 <= 0) {
    throw new TypeError('O valor de sigma0 deve ser um número estritamente positivo.');
  }
  return Number((hdop * sigma0).toFixed(2));
}

/**
 * Retorna o estado de status operacional com base no valor de HDOP.
 * Limiares estabelecidos com base no Manual do Recenseador e estudos de precisão GNSS
 *
 * @param {number} hdop - Índice de diluição de precisão horizontal.
 * @returns {string} Estado da precisão: 'optimal', 'acceptable', ou 'insufficient'.
 * @throws {TypeError} Se o HDOP for inválido.
 */
export function getStatus(hdop) {
  if (typeof hdop !== 'number' || isNaN(hdop) || hdop < 0) {
    throw new TypeError('O valor de HDOP deve ser um número positivo.');
  }
  if (hdop <= HDOP_THRESHOLD_OPTIMAL) {
    return STATUS.OPTIMAL;
  } else if (hdop <= HDOP_THRESHOLD_ACCEPTABLE) {
    return STATUS.ACCEPTABLE;
  } else {
    return STATUS.INSUFFICIENT;
  }
}

/**
 * Determina se a precisão do ponto geodésico é válida para gravação de acordo com o limite do IBGE.
 * Regra: Válido se a incerteza calculada (σ_h) for estritamente inferior a 5.0 metros.
 *
 * @param {number} hdop - Índice de diluição de precisão horizontal.
 * @param {number} [sigma0=DEFAULT_SIGMA_0] - Desvio padrão de base do receptor do dispositivo.
 * @returns {boolean} True se a precisão for válida para gravação (incerteza < 5.0m), false caso contrário.
 */
export function isValid(hdop, sigma0 = DEFAULT_SIGMA_0) {
  try {
    const precision = calculatePrecision(hdop, sigma0);
    return precision < MAX_HDOP_FOR_VALID_REGISTRATION;
  } catch (e) {
    return false;
  }
}

/**
 * Verifica se o número de satélites disponíveis é suficiente para um posicionamento confiável.
 * Estudos mostram que a relação entre o número de satélites e a máscara de elevação
 * afeta diretamente o HDOP.
 *
 * @param {number} satelliteCount - Número de satélites visíveis.
 * @param {number} [minSatellites=RECOMMENDED_MIN_SATELLITES] - Número mínimo recomendado.
 * @returns {boolean} True se o número de satélites for suficiente.
 */
export function hasEnoughSatellites(satelliteCount, minSatellites = RECOMMENDED_MIN_SATELLITES) {
  if (typeof satelliteCount !== 'number' || isNaN(satelliteCount)) {
    return false;
  }
  return satelliteCount >= minSatellites;
}

/**
 * Verifica se a máscara de elevação atual está dentro dos limites recomendados.
 * Baseado em estudos que relacionam máscara de elevação e erro de posicionamento
 *
 * @param {number} maskAngle - Ângulo de máscara atual em graus.
 * @returns {boolean} True se o ângulo estiver dentro do recomendado.
 */
export function isMaskAngleValid(maskAngle) {
  return typeof maskAngle === 'number' && !isNaN(maskAngle) && maskAngle <= RECOMMENDED_MASK_ANGLE;
}

// === FUNÇÕES DE ORIENTAÇÃO EM LINGUAGEM SIMPLES ===

/**
 * Gera uma mensagem de orientação para o recenseador com base no HDOP e na máscara de elevação.
 * Baseado em estudos que relacionam HDOP, máscara de elevação e erro de posicionamento
 *
 * @param {number} hdop - Índice de diluição de precisão horizontal.
 * @param {number} [satelliteCount] - Número de satélites disponíveis.
 * @param {number} [maskAngle] - Ângulo de máscara em graus.
 * @returns {string} Mensagem de orientação em Linguagem Simples.
 */
export function getOrientationMessage(hdop, satelliteCount, maskAngle) {
  const status = getStatus(hdop);
  const hasSatellites = satelliteCount !== undefined ? hasEnoughSatellites(satelliteCount) : true;
  const isValidMask = maskAngle !== undefined ? isMaskAngleValid(maskAngle) : true;

  switch (status) {
    case STATUS.OPTIMAL:
      return '🟢 Precisão ótima para registro. Posicione-se na sede ou porteira do estabelecimento e registre a coordenada.';
    
    case STATUS.ACCEPTABLE:
      if (!isValidMask) {
        return '🟡 O ângulo de visão do céu não está ideal. Tente se afastar de árvores ou construções altas para melhorar o sinal.';
      }
      if (!hasSatellites) {
        return '🟡 Número de satélites insuficiente para alta precisão. Aguarde alguns instantes.';
      }
      return '🟡 Precisão aceitável. Aguarde alguns instantes para verificar se a precisão melhora antes de registrar.';
    
    case STATUS.INSUFFICIENT:
      let message = '🔴 Sinal insuficiente para registrar a coordenada.';
      if (!isValidMask) {
        message += ' Afaste-se de obstáculos físicos como árvores, muros ou edificações.';
      }
      if (!hasSatellites) {
        message += ' Aguarde mais satélites ficarem disponíveis na região.';
      }
      message += ' O ângulo de máscara recomendado é de 20° para minimizar o erro de posicionamento.';
      return message;
    
    default:
      return '⏳ Aguardando estabilização do sinal GNSS.';
  }
}

/**
 * Gera uma mensagem de orientação sobre o ângulo de máscara.
 *
 * @param {number} maskAngle - Ângulo de máscara atual em graus.
 * @returns {string} Mensagem de orientação em Linguagem Simples.
 */
export function getMaskAngleMessage(maskAngle) {
  if (typeof maskAngle !== 'number' || isNaN(maskAngle)) {
    return '❌ Ângulo de máscara não disponível.';
  }
  if (maskAngle <= 15) {
    return '✅ Configuração de satélites excelente. O ângulo de máscara permite boa visibilidade do céu.';
  } else if (maskAngle <= 20) {
    return '⚠️ Configuração aceitável. Posicione-se em local mais aberto para melhorar a visibilidade.';
  } else {
    return '🔴 Ângulo de máscara elevado. O número de satélites visíveis pode ser insuficiente para um posicionamento preciso. Afaste-se de obstáculos verticais.';
  }
}

// === INTEGRAÇÃO COM GEOLOCATION API ===

/**
 * Solicita as coordenadas geográficas utilizando a Geolocation API do navegador
 * e calcula os parâmetros geodésicos correspondentes.
 *
 * @param {Object} [options={}] - Opções personalizadas para a requisição e cálculo.
 * @param {number} [options.sigma0=DEFAULT_SIGMA_0] - Desvio padrão de base para o cálculo de incerteza.
 * @param {number} [options.timeout=30000] - Tempo máximo de espera em milissegundos.
 * @param {boolean} [options.enableHighAccuracy=true] - Habilita alta precisão.
 * @param {number} [options.maximumAge=0] - Idade máxima do cache em milissegundos.
 * @returns {Promise<Object>} Promessa contendo os dados de localização e os metadados geodésicos calculados.
 */
export function requestPosition(options = {}) {
  const sigma0 = options.sigma0 || DEFAULT_SIGMA_0;

  const geoOptions = {
    enableHighAccuracy: true,
    timeout: 30000,
    maximumAge: 0,
    ...options
  };

  return new Promise((resolve, reject) => {
    if (typeof navigator === 'undefined' || !navigator.geolocation) {
      reject(new Error('A API de Geolocalização não é suportada por este ambiente ou navegador.'));
      return;
    }

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude, accuracy } = position.coords;

        // O número de satélites pode não estar disponível em todos os navegadores
        const satellites = position.coords.satellites || null;

        // A precisão (accuracy) retornada pelo navegador representa a margem de erro horizontal a 95% de confiança.
        // Em termos de desvio padrão clássico, accuracy ≈ 2 * σ_h.
        // Logo, estimamos σ_h (precision) como accuracy / 2.
        const precision = Number((accuracy / 2).toFixed(2));

        // Sabendo que σ_h = HDOP * σ_0, estimamos o HDOP como σ_h / σ_0.
        const hdop = Number((precision / sigma0).toFixed(2));

        const status = getStatus(hdop);
        const valid = isValid(hdop, sigma0);
        const orientation = getOrientationMessage(hdop, satellites);

        resolve({
          coords: {
            latitude,
            longitude,
            accuracy
          },
          geodetic: {
            hdop,
            sigma0,
            precision,
            status,
            isValid: valid,
            orientation,
            timestamp: position.timestamp,
            satellites: satellites
          }
        });
      },
      (error) => {
        reject(error);
      },
      geoOptions
    );
  });
}

// === FUNÇÕES DE SIMULAÇÃO PARA TESTE ===

/**
 * Simula a captura de coordenadas geográficas com fins de teste ou demonstração offline.
 * Permite simular diferentes constelações de satélites variando o HDOP.
 *
 * @param {number} simulatedHdop - Valor de HDOP simulado (ex: 1.0, 3.5, 6.0).
 * @param {number} [sigma0=DEFAULT_SIGMA_0] - Desvio de base simulado.
 * @param {Object} [coords={}] - Coordenadas personalizadas para simulação.
 * @param {number} [coords.latitude=-22.326] - Latitude simulada.
 * @param {number} [coords.longitude=-42.669] - Longitude simulada.
 * @param {number} [coords.satellites=6] - Número de satélites simulado.
 * @returns {Promise<Object>} Promessa com dados de coordenadas e metadados geodésicos simulados.
 */
export function simulatePosition(simulatedHdop, sigma0 = DEFAULT_SIGMA_0, coords = {}) {
  return new Promise((resolve) => {
    const latitude = coords.latitude || -22.326;
    const longitude = coords.longitude || -42.669;
    const satellites = coords.satellites || 6;

    const precision = calculatePrecision(simulatedHdop, sigma0);
    const status = getStatus(simulatedHdop);
    const valid = isValid(simulatedHdop, sigma0);
    const orientation = getOrientationMessage(simulatedHdop, satellites);

    const accuracy = Number((precision * 2).toFixed(2));

    setTimeout(() => {
      resolve({
        coords: {
          latitude,
          longitude,
          accuracy
        },
        geodetic: {
          hdop: simulatedHdop,
          sigma0,
          precision,
          status,
          isValid: valid,
          orientation,
          timestamp: Date.now(),
          satellites: satellites
        }
      });
    }, 500);
  });
}