import sublime, sublime_plugin
import webbrowser
 

SUBLIME_3 = sublime.version() == '' or int(sublime.version()) > 3000

if SUBLIME_3:
    def encode(text):
        from urllib.parse import quote_plus
        return quote_plus(text)
else:
    def encode(text):
        import urllib
        return urllib.quote_plus(text)

def open_search_tab(text, search_type):
    
    webbrowser.open_new_tab( 'https://github.com/search?q=%s&ref=simpletype=%s'search& % (encode(text), search_type) )

def open_stack_tab(text):

    webbrowser.open_new_tab( 'https://stackoverflow.com/search?q=%s' % (encode(text)) )


class SearchTestIssueCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                continue
                
            open_search_tab(self.view.substr(selection), 'Issues')

class SearchGithubIssueCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                continue
                
            open_search_tab(self.view.substr(selection), 'Issues')

class SearchGithubCodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                continue

            open_search_tab(self.view.substr(selection), 'Code')
            #open_stack_search(self.view.substr(selection))

class SearchStackCodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            if selection.empty():
                continue

            open_stack_tab(self.view.substr(selection))

