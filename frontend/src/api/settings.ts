import { api } from "./client";

import type {
  PipelineScheduleIn,
  EnrichedBatchSizeIn,
  IndexDailyBatchSizeIn,
  LimitLadderMonitorIn,
  DepthPollingIntervalIn,
  DepthFinalizeTimeIn,
  ReviewScheduleIn,
  ReviewPushIn,
} from "./types";

export const settingsApi = {
  updatePipelineSchedule(data: PipelineScheduleIn) {
    return api.put(
      "/api/settings/preferences/pipeline-schedule",
      data,
    );
  },

  updateInstrumentsSchedule(data: PipelineScheduleIn) {
    return api.put(
      "/api/settings/preferences/instruments-schedule",
      data,
    );
  },

  updateEnrichedBatchSize(data: EnrichedBatchSizeIn) {
    return api.put(
      "/api/settings/preferences/enriched-batch-size",
      data,
    );
  },

  updateIndexDailyBatchSize(data: IndexDailyBatchSizeIn) {
    return api.put(
      "/api/settings/preferences/index-daily-batch-size",
      data,
    );
  },

  updateLimitLadderMonitor(data: LimitLadderMonitorIn) {
    return api.put(
      "/api/settings/preferences/limit-ladder-monitor",
      data,
    );
  },

  runLimitLadderFix() {
    return api.post(
      "/api/settings/preferences/limit-ladder-monitor/run",
    );
  },

  updateDepthPollingInterval(
    data: DepthPollingIntervalIn,
  ) {
    return api.put(
      "/api/settings/preferences/depth-polling-interval",
      data,
    );
  },

  updateDepthFinalizeTime(
    data: DepthFinalizeTimeIn,
  ) {
    return api.put(
      "/api/settings/preferences/depth-finalize-time",
      data,
    );
  },

  updateReviewSchedule(
    data: ReviewScheduleIn,
  ) {
    return api.put(
      "/api/settings/preferences/review-schedule",
      data,
    );
  },

  updateReviewPush(
    data: ReviewPushIn,
  ) {
    return api.put(
      "/api/settings/preferences/review-push",
      data,
    );
  },
};