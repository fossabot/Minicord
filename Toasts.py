import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

app = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\WindowsPowerShell\\v1.0\\powershell.exe'

#create notifier
nManager = notifications.ToastNotificationManager
notifier = nManager.create_toast_notifier(app)

#define your notification as string
tString = """
  <toast>
    <visual>
      <binding template='ToastGeneric'>
        <text>Minicord Open Beta Test</text>
        <text>Thanks for trying out Minicord hope you enjoyed</text>
      </binding>
    </visual>
    <actions>
      <action
        content="Fuck off"
        arguments="action=delete"/>
      <action
        content="eat my ass"
        arguments="action=dismiss"/>
    </actions>        
  </toast>
"""

#convert notification to an XmlDocument
xDoc = dom.XmlDocument()
xDoc.load_xml(tString)

#display notification
notifier.show(notifications.ToastNotification(xDoc))