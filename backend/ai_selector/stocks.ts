import { api } from "./client";

import type {
  StockSpot,
  StockSpotResponse,
} from "./types";

export const stocksApi = {
  spot() {
    return api.get<StockSpotResponse>(
      "/api/stocks/spot",
    );
  },
};