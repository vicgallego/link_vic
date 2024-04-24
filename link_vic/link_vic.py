import reflex as rx
import link_vic.styles.styles as styles

def index() -> rx.Component:
    return rx.box(

    )

app = rx.App(
    styleheets=styles.STYLEHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="Portafolio",
    description="description"
)

