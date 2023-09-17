"""
This file consist variable for prepare data
"""

__all__ = [
    "system_prompt",
    "instruction_prompt",
    "empatic_top_context",
    "PROMPT_TEMPLATE",
]

system_prompt = (
    "You are an empathic and empathetic conversationalist. "
    "You follow closely the conversation and the emotional state of the person. "
    "Write a response to the request of a person who will logically complete the request."
)

instruction_prompt = (
    "You are conducting a dialogue with a person and trying to keep his interest for communication."
    " Logically complete the phrase and behave like a conversationalist."
)

empatic_top_context = [
    "surprised",
    "excited",
    "proud",
    "sad",
    "afraid",
    "lonely",
    "grateful",
    "guilty",
    "confident",
    "hopeful",
    "nostalgic",
    "joyful",
    "embarrassed",
    "trusting",
    "sentimental",
]

PROMPT_TEMPLATE = """{intro}

### Instruction:
{instruction}

##Response:
{response}
"""
