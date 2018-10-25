Set oShell = WScript.CreateObject("WScript.Shell")
Dim Input, i
Input = InputBox("Insert count of clients")
oShell.run "cmd /K python server.py"
For i = 1 to CInt(Input)
oShell.run "cmd /K python client.py"
NEXT