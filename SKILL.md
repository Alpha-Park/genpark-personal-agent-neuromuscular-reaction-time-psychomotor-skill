---
name: genpark-personal-agent-neuromuscular-reaction-time-psychomotor-skill
version: "1.0.0"
description: "Zero-dependency Psychomotor Vigilance Task (PVT) attentional lapse counter, reciprocal speed modeler, and cumulative sleep debt neurobehavioral impairment evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Neuromuscular Reaction Time Psychomotor Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI companions to quantify sustained attention, calculate Psychomotor Vigilance Task (PVT) performance metrics (Mean RT, Median RT, Reciprocal Speed $\frac{1000}{RT}$, Lapse Count $\ge 500$ ms, False Starts $< 100$ ms), and estimate cumulative neurobehavioral sleep debt based on David Dinges' state-instability model.

## Agent In-Context Capabilities

- **Gold-Standard PVT Metrics**: Filters out anticipation errors and computes the reciprocal response speed ($s^{-1}$) sensitive to central nervous system slowing.
- **Sleep Loss Impairment Equivalence**: Translates attentional lapse frequency into objective physiological equivalents (e.g., equivalent to $0.05\%$ or $\ge 0.08\%$ Blood Alcohol Concentration).
- **Cumulative Sleep Debt Dose-Response**: Predicts the hours of chronic sleep pressure required to induce the observed vigilance state dispersion.

## Tools Summary

1. `evaluate_pvt_attentional_performance`: Computes reaction time distribution, lapses, reciprocal speed, and alertness tier.
2. `estimate_sleep_debt_from_pvt_lapses`: Correlates lapses to cumulative sleep debt hours and outlines restorative protocols.
