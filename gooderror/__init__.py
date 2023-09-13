import sys
from types import TracebackType
from linecache import getline
from os import path
import openai

class GoodError:
    """
    GoodError Initializer

    Attributes:
        gpt_key (str): Your GPT API key.
        use_colors (bool): Whether to use colors in the output.
    """

    ERROR = '\033[31;1m'
    TITLE = '\033[34m'
    LINE = '\033[33m'
    RESET = '\033[0m'


    def __init__(self, gpt_key=None, use_colors=True) -> None:
        self.__gpt_line = None
        self.gpt_key = gpt_key
        self.use_colors = use_colors
        sys.excepthook = self.handle_exception


    def __c(self, text, color):
        if self.use_colors:
            return f"{color}{text}{self.RESET}"
        return text


    def __send_to_gpt(self):
        if not self.gpt_key: return
        print(self.__c("\nWaiting for GPT to respond...", self.TITLE))
        try:
            openai.api_key = self.gpt_key
            response = openai.ChatCompletion.create(
                messages=[{"role": "user", "content": self.__gpt_line}],
                model="gpt-3.5-turbo"
            )
            gpt_response = response.choices[0].message.content
            print(self.__c(gpt_response, self.LINE))
        except Exception as e:
            print(self.__c(f"An error occurred while contacting GPT-3: {str(e)}", self.ERROR))


    def handle_exception(self, exc_type: type, exc_value: Exception, exc_traceback: TracebackType):
        trace_list: list[TracebackType] = []
        trace = exc_traceback
        while trace:
            trace_list.append(trace)
            trace = trace.tb_next

        exception_name = exc_type.__name__
        exception_message = str(exc_value).capitalize()

        print(f"{self.__c(f'{exception_name}({exception_message})', self.ERROR)}")

        for i, trace_item in enumerate(trace_list):
            line_number = trace_item.tb_lineno
            filename = trace_item.tb_frame.f_code.co_filename
            file_name = path.splitext(path.basename(filename))[0]
            line = getline(filename, line_number)
            if line:
                file_name = self.__c(file_name, self.TITLE)
                line_number = self.__c(f"Line {line_number}", self.LINE)
                if i == len(trace_list) - 1: 
                    line = self.__c(line.strip(), self.ERROR)
                    self.__gpt_line = f"Python code generated an error, {exception_name} : {line.strip()}"
                else: 
                    line = line.strip()
                print(f"{file_name}, {line_number} -> {line}")
        self.__send_to_gpt()
