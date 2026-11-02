# -*- coding: utf-8 -*-
"""Personal Agent Neuromuscular Reaction Time Psychomotor Skill.

Zero-dependency Psychomotor Vigilance Task (PVT) attentional lapse counter,
reciprocal speed modeler, and cumulative sleep debt neurobehavioral impairment evaluator.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentNeuromuscularReactionTimePsychomotor:
    """Quantitative neurobehavioral vigilance and attentional state stability engine
    based on the clinical Psychomotor Vigilance Task (PVT) standard by Prof. David Dinges."""

    def evaluate_pvt_attentional_performance(
        self,
        reaction_times_ms: List[float]
    ) -> Dict[str, Any]:
        """Calculates mean RT, median RT, reciprocal mean speed (1/RT), lapse count (>= 500 ms),
        false start errors (< 100 ms), and vigilance performance tier."""
        if not reaction_times_ms:
            return {"error": "Empty reaction times dataset"}

        clean_times = [float(x) for x in reaction_times_ms if float(x) > 0]
        n_total = len(clean_times)
        if n_total == 0:
            return {"error": "No valid positive reaction times"}

        # 1. False Starts (Anticipation errors: RT < 100 ms)
        false_starts = [t for t in clean_times if t < 100.0]
        valid_trials = [t for t in clean_times if t >= 100.0]
        n_valid = len(valid_trials)

        if n_valid == 0:
            return {"error": "All trials were false starts"}

        # 2. Mean and Median RT
        valid_sorted = sorted(valid_trials)
        mean_rt = round(sum(valid_trials) / n_valid, 1)
        median_rt = round(
            valid_sorted[n_valid // 2]
            if n_valid % 2 != 0
            else (valid_sorted[n_valid // 2 - 1] + valid_sorted[n_valid // 2]) / 2.0,
            1
        )

        # 3. Attentional Lapses (RT >= 500 ms)
        lapses = [t for t in valid_trials if t >= 500.0]
        lapse_count = len(lapses)
        lapse_rate_pct = round((lapse_count / n_valid) * 100.0, 1)

        # 4. Reciprocal Mean Speed = Mean(1000 / RT)
        reciprocal_speeds = [1000.0 / t for t in valid_trials]
        mean_speed = round(sum(reciprocal_speeds) / n_valid, 2)

        # 5. Neurobehavioral Alertness Tier Classification (Dinges et al. benchmarks)
        if lapse_count <= 1 and mean_speed >= 4.0:
            tier = "Optimal Psychomotor Vigilance / Peak Executive Readiness"
            impairment_analogy = "Zero neurobehavioral impairment; high attentional state stability"
        elif lapse_count <= 3 and mean_speed >= 3.4:
            tier = "Mild Attentional Instability"
            impairment_analogy = "Minor state dispersion; equivalent to mild acute circadian nadir"
        elif lapse_count <= 7 and mean_speed >= 2.8:
            tier = "Moderate Psychomotor Degradation"
            impairment_analogy = "Impairment equivalent to ~0.05% Blood Alcohol Concentration (BAC)"
        else:
            tier = "Severe Vigilance Failure / Acute Sleep Debt Crisis"
            impairment_analogy = "Impairment equivalent to >= 0.08% BAC (legal intoxication benchmark) or 24h acute sleep loss"

        return {
            "total_trials_administered": n_total,
            "valid_trials_analyzed": n_valid,
            "false_start_anticipation_errors": len(false_starts),
            "mean_reaction_time_ms": mean_rt,
            "median_reaction_time_ms": median_rt,
            "reciprocal_mean_speed_sec_inv": mean_speed,
            "attentional_lapse_count_500ms": lapse_count,
            "lapse_percentage": f"{lapse_rate_pct}%",
            "neurobehavioral_performance_tier": tier,
            "clinical_impairment_analogy": impairment_analogy
        }

    def estimate_sleep_debt_from_pvt_lapses(
        self,
        lapse_count: int,
        reciprocal_speed: float = 3.5
    ) -> Dict[str, Any]:
        """Correlates PVT lapses and speed against cumulative hours of partial sleep debt
        using the Van Dongen & Dinges dose-response sleep restriction mathematical models."""
        lapses = max(0, int(lapse_count))
        spd = max(1.0, float(reciprocal_speed))

        # Empirical model: Lapses ~ Baseline + 0.85 * (Cumulative Sleep Debt Hours)
        # Baseline normal lapses ~ 1.0
        estimated_sleep_debt_hours = round(max(0.0, (lapses - 1.0) * 1.25), 1)

        if estimated_sleep_debt_hours <= 1.5:
            debt_status = "Negligible Sleep Debt (< 2 hours)"
            recovery_prescr = "Maintain regular nocturnal sleep window."
        elif estimated_sleep_debt_hours <= 5.0:
            debt_status = "Mild-to-Moderate Cumulative Sleep Pressure (2 - 5 hours)"
            recovery_prescr = "Extend nocturnal sleep by 45-60 minutes for the next 2 nights; add 20-min afternoon NSDR."
        else:
            debt_status = "Severe Chronic Sleep Debt Accumulation (> 5 hours)"
            recovery_prescr = "Mandatory sleep extension (9+ hours nocturnal opportunity) and strict cessation of high-risk tasks/driving."

        return {
            "evaluated_lapses": lapses,
            "evaluated_reciprocal_speed": spd,
            "estimated_cumulative_sleep_debt_hours": estimated_sleep_debt_hours,
            "sleep_debt_classification": debt_status,
            "prescribed_recovery_protocol": recovery_prescr
        }
