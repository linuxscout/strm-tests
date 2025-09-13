import logging
import os.path
import json
from fastapi import FastAPI, Request, Query
from fastapi import HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional, Dict, Any

from pydantic import BaseModel
class Submission(BaseModel):
    category: str
    command: str
    args: Dict[str, Any]
    select_random_values: bool = True
    outformat: str = "html"
    quizid: str = ""

from strmquiz.quizbuilder import QuizBuilder

WEB_TEMPALTES_DIR = os.path.join(os.path.dirname(__file__),"templates")
# WEB_TEMPALTES_DIR = "templates"
WEB_STATIC_DIR = os.path.join(os.path.dirname(__file__),"static")
# WEB_STATIC_DIR = "static"



QUIZ_TEMPALTES_DIR = os.path.join(os.path.dirname(__file__),"..", "templates")
CONF_DIR = os.path.join(os.path.dirname(__file__),"..", "tests", "config")
CONF_FILE = os.path.join(CONF_DIR, "quiz7.conf")
app = FastAPI()

# Setup templates and static
templates = Jinja2Templates(directory=WEB_TEMPALTES_DIR)
app.mount("/static", StaticFiles(directory=WEB_STATIC_DIR), name="static")
# app.mount("/static", StaticFiles(directory="static"), name="static")
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
    return templates.TemplateResponse(request,"base.html", {"request": request})


@app.get("/quiz", response_class=HTMLResponse)
async def get_quiz(request: Request):
    """Generate and display a new quiz."""
    commands_dict = QuizBuilder.get_commands_info()
    categories_dict = QuizBuilder.get_categories()
    quiz_id_list = quiz_builder.get_quiz_id_list()
    formats_dict = QuizBuilder.get_available_formats()
    category_commands = {
        cat: cats["commands"] for cat, cats in categories_dict.items()
    }
    response  = {"request": request,
                 "commands_dict": commands_dict,
                 "commands_dict_json": json.dumps(commands_dict),
                 "categories_dict": categories_dict,
                 "category_commands_json": json.dumps(category_commands),
                 "format_dict": formats_dict,
                 "quiz_id_list": quiz_id_list
                 }
    return templates.TemplateResponse(request,"quiz.html", response)



@app.get("/api/categories")
async def get_categories():
    """Return all categories with descriptions."""
    categories_info = QuizBuilder.get_categories()
    return JSONResponse(categories_info)


@app.get("/api/commands")
async def get_commands(category: Optional[str] = Query(None, description="Filter by category name")):
    """Return all commands, optionally filtered by category."""
    commands_dict = QuizBuilder.get_commands_info()
    if category:
        cmds =  QuizBuilder.get_commands_info(category=category)
        return JSONResponse(cmds)
    return JSONResponse(commands_dict)


@app.get("/api/random-commands")
async def get_random_commands(n: int = 3, category: Optional[str] = None):
    """Return N random commands (default 3)."""
    cmd_info = quiz_builder.get_random_commands(n=n,category=category)
    if not cmd_info:
        return {"error": "No commands in this category"}
    return {"commands_list": cmd_info}


@app.post("/submit",)
async def submit(request:Request, data: Submission):
    """Process submitted answers with validation."""

    # Normalize input (in case user manipulates HTML or sends uppercase)
    command = data.command.strip().lower()
    category = data.category.strip().lower()
    args = data.model_dump().get("args",{})
    # use random values for question or defaults
    # select_random_values = data.select_random_values
    # quiz_id = data.quizid
    # outformat = data.outformat



    # Validate category if not "random"
    valid_categories = set(quiz_builder.categories_info.keys())
    if category and category != "random" and category not in valid_categories:
        raise HTTPException(status_code=400, detail=f"Invalid category '{category}'")

    # Decide command
    if command == "random":
        # If both category and command are random → pick fully random
        if category == "random":
            category = ""
        # quiz_builder will handle empty category as "any"
        cmd_list = quiz_builder.get_random_commands_list(category=category)
        command_to_run = cmd_list[0] if cmd_list else ""
    else:
        # Validate command exists
        if command not in quiz_builder.commands_info:
            raise HTTPException(status_code=400, detail=f"Invalid command '{command}'")

        # If a specific category is chosen, enforce consistency
        if category and category != "random":
            cmd_info = quiz_builder.commands_info[command]
            if cmd_info["category"] != category:
                raise HTTPException(
                    status_code=400,
                    detail=f"Command '{command}' does not belong to category '{category}'"
                )

        command_to_run = command

    # Get question and answer
    # args = {command:args}
    # set random mode or disable it for quizbuiler
    quiz_builder.set_select_random_values(data.select_random_values)
    new_args = quiz_builder.validate_command_args(command=command_to_run, args_src=args)

    # set format:
    quiz_builder.set_format(outformat=data.outformat)
    question, answer = quiz_builder.get_question(command=command_to_run, args = new_args)

    if data.quizid:
        quiztext = quiz_builder.get_quiz(test_no=data.quizid)
    else:
        quiztext =""

    response = {
        # "request": request,
        "command": command_to_run,
        "outformat":data.outformat,
        "category": category,
        "question": question,
        "answer": answer,
        "args":new_args,
        "quiztext":quiztext,
    }
    # return templates.TemplateResponse(request, "result.html", response)
    if data.outformat.lower() == "json":
        return JSONResponse(content=response)
    else:
        # return HTML
        return  templates.TemplateResponse(request, "result.html", response)
        # return HTMLResponse(content=html_content)




