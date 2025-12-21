from features.open_web import open_website
from features.launch_apps import launch_application
from features.tell_joke import tell_joke
from features.get_datetime import tell_date_time
from features.notes import write_note, read_notes, clear_notes
from core.intents import Intent

COMMAND_REGISTRY = {
    Intent.OPEN: open_website,
    Intent.LAUNCH: launch_application,
    Intent.JOKE: tell_joke,
    Intent.TIME: tell_date_time,
    Intent.DATE: tell_date_time,
    Intent.WRITE_NOTE: write_note,
    Intent.READ_NOTES: read_notes,
    Intent.CLEAR_NOTES: clear_notes,
}
