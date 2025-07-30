import webview
import sys
import time
sys.path.append('../')
import strmquiz.test_builder
class mywebviewer:
    def __init__(self, config_file=""):
        self.filename = None
        # parser 
        self.parser = strmquiz.test_builder.test_builder(config_file=config_file)
    def load_css(self, window, ):
        filepath = "./timetable/css/style.css"
        try:
            cssfile = open(filepath)
        except:
            print("Can't open CSS file", filepath)
            sys.exit()

        csstring = cssfile.read()
        # ~ print("CSS:", csstring)
        window.load_css(csstring)
    def open_file_dialog(self, window):
        
        time.sleep(3)
        file_types = ('TimeTable (*.oct)', 'All files (*.*)')

        filenames = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False, file_types=file_types)
        print(filenames[0])
        self.filename = filenames[0]

        window.load_url("resources/html/main.html")

     
    
    def update(self, command):
        result = "Nothing"
      
        # ~ if command in self.parser.commands:
        if command in ["test1", "test2", "test3"]:
            result = self.parser.get_test(command) 
        else: # reset
            donothing()
            result = "Nothing to do with %s"%command
        return result

if __name__ == '__main__':
    viewer = mywebviewer()
    window = webview.create_window('Open file dialog', 'https://pywebview.flowrl.com/hello')
    webview.start(viewer.open_file_dialog, window)
    # ~ webview.start(viewer.load_css, window)

