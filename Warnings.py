from enum import Enum
import traceback
import sys
import os

class FancyError(Enum):
    PASSWORD_WEAK = "Password does not meet complexity rules."
    SQL_INJECTION_DETECTED = "SQL injection attack detected."
    USER_BANNED = "User is banned due to repeated violations."
    INVALID_EMAIL = "Provided email address is not valid."
    VALUE_ERROR = "A general value error occurred."
    AIDECT ="AI detected"

class ErrorCollector:
    def __init__(self):
        self.errors = []

    def fancy_error(self, error: FancyError, *, raise_error=False, details=None):
        # Extract traceback info
        tb = traceback.extract_stack(limit=3)[-2]
        filepath = os.path.abspath(tb.filename)
        line_no = tb.lineno
        code_line = tb.line.strip() if tb.line else ""

        # ANSI red
        RED = "\033[91m"
        RESET = "\033[0m"
        BLOCK = RED + "✖" * 70 + RESET

        # Full message
        main_msg = f"{error.name}: {error.value}"
        if details:
            main_msg += f" ({details})"

        error_block = f"""{RED}
{'✖'*70}
❌ ERROR: {main_msg}
📄 FILE: {filepath}:{line_no}
💬 CODE: {code_line}
🚨 TYPE: {error.name}
{'✖'*70}{RESET}
"""
        print(error_block, file=sys.stderr)
        self.errors.append(error_block)

        if raise_error:
            raise Exception(main_msg)

    def report_all(self):
        if not self.errors:
            return
        RED = "\033[91m"
        RESET = "\033[0m"
        for err in self.errors:
            print(err)
        sys.exit(1)