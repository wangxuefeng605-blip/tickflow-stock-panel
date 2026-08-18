import { api } from "./client";

import type {
  RunRequest,
  RunAllRequest,
  SaveConfigRequest,
  BuildRequest,
  AIGenerateRequest,
  AISaveRequest,
  StrategyListResponse,
  ReloadStrategiesResponse,
} from "./types";

export const strategiesApi = {
  list() {
    return api.get<StrategyListResponse>(
      "/api/strategies",
    );
  },

  get(strategyId: string) {
    return api.get<unknown>(
      `/api/strategies/${encodeURIComponent(strategyId)}`,
    );
  },

  remove(strategyId: string) {
    return api.delete<unknown>(
      `/api/strategies/${encodeURIComponent(strategyId)}`,
    );
  },

  run(data: RunRequest) {
    return api.post<unknown>(
      "/api/strategies/run",
      data,
    );
  },

  runAll(data: RunAllRequest = {}) {
    return api.post<unknown>(
      "/api/strategies/run-all",
      data,
    );
  },

  saveConfig(data: SaveConfigRequest) {
    return api.post<unknown>(
      "/api/strategies/config",
      data,
    );
  },

  resetConfig(strategyId: string) {
    return api.delete<unknown>(
      `/api/strategies/config/${encodeURIComponent(strategyId)}`,
    );
  },

  aiStatus() {
    return api.get<unknown>(
      "/api/strategies/ai/status",
    );
  },

  aiTest() {
    return api.post<unknown>(
      "/api/strategies/ai/test",
    );
  },

  build(data: BuildRequest) {
    return api.post<unknown>(
      "/api/strategies/build",
      data,
    );
  },

  aiGenerate(data: AIGenerateRequest) {
    return api.post<unknown>(
      "/api/strategies/ai/generate",
      data,
    );
  },

  aiSave(data: AISaveRequest) {
    return api.post<unknown>(
      "/api/strategies/ai/save",
      data,
  );
  },

  reload() {
    return api.post<ReloadStrategiesResponse>(
      "/api/strategies/reload",
    );
  },

  source(strategyId: string) {
    return api.get<unknown>(
      `/api/strategies/${encodeURIComponent(strategyId)}/source`,
    );
  },
};
