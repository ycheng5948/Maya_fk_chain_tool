from maya import cmds

class fk_chain(object):

    #constructor
    def __init__(self):

        self.window = "fk_chain"
        self.title = "Create Simple FK"
        self.size = (550, 600)

        # close old window if open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window=True)

        #create new window
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)

################################################################### UI CONTENT

        cmds.columnLayout(adjustableColumn = True)

        cmds.separator(h=10)
        cmds.text(self.title, h=30)
        cmds.separator(h=10)

###################################################################
        #CHECK JOINTS' NAMES
        cmds.separator(h=10)

        cmds.text(label="Do all ends with \"_JNT\"?")
        cmds.text(label="")
        cmds.text(label="If yes, skip this step, if no, please rename")
        cmds.text(label="Select target joint(s) and...")
        cmds.text(label="")

        self.addJNTtoSel = cmds.button(label="add _JNT to selected JNTs", command=self.addJNTtoSel)
        self.addJNTtoAll = cmds.button(label="add _JNT to hierarchy JNTs", command=self.addJNTtoAll)
        self.rename_TarJNT = cmds.ls(sl=True)

###################################################################
        #SELECT JNT
        cmds.separator(h=10)

        cmds.text(label="I. Select target joint(s)")
        cmds.text(label="")
        cmds.text(label="1. Please select the first target JNT(s)")
        self.First_TarJNT = cmds.ls(sl=True)
        cmds.text(label="2. Select its hierarchy? (End JNT excluded)")
        cmds.text(label="")
        self.DeselectEndJNT = cmds.button(label="Yes", command=self.DeselectEndJNT)

        self.TarJNTs = cmds.ls(sl=True)

###################################################################
        #CTRL DESIGN
        cmds.separator(h=10)

        cmds.text(label="II. Controls' design and color")
        cmds.text(label="")
        self.CTRLColor = cmds.optionMenuGrp(label="Color", columnWidth=(2, 80))
        cmds.menuItem(label="Blue")
        cmds.menuItem(label="Red")
        cmds.menuItem(label="Yellow")
        cmds.menuItem(label="Green")

        self.CTRLDesign = cmds.optionMenuGrp(label="Design", columnWidth=(2, 80))
        cmds.menuItem(label="Basic_Circle")
        cmds.menuItem(label="Basic_Square")
        cmds.menuItem(label="Circle_Pin")
        cmds.menuItem(label="Ball_Pin")
        cmds.menuItem(label="Triangle_Pin")
        cmds.menuItem(label="Pyramid_Pin")
        cmds.menuItem(label="Trapezoid_Pin")

###################################################################
        #RENAME
        cmds.separator(h=10)

        cmds.text(label="III. Create!")
        cmds.text(label="")
        self.Create = cmds.button(label="Create CTRLs", command=self.Create)
        cmds.text(label="")

        cmds.separator(h=10)
        cmds.text(label="Rename?")
        self.CTRLsName = cmds.textFieldGrp(label="New name:", columnWidth=(2, 180))
        cmds.text(label="Skip if only 1 joint is selected")
        self.order = cmds.optionMenuGrp(label="Sort in", columnWidth=(2, 150), extraLabel="order")
        cmds.menuItem(label="-")
        cmds.menuItem(label="Numeric_0")
        cmds.menuItem(label="Numeric_1")
        cmds.menuItem(label="Alphabetic_UPPER")
        cmds.menuItem(label="Alphabetic_lower")
        cmds.text(label="")
        self.RenameAndCreate = cmds.button(label="Rename and Create", command=self.RenameAndCreate)
        cmds.text(label="")
        cmds.text(label="*All CTRLs will inherite JNTs' names and replace _JNT with _CTRL")
        cmds.text(label="*All CTRLs' GRPs will inherite CTRLs' name and end with _GRP")

################################################################### UI CONTENT

        #display new window
        cmds.showWindow()

################################################################### ACTION

    def addJNTtoSel(self, *arg):

        joints = cmds.ls(sl=True)

        for jnt in joints:
            cmds.rename(jnt, jnt + "_JNT")


    def addJNTtoAll(self, *arg):

        self.rename_TarJNT = cmds.ls(sl=True)
        cmds.select(self.rename_TarJNT, hi=True)
        joints = cmds.ls(sl=True, type="joint")

        for jnt in joints:
            cmds.rename(jnt, jnt + "_JNT")


################################################################### ACTION
    
    def DeselectEndJNT(self, *arg):

        self.First_TarJNT = cmds.ls(sl=True)
        cmds.select(self.First_TarJNT, hi=True)
        joints = cmds.ls(sl=True, type="joint")[:-1]
        cmds.select(joints)

        self.TarJNTs = cmds.ls(sl=True)

################################################################### ACTION

    def Create(self, *arg):

        cmds.file("assets/finger_ctrls_01.ma", i=True)
        cmds.hide("tags_GRP")
        cmds.delete("finger_ctrls_CAM")

        colors = {
            "Blue":"6",
            "Red":"13",
            "Yellow":"17",
            "Green":"14"}
        color = cmds.optionMenuGrp(self.CTRLColor, query=True, value=True)
        color_code = int(colors[color])

        design = cmds.optionMenuGrp(self.CTRLDesign, query=True, value=True)

        previous_ctrl = None

        ctrls = ["Basic_Circle", "Basic_Square", "Circle_Pin", "Ball_Pin", "Triangle_Pin", "Pyramid_Pin", "Trapezoid_Pin"]
        def filter_ctrls(ctrls):
            chosen_design = [design]
            return True if ctrls in chosen_design else False

        filtered_ctrl = filter(filter_ctrls, ctrls)

        final_design = tuple(filtered_ctrl)

        cmds.parent(final_design, w=True)
        cmds.rename(final_design, "fin_template_CTRL")
        cmds.group("fin_template_CTRL", n="fin_template_GRP")
        cmds.move(0, 0, 0, "fin_template_GRP.scalePivot", "fin_template_GRP.rotatePivot", absolute=True)
        cmds.delete("tags_GRP")

        cmds.select(self.TarJNTs)

        joints = cmds.ls (sl=1)

        for jnt in joints:
            grp = cmds.duplicate("fin_template_GRP", name=jnt.replace("JNT", "GRP"), rc=True) [0]
            ctrl = cmds.listRelatives(grp, c=True) [0]
            ctrl = cmds.rename(ctrl, jnt.replace("JNT", "CTRL"))

            cmds.delete(cmds.parentConstraint(jnt, grp, mo=False))

            if previous_ctrl:
                cmds.parent(grp, previous_ctrl)

            previous_ctrl = ctrl

            cmds.pointConstraint(ctrl, jnt)
            cmds.orientConstraint(ctrl, jnt)
            cmds.scaleConstraint(ctrl, jnt)

            cmds.setAttr("{0}.overrideEnabled".format(ctrl), 1)
            cmds.setAttr("{0}.overrideColor".format(ctrl), color_code)

        cmds.delete("fin_template_GRP")

###################################################################ACTION

    def RenameAndCreate(self, *arg):

        cmds.file("assets/finger_ctrls_01.ma", i=True)
        cmds.hide("tags_GRP")
        cmds.delete("finger_ctrls_CAM")

        colors = {
            "Blue":"6",
            "Red":"13",
            "Yellow":"17",
            "Green":"14"}
        color = cmds.optionMenuGrp(self.CTRLColor, query=True, value=True)
        color_code = int(colors[color])

        design = cmds.optionMenuGrp(self.CTRLDesign, query=True, value=True)

        previous_ctrl = None

        ctrls = ["Basic_Circle", "Basic_Square", "Circle_Pin", "Ball_Pin", "Triangle_Pin", "Pyramid_Pin", "Trapezoid_Pin"]
        def filter_ctrls(ctrls):
            chosen_design = [design]
            return True if ctrls in chosen_design else False

        filtered_ctrl = filter(filter_ctrls, ctrls)

        final_design = tuple(filtered_ctrl)

        cmds.parent(final_design, w=True)
        cmds.rename(final_design, "fin_template_CTRL")
        cmds.group("fin_template_CTRL", n="fin_template_GRP")
        cmds.move(0, 0, 0, "fin_template_GRP.scalePivot", "fin_template_GRP.rotatePivot", absolute=True)
        cmds.delete("tags_GRP")

        cmds.select(self.TarJNTs)

        new_name = cmds.textFieldGrp(self.CTRLsName, query=True, text=True)
        order = cmds.optionMenuGrp(self.order, query=True, value=True)

        joints = cmds.ls (sl=True)
        length=len(joints)
      
        #CREATING & ORGANIZING LISTS
        Alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        NullList = []
        NumericList_0 = []
        NumericList_1 = []
        AlphabeticList = []
        AlphabeticSecondList = []
        AlphabetsLow = []
        
        def CreateNullList(length):
                a=0
                while a<length:
                        a+=1
                        NullList.append("-")

        def CreateNumList_0(length):
                a=0
                while a<length:
                        a+=1
                        NumericList_0.append(a-1)
        
        def CreateNumList_1(length):
                a=0
                while a<length:
                        a+=1
                        NumericList_1.append(a)

        def Single(length):
                i = 0
                while i < length:
                        Letter=Alphabets[i]
                        i+=1
                        AlphabeticList.append(Letter)

        def Double(length):
                f=0
                s=0
                while f<int(length//26) :
                        Letter_First=Alphabets[f]
                        Letter_Second=Alphabets[s]
                        AlphabeticSecondList.append("{0}{1}".format(Letter_First,Letter_Second))
                        s+=1
                        if s==26 and f<int(length/26):
                                f+=1
                                s-=26
                del AlphabeticSecondList[length-26:]

        def CreateAlphabetList(length):
                f_count = length//26
                s_count = length%26
                if f_count <1:
                        Single(s_count)

                if 1 <= f_count <= 26:
                        Single(26)
                        Double(length)
                        AlphabeticList.extend(AlphabeticSecondList)        

        if order == "-":
                CreateNullList(length)
                chosen_order = NullList
        if order == "Numeric_0":
                CreateNumList_0(length)
                chosen_order = NumericList_0
        if order == "Numeric_1":
                CreateNumList_1(length)
                chosen_order = NumericList_1
        if order == "Alphabetic_UPPER":
                CreateAlphabetList(length)
                chosen_order = AlphabeticList
        if order == "Alphabetic_lower":
                CreateAlphabetList(length)
                for x in AlphabeticList:
                        AlphabetsLow.append(x.lower())
                chosen_order = AlphabetsLow

        joints = cmds.ls (sl=1)

        for jnt, i in zip(joints, chosen_order):

            if order == "-":
                grp = cmds.duplicate("fin_template_GRP", name="{0}_GRP".format(new_name), rc=True) [0]
                ctrl = cmds.listRelatives(grp, c=True) [0]
                ctrl = cmds.rename(ctrl, "{0}_CTRL".format(new_name))

            else:
                grp = cmds.duplicate("fin_template_GRP", name="{0}_{1}_GRP".format(new_name, i), rc=True) [0]
                ctrl = cmds.listRelatives(grp, c=True) [0]
                ctrl = cmds.rename(ctrl, "{0}_{1}_CTRL".format(new_name, i))

            cmds.delete(cmds.parentConstraint(jnt, grp, mo=False))

            if previous_ctrl:
                cmds.parent(grp, previous_ctrl)

            previous_ctrl = ctrl

            cmds.pointConstraint(ctrl, jnt)
            cmds.orientConstraint(ctrl, jnt)
            cmds.scaleConstraint(ctrl, jnt)

            cmds.setAttr("{0}.overrideEnabled".format(ctrl), 1)
            cmds.setAttr("{0}.overrideColor".format(ctrl), color_code)

        cmds.delete("fin_template_GRP")

#IN maya
fk_chain_UI.fk_chain()
