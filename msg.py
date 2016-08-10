
import sys, argparse
from PySide.QtGui import QApplication, QMessageBox

TYPES = {
    'info': QMessageBox.Information,
    'warn': QMessageBox.Warning,
    'question': QMessageBox.Question,
    'critical': QMessageBox.Critical
}

def show_message(title, message, icon):
    msg = QMessageBox(TYPES[icon], title, message, buttons=QMessageBox.Ok | QMessageBox.Cancel)
    return msg.exec_()

if __name__ == '__main__':

    parse = argparse.ArgumentParser()
    parse.add_argument('-t','--title', metavar='name', help='The title name')
    parse.add_argument('-m','--message', metavar='text', help='Message text')
    parse.add_argument('-i','--icon', metavar='type', help='Icon type: info, warn, question or critical')
    args = parse.parse_args()
    app = QApplication(sys.argv)

    title = 'Message Box' if args.title is None else args.title
    message = 'Lorem ipsum dolor sit amet' if args.message is None else args.message
    icon = 'info' if args.icon is None else args.icon

    sys.exit(show_message(title, message, icon))

