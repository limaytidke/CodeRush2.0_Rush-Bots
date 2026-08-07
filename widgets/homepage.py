from textual.widgets import Static


class HomePage(Static):

    def on_mount(self):

        self.update(
"""
Repository Overview

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Welcome to CodeHarness

✔ Repository not loaded

✔ Memory Ready

✔ Context Manager Ready

✔ Awaiting user action...
"""
        )