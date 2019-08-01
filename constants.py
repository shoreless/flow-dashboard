# General info

AUTHOR_NAME = "Jeremy Gordon"
SITENAME = "Flow"
EMAIL_PREFIX = "[ Flow ] "
TAGLINE = "A personal dashboard to focus on what matters"
SECURE_BASE = "https://flowdash.co"

# Emails
APP_OWNER = "palehorsesailor@gmail.com"
ADMIN_EMAIL = APP_OWNER
DAILY_REPORT_RECIPS = [APP_OWNER]
SENDER_EMAIL = APP_OWNER
NOTIF_EMAILS = [APP_OWNER]

GCS_REPORT_BUCKET = "/flow_reports"
BACKGROUND_SERVICE = "default"

# Flags
NEW_USER_NOTIFICATIONS = False

DEFAULT_USER_SETTINGS = {
    'journals': {
        'questions': [
            {
                'name': "narrative",
                'text': "A few words on your day?",
                'response_type': "text",
                'parse_tags': True
            },
            {
                'name': "day_rating",
                'label': "Rating",
                'text': "How was the day?",
                'response_type': "slider",
                'chart': True,
                'chart_default': True,
                'tag_segment_chart': True,
                'color': '#dd0000'
            }
        ]
    }
}

# Strings
HABIT_DONE_REPLIES = [
    "Well done!",
    "Nice work!",
    "Alright!",
    "Great!",
    "Great job!",
    "Keep it up!"
]

HABIT_COMMIT_REPLIES = [
    "Yeah, do it!",
    "You can do it!",
    "Can't wait!",
    "Great idea!",
    "You got this"
]

TASK_DONE_REPLIES = [
    "That didn't look hard!",
    "Just like that",
    "Fini",
    "OK!",
    "OK",
    "Roger",
    "Check",
    "Great"
]

COOKIE_NAME = "flow_session"


class HABIT():

    HELP = "You can set habits to build, and track completion. Try saying 'new habit: run', 'habit progress', or 'commit to run tonight'"

    ACTIVE_LIMIT = 20


class EVENT():
    # Type
    PERSONAL = 1
    FAMILY = 2
    PROFESSIONAL = 3
    PUBLIC = 4


class JOURNAL():

    HELP = "You can set up daily questions to track anything you want over time. Try saying 'daily report'"

    # Timing
    START_HOUR = 21
    END_HOUR = 4
    HOURS_BACK = 8

    # Patterns
    PTN_TEXT_RESPONSE = '.*'
    PTN_NUM_RESPONSE = '\d{1,4}\.?\d{0,2}'

    # Response Types
    PATTERNS = {
        'text': PTN_TEXT_RESPONSE,
        'number': PTN_NUM_RESPONSE,
        'number_oe': PTN_NUM_RESPONSE,  # For input box entry
        'slider': PTN_NUM_RESPONSE
    }

    NUMERIC_RESPONSES = ['number', 'slider', 'number_oe']

    INVALID_REPLY = "I couldn't understand your answer."
    INVALID_SUFFIX_NUMERIC = "I'm expecting a number between 1 and 10."
    INVALID_TASK = "That didn't look like a task, please try again"
    TOP_TASK_PROMPT = "Enter a top task for tomorrow (or you can say 'done')"
    TOP_TASK_PROMPT_ADDTL = "Enter another top task for tomorrow (you can say 'done')"

    ALREADY_SUBMITTED_REPLY = "Sorry, you've already submitted today's journal."


class JOURNALTAG():
    # Types
    PERSON = 1
    HASHTAG = 2 # Activities, etc


class READABLE():
    # Type
    ARTICLE = 1
    BOOK = 2
    PAPER = 3

    LABELS = {
        ARTICLE: "Article",
        BOOK: "Book",
        PAPER: "Paper"
    }

    LOOKUP = {
        "article": 1,
        "book": 2,
        "paper": 3
    }


class TASK():
    # Status
    NOT_DONE = 1
    DONE = 2

    HELP = "You can set and track top tasks each day. Try saying 'add task remember the milk' or 'my tasks'"


class USER():
    USER = 1
    ADMIN = 2


class GOAL():

    HELP = "You can review your monthly and annual goals. Try saying 'view goals'"
    SET_INFO = "Bear with us as we're still in beta! Please visit flowdash.co to create monthly, annual, and long-term goals."

    DEFAULT_GOAL_SLOTS = 4

class REPORT():
    # Types
    HABIT_REPORT = 1
    TASK_REPORT = 2
    GOAL_REPORT = 3
    JOURNAL_REPORT = 4
    EVENT_REPORT = 5
    PROJECT_REPORT = 6
    TRACKING_REPORT = 7

    # Status
    CREATED = 1
    GENERATING = 2
    DONE = 3
    CANCELLED = 4
    ERROR = 5

    # STORAGE TYPES
    GCS_CLIENT = 1

    # Ftypes
    CSV = 1

    TYPE_LABELS = {
        HABIT_REPORT: "Habit Report",
        TASK_REPORT: "Task Report",
        GOAL_REPORT: "Goal Report",
        JOURNAL_REPORT: "Journal Report",
        EVENT_REPORT: "Event Report",
        TRACKING_REPORT: "Tracking Report"
    }

    STATUS_LABELS = {
        CREATED: "Created",
        GENERATING: "Generating",
        DONE: "Done",
        CANCELLED: "Cancelled",
        ERROR: "Error"
    }

    EXTENSIONS = {CSV: "csv"}
