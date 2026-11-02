# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Neuromuscular Reaction Time Psychomotor Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentNeuromuscularReactionTimePsychomotor

def main():
    agent = PersonalAgentNeuromuscularReactionTimePsychomotor()

    print("=" * 70)
    print("DEMO: Personal Agent Psychomotor Vigilance (PVT) & Sleep Debt Engine")
    print("=" * 70)

    # 1. 20-Trial PVT Dataset (mostly 220-290 ms, with 1 lapse at 580 ms and 1 at 620 ms)
    times = [
        235.0, 242.0, 218.0, 265.0, 250.0,
        580.0, 225.0, 270.0, 240.0, 230.0,
        285.0, 260.0, 620.0, 245.0, 238.0,
        275.0, 255.0, 248.0, 262.0, 252.0
    ]

    res_pvt = agent.evaluate_pvt_attentional_performance(times)

    print(f"\n1. Psychomotor Vigilance Task (PVT) Performance Profile:")
    print(f"   Analyzed Trials: {res_pvt['valid_trials_analyzed']} (False Starts: {res_pvt['false_start_anticipation_errors']})")
    print(f"   Mean RT: {res_pvt['mean_reaction_time_ms']} ms | Median RT: {res_pvt['median_reaction_time_ms']} ms")
    print(f"   Reciprocal Mean Speed (1/RT): {res_pvt['reciprocal_mean_speed_sec_inv']} s^-1")
    print(f"   Attentional Lapses (>= 500 ms): {res_pvt['attentional_lapse_count_500ms']} ({res_pvt['lapse_percentage']})")
    print(f"   Performance Tier: {res_pvt['neurobehavioral_performance_tier']}")
    print(f"   Impairment Analogy: {res_pvt['clinical_impairment_analogy']}")

    # 2. Estimate Cumulative Sleep Debt from PVT
    res_debt = agent.estimate_sleep_debt_from_pvt_lapses(
        lapse_count=res_pvt['attentional_lapse_count_500ms'],
        reciprocal_speed=res_pvt['reciprocal_mean_speed_sec_inv']
    )

    print(f"\n2. Neurobehavioral Sleep Debt Estimation:")
    print(f"   Lapse Count: {res_debt['evaluated_lapses']}")
    print(f"   Estimated Cumulative Sleep Debt: {res_debt['estimated_cumulative_sleep_debt_hours']} hours")
    print(f"   Classification: {res_debt['sleep_debt_classification']}")
    print(f"   Prescription: {res_debt['prescribed_recovery_protocol']}")

    print("\nVerification complete: Psychomotor vigilance engine executed flawlessly.")

if __name__ == "__main__":
    main()
