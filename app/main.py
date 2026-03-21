"""
HEALTH RISK CHECKER APP - MAIN FILE
Mobile-optimized version for Android/Web deployment
"""

import flet as ft
from prediction_engine import PredictionEngine
from ui_components import (
    create_welcome_screen,
    create_selection_screen,
    create_diabetes_form,
    create_hypertension_form,
    create_results_screen,
    create_educational_screen
)


class HealthRiskApp:
    """Main application class"""

    def __init__(self, page: ft.Page):
        """Initialize the app"""
        self.page = page
        self.page.title = "Health Risk Checker"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 16
        self.page.bgcolor = ft.colors.WHITE

        # Mobile-first responsive settings
        self.page.window_width = 400
        self.page.window_height = 700
        self.page.window_resizable = True

        # Initialize prediction engine
        self.prediction_engine = PredictionEngine()

        # App state
        self.current_condition = None
        self.prediction_results = None

        # Show welcome screen
        self.show_welcome_screen()

    def show_welcome_screen(self):
        """Display welcome screen"""
        self.page.clean()
        welcome_content = create_welcome_screen(
            on_get_started=self.show_selection_screen
        )
        self.page.add(welcome_content)
        self.page.update()

    def show_selection_screen(self, e=None):
        """Display condition selection screen"""
        self.page.clean()
        selection_content = create_selection_screen(
            on_diabetes=self.show_diabetes_form,
            on_hypertension=self.show_hypertension_form,
            on_both=self.show_both_forms
        )
        self.page.add(selection_content)
        self.page.update()

    def show_diabetes_form(self, e=None):
        """Display diabetes assessment form"""
        self.current_condition = 'diabetes'
        self.page.clean()
        diabetes_content = create_diabetes_form(
            on_submit=self.handle_diabetes_prediction,
            on_back=self.show_selection_screen
        )
        self.page.add(diabetes_content)
        self.page.update()

    def show_hypertension_form(self, e=None):
        """Display hypertension assessment form"""
        self.current_condition = 'hypertension'
        self.page.clean()
        hypertension_content = create_hypertension_form(
            on_submit=self.handle_hypertension_prediction,
            on_back=self.show_selection_screen
        )
        self.page.add(hypertension_content)
        self.page.update()

    def show_both_forms(self, e=None):
        """Show diabetes form first, then hypertension"""
        self.current_condition = 'both'
        self.show_diabetes_form()

    def handle_diabetes_prediction(self, user_inputs):
        """Process diabetes prediction"""
        try:
            # Show loading
            self.page.clean()
            self.page.add(
                ft.Container(
                    content=ft.Column([
                        ft.ProgressRing(),
                        ft.Text("Analyzing your data...", size=16)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                    expand=True
                )
            )
            self.page.update()

            # Make prediction
            results = self.prediction_engine.predict_diabetes(user_inputs)

            # Show results
            self.show_results(results, 'diabetes')

        except Exception as e:
            self.show_error(f"Error making prediction: {str(e)}")

    def handle_hypertension_prediction(self, user_inputs):
        """Process hypertension prediction"""
        try:
            # Show loading
            self.page.clean()
            self.page.add(
                ft.Container(
                    content=ft.Column([
                        ft.ProgressRing(),
                        ft.Text("Analyzing your data...", size=16)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    alignment=ft.alignment.center,
                    expand=True
                )
            )
            self.page.update()

            # Make prediction
            results = self.prediction_engine.predict_hypertension(user_inputs)

            # Show results
            self.show_results(results, 'hypertension')

        except Exception as e:
            self.show_error(f"Error making prediction: {str(e)}")

    def show_results(self, results, condition_type):
        """Display prediction results"""
        self.prediction_results = results
        self.page.clean()
        results_content = create_results_screen(
            results=results,
            condition_type=condition_type,
            on_learn_more=lambda e: self.show_educational_content(condition_type),
            on_reset=self.reset_app
        )
        self.page.add(results_content)
        self.page.update()

    def show_educational_content(self, condition_type):
        """Display educational information"""
        self.page.clean()
        educational_content = create_educational_screen(
            condition_type=condition_type,
            on_back=lambda e: self.show_results(self.prediction_results, condition_type)
        )
        self.page.add(educational_content)
        self.page.update()

    def show_error(self, error_message):
        """Display error screen"""
        self.page.clean()
        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.ERROR_OUTLINE, size=100, color=ft.colors.RED),
                    ft.Text("Oops! Something went wrong", size=24, weight=ft.FontWeight.BOLD),
                    ft.Container(height=20),
                    ft.Text(error_message, size=14, text_align=ft.TextAlign.CENTER),
                    ft.Container(height=40),
                    ft.ElevatedButton(
                        "Try Again",
                        on_click=self.reset_app,
                        bgcolor=ft.colors.BLUE,
                        color="white"
                    )
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=40,
                alignment=ft.alignment.center,
                expand=True
            )
        )
        self.page.update()

    def reset_app(self, e=None):
        """Reset app to welcome screen"""
        self.current_condition = None
        self.prediction_results = None
        self.show_welcome_screen()


def main(page: ft.Page):
    """App entry point"""
    HealthRiskApp(page)


# Run the app
if __name__ == "__main__":
    ft.app(target=main)
