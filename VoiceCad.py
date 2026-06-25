import adsk.core
import adsk.fusion
import traceback
import json


def create_cube(rootComp, size):

    sketches = rootComp.sketches
    xyPlane = rootComp.xYConstructionPlane

    sketch = sketches.add(xyPlane)

    sketch.sketchCurves.sketchLines.addTwoPointRectangle(
        adsk.core.Point3D.create(0, 0, 0),
        adsk.core.Point3D.create(size, size, 0)
    )

    profile = sketch.profiles.item(0)

    extrudes = rootComp.features.extrudeFeatures

    distance = adsk.core.ValueInput.createByReal(size)

    extrudeInput = extrudes.createInput(
        profile,
        adsk.fusion.FeatureOperations.NewBodyFeatureOperation
    )

    extrudeInput.setDistanceExtent(False, distance)

    extrudes.add(extrudeInput)


def run(context):

    ui = None

    try:

        app = adsk.core.Application.get()
        ui = app.userInterface

        design = app.activeProduct
        rootComp = design.rootComponent

        with open(
            r"C:\Users\Kushamb\OneDrive\文档\phone cover\command.json",
            "r"
        ) as file:

            command = json.load(file)

        if command["shape"] == "cube":

            SIZE = command["size"] / 10

            ui.messageBox(
                "Creating Cube : "
                + str(command["size"])
                + " mm"
            )

            create_cube(rootComp, SIZE)

        else:

            ui.messageBox(
                "This shape is not supported yet."
            )

    except:

        if ui:

            ui.messageBox(
                "Failed:\n{}".format(
                    traceback.format_exc()
                )
            )