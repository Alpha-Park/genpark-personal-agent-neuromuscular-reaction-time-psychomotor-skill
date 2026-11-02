# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Neuromuscular Reaction Time Psychomotor Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentNeuromuscularReactionTimePsychomotor

mcp = FastMCP("PersonalAgentNeuromuscularReactionTimePsychomotor")
client = PersonalAgentNeuromuscularReactionTimePsychomotor()

@mcp.tool()
def evaluate_pvt_attentional_performance(
    reaction_times_json: str
) -> str:
    """Calculates mean RT, median RT, reciprocal speed (1/RT), lapse count (>= 500ms), and alertness tier."""
    import json
    data = json.loads(reaction_times_json) if isinstance(reaction_times_json, str) else reaction_times_json
    return json.dumps(client.evaluate_pvt_attentional_performance(
        data
    ), indent=2)

@mcp.tool()
def estimate_sleep_debt_from_pvt_lapses(
    lapse_count: int = 4,
    reciprocal_speed: float = 3.3
) -> str:
    """Estimates cumulative sleep debt hours and impairment tier from PVT lapses."""
    import json
    return json.dumps(client.estimate_sleep_debt_from_pvt_lapses(
        lapse_count, reciprocal_speed
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
