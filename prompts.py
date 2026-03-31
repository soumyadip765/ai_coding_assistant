# prompts.py

def generate_code(language, problem, level):
    return f"""
You are an expert {language} developer.

Write {level} level {language} code for the following problem:

{problem}

Provide only the code.
"""


def explain_code(code):
    return f"""
Explain the following code in detail:

{code}
"""


def explain_code_simple(code):
    return f"""
Explain the following code in very simple beginner-friendly language:

{code}
"""


def debug_code(code, error):
    return f"""
The following code has an error.

Code:
{code}

Error:
{error}

Identify the issue and provide the corrected version of the code.
"""


def explain_concept(concept):
    return f"""
Explain the concept of:

{concept}

Provide examples where possible.
"""