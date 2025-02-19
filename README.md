# Maya_fk_chain_tool
**Creating simple fk controls in Maya**

![UI](https://github.com/user-attachments/assets/23b220ad-cea2-404e-a056-df32af99a216)

Also have a quick tutorial on Youtube:<br/>
  <a href="https://www.youtube.com/watch?v=Uqdp5lbCdl4"><img src="https://img.youtube.com/vi/Uqdp5lbCdl4/0.jpg" alt="IMAGE ALT TEXT"></a><br/>
  https://www.youtube.com/watch?v=Uqdp5lbCdl4
<br/>

Another personal project of creating a simple fk chain tool in Maya back in 2022/2023.<br/>
Mainly used for fingers, or maybe tails on animals.<br/>
Added various "customization" and "designs" for the controls...because I can...and it was a fun practice
## Setting Up
**1. First and foremost, set project to your project folder in Maya**<br/>
2. Make sure `finger_ctrls_01.ma` is placed in the `assets` folder in your project folder before actually running the script in Maya

It should look something like this:

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
Fast way:<br/>
Simply copy and paste the code to a new tab in Maya Script Editor<br/>
Select all and middle-mouse-button drag the code to the desired shelf for quick access

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
> Remember to run `reload(fk_chain_UI)` in Maya Script Editor if any changes were made to the `.py` file

## Features
The tool is fairly straight-forward and self-explanatory with all the steps read from top to bottom<br/>
1. Check if all joints are properly named<br/>
   Make sure the joints ends with `_JNT` before setting up the rig since the controls would inherit the joints' name and replace `_JNT` with `_CTRL` as their suffix
   > I am aware that this step shouldn't be necessary, but I do prefer the tidiness of my rigs<br/>
   This feature was added purely for my own convenience

2. Select the joints<br/>
   Make sure the joints are selected properly before building the rig<br/>
   > Since this is an fk chain rig, the last joint should be omitted, this feature is here to help select all the needed joints more easily and faster<br/>
   It also serves the purpose of identifying the root joint
   
3. Decide how the controls should look<br/>
   There are 4 colors and 7 designs to choose from for the controls<br/>
   The available colors are `Blue`, `Red`, `Yellow`, and `Green`<br/><br/>
   Designs:<br/>
   ![designs](https://github.com/user-attachments/assets/ff413d11-476c-4880-a3c6-da131d00343a)<br/>
   (from left to right)<br/>
   `Basic Circle`, `Basic Square`, `Circle Pin`, `Ball, Pin`, `Triangle Pin`, `Pyramid Pin`, and `Trapezoid Pin`
   
4. Create<br/>
   Hit `Create CTRLs` and start posing!
   > A student-version file pop-up should show up while importing the controls to the scene<br/>
   I know I could've edited it out in the `.ma` file, but I kept it there simply because all of this was *indeed* made in a student version of Maya during my time at AnimSchool<br/>
   Removing it felt wrong as if editing out the watermarks on a file exported with a free version application...
   
   > If it really bothers you to hit enter each time when creating the fk chain rig, deleting line `17` in the `.ma` file should stop the pop-up
5. Rename<br/>
   Put the new name in the text field and choose how the joints and controls should be sorted<br/>
   The `-` option(the default option) should follow Maya's default naming convention<br/>
   The `Numeric_0` starts with `0` whereas `Numeric_1` starts with `1`<br/>
   Alphabetic orders sort the joints and controls from `A` to `Z` and continue with `AA` to `ZZ`
   > Please refer to the [rename tool features](https://github.com/ycheng5948/Maya_rename_tool/tree/main#features) for more details<br/>
   
   > This feature was added after making the rename tool, and was not recorded in the above tutorial
   
