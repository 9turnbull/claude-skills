"""
Python Agent SDK App — Claude Code Skills Repository Explorer

Uses the Claude Agent SDK to explore this skills repository
with built-in file tools (Read, Glob, Grep).

Requirements:
    pip install claude-agent-sdk

Usage:
    python agent_app.py
    python agent_app.py "find all Python scripts in engineering-team"
"""

import sys
import anyio
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage, SystemMessage


async def run_agent(prompt: str) -> None:
    """Run the agent with the given prompt and print results."""
    print(f"Prompt: {prompt}\n")
    print("─" * 60)

    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            cwd="/home/user/claude-skills",
            allowed_tools=["Read", "Glob", "Grep"],
            model="claude-opus-4-6",
            max_turns=10,
        ),
    ):
        if isinstance(message, ResultMessage):
            print(message.result)
            print(f"\n[stop_reason: {message.stop_reason}]")
        elif isinstance(message, SystemMessage) and message.subtype == "init":
            session_id = message.data.get("session_id", "unknown")
            print(f"[session: {session_id}]\n")


def main() -> None:
    prompt = (
        " ".join(sys.argv[1:])
        if len(sys.argv) > 1
        else "List the top-level skill domains in this repository and briefly describe each one."
    )
    anyio.run(run_agent, prompt)


if __name__ == "__main__":
    main()
