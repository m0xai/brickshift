from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from ...models import CalendarWeek


class Command(BaseCommand):
    help = "Generate and save all calendar weeks for a given year"

    def add_arguments(self, parser):
        parser.add_argument(
            "year",
            type=int,
            help="Specify the year for which to generate calendar weeks",
        )

    def handle(self, *args, **options):
        year = options["year"]

        self.stdout.write(
            self.style.SUCCESS(f"Generating calendar weeks for {year}...")
        )

        # Get the first day of the year
        first_day = datetime(year, 1, 1)

        # Find the first Monday of the year
        first_monday = first_day + timedelta(days=(7 - first_day.weekday()))

        # Iterate through the weeks of the year
        current_week = 1
        while first_monday.year == year:
            start_of_week = first_monday
            end_of_week = start_of_week + timedelta(days=6)

            # Save the calendar week to the database
            CalendarWeek.objects.create(
                year=year, number=current_week, start=start_of_week, end=end_of_week
            )

            # Move to the next Monday
            first_monday += timedelta(weeks=1)
            current_week += 1

        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated calendar weeks for {year}")
        )
