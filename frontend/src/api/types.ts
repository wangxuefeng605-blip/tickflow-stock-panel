export interface PipelineScheduleIn {
  hour: number;
  minute: number;
}

export interface EnrichedBatchSizeIn {
  size: number;
}

export interface IndexDailyBatchSizeIn {
  size: number;
}

export interface LimitLadderMonitorIn {
  enabled: boolean;
}

export interface DepthPollingIntervalIn {
  interval: number;
}

export interface DepthFinalizeTimeIn {
  hour: number;
  minute: number;
}

export interface ReviewScheduleIn {
  enabled: boolean;
  hour: number;
  minute: number;
}

export interface ReviewPushIn {
  channels: string[];
}

// ============================================================
// Strategy API
// ============================================================

export interface RunRequest {
  strategy_id: string;
  as_of?: string | null;
  pool?: string[] | null;
  params?: Record<string, unknown> | null;
}

export interface RunAllRequest {
  as_of?: string | null;
}

export interface SaveConfigRequest {
  strategy_id: string;
  overrides: Record<string, unknown>;
}

export interface BuildRequest {
  step: number;
  name?: string;
  description?: string;
  direction?: string;
  rules?: string;
  strategy_id?: string;
  current_code?: string;
  instruction?: string;
}

export interface AIGenerateRequest {
  prompt: string;
}

export interface AISaveRequest {
  code: string;
  strategy_id: string;
}

export interface ReloadStrategiesResponse {
  ok: boolean;
  count: number;
}

export interface StrategyDetail {
  id: string;
  name: string;
  description: string;
  tags: string[];
  source: string;
  version: string;
  basic_filter: Record<string, unknown>;
  params: unknown[];
  params_defaults: Record<string, unknown>;
  scoring: Record<string, unknown>;
  entry_signals: unknown[];
  exit_signals: unknown[];
  stop_loss: unknown;
  take_profit: unknown;
  trailing_stop: unknown;
  trailing_take_profit_activate: unknown;
  trailing_take_profit_drawdown: unknown;
  max_hold_days: unknown;
  alerts: unknown[];
  order_by: string;
  descending: boolean;
  limit: number;
  display_limit: number | null;
}

export interface StrategyListResponse {
  strategies: StrategyDetail[];
}

// ============================================================
// Stocks API
// ============================================================

export interface StockSpot {
  code: string;
  name: string;
  price: number | string;
  change_pct: number | string;
  change: number | string;
  volume: number | string;
  amount: number | string;
}

export interface StockSpotResponse {
  count: number;
  data: StockSpot[];
}