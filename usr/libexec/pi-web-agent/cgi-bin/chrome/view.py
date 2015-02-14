import sys
import os
if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/pi-web-agent'
sys.path.append(os.environ['MY_HOME']+'/cgi-bin')
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/chrome')
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/toolkit')
sys.path.append(os.environ['MY_HOME']+'/etc/config')
import httplib
import cgi
from pi_web_agent import VERSION

def get_template(template):
    return os.environ['MY_HOME']+'/templates/' + template + '.htm'

def composeJS(stringifiedJSON, code=httplib.OK):
    print 'Status: ', code, ' ', httplib.responses[code]
    print 'Content-Type: application/json'
    print 'Cache-Control: no-store'
    print 'Length:', len(stringifiedJSON)
    print ''
    print stringifiedJSON
    
#any extension should be a subclass of view. View implements by default the default views
#of the menus in the user interface. The difference of each subclass of view should be
#on the content part of the interface. 

#The interface consists of two columns, one on the left and one on the far right. In the
#middle there are the results of an action and possible options and actions.


class View(object):
    '''
    This class forms the skeleton of the main view of the system. It forms
    the menus, titles and the main display area, where the results of each
    call are placed. This is returned by the function content. The rest are
    private since the skeleton parts must remain the same through the application's
    lifecycle
    '''

    def __init__(self, actions, cmdactions):
        self.start_part = ""
        self.end_part = ""
        self.content = ""
        self.contentTitle = ""
        self.setContent('Welcome', 'This is the web agent for the Raspberry PI')
        
    def setContent(self, title, content):
        self.content = content
        
    def output(self):
        template_start = get_template("_main_part1")
        template_end = get_template("_main_part2")
        with open(template_start) as sfile:
            self.start_part = sfile.read()
        with open(template_end) as efile:
            self.end_part = efile.read()
        outputHTMLDocument(self.start_part, self.contentTitle, self.content, self.end_part)
        
    def js_output(self):
        composeJS(self.content)
	

