# Maya_fk_chain_tool
**Creating simple fk controls in Maya**

![UI](https://github.com/user-attachments/assets/23b220ad-cea2-404e-a056-df32af99a216)

Another personal project of creating a simple fk chain tool in Maya back in 2022/2023.<br/>
Mainly used for fingers, or maybe tails on animals.<br/>
Added various "customization" and "designs" for the controls...because I can...and it was a fun practice<br/><br/>
**1. First and foremost, set project to you project folder in Maya**<br/>
2. Make `finger_ctrls_01.ma` is placed in the `assets` folder in your project folder before actully running the script in Maya

```
.
└─ your Maya project folder\
   ├─ assets\
   │  └─ finger_ctrls_01.ma
   │
   ├─ autosave\
   ├─ cache\
   ├─ clips\
   ├─ data\
   ├─ ...
   └─ workspace.mel
```
----------<br/>
Fast way:<br/>
Simply copy and paste the code to a new tab in Maya Script Editor.<br/>
Select all and middle-mouse-button drag the code to the desired shelf for quick access.

----------<br/>

Or the slower but more tidier way:<br/>
1. Delete or comment out the last line at the end of the code
```
#IN Maya
fk_chain_UI.fk_chain() #comment this line out
```

2. Create a `fk_chain_UI.py` file and place it in your desired script folder, which might look a bit like: 
`C:\Users\user\Documents\maya\$MAYA_VERSION\scripts\$SCRIPT_FOLDER\fk_chain_UI.py`<br/>
3. In Maya Script editor, type or copy and paste the following:
```
from $SCRIPT_FOLDER import fk_chain_UI
fk_chain_UI.fk_chain()
```
> Make sure that the `$SCRIPT_FOLDER` has been changed to whatever you've named your script folder
> Remember to run `reload(fk_chain_UI)` in Maya Script Editor if you made any changes to the .py file

## Features
