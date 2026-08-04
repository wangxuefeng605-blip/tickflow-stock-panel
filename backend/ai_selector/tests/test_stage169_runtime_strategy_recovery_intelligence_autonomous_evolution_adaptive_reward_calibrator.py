from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_reward_calibrator import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveRewardCalibrator
)



def test_reward_increase():

    calibrator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveRewardCalibrator()
    )


    result = calibrator.calibrate(
        {
            "strategy": "adaptive_restore",
            "performance": 0.8,
            "improvement_signal": "increase"
        }
    )


    assert result["reward"] == 0.9
    assert result["calibrated"] is True



def test_reward_adjust():

    calibrator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveRewardCalibrator()
    )


    result = calibrator.calibrate(
        {
            "strategy": "rollback",
            "performance": 0,
            "improvement_signal": "adjust"
        }
    )


    assert result["reward"] == 0



def test_reward_history():

    calibrator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveRewardCalibrator()
    )


    calibrator.calibrate(
        {
            "strategy": "test",
            "performance": 1,
            "improvement_signal": "increase"
        }
    )


    assert len(
        calibrator.get_history()
    ) == 1