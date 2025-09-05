import os.path
import json
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from strmquiz.quizbuilder import QuizBuilder
WEB_TEMPALTES_DIR = os.path.join(os.path.dirname(__file__),"templates")
QUIZ_TEMPALTES_DIR = os.path.join(os.path.dirname(__file__),"..", "templates")
CONF_DIR = os.path.join(os.path.dirname(__file__),"..", "tests", "config")
CONF_FILE = os.path.join(CONF_DIR, "quiz6.conf")
app = FastAPI()

# Setup templates and static
templates = Jinja2Templates(directory=WEB_TEMPALTES_DIR)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize your quiz generator
quiz_builder = QuizBuilder(
    outformat="html",
    config_file=CONF_FILE,   # example config file
    lang="en",
    templates_dir=QUIZ_TEMPALTES_DIR
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Homepage with a button to generate quiz."""
    return templates.TemplateResponse("base.html", {"request": request})


@app.get("/quiz", response_class=HTMLResponse)
async def get_quiz(request: Request):
    """Generate and display a new quiz."""
    commands_dict = quiz_builder.get_commands_info()  # assumes generate() returns dict with questions
    categories_dict = quiz_builder.get_categories()  # assumes generate() returns dict with questions
    category_commands = {
        cat: cats["commands"] for cat, cats in categories_dict.items()
    }
    response  = {"request": request,
                 "commands_dict": commands_dict,
                 "categories_dict": categories_dict,
                 "category_commands_json": json.dumps(category_commands),
                 }
    return templates.TemplateResponse("quiz.html", response)


@app.post("/submit", response_class=HTMLResponse)
async def submit_quiz(request: Request, command: str = Form(...), category: str = Form(...)):
    """Process submitted answers."""
    # TODO: replace with quiz_builder’s checking logic
    if command.lower() == "random":
        if category.lower()=="random":
            category = ""
        command_to_run, _ = quiz_builder.get_random_command(category=category)
    else:
        command_to_run = command
    question,answer = quiz_builder.get_question(command=command_to_run)
    # question = "".join(question)
    # answer = "".join(answer)
    response  =  {"request": request,
                  "command": command,
                  "category":category,
                  "question": question,
                  "answer": answer,
                  }
    return templates.TemplateResponse(
        "result.html",
       response,
    )
