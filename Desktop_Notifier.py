#python Desktop Notifier

from win10toast import ToastNotifier

Toast = ToastNotifier()

Toast.show_toast("Coding Time","It's time to code Shaon!", duration=10, threaded=True)