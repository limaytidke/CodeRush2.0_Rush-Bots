from textual.screen import Screen
from textual.containers import Horizontal, Vertical
from textual.widgets import Static
from textual.widgets import Button
from widgets.sidebar import SideBar
from widgets.homepage import HomePage
from widgets.topbar import TopBar
from widgets.footerbar import FooterBar

class Dashboard(Screen):

    def compose(self):
        yield FooterBar()

        yield TopBar()

        with Horizontal():

            with Vertical(id="sidebar"):

                yield SideBar()

            with Vertical(id="content"):

                yield HomePage()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle sidebar button clicks."""

        if event.button.id == "exit":
            self.app.exit()