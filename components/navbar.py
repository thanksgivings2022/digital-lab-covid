from dash import html
import dash_bootstrap_components as dbc

# make a reuseable dropdown for the different examples
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Entry 1"),
        dbc.DropdownMenuItem("Entry 2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Entry 3"),
    ],
    nav=True,
    in_navbar=True,
    label="Menu",
)


def navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Accueil", href="/")),
            dbc.NavItem(dbc.NavLink("Exploration", href="exploration")),
            dbc.NavItem(dbc.NavLink("Prediction", href="prediction")),
        ],
        brand="Centrale DigitalLab - Team 1",
        brand_href="#",
        sticky="top",
        color="primary",
        dark=True,
        className="mb-5",
    )
